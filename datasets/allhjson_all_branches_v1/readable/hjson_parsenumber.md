# allhjson/hjson_parsenumber.cpp

4 focal methods with source-level branch indicators. Source commit: `d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3`.

[Overview](../README.md) · [Machine-readable JSONL](../focal_methods.jsonl)

## Functions

| Source line | Focal method |
| --- | --- |
| [L24](#l24) | `static bool _parseFloat(double *pNumber, const char *pCh, size_t nCh)` |
| [L50](#l50) | `static bool _parseInt(std::int64_t *pNumber, const char *pCh, size_t nCh)` |
| [L75](#l75) | `static bool _next(NumberParser *p)` |
| [L92](#l92) | `bool tryParseNumber(Value *pValue, const char *text, size_t textSize, bool stopAtNext)` |

## L24

**Focal:** `static bool _parseFloat(double *pNumber, const char *pCh, size_t nCh)`  
**Source:** [allhjson/hjson_parsenumber.cpp:24-48](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_parsenumber.cpp#L24-L48)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 3, *not an LLVM coverage measurement*

### Focal method

```cpp
static bool _parseFloat(double *pNumber, const char *pCh, size_t nCh) {
#if HJSON_USE_CHARCONV
  auto res = std::from_chars(pCh, pCh + nCh, *pNumber);

  return res.ptr == pCh + nCh && res.ec != std::errc::result_out_of_range &&
    !std::isinf(*pNumber) && !std::isnan(*pNumber);
#elif HJSON_USE_STRTOD
  char *endptr;
  errno = 0;
  *pNumber = std::strtod(pCh, &endptr);

  return !errno && endptr - pCh == nCh && !std::isinf(*pNumber) && !std::isnan(*pNumber);
#else
  std::string str(pCh, nCh);
  std::stringstream ss(str);

  // Make sure we expect dot (not comma) as decimal point.
  ss.imbue(std::locale::classic());

  ss >> *pNumber;

  return ss.eof() && !ss.fail() && !std::isinf(*pNumber) && !std::isnan(*pNumber);
#endif
}
```

### Context

```cpp
#include "hjson.h"
// Source excerpts below are for model context. They already exist in the project; do not redeclare them in a test TU.

// Build: test TU includes "hjson_parsenumber.cpp"; link other three .cpp files once.
```

---

## L50

**Focal:** `static bool _parseInt(std::int64_t *pNumber, const char *pCh, size_t nCh)`  
**Source:** [allhjson/hjson_parsenumber.cpp:50-73](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_parsenumber.cpp#L50-L73)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
static bool _parseInt(std::int64_t *pNumber, const char *pCh, size_t nCh) {
#if HJSON_USE_CHARCONV
  auto res = std::from_chars(pCh, pCh + nCh, *pNumber);

  return res.ptr == pCh + nCh && res.ec != std::errc::result_out_of_range;
#elif HJSON_USE_STRTOD
  char *endptr;
  errno = 0;
  *pNumber = std::strtoll(pCh, &endptr, 0);

  return !errno && endptr - pCh == nCh;
#else
  std::string str(pCh, nCh);
  std::stringstream ss(str);

  // Avoid localization surprises.
  ss.imbue(std::locale::classic());

  ss >> *pNumber;

  return ss.eof() && !ss.fail();
#endif
}
```

### Context

```cpp
#include "hjson.h"
// Source excerpts below are for model context. They already exist in the project; do not redeclare them in a test TU.

// Build: test TU includes "hjson_parsenumber.cpp"; link other three .cpp files once.
```

---

## L75

**Focal:** `static bool _next(NumberParser *p)`  
**Source:** [allhjson/hjson_parsenumber.cpp:75-90](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_parsenumber.cpp#L75-L90)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
static bool _next(NumberParser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  if (p->indexNext == p->dataSize) {
    p->indexNext++;
  }

  p->ch = 0;

  return false;
}
```

### Context

```cpp
#include "hjson.h"
// Source excerpts below are for model context. They already exist in the project; do not redeclare them in a test TU.

// Original number-parser state from hjson_parsenumber.cpp
struct NumberParser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
};

// Example NumberParser fixture for same-translation-unit harness
namespace Hjson {
void example_number_parser_seed() {
  const char data[] = "123";
  NumberParser p = {reinterpret_cast<const unsigned char*>(data), 3, 0, ' '};
  // Use _next(&p) to advance, then vary data and dataSize per branch.
}
} // namespace Hjson

// Build: test TU includes "hjson_parsenumber.cpp"; link other three .cpp files once.
```

---

## L92

**Focal:** `bool tryParseNumber(Value *pValue, const char *text, size_t textSize, bool stopAtNext)`  
**Source:** [allhjson/hjson_parsenumber.cpp:92-175](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_parsenumber.cpp#L92-L175)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 31, *not an LLVM coverage measurement*

### Focal method

```cpp
// Parse a number value. The parameter "text" must be zero terminated.
bool tryParseNumber(Value *pValue, const char *text, size_t textSize, bool stopAtNext) {
  NumberParser p = {
    (const unsigned char*) text,
    textSize,
    0,
    ' '
  };

  int leadingZeros = 0;
  bool testLeading = true;

  _next(&p);

  if (p.ch == '-') {
    _next(&p);
  }

  while (p.ch >= '0' && p.ch <= '9') {
    if (testLeading) {
      if (p.ch == '0') {
        leadingZeros++;
      } else {
        testLeading = false;
      }
    }
    _next(&p);
  }

  if (testLeading) {
    leadingZeros--;
  } // single 0 is allowed

  if (p.ch == '.') {
    while (_next(&p) && p.ch >= '0' && p.ch <= '9') {
    }
  }
  if (p.ch == 'e' || p.ch == 'E') {
    _next(&p);
    if (p.ch == '-' || p.ch == '+') {
      _next(&p);
    }
    while (p.ch >= '0' && p.ch <= '9') {
      _next(&p);
    }
  }

  auto end = p.indexNext;

  // skip white/to (newline)
  while (p.ch > 0 && p.ch <= ' ') {
    _next(&p);
  }

  if (stopAtNext) {
    // end scan if we find a punctuator character like ,}] or a comment
    if (p.ch == ',' || p.ch == '}' || p.ch == ']' ||
      p.ch == '#' || (p.indexNext < textSize && p.ch == '/' &&
      (p.data[p.indexNext] == '/' || p.data[p.indexNext] == '*')))
    {
      p.ch = 0;
    }
  }

  if (p.ch > 0 || leadingZeros != 0) {
    // Invalid number.
    return false;
  }

  std::int64_t i;
  if (_parseInt(&i, (char*) p.data, end - 1)) {
    *pValue = Value(i);
    return true;
  } else {
    double d;
    if (_parseFloat(&d, (char*) p.data, end - 1)) {
      *pValue = Value(d);
      return true;
    }
  }

  return false;
}
```

### Context

```cpp
#include "hjson.h"
// Source excerpts below are for model context. They already exist in the project; do not redeclare them in a test TU.

// Original number-parser state from hjson_parsenumber.cpp
struct NumberParser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static bool _next(NumberParser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  if (p->indexNext == p->dataSize) {
    p->indexNext++;
  }

  p->ch = 0;

  return false;
}

static bool _parseInt(std::int64_t *pNumber, const char *pCh, size_t nCh);

static bool _parseFloat(double *pNumber, const char *pCh, size_t nCh);

// External function declaration absent from hjson.h; forward-declare in test if linking hjson_parsenumber.cpp
namespace Hjson { bool tryParseNumber(Value*, const char*, size_t, bool); }

// Example direct invocation of tryParseNumber (text must be NUL-terminated)
namespace Hjson {
void example_number_input() {
  const char text[] = "12.5";
  Value result;
  bool accepted = tryParseNumber(&result, text, sizeof(text) - 1, false);
  (void)accepted;
}
} // namespace Hjson

// Build: include hjson.h and link all four original .cpp files.
```

