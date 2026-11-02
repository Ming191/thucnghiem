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

The JSONL remains the programmatic source of truth. The catalogs show the exact same `focal_method` and `minimal_context` fields.

## Every JSONL row contains

- `focal_method`: original function definition/body at pinned `source_path`, `source_lines`, `source_url`.
- `minimal_context`: short relevant type layouts and direct helper signatures, not a pasted whole project.
- `method_signature`, `linkage`, `benchmark_exposure`, `dependencies`: how to compile/access the original function.
- `branch_gate`: source-level lexical markers, with the LLVM-measured coverage fields deliberately empty.

Context length is 97–880 characters, while focal bodies are retained in full.

## Private and static access

These are changes **for the benchmark copy only**, leaving the original project untouched:

1. **44 rows require same-translation-unit access** (static/inline namespace helpers or implementation-only nested types). The test harness can `#include` its defining `.cpp`, and compile/link the other three sources separately. **Do not** link the same defining `.cpp` twice.
2. **One private `MapProxy` constructor** (hjson_value.cpp) is exposed by `adapter/mapproxy_public.patch`: change the `private:` section in `class MapProxy` to `public:` in a generated copy of `hjson.h`. This does not edit method bodies.
3. The remaining **74 rows** use the original header and library linkage.

For a self-contained benchmark compile, work from a fresh copy of all four sources and header, apply the visibility patch there, and add the test driver in the same directory as the source it includes. Both source-original and exposed builds must be pinned and tracked separately.

## What qualifies as 'branch-bearing' here?

The extractor kept every function definition containing at least one of the following in the active default preprocessor path:

- `if`, `for`, `while`, `switch`;
- short-circuit `&&` or `||`;
- ternary `?:`, including constructor initializer expressions.

The count `lexical_branch_markers` is an **extraction heuristic**, not the official `llvm-cov` number of branch outcomes. Some expressions may compile into a different number of branch records. No method in this v1 dataset is claimed as *dynamically covered*.

To convert this into the measured coverage dataset, instrument Clang C++11 sources with `-fprofile-instr-generate -fcoverage-mapping -O0`, run the harness with per-test `LLVM_PROFILE_FILE`, merge with `llvm-profdata`, then obtain actual per-function branch outcomes via `llvm-cov export`. Keep the original function bodies unchanged in the benchmark copy. Record compiler/backend macros, test validity, and exact measured outcomes. Do not count branches in callees as focal-method branches.

## MI experiment use

Prompt = `minimal_context` + `focal_method` + covered branch history. Let the model output only short input construction / invocation code. Keep build glue external. Compare incremental **focal** branch coverage with a fixed compiler/coverage configuration and matched baseline vs MI generation budgets.

**No claim of LLVM-verified coverage rate, compilation success of every generated fixture, or positive MI intervention is made by this source extraction alone.**
