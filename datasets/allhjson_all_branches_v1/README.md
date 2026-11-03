# allhjson: all branch-bearing focal methods (v1)

Source: [Ming191/thucnghiem](https://github.com/Ming191/thucnghiem), commit `d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3`, project `allhjson`.

**119 source-level branch candidates out of 188 detected C++ function definitions.** Nothing is excluded for being `static`, private, protected, long, or difficult to construct. The four `.cpp` files are covered; `hjson.h` has declarations and no inline function bodies with conditional control flow.

| File | Selected |
| --- | ---: |
| `hjson_decode.cpp` | 26 |
| `hjson_encode.cpp` | 16 |
| `hjson_parsenumber.cpp` | 4 |
| `hjson_value.cpp` | 73 |
| **Total** | **119** |

## Human-readable dataset

The JSONL stores multi-line C++ as escaped `\\n`. For reviewing methods, open one of these rendered Markdown catalogs instead. All code fences contain **real line breaks**.

- [hjson_decode.cpp (26 methods)](readable/hjson_decode.md)
- [hjson_encode.cpp (16 methods)](readable/hjson_encode.md)
- [hjson_parsenumber.cpp (4 methods)](readable/hjson_parsenumber.md)
- [hjson_value.cpp (73 methods)](readable/hjson_value.md)

The JSONL remains the programmatic source of truth. The catalogs show the exact same `focal_method` and `context` fields, with real newlines and C++ highlighting.

## Every JSONL row contains

- `focal_method`: original function definition/body at pinned `source_path`, `source_lines`, `source_url`.
- `context`: source-faithful C++ declarations and local helper code/signatures relevant to this focal method, with focal-specific state preconditions where needed. Build instructions and example fixtures are excluded; self-contained methods may have an empty context. Declarations are source excerpts already defined in the project, not code to redeclare in a test TU.
- `method_signature`, `linkage`, `benchmark_exposure`, `dependencies`: how to compile/access the original function.
- `branch_gate`: source-level lexical markers, with the LLVM-measured coverage fields deliberately empty.

Context length is 0–6027 characters (median 1945). Focal bodies are retained in full.

## Private and static access

These are changes **for the benchmark copy only**, leaving the original project untouched:

1. **44 rows require same-translation-unit access** (static/inline namespace helpers or implementation-only nested types). The test harness can `#include` its defining `.cpp`, and compile/link the other three sources separately. **Do not** link the same defining `.cpp` twice.
2. **One private `MapProxy` constructor** (`hjson_value.cpp`) is reachable through the original public `Value::operator[]` without patching. For direct constructor tests only, `adapter/mapproxy_public.patch` exposes the `(parent, key, pTarget)` constructor in an isolated benchmark copy of `hjson.h`; its copy and move constructors remain private.
3. The remaining **74 rows** use the original header and library linkage.

For a self-contained benchmark compile, work from a fresh copy of all four sources and header, apply the visibility patch only if directly testing the private constructor, and add the test driver in the same directory as the source it includes. Both source-original and exposed builds must be pinned and tracked separately.

## What qualifies as 'branch-bearing' here?

The extractor kept every function definition containing at least one of the following in the active default preprocessor path. Macro-generated integer conversion wrappers at `hjson_value.cpp:1223-1236` are not independent focal branch targets; the record now targets only `Value::operator long long()` at lines 1239-1253:

- `if`, `for`, `while`, `switch`;
- short-circuit `&&` or `||`;
- ternary `?:`, including constructor initializer expressions.

The count `lexical_branch_markers` is an **extraction heuristic**, not the official `llvm-cov` number of branch outcomes. Some expressions may compile into a different number of branch records. No method in this v1 dataset is claimed as *dynamically covered*.

Known source limitations: `hjson_decode.cpp:_readObjectBegin` checks `vParent.empty()` after dereferencing `back()`, so its true path is infeasible for valid state; `Value::operator[](int)` contains a redundant nested type condition; and `_readMLString` contains a nested lambda whose branch records must not be attributed to the outer function without an explicit policy. The default C++11 target uses stringstream conversion (`HJSON_USE_CHARCONV` and `HJSON_USE_STRTOD` undefined); alternate backends require separate builds. 

To convert this into the measured coverage dataset, instrument Clang C++11 sources with `-fprofile-instr-generate -fcoverage-mapping -O0`, run the harness with per-test `LLVM_PROFILE_FILE`, merge with `llvm-profdata`, then obtain actual per-function branch outcomes via `llvm-cov export`. Keep the original function bodies unchanged in the benchmark copy. Record compiler/backend macros, test validity, and exact measured outcomes. Do not count branches in callees as focal-method branches.

## MI experiment use

Prompt = `context` + `focal_method` + covered branch history. Context contains only source dependencies and branch-relevant state constraints; build and harness details stay in metadata. Let the model output only short input construction / invocation code. Keep build glue external. Compare incremental **focal** branch coverage with a fixed compiler/coverage configuration and matched baseline vs MI generation budgets.

**No claim of LLVM-verified coverage rate, compilation success of generated tests, or positive MI intervention is made by this source extraction alone.**
