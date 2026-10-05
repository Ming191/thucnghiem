from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from llvm_coverage_backend import LLVMBackend, ProjectConfig

PROJECTS = ("allhjson", "alljson", "allxml", "jsonxx", "jvar")


@dataclass(frozen=True)
class Candidate:
    project: str
    function_id: str
    qualified_name: str
    signature: str
    file: str
    start_line: int
    end_line: int
    lines: int
    parameters: int
    calls: int
    constructions: int
    static_branch_points: int
    short_circuit_predicates: int
    score: float


CONTROL_PATTERNS = (
    r"\bif\s*\(",
    r"\bfor\s*\(",
    r"\bwhile\s*\(",
    r"\bswitch\s*\(",
    r"\bcase\b",
    r"\bcatch\s*\(",
    r"&&",
    r"\|\|",
    r"\?(?!\?)",
)


def static_branch_points(source: str) -> int:
    return sum(len(re.findall(pattern, source)) for pattern in CONTROL_PATTERNS)


def score_candidate(info, context) -> Candidate | None:
    lines = info.end_line - info.start_line + 1
    branches = static_branch_points(context.source)
    params = len(context.parameters)
    calls = len(context.calls)
    constructions = len(context.constructions)
    short_circuit = len(context.control_predicates)

    if lines < 6 or lines > 180:
        return None
    if branches < 2:
        return None
    if params > 8:
        return None

    score = (
        branches * 4.0
        + min(lines, 80) * 0.08
        + min(calls, 8) * 0.6
        + min(constructions, 5) * 0.4
        + short_circuit * 1.5
    )
    if info.kind in {"CXXConstructorDecl", "CXXDestructorDecl"}:
        score -= 2.0
    if lines > 120:
        score -= (lines - 120) * 0.08

    return Candidate(
        project="",
        function_id=info.function_id,
        qualified_name=info.qualified_name,
        signature=info.signature,
        file=str(info.file),
        start_line=info.start_line,
        end_line=info.end_line,
        lines=lines,
        parameters=params,
        calls=calls,
        constructions=constructions,
        static_branch_points=branches,
        short_circuit_predicates=short_circuit,
        score=round(score, 3),
    )


def select_project(root: Path, project_name: str, per_project: int) -> tuple[list[Candidate], dict]:
    project_root = root / project_name
    backend = LLVMBackend()
    project = backend.prepare(ProjectConfig(root=project_root))
    contexts = {item.function_id: item for item in project.function_contexts}

    candidates: list[Candidate] = []
    for info in project.functions:
        context = contexts.get(info.function_id)
        if context is None:
            continue
        candidate = score_candidate(info, context)
        if candidate is None:
            continue
        candidates.append(
            Candidate(
                **{
                    **asdict(candidate),
                    "project": project_name,
                    "file": str(info.file.relative_to(project_root)),
                }
            )
        )

    candidates.sort(key=lambda item: (-item.score, item.file, item.start_line))

    selected: list[Candidate] = []
    per_file: dict[str, int] = {}
    for item in candidates:
        if per_file.get(item.file, 0) >= 3:
            continue
        selected.append(item)
        per_file[item.file] = per_file.get(item.file, 0) + 1
        if len(selected) >= per_project:
            break

    if len(selected) < per_project:
        chosen = {item.function_id for item in selected}
        for item in candidates:
            if item.function_id in chosen:
                continue
            selected.append(item)
            if len(selected) >= per_project:
                break

    summary = {
        "functions_discovered": len(project.functions),
        "eligible": len(candidates),
        "selected": len(selected),
        "cache_key": project.cache_key,
    }
    return selected, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--per-project", type=int, default=8)
    parser.add_argument("--output", type=Path, default=Path("benchmark-manifest.json"))
    args = parser.parse_args()

    root = args.root.resolve()
    selected: list[Candidate] = []
    summaries = {}
    for project in PROJECTS:
        items, summary = select_project(root, project, args.per_project)
        selected.extend(items)
        summaries[project] = summary

    payload = {
        "schema_version": 1,
        "selection_method": "static-control-flow-balanced-v1",
        "projects": list(PROJECTS),
        "per_project_target": args.per_project,
        "selected_count": len(selected),
        "project_summary": summaries,
        "functions": [asdict(item) for item in selected],
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summaries, indent=2))
    print(f"selected={len(selected)}")
    for item in selected:
        print(
            f"{item.project}\t{item.score:6.2f}\t"
            f"branches~{item.static_branch_points}\t"
            f"{item.qualified_name}"
        )


if __name__ == "__main__":
    main()
