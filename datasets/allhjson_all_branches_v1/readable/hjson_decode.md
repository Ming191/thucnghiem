# allhjson/hjson_decode.cpp

26 focal methods with source-level branch indicators. Source commit: `d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3`.

[Overview](../README.md) · [Machine-readable JSONL](../focal_methods.jsonl)

## Functions

| Source line | Focal method |
| --- | --- |
| [L15](#l15) | `inline void _setComment(Value& val, void (Value::*fp)(const std::string&), Parser *p, const CommentInfo& ci)` |
| [L24](#l24) | `inline void _setComment(Value& val, void (Value::*fp)(const std::string&), Parser *p, const CommentInfo& ciA, const CommentInfo& c` |
| [L39](#l39) | `static bool _next(Parser *p)` |
| [L53](#l53) | `static bool _prev(Parser *p)` |
| [L70](#l70) | `static bool _isPunctuatorChar(char c)` |
| [L75](#l75) | `static std::string _errAt(Parser *p, const std::string& message)` |
| [L101](#l101) | `static unsigned char _peek(Parser *p, int offs)` |
| [L112](#l112) | `static unsigned char _escapee(unsigned char c)` |
| [L143](#l143) | `static std::string _readMLString(Parser *p)` |
| [L217](#l217) | `static void _toUtf8(std::vector<char> &res, uint32_t uIn)` |
| [L238](#l238) | `static std::string _readString(Parser *p, bool allowML)` |
| [L297](#l297) | `static std::string _readKeyname(Parser *p)` |
| [L337](#l337) | `static CommentInfo _white(Parser *p)` |
| [L382](#l382) | `static CommentInfo _getCommentAfter(Parser *p)` |
| [L425](#l425) | `static Value _readTfnns2(Parser *p, size_t &valEnd)` |
| [L509](#l509) | `static void _readArrayBegin(Parser* p)` |
| [L530](#l530) | `static void _readArrayElemEnd(Parser* p)` |
| [L564](#l564) | `static void _readObjectBegin(Parser *p)` |
| [L586](#l586) | `static void _readObjectElemBegin(Parser* p)` |
| [L619](#l619) | `static void _readObjectElemEnd(Parser *p)` |
| [L658](#l658) | `static void _readValueBegin(Parser *p)` |
| [L705](#l705) | `static void _parseLoop(Parser* p)` |
| [L747](#l747) | `static Value _rootValue(Parser *p)` |
| [L802](#l802) | `Value Unmarshal(const char *data, size_t dataSize, const DecoderOptions& options)` |
| [L825](#l825) | `Value Unmarshal(const char *data, const DecoderOptions& options)` |
| [L839](#l839) | `Value UnmarshalFromFile(const std::string &path, const DecoderOptions& options)` |

## L15

**Focal:** `inline void _setComment(Value& val, void (Value::*fp)(const std::string&), Parser *p, const CommentInfo& ci)`  
**Source:** [allhjson/hjson_decode.cpp:15-22](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L15-L22)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ci)
{
  if (ci.hasComment) {
    (val.*fp)(std::string(p->data + ci.cmStart, p->data + ci.cmEnd));
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};
```

---

## L24

**Focal:** `inline void _setComment(Value& val, void (Value::*fp)(const std::string&), Parser *p, const CommentInfo& ciA, const CommentInfo& ciB)`  
**Source:** [allhjson/hjson_decode.cpp:24-37](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L24-L37)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 4, *not an LLVM coverage measurement*

### Focal method

```cpp
inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ciA, const CommentInfo& ciB)
{
  if (ciA.hasComment && ciB.hasComment) {
    (val.*fp)(std::string(p->data + ciA.cmStart, p->data + ciA.cmEnd) +
      std::string(p->data + ciB.cmStart, p->data + ciB.cmEnd));
  } else if (!ciA.hasComment && !ciB.hasComment) {
    (val.*fp)("");
  } else {
    _setComment(val, fp, p, ciA);
    _setComment(val, fp, p, ciB);
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};
```

---

## L39

**Focal:** `static bool _next(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:39-51](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L39-L51)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};
```

---

## L53

**Focal:** `static bool _prev(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:53-62](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L53-L62)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
static bool _prev(Parser *p) {
  // get the previous character.
  if (p->indexNext > 1) {
    p->ch = p->data[p->indexNext-- - 2];
    return true;
  }

  return false;
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct invocation only: _prev has no decoder caller; to read back safely, use 2 <= indexNext <= dataSize + 1. Avoid repeated _next EOF past the buffer.
```

---

## L70

**Focal:** `static bool _isPunctuatorChar(char c)`  
**Source:** [allhjson/hjson_decode.cpp:70-73](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L70-L73)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 5, *not an LLVM coverage measurement*

### Focal method

```cpp
static bool _isPunctuatorChar(char c) {
  return c == '{' || c == '}' || c == '[' || c == ']' || c == ',' || c == ':';
}
```

### Context

```cpp

```

---

## L75

**Focal:** `static std::string _errAt(Parser *p, const std::string& message)`  
**Source:** [allhjson/hjson_decode.cpp:75-99](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L75-L99)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 6, *not an LLVM coverage measurement*

### Focal method

```cpp
static std::string _errAt(Parser *p, const std::string& message) {
  if (p->dataSize && p->indexNext <= p->dataSize) {
    size_t decoderIndex = std::max(static_cast<size_t>(1), std::min(p->dataSize,
      static_cast<size_t>(p->indexNext))) - 1;
    size_t i = decoderIndex, col = 0, line = 1;

    for (; i > 0 && p->data[i] != '\n'; i--) {
      col++;
    }

    for (; i > 0; i--) {
      if (p->data[i] == '\n') {
        line++;
      }
    }

    size_t samEnd = std::min((size_t)20, p->dataSize - (decoderIndex - col));

    return message + " at line " + std::to_string(line) + "," +
      std::to_string(col) + " >>> " + std::string((char*)p->data + decoderIndex - col, samEnd);
  } else {
    return message;
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};
```

---

## L101

**Focal:** `static unsigned char _peek(Parser *p, int offs)`  
**Source:** [allhjson/hjson_decode.cpp:101-110](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L101-L110)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
static unsigned char _peek(Parser *p, int offs) {
  int pos = p->indexNext + offs;

  if (pos >= 0 && pos < p->dataSize) {
    return p->data[pos];
  }

  return 0;
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};
```

---

## L112

**Focal:** `static unsigned char _escapee(unsigned char c)`  
**Source:** [allhjson/hjson_decode.cpp:112-141](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L112-L141)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 9, *not an LLVM coverage measurement*

### Focal method

```cpp
static unsigned char _escapee(unsigned char c) {
  if ((c == '"') || (c == '\'') || (c == '\\') || (c == '/')) {

    return c;
  
  } else if ((c == 'b')) {

    return '\b';
  
  } else if ((c == 'f')) {

    return '\f';
  
  } else if ((c == 'n')) {

    return '\n';
  
  } else if ((c == 'r')) {

    return '\r';
  
  } else if ((c == 't')) {

    return '\t';
  
  }

  return 0;
}
```

### Context

```cpp

```

---

## L143

**Focal:** `static std::string _readMLString(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:143-215](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L143-L215)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 19, *not an LLVM coverage measurement*

### Focal method

```cpp
// Parse a multiline string value.
static std::string _readMLString(Parser *p) {
  // Store the string in a new vector, because the length of it might be
  // different than the length in the input data.
  std::vector<char> res;
  int triple = 0;

  // we are at ''' +1 - get indent
  int indent = 0;

  for (;;) {
    auto c = _peek(p, -indent - 5);
    if (c == 0 || c == '\n') {
      break;
    }
    indent++;
  }

  auto skipIndent = [&]() {
    auto skip = indent;
    while (p->ch > 0 && p->ch <= ' ' && p->ch != '\n' && skip > 0) {
      skip--;
      _next(p);
    }
  };

  // skip white/to (newline)
  while (p->ch > 0 && p->ch <= ' ' && p->ch != '\n') {
    _next(p);
  }
  if (p->ch == '\n') {
    _next(p);
    skipIndent();
  }

  // When parsing multiline string values, we must look for ' characters.
  bool lastLf = false;
  for (;;) {
    if (p->ch == 0) {
      throw syntax_error(_errAt(p, "Bad multiline string"));
    } else if (p->ch == '\'') {
      triple++;
      _next(p);
      if (triple == 3) {
        auto sres = res.data();
        if (lastLf) {
          return std::string(sres, res.size() - 1); // remove last EOL
        }
        return std::string(sres, res.size());
      }
      continue;
    } else {
      while (triple > 0) {
        res.push_back('\'');
        triple--;
        lastLf = false;
      }
    }
    if (p->ch == '\n') {
      res.push_back('\n');
      lastLf = true;
      _next(p);
      skipIndent();
    } else {
      if (p->ch != '\r') {
        res.push_back(p->ch);
        lastLf = false;
      }
      _next(p);
    }
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static unsigned char _peek(Parser *p, int offs) {
  int pos = p->indexNext + offs;

  if (pos >= 0 && pos < p->dataSize) {
    return p->data[pos];
  }

  return 0;
}

static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

static std::string _errAt(Parser *p, const std::string& message);

// _readMLString requires the cursor immediately after the opening three apostrophes.
```

---

## L217

**Focal:** `static void _toUtf8(std::vector<char> &res, uint32_t uIn)`  
**Source:** [allhjson/hjson_decode.cpp:217-236](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L217-L236)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 4, *not an LLVM coverage measurement*

### Focal method

```cpp
static void _toUtf8(std::vector<char> &res, uint32_t uIn) {
  if (uIn < 0x80) {
    res.push_back(uIn);
  } else if (uIn < 0x800) {
    res.push_back(0xc0 | ((uIn >> 6) & 0x1f));
    res.push_back(0x80 | (uIn & 0x3f));
  } else if (uIn < 0x10000) {
    res.push_back(0xe0 | ((uIn >> 12) & 0xf));
    res.push_back(0x80 | ((uIn >> 6) & 0x3f));
    res.push_back(0x80 | (uIn & 0x3f));
  } else if (uIn < 0x110000) {
    res.push_back(0xf0 | ((uIn >> 18) & 0x7));
    res.push_back(0x80 | ((uIn >> 12) & 0x3f));
    res.push_back(0x80 | ((uIn >> 6) & 0x3f));
    res.push_back(0x80 | (uIn & 0x3f));
  } else {
    throw std::logic_error("Invalid unicode code point");
  }
}
```

### Context

```cpp
// Directly call _toUtf8 with 0x10000 for its four-byte path and 0x110000 for the rejection path. The public \uXXXX parser cannot reach these code points.
```

---

## L238

**Focal:** `static std::string _readString(Parser *p, bool allowML)`  
**Source:** [allhjson/hjson_decode.cpp:238-295](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L238-L295)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 18, *not an LLVM coverage measurement*

### Focal method

```cpp
// Parse a string value.
// callers make sure that (ch === '"' || ch === "'")
// When parsing for string values, we must look for " and \ characters.
static std::string _readString(Parser *p, bool allowML) {
  // Store the string in a new vector, because the length of it might be
  // different than the length in the input data.
  std::vector<char> res;

  char exitCh = p->ch;
  while (_next(p)) {
    if (p->ch == exitCh) {
      _next(p);
      if (allowML && exitCh == '\'' && p->ch == '\'' && res.size() == 0) {
        // ''' indicates a multiline string
        _next(p);
        return _readMLString(p);
      } else {
        return std::string(res.data(), res.size());
      }
    }
    if (p->ch == '\\') {
      unsigned char ech;
      _next(p);
      if (p->ch == 'u') {
        uint32_t uffff = 0;
        for (int i = 0; i < 4; i++) {
          _next(p);
          unsigned char hex;
          if (p->ch >= '0' && p->ch <= '9') {
            hex = p->ch - '0';
          } else if (p->ch >= 'a' && p->ch <= 'f') {
            hex = p->ch - 'a' + 0xa;
          } else if (p->ch >= 'A' && p->ch <= 'F') {
            hex = p->ch - 'A' + 0xa;
          } else {
            throw syntax_error(_errAt(p, std::string("Bad \\u char ") + (char)p->ch));
          }
          uffff = uffff * 16 + hex;
        }
        _toUtf8(res, uffff);
      } else {
        ech = _escapee(p->ch);
        if (ech) {
          res.push_back(ech);
        } else {
          throw syntax_error(_errAt(p, std::string("Bad escape \\") + (char)p->ch));
        }
      }
    } else if (p->ch == '\n' || p->ch == '\r') {
      throw syntax_error(_errAt(p, "Bad string containing newline"));
    } else {
      res.push_back(p->ch);
    }
  }

  throw syntax_error(_errAt(p, "Bad string"));
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

static std::string _readMLString(Parser *p);

static std::string _errAt(Parser *p, const std::string& message);

static void _toUtf8(std::vector<char> &res, uint32_t uIn);

static unsigned char _escapee(unsigned char c) {
  if ((c == '"') || (c == '\'') || (c == '\\') || (c == '/')) {

    return c;
  
  } else if ((c == 'b')) {

    return '\b';
  
  } else if ((c == 'f')) {

    return '\f';
  
  } else if ((c == 'n')) {

    return '\n';
  
  } else if ((c == 'r')) {

    return '\r';
  
  } else if ((c == 't')) {

    return '\t';
  
  }

  return 0;
}

// Entry cursor for _readString: p.ch must be the opening single/double quote, and indexNext points just after it. Example input: "\"x\"".
```

---

## L297

**Focal:** `static std::string _readKeyname(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:297-335](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L297-L335)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 11, *not an LLVM coverage measurement*

### Focal method

```cpp
// quotes for keys are optional in Hjson
// unless they include {}[],: or whitespace.
static std::string _readKeyname(Parser *p) {
  if (p->ch == '"' || p->ch == '\'') {
    return _readString(p, false);
  }

  // keyStart is the index for the first char of the key.
  size_t keyStart = p->indexNext - 1;
  // keyEnd is the index for the first char after the key (i.e. not included in the key).
  size_t keyEnd = keyStart;
  int firstSpace = -1;
  for (;;) {
    if (p->ch == ':') {
      if (keyEnd <= keyStart) {
        throw syntax_error(_errAt(p, "Found ':' but no key name (for an empty key name use quotes)"));
      } else if (firstSpace >= 0 && firstSpace != keyEnd) {
        p->indexNext = firstSpace + 1;
        throw syntax_error(_errAt(p, "Found whitespace in your key name (use quotes to include)"));
      }
      return std::string(reinterpret_cast<const char*>(p->data) + keyStart, keyEnd - keyStart);
    } else if (p->ch <= ' ') {
      if (p->ch == 0) {
        throw syntax_error(_errAt(p, "Found EOF while looking for a key name (check your syntax)"));
      }
      if (firstSpace < 0) {
        firstSpace = p->indexNext - 1;
      }
    } else {
      if (_isPunctuatorChar(p->ch)) {
        throw syntax_error(_errAt(p, std::string("Found '") + (char)p->ch + std::string(
          "' where a key name was expected (check your syntax or use quotes if the key name includes {}[],: or whitespace)")));
      }
      keyEnd = p->indexNext;
    }
    _next(p);
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static std::string _readString(Parser *p, bool allowML);

static std::string _errAt(Parser *p, const std::string& message);

static bool _isPunctuatorChar(char c) {
  return c == '{' || c == '}' || c == '[' || c == ']' || c == ',' || c == ':';
}

static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

// _readKeyname requires the cursor at the first key character, not at '{'.
```

---

## L337

**Focal:** `static CommentInfo _white(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:337-380](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L337-L380)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 18, *not an LLVM coverage measurement*

### Focal method

```cpp
static CommentInfo _white(Parser *p) {
  CommentInfo ci;
  ci.cmStart = p->indexNext - 1;

  while (p->ch > 0) {
    // Skip whitespace.
    while (p->ch > 0 && p->ch <= ' ') {
      _next(p);
    }
    // Hjson allows comments
    if (p->ch == '#' || (p->ch == '/' && _peek(p, 0) == '/')) {
      if (p->opt.comments) {
        ci.hasComment = true;
      }
      while (p->ch > 0 && p->ch != '\n') {
        _next(p);
      }
    } else if (p->ch == '/' && _peek(p, 0) == '*') {
      if (p->opt.comments) {
        ci.hasComment = true;
      }
      _next(p);
      _next(p);
      while (p->ch > 0 && !(p->ch == '*' && _peek(p, 0) == '/')) {
        _next(p);
      }
      if (p->ch > 0) {
        _next(p);
        _next(p);
      }
    } else {
      break;
    }
  }

  // cmEnd is the first char after the comment (i.e. not included in the comment).
  ci.cmEnd = p->indexNext - 1;

  ci.hasComment = (ci.hasComment || (p->opt.whitespaceAsComments &&
    (ci.cmEnd > ci.cmStart)));

  return ci;
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Decoder options from hjson.h
struct DecoderOptions {
  // Keep all comments from the Hjson input, store them in
  // the Hjson::Value objects.
  bool comments = true;
  // Store all whitespace and comments in the Hjson::Value objects so that
  // linefeeds and custom indentation is kept. The "comments" option is
  // ignored if this option is true.
  bool whitespaceAsComments = false;
  // If true, an Hjson::syntax_error exception is thrown from the unmarshal
  // functions if a map contains duplicate keys.
  bool duplicateKeyException = false;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

static unsigned char _peek(Parser *p, int offs) {
  int pos = p->indexNext + offs;

  if (pos >= 0 && pos < p->dataSize) {
    return p->data[pos];
  }

  return 0;
}
```

---

## L382

**Focal:** `static CommentInfo _getCommentAfter(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:382-423](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L382-L423)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 17, *not an LLVM coverage measurement*

### Focal method

```cpp
static CommentInfo _getCommentAfter(Parser *p) {
  CommentInfo ci;
  ci.hasComment = p->opt.whitespaceAsComments;
  ci.cmStart = p->indexNext - 1;

  while (p->ch > 0) {
    // Skip whitespace, but only until EOL.
    while (p->ch > 0 && p->ch <= ' ' && p->ch != '\n') {
      _next(p);
    }
    // Hjson allows comments
    if (p->ch == '#' || (p->ch == '/' && _peek(p, 0) == '/')) {
      if (p->opt.comments) {
        ci.hasComment = true;
      }
      while (p->ch > 0 && p->ch != '\n') {
        _next(p);
      }
    } else if (p->ch == '/' && _peek(p, 0) == '*') {
      if (p->opt.comments) {
        ci.hasComment = true;
      }
      _next(p);
      _next(p);
      while (p->ch > 0 && !(p->ch == '*' && _peek(p, 0) == '/')) {
        _next(p);
      }
      if (p->ch > 0) {
        _next(p);
        _next(p);
      }
    } else {
      break;
    }
  }

  // cmEnd is the first char after the comment (i.e. not included in the comment).
  ci.cmEnd = p->indexNext - 1;

  return ci;
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Decoder options from hjson.h
struct DecoderOptions {
  // Keep all comments from the Hjson input, store them in
  // the Hjson::Value objects.
  bool comments = true;
  // Store all whitespace and comments in the Hjson::Value objects so that
  // linefeeds and custom indentation is kept. The "comments" option is
  // ignored if this option is true.
  bool whitespaceAsComments = false;
  // If true, an Hjson::syntax_error exception is thrown from the unmarshal
  // functions if a map contains duplicate keys.
  bool duplicateKeyException = false;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

static unsigned char _peek(Parser *p, int offs) {
  int pos = p->indexNext + offs;

  if (pos >= 0 && pos < p->dataSize) {
    return p->data[pos];
  }

  return 0;
}
```

---

## L425

**Focal:** `static Value _readTfnns2(Parser *p, size_t &valEnd)`  
**Source:** [allhjson/hjson_decode.cpp:425-497](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L425-L497)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 29, *not an LLVM coverage measurement*

### Focal method

```cpp
// Hjson strings can be quoteless
// returns string, true, false, or null.
static Value _readTfnns2(Parser *p, size_t &valEnd) {
  if (_isPunctuatorChar(p->ch)) {
    throw syntax_error(_errAt(p, std::string("Found a punctuator character '") +
      (char)p->ch + std::string("' when expecting a quoteless string (check your syntax)")));
  }
  size_t valStart = p->indexNext - 1;

  if (std::isspace(p->ch)) {
    ++valStart;
  } else {
    // valEnd is the first char after the value.
    valEnd = p->indexNext;
  }

  for (;;) {
    _next(p);
    bool isEol = (p->ch == '\r' || p->ch == '\n' || p->ch == 0);
    if (isEol ||
      p->ch == ',' || p->ch == '}' || p->ch == ']' ||
      p->ch == '#' ||
      (p->ch == '/' && (_peek(p, 0) == '/' || _peek(p, 0) == '*')))
    {
      const char *pVal = reinterpret_cast<const char*>(p->data) + valStart;
      size_t valLen = valEnd - valStart;

      if ((*pVal == 'f')) {

        if (valLen == 5 && !std::strncmp(pVal, "false", 5)) {
          return false;
        }
        
      
      } else if ((*pVal == 'n')) {

        if (valLen == 4 && !std::strncmp(pVal, "null", 4)) {
          return Value(Type::Null);
        }
        
      
      } else if ((*pVal == 't')) {

        if (valLen == 4 && !std::strncmp(pVal, "true", 4)) {
          return true;
        }
        
      
      } else {

        if (*pVal == '-' || (*pVal >= '0' && *pVal <= '9')) {
          Value number;
          if (tryParseNumber(&number, pVal, valLen, false)) {
            return number;
          }
        }
      
      }
      if (isEol) {
        return std::string(pVal, valLen);
      }
    }
    if (std::isspace(p->ch)) {
      if (valEnd <= valStart) {
        ++valStart;
      }
    } else {
      // valEnd is the first char after the value.
      valEnd = p->indexNext;
    }
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Hjson::Type enum from hjson.h
enum class Type {
  Undefined,
  Null,
  Bool,
  Double,
  Int64,
  String,
  Vector,
  Map
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static bool _isPunctuatorChar(char c) {
  return c == '{' || c == '}' || c == '[' || c == ']' || c == ',' || c == ':';
}

static std::string _errAt(Parser *p, const std::string& message);

static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

static unsigned char _peek(Parser *p, int offs) {
  int pos = p->indexNext + offs;

  if (pos >= 0 && pos < p->dataSize) {
    return p->data[pos];
  }

  return 0;
}

bool tryParseNumber(Value *pNumber, const char *text, size_t textSize, bool stopAtNext);

// Safe direct-call input for initial-whitespace path: use "  alpha\n", not whitespace-only text; valEnd can remain 0 and unsigned valEnd-valStart underflows on all-whitespace direct inputs.
```

---

## L509

**Focal:** `static void _readArrayBegin(Parser* p)`  
**Source:** [allhjson/hjson_decode.cpp:509-528](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L509-L528)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
// Parse an array value.
// assuming ch == '['
static void _readArrayBegin(Parser* p) {
  // Skip '['.
  _next(p);

  p->vParent.back().val = Value(Type::Vector);
  p->vParent.back().ciElemBefore = _white(p);
  p->vParent.back().ciElemExtra = CommentInfo();

  if (p->ch == ']') {
    _setComment(p->vParent.back().val, &Value::set_comment_inside, p, p->vParent.back().ciElemBefore);
    _next(p);
    p->vState.back() = ParseState::ValueEnd;
  } else {
    p->vState.back() = ParseState::VectorElemEnd;
    p->vState.push_back(ParseState::ValueBegin);
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Hjson::Type enum from hjson.h
enum class Type {
  Undefined,
  Null,
  Bool,
  Double,
  Int64,
  String,
  Vector,
  Map
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

static CommentInfo _white(Parser *p);

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ci)
{
  if (ci.hasComment) {
    (val.*fp)(std::string(p->data + ci.cmStart, p->data + ci.cmEnd));
  }
}

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ciA, const CommentInfo& ciB)
{
  if (ciA.hasComment && ciB.hasComment) {
    (val.*fp)(std::string(p->data + ciA.cmStart, p->data + ciA.cmEnd) +
      std::string(p->data + ciB.cmStart, p->data + ciB.cmEnd));
  } else if (!ciA.hasComment && !ciB.hasComment) {
    (val.*fp)("");
  } else {
    _setComment(val, fp, p, ciA);
    _setComment(val, fp, p, ciB);
  }
}

// _readArrayBegin requires p.ch=='[', a nonempty parent stack, and VectorBegin state.
```

---

## L530

**Focal:** `static void _readArrayElemEnd(Parser* p)`  
**Source:** [allhjson/hjson_decode.cpp:530-562](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L530-L562)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 4, *not an LLVM coverage measurement*

### Focal method

```cpp
static void _readArrayElemEnd(Parser* p) {
  Value elem = p->vParent.back().val;
  p->vParent.pop_back();

  _setComment(elem, &Value::set_comment_before, p, p->vParent.back().ciElemBefore, p->vParent.back().ciElemExtra);
  auto ciAfter = _white(p);
  // in Hjson the comma is optional and trailing commas are allowed
  if (p->ch == ',') {
    _next(p);
    // It is unlikely that someone writes a comment after the value but
    // before the comma, so we include any such comment in "comment_after".
    p->vParent.back().ciElemExtra = _white(p);
  } else {
    p->vParent.back().ciElemExtra = CommentInfo();
  }
  if (p->ch == ']') {
    auto existingAfter = elem.get_comment_after();
    _setComment(elem, &Value::set_comment_after, p, ciAfter, p->vParent.back().ciElemExtra);
    if (!existingAfter.empty()) {
      elem.set_comment_after(existingAfter + elem.get_comment_after());
    }
    _next(p);
    p->vState.back() = ParseState::ValueEnd;
  } else {
    if (p->ch == 0) {
      throw syntax_error(_errAt(p, "End of input while parsing an array (did you forget a closing ']'?)"));
    }
    p->vParent.back().ciElemBefore = ciAfter;
    p->vState.push_back(ParseState::ValueBegin);
  }
  p->vParent.back().val.push_back(elem);
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ci)
{
  if (ci.hasComment) {
    (val.*fp)(std::string(p->data + ci.cmStart, p->data + ci.cmEnd));
  }
}

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ciA, const CommentInfo& ciB)
{
  if (ciA.hasComment && ciB.hasComment) {
    (val.*fp)(std::string(p->data + ciA.cmStart, p->data + ciA.cmEnd) +
      std::string(p->data + ciB.cmStart, p->data + ciB.cmEnd));
  } else if (!ciA.hasComment && !ciB.hasComment) {
    (val.*fp)("");
  } else {
    _setComment(val, fp, p, ciA);
    _setComment(val, fp, p, ciB);
  }
}

static CommentInfo _white(Parser *p);

static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

static std::string _errAt(Parser *p, const std::string& message);
```

---

## L564

**Focal:** `static void _readObjectBegin(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:564-584](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L564-L584)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 4, *not an LLVM coverage measurement*

### Focal method

```cpp
static void _readObjectBegin(Parser *p) {
  p->vParent.back().val = Value(Type::Map);

  if (p->ch == '{') {
    _next(p);
    p->vParent.back().ciElemBefore = _white(p);
  } else {
    p->vParent.back().ciElemBefore = p->vParent.back().ciBefore;
    p->vParent.back().ciBefore = CommentInfo();
  }


  if (p->ch == '}' && !(p->vParent.empty() && p->withoutBraces)) {
    _setComment(p->vParent.back().val, &Value::set_comment_inside, p, p->vParent.back().ciElemBefore);
    _next(p);
    p->vState.back() = ParseState::ValueEnd;
  } else {
    p->vState.back() = ParseState::MapElemBegin;
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Hjson::Type enum from hjson.h
enum class Type {
  Undefined,
  Null,
  Bool,
  Double,
  Int64,
  String,
  Vector,
  Map
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

static CommentInfo _white(Parser *p);

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ci)
{
  if (ci.hasComment) {
    (val.*fp)(std::string(p->data + ci.cmStart, p->data + ci.cmEnd));
  }
}

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ciA, const CommentInfo& ciB)
{
  if (ciA.hasComment && ciB.hasComment) {
    (val.*fp)(std::string(p->data + ciA.cmStart, p->data + ciA.cmEnd) +
      std::string(p->data + ciB.cmStart, p->data + ciB.cmEnd));
  } else if (!ciA.hasComment && !ciB.hasComment) {
    (val.*fp)("");
  } else {
    _setComment(val, fp, p, ciA);
    _setComment(val, fp, p, ciB);
  }
}

// Reachability: _readObjectBegin dereferences vParent.back() before checking vParent.empty(). The empty-parent && withoutBraces true outcome is infeasible for valid state; never force it via an empty stack.
```

---

## L586

**Focal:** `static void _readObjectElemBegin(Parser* p)`  
**Source:** [allhjson/hjson_decode.cpp:586-617](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L586-L617)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
static void _readObjectElemBegin(Parser* p) {
  Value &object = p->vParent.back().val;

  if (p->ch == 0) {
    if (p->vParent.size() == 1 && p->withoutBraces) {
      if (object.empty()) {
        _setComment(object, &Value::set_comment_inside, p, p->vParent.back().ciElemBefore);
      } else {
        _setComment(object[static_cast<int>(object.size() - 1)],
          &Value::set_comment_after, p, p->vParent.back().ciElemBefore, p->vParent.back().ciElemExtra);
      }
      p->vState.back() = ParseState::ValueEnd;
      return;
    } else {
      throw syntax_error(_errAt(p, "End of input while parsing an object (did you forget a closing '}'?)"));
    }
  }

  p->vParent.back().key = _readKeyname(p);
  if (p->opt.duplicateKeyException && object[p->vParent.back().key].defined()) {
    throw syntax_error(_errAt(p, "Found duplicate of key '" + p->vParent.back().key + "'"));
  }
  p->vParent.back().ciKey = _white(p);
  if (p->ch != ':') {
    throw syntax_error(_errAt(p, std::string(
      "Expected ':' instead of '") + (char)(p->ch) + "'"));
  }
  _next(p);
  p->vState.back() = ParseState::MapElemEnd;
  p->vState.push_back(ParseState::ValueBegin);
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Decoder options from hjson.h
struct DecoderOptions {
  // Keep all comments from the Hjson input, store them in
  // the Hjson::Value objects.
  bool comments = true;
  // Store all whitespace and comments in the Hjson::Value objects so that
  // linefeeds and custom indentation is kept. The "comments" option is
  // ignored if this option is true.
  bool whitespaceAsComments = false;
  // If true, an Hjson::syntax_error exception is thrown from the unmarshal
  // functions if a map contains duplicate keys.
  bool duplicateKeyException = false;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ci)
{
  if (ci.hasComment) {
    (val.*fp)(std::string(p->data + ci.cmStart, p->data + ci.cmEnd));
  }
}

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ciA, const CommentInfo& ciB)
{
  if (ciA.hasComment && ciB.hasComment) {
    (val.*fp)(std::string(p->data + ciA.cmStart, p->data + ciA.cmEnd) +
      std::string(p->data + ciB.cmStart, p->data + ciB.cmEnd));
  } else if (!ciA.hasComment && !ciB.hasComment) {
    (val.*fp)("");
  } else {
    _setComment(val, fp, p, ciA);
    _setComment(val, fp, p, ciB);
  }
}

static std::string _errAt(Parser *p, const std::string& message);

static std::string _readKeyname(Parser *p);

static CommentInfo _white(Parser *p);

static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}

// Entry state for _readObjectElemBegin: p.vParent.back().val is an existing Map, key cursor at first key character (or closing brace), and vState.back()==MapElemBegin.
```

---

## L619

**Focal:** `static void _readObjectElemEnd(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:619-656](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L619-L656)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 6, *not an LLVM coverage measurement*

### Focal method

```cpp
static void _readObjectElemEnd(Parser *p) {
  Value elem = p->vParent.back().val;
  p->vParent.pop_back();
  _setComment(elem, &Value::set_comment_key, p, p->vParent.back().ciKey);
  if (!elem.get_comment_before().empty()) {
    elem.set_comment_key(elem.get_comment_key() +
      elem.get_comment_before());
    elem.set_comment_before("");
  }
  _setComment(elem, &Value::set_comment_before, p, p->vParent.back().ciElemBefore, p->vParent.back().ciElemExtra);
  auto ciAfter = _white(p);

  // in Hjson the comma is optional and trailing commas are allowed
  if (p->ch == ',') {
    _next(p);
    // It is unlikely that someone writes a comment after the value but
    // before the comma, so we include any such comment in "comment_after".
    p->vParent.back().ciElemExtra = _white(p);
  } else {
    p->vParent.back().ciElemExtra = {};
  }

  if (p->ch == '}' && !(p->vParent.size() == 1 && p->withoutBraces)) {
    auto existingAfter = elem.get_comment_after();
    _setComment(elem, &Value::set_comment_after, p, ciAfter, p->vParent.back().ciElemExtra);
    if (!existingAfter.empty()) {
      elem.set_comment_after(existingAfter + elem.get_comment_after());
    }
    p->vParent.back().val[p->vParent.back().key].assign_with_comments(std::move(elem));
    _next(p);
    p->vState.back() = ParseState::ValueEnd;
  } else {
    p->vParent.back().val[p->vParent.back().key].assign_with_comments(std::move(elem));
    p->vParent.back().ciElemBefore = ciAfter;
    p->vState.back() = ParseState::MapElemBegin;
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ci)
{
  if (ci.hasComment) {
    (val.*fp)(std::string(p->data + ci.cmStart, p->data + ci.cmEnd));
  }
}

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ciA, const CommentInfo& ciB)
{
  if (ciA.hasComment && ciB.hasComment) {
    (val.*fp)(std::string(p->data + ciA.cmStart, p->data + ciA.cmEnd) +
      std::string(p->data + ciB.cmStart, p->data + ciB.cmEnd));
  } else if (!ciA.hasComment && !ciB.hasComment) {
    (val.*fp)("");
  } else {
    _setComment(val, fp, p, ciA);
    _setComment(val, fp, p, ciB);
  }
}

static CommentInfo _white(Parser *p);

static bool _next(Parser *p) {
  // get the next character.
  if (p->indexNext < p->dataSize) {
    p->ch = p->data[p->indexNext++];
    return true;
  }

  ++p->indexNext;
  p->ch = 0;

  return false;
}
```

---

## L658

**Focal:** `static void _readValueBegin(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:658-687](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L658-L687)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 4, *not an LLVM coverage measurement*

### Focal method

```cpp
// Parse a Hjson value. It could be an object, an array, a string, a number or a word.
static void _readValueBegin(Parser *p) {
  p->vParent.push_back(DecodeParent());
  p->vParent.back().ciBefore = _white(p);

  if ((p->ch == '{')) {

    p->vState.back() = ParseState::MapBegin;
    
  
  } else if ((p->ch == '[')) {

    p->vState.back() =  ParseState::VectorBegin;
    
  
  } else if ((p->ch == '"') || (p->ch == '\'')) {

    p->vParent.back().val.assign_with_comments(_readString(p, true));
    p->vState.back() = ParseState::ValueEnd;
    
  
  } else {

    p->vParent.back().val.assign_with_comments(_readTfnns(p));
    p->vState.back() = ParseState::ValueEnd;
    
  
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static CommentInfo _white(Parser *p);

static std::string _readString(Parser *p, bool allowML);

static Value _readTfnns(Parser *p);
```

---

## L705

**Focal:** `static void _parseLoop(Parser* p)`  
**Source:** [allhjson/hjson_decode.cpp:705-745](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L705-L745)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 8, *not an LLVM coverage measurement*

### Focal method

```cpp
static void _parseLoop(Parser* p) {
  while (!p->vState.empty()) {
    if ((p->vState.back() == ParseState::ValueBegin)) {

      _readValueBegin(p);
      
    
    } else if ((p->vState.back() == ParseState::ValueEnd)) {

      _readValueEnd(p);
      
    
    } else if ((p->vState.back() == ParseState::MapBegin)) {

      _readObjectBegin(p);
      
    
    } else if ((p->vState.back() == ParseState::MapElemBegin)) {

      _readObjectElemBegin(p);
      
    
    } else if ((p->vState.back() == ParseState::MapElemEnd)) {

      _readObjectElemEnd(p);
      
    
    } else if ((p->vState.back() == ParseState::VectorBegin)) {

      _readArrayBegin(p);
      
    
    } else if ((p->vState.back() == ParseState::VectorElemEnd)) {

      _readArrayElemEnd(p);
      
    
    }
  }
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static void _readValueBegin(Parser *p);

static void _readValueEnd(Parser *p);

static void _readObjectBegin(Parser *p);

static void _readObjectElemBegin(Parser* p);

static void _readObjectElemEnd(Parser *p);

static void _readArrayBegin(Parser* p);

static void _readArrayElemEnd(Parser* p);
```

---

## L747

**Focal:** `static Value _rootValue(Parser *p)`  
**Source:** [allhjson/hjson_decode.cpp:747-800](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L747-L800)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
// Braces for the root object are optional
static Value _rootValue(Parser *p) {
  CommentInfo ciExtra;

  p->vParent.push_back(DecodeParent());
  p->vParent.back().ciBefore = _white(p);

  if (p->ch == '[') {
    p->vState.push_back(ParseState::VectorBegin);
  } else {
    if (p->ch != '{') {
      // Assume root object without braces
      p->withoutBraces = true;
    }
    p->vState.push_back(ParseState::MapBegin);
  }

  try {
    _parseLoop(p);
    if (_hasTrailing(p, &ciExtra)) {
      throw syntax_error(_errAt(p, "Syntax error, found trailing characters"));
    }
  } catch (const syntax_error& e1) {
    if (p->withoutBraces) {
      // test if we are dealing with a single JSON value instead (true/false/null/num/"")
      _resetAt(p);
      p->vParent.clear();
      p->vState.clear();
      p->vState.push_back(ParseState::ValueBegin);
      try {
        _parseLoop(p);
        if (_hasTrailing(p, &ciExtra)) {
          throw syntax_error(_errAt(p, "Syntax error, found trailing characters"));
        }
      } catch (const syntax_error&) {
        throw e1;
      }
    } else {
      throw e1;
    }
  }

  Value ret = p->vParent.back().val;
  if (ciExtra.hasComment) {
    auto existingAfter = ret.get_comment_after();
    _setComment(ret, &Value::set_comment_after, p, ciExtra);
    if (!existingAfter.empty()) {
      ret.set_comment_after(existingAfter + ret.get_comment_after());
    }
  }

  return ret;
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static CommentInfo _white(Parser *p);

static void _parseLoop(Parser* p);

static Value _hasTrailing(Parser *p, CommentInfo *ci);

static std::string _errAt(Parser *p, const std::string& message);

static void _resetAt(Parser *p);

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ci)
{
  if (ci.hasComment) {
    (val.*fp)(std::string(p->data + ci.cmStart, p->data + ci.cmEnd));
  }
}

inline void _setComment(Value& val, void (Value::*fp)(const std::string&),
  Parser *p, const CommentInfo& ciA, const CommentInfo& ciB)
{
  if (ciA.hasComment && ciB.hasComment) {
    (val.*fp)(std::string(p->data + ciA.cmStart, p->data + ciA.cmEnd) +
      std::string(p->data + ciB.cmStart, p->data + ciB.cmEnd));
  } else if (!ciA.hasComment && !ciB.hasComment) {
    (val.*fp)("");
  } else {
    _setComment(val, fp, p, ciA);
    _setComment(val, fp, p, ciB);
  }
}
```

---

## L802

**Focal:** `Value Unmarshal(const char *data, size_t dataSize, const DecoderOptions& options)`  
**Source:** [allhjson/hjson_decode.cpp:802-823](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L802-L823)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
// Unmarshal parses the Hjson-encoded data and returns a tree of Values.
//
// Unmarshal uses the inverse of the encodings that Marshal uses.
//
Value Unmarshal(const char *data, size_t dataSize, const DecoderOptions& options) {
  Parser parser = {
    (const unsigned char*) data,
    dataSize,
    0,
    ' ',
    false,
    options
  };

  if (parser.opt.whitespaceAsComments) {
    parser.opt.comments = true;
  }

  _resetAt(&parser);
  return _rootValue(&parser);
}
```

### Context

```cpp
// Original parser state declarations from hjson.h
enum class ParseState {
  ValueBegin,
  ValueEnd,
  VectorBegin,
  VectorElemEnd,
  MapBegin,
  MapElemBegin,
  MapElemEnd,
};

struct CommentInfo {
  CommentInfo() : hasComment(false), cmStart(0), cmEnd(0) {}
  bool hasComment;
  int cmStart, cmEnd;
};

struct DecodeParent {
  Value val;
  CommentInfo ciBefore, ciKey, ciElemBefore, ciElemExtra;
  std::string key;
};

struct Parser {
  const unsigned char *data;
  size_t dataSize;
  int indexNext;
  unsigned char ch;
  bool withoutBraces;
  DecoderOptions opt;
  std::vector<ParseState> vState;
  std::vector<DecodeParent> vParent;
};

// Decoder options from hjson.h
struct DecoderOptions {
  // Keep all comments from the Hjson input, store them in
  // the Hjson::Value objects.
  bool comments = true;
  // Store all whitespace and comments in the Hjson::Value objects so that
  // linefeeds and custom indentation is kept. The "comments" option is
  // ignored if this option is true.
  bool whitespaceAsComments = false;
  // If true, an Hjson::syntax_error exception is thrown from the unmarshal
  // functions if a map contains duplicate keys.
  bool duplicateKeyException = false;
};

// Direct helpers in the original source (definitions when short, otherwise declarations)
static void _resetAt(Parser *p);

static Value _rootValue(Parser *p);
```

---

## L825

**Focal:** `Value Unmarshal(const char *data, const DecoderOptions& options)`  
**Source:** [allhjson/hjson_decode.cpp:825-832](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L825-L832)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value Unmarshal(const char *data, const DecoderOptions& options) {
  if (!data) {
    return Value();
  }

  return Unmarshal(data, std::strlen(data), options);
}
```

### Context

```cpp

```

---

## L839

**Focal:** `Value UnmarshalFromFile(const std::string &path, const DecoderOptions& options)`  
**Source:** [allhjson/hjson_decode.cpp:839-864](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_decode.cpp#L839-L864)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
Value UnmarshalFromFile(const std::string &path, const DecoderOptions& options) {
  std::ifstream infile(path, std::ifstream::ate | std::ifstream::binary);
  if (!infile.is_open()) {
    throw file_error("Could not open file '" + path + "' for reading");
  }
  std::string inStr;
  size_t len = infile.tellg();
  inStr.resize(len);
  infile.seekg(0, std::ios::beg);
  infile.read(&inStr[0], inStr.size());
  infile.close();

  while (len > 0 && inStr.at(len - 1) == '\0') {
    --len;
  }

  if (len > 0 && inStr.at(len - 1) == '\n') {
    --len;
  }
  if (len > 0 && inStr.at(len - 1) == '\r') {
    --len;
  }

  return Unmarshal(inStr.c_str(), len, options);
}
```

### Context

```cpp

```

