# allhjson/hjson_value.cpp

73 focal methods with source-level branch indicators. Source commit: `d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3`.

[Overview](../README.md) · [Machine-readable JSONL](../focal_methods.jsonl)

## Functions

| Source line | Focal method |
| --- | --- |
| [L96](#l96) | `Value::ValueImpl::ValueImpl(Type _type) : type(_type)` |
| [L118](#l118) | `void Value::ValueImpl::DeepClear(Value &val)` |
| [L143](#l143) | `Value::ValueImpl::~ValueImpl()` |
| [L282](#l282) | `Value::Value(const Value& other) : prv(other.prv)` |
| [L319](#l319) | `Value& Value::operator=(const Value& other)` |
| [L332](#l332) | `Value& Value::operator=(Value&& other)` |
| [L345](#l345) | `const Value& Value::at(const std::string& name) const` |
| [L365](#l365) | `Value& Value::at(const std::string& name)` |
| [L395](#l395) | `const Value Value::operator[](const std::string& name) const` |
| [L410](#l410) | `MapProxy Value::operator[](const std::string& name)` |
| [L447](#l447) | `const Value& Value::operator[](int index) const` |
| [L480](#l480) | `Value& Value::operator[](int index)` |
| [L595](#l595) | `Value operator+(const Value& a, const Value& b)` |
| [L624](#l624) | `bool operator<(const Value& a, const Value& b)` |
| [L653](#l653) | `bool operator>(const Value& a, const Value& b)` |
| [L682](#l682) | `bool operator<=(const Value& a, const Value& b)` |
| [L711](#l711) | `bool operator>=(const Value& a, const Value& b)` |
| [L740](#l740) | `bool operator==(const Value& a, const Value& b)` |
| [L792](#l792) | `Value operator-(const Value& a, const Value& b)` |
| [L817](#l817) | `Value operator*(const Value& a, const Value& b)` |
| [L842](#l842) | `Value operator/(const Value& a, const Value& b)` |
| [L867](#l867) | `Value operator%(const Value& a, const Value& b)` |
| [L911](#l911) | `Value& Value::operator+=(const std::string& b)` |
| [L922](#l922) | `Value& Value::operator+=(const Value& b)` |
| [L966](#l966) | `Value& Value::operator*=(const Value& b)` |
| [L998](#l998) | `Value& Value::operator/=(const Value& b)` |
| [L1030](#l1030) | `Value& Value::operator%=(const Value& b)` |
| [L1041](#l1041) | `Value Value::operator+() const` |
| [L1061](#l1061) | `Value Value::operator-() const` |
| [L1081](#l1081) | `Value& Value::operator++()` |
| [L1103](#l1103) | `Value& Value::operator--()` |
| [L1125](#l1125) | `Value Value::operator++(int)` |
| [L1151](#l1151) | `Value Value::operator--(int)` |
| [L1177](#l1177) | `Value::operator bool() const` |
| [L1201](#l1201) | `Value::operator double() const` |
| [L1239](#l1239) | `Value::operator long long() const` |
| [L1256](#l1256) | `Value::operator const char*() const` |
| [L1265](#l1265) | `Value::operator std::string() const` |
| [L1279](#l1279) | `bool Value::empty() const` |
| [L1293](#l1293) | `bool Value::is_container() const` |
| [L1298](#l1298) | `bool Value::is_numeric() const` |
| [L1303](#l1303) | `size_t Value::size() const` |
| [L1318](#l1318) | `bool Value::deep_equal(const Value& other) const` |
| [L1365](#l1365) | `Value Value::clone() const` |
| [L1396](#l1396) | `void Value::clear()` |
| [L1414](#l1414) | `void Value::erase(int index)` |
| [L1448](#l1448) | `void Value::push_back(const Value& other)` |
| [L1461](#l1461) | `void Value::move(int from, int to)` |
| [L1511](#l1511) | `std::string Value::key(int index) const` |
| [L1527](#l1527) | `ValueMap::iterator Value::begin()` |
| [L1538](#l1538) | `ValueMap::iterator Value::end()` |
| [L1549](#l1549) | `ValueMap::const_iterator Value::begin() const` |
| [L1560](#l1560) | `ValueMap::const_iterator Value::end() const` |
| [L1571](#l1571) | `size_t Value::erase(const std::string &key)` |
| [L1599](#l1599) | `double Value::to_double() const` |
| [L1658](#l1658) | `std::int64_t Value::to_int64() const` |
| [L1718](#l1718) | `std::string Value::to_string() const` |
| [L1831](#l1831) | `void Value::set_comment_before(const std::string& str)` |
| [L1843](#l1843) | `std::string Value::get_comment_before() const` |
| [L1852](#l1852) | `void Value::set_comment_key(const std::string& str)` |
| [L1864](#l1864) | `std::string Value::get_comment_key() const` |
| [L1873](#l1873) | `void Value::set_comment_inside(const std::string& str)` |
| [L1885](#l1885) | `std::string Value::get_comment_inside() const` |
| [L1894](#l1894) | `void Value::set_comment_after(const std::string& str)` |
| [L1906](#l1906) | `std::string Value::get_comment_after() const` |
| [L1915](#l1915) | `void Value::set_comments(const Value& other)` |
| [L1933](#l1933) | `Value& Value::assign_with_comments(const Value& other)` |
| [L1943](#l1943) | `Value& Value::assign_with_comments(Value&& other)` |
| [L1953](#l1953) | `MapProxy::MapProxy(std::shared_ptr<ValueImpl> _parent, const std::string &_key, Value *_pTarget) : Value(_pTarget ? _pTarget->prv ` |
| [L1971](#l1971) | `MapProxy::~MapProxy()` |
| [L2018](#l2018) | `MapProxy& MapProxy::assign_with_comments(const Value& other)` |
| [L2028](#l2028) | `MapProxy& MapProxy::assign_with_comments(Value&& other)` |
| [L2038](#l2038) | `Value Merge(const Value& base, const Value& ext)` |

## L96

**Focal:** `Value::ValueImpl::ValueImpl(Type _type) : type(_type)`  
**Source:** [allhjson/hjson_value.cpp:96-116](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L96-L116)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 3, *not an LLVM coverage measurement*

### Focal method

```cpp
Value::ValueImpl::ValueImpl(Type _type)
  : type(_type)
{
  if ((_type == Type::String)) {

    s = new std::string();
    
  
  } else if ((_type == Type::Vector)) {

    v = new ValueVec();
    
  
  } else if ((_type == Type::Map)) {

    m = new ValueVecMap();
    
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L118

**Focal:** `void Value::ValueImpl::DeepClear(Value &val)`  
**Source:** [allhjson/hjson_value.cpp:118-141](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L118-L141)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 6, *not an LLVM coverage measurement*

### Focal method

```cpp
// Bottom-up destruction in order to avoid stack overflow due to recursive destructor calls.
void Value::ValueImpl::DeepClear(Value &val) {
  // The map/vector will only be destroyed if use_count == 1
  if (val.size() && val.prv.use_count() == 1) {
    std::vector<std::pair<Value, int> > v;

    v.emplace_back(val, 0);

    while (!v.empty()) {
      if (v.back().second >= v.back().first.size()) {
        v.back().first.clear();
        v.pop_back();
      } else {
        Value &n = v.back().first[v.back().second];
        v.back().second++;
        // The map/vector will only be destroyed if use_count == 1
        if (n.size() && n.prv.use_count() == 1) {
          v.emplace_back(v.back().first[v.back().second - 1], 0);
        }
      }
    }
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L143

**Focal:** `Value::ValueImpl::~ValueImpl()`  
**Source:** [allhjson/hjson_value.cpp:143-167](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L143-L167)  
**Access:** `include_defining_cpp_in_harness`  
**Lexical branch indicators:** 5, *not an LLVM coverage measurement*

### Focal method

```cpp
Value::ValueImpl::~ValueImpl() {
  if ((type == Type::String)) {

    delete s;
    
  
  } else if ((type == Type::Vector)) {

    for (auto e = v->begin(); e != v->end(); ++e) {
      DeepClear(*e);
    }
    delete v;
    
  
  } else if ((type == Type::Map)) {

    for (auto e = m->m.begin(); e != m->m.end(); ++e) {
      DeepClear(e->second);
    }
    delete m;
    
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L282

**Focal:** `Value::Value(const Value& other) : prv(other.prv)`  
**Source:** [allhjson/hjson_value.cpp:282-291](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L282-L291)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value::Value(const Value& other)
  : prv(other.prv)
{
  if (other.cm) {
    // Clone the comments instead of sharing the reference. This way a change
    // in the other Value does not affect the comments in this Value.
    cm.reset(new Comments(*other.cm));
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Copy/assignment semantics: `prv` is shared; copy construction clones Comments, not the payload. Assignment to a defined destination preserves its old comments; assignment to Undefined adopts source comments. A move assignment copies shared pointers and does not guarantee that the source becomes empty.
```

---

## L319

**Focal:** `Value& Value::operator=(const Value& other)`  
**Source:** [allhjson/hjson_value.cpp:319-330](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L319-L330)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator=(const Value& other) {
  // So that comments are kept when assigning a Value to a new key in a map,
  // or to a variable that has not been assigned any other value yet.
  if (!this->defined()) {
    this->set_comments(other);
  }

  this->prv = other.prv;

  return *this;
}
```

### Context

```cpp
// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Copy/assignment semantics: `prv` is shared; copy construction clones Comments, not the payload. Assignment to a defined destination preserves its old comments; assignment to Undefined adopts source comments. A move assignment copies shared pointers and does not guarantee that the source becomes empty.
```

---

## L332

**Focal:** `Value& Value::operator=(Value&& other)`  
**Source:** [allhjson/hjson_value.cpp:332-343](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L332-L343)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator=(Value&& other) {
  // So that comments are kept when assigning a Value to a new key in a map,
  // or to a variable that has not been assigned any other value yet.
  if (!this->defined()) {
    this->cm = other.cm;
  }

  this->prv = other.prv;

  return *this;
}
```

### Context

```cpp
// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Copy/assignment semantics: `prv` is shared; copy construction clones Comments, not the payload. Assignment to a defined destination preserves its old comments; assignment to Undefined adopts source comments. A move assignment copies shared pointers and does not guarantee that the source becomes empty.
```

---

## L345

**Focal:** `const Value& Value::at(const std::string& name) const`  
**Source:** [allhjson/hjson_value.cpp:345-363](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L345-L363)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
const Value& Value::at(const std::string& name) const {
  if ((prv->type == Type::Undefined)) {

    throw index_out_of_bounds("Key not found.");
  
  } else if ((prv->type == Type::Map)) {

    try {
      return prv->m->m.at(name);
    } catch(const std::out_of_range&) {}
    throw index_out_of_bounds("Key not found.");
  
  } else {

    throw type_mismatch("Must be of type Map for that operation.");
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L365

**Focal:** `Value& Value::at(const std::string& name)`  
**Source:** [allhjson/hjson_value.cpp:365-383](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L365-L383)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::at(const std::string& name) {
  if ((prv->type == Type::Undefined)) {

    throw index_out_of_bounds("Key not found.");
  
  } else if ((prv->type == Type::Map)) {

    try {
      return prv->m->m.at(name);
    } catch(const std::out_of_range&) {}
    throw index_out_of_bounds("Key not found.");
  
  } else {

    throw type_mismatch("Must be of type Map for that operation.");
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L395

**Focal:** `const Value Value::operator[](const std::string& name) const`  
**Source:** [allhjson/hjson_value.cpp:395-408](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L395-L408)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 3, *not an LLVM coverage measurement*

### Focal method

```cpp
const Value Value::operator[](const std::string& name) const {
  if (prv->type == Type::Undefined) {
    return Value();
  } else if (prv->type == Type::Map) {
    auto it = prv->m->m.find(name);
    if (it == prv->m->m.end()) {
      return Value();
    }
    return it->second;
  }

  throw type_mismatch("Must be of type Undefined or Map for that operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L410

**Focal:** `MapProxy Value::operator[](const std::string& name)`  
**Source:** [allhjson/hjson_value.cpp:410-425](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L410-L425)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 3, *not an LLVM coverage measurement*

### Focal method

```cpp
MapProxy Value::operator[](const std::string& name) {
  if (prv->type == Type::Undefined) {
    prv->~ValueImpl();
    // Recreate the private object using the same memory block.
    new(&(*prv)) ValueImpl(Type::Map);
  } else if (prv->type != Type::Map) {
    throw type_mismatch("Must be of type Undefined or Map for that operation.");
  }

  auto it = prv->m->m.find(name);
  if (it == prv->m->m.end()) {
    return MapProxy(prv, name, 0);
  }
  return MapProxy(prv, name, &it->second);
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Original MapProxy declaration from hjson.h
// MapProxy is only used for temporary references to elements in a Map. It is
// not possible to store a MapProxy in a variable. It only exists to make it
// possible to check for the existence of a specific key in a Map without
// creating an empty element in the Map with that key.
class MapProxy : public Value {
  private:
  friend class Value;

  std::shared_ptr<ValueImpl> parentPrv;
  std::string key;
  Value *pTarget;
  // True if an explicit assignment has been made to this MapProxy.
  bool wasAssigned;

  MapProxy(std::shared_ptr<ValueImpl> parent, const std::string& key,
    Value *pTarget);

  // Make the copy constructor private in order to avoid accidental creation of
  // MapProxy variables like this:
  //   auto myVal = val["one"];
  MapProxy(const MapProxy&) = default;
  MapProxy(Value&&);

public:
  ~MapProxy() override;
  MapProxy& operator =(const MapProxy&);
  MapProxy& operator =(const Value&);
  MapProxy& operator =(Value&&);
  MapProxy& assign_with_comments(const MapProxy&);
  MapProxy& assign_with_comments(const Value&);
  MapProxy& assign_with_comments(Value&&);
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// MapProxy lifecycle: a temporary missing-key read is not inserted unless explicitly assigned or made nonempty; normal obj["key"] = Value(...) commits at proxy destruction. A nonconst [] on Undefined converts the parent to Map. Do not store/copy a proxy to postpone destructor effects.
```

---

## L447

**Focal:** `const Value& Value::operator[](int index) const`  
**Source:** [allhjson/hjson_value.cpp:447-478](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L447-L478)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
const Value& Value::operator[](int index) const {
  if ((prv->type == Type::Undefined)) {

    throw index_out_of_bounds("Index out of bounds.");
  
  } else if ((prv->type == Type::Vector) || (prv->type == Type::Map)) {

    if (index < 0 || index >= size()) {
      throw index_out_of_bounds("Index out of bounds.");
    }

    if ((prv->type == Type::Vector)) {

      return prv->v[0][index];
    
    } else if ((prv->type == Type::Map)) {

      {
        auto it = prv->m->m.find(prv->m->v[index]);
        assert(it != prv->m->m.end());
        return it->second;
      }
    
    }
  
  } else {

    throw type_mismatch("Must be of type Undefined, Vector or Map for that operation.");
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Reachability: inside Vector||Map, the later else-if Map false outcome is impossible after Vector has already been excluded. Never force an invalid type discriminator to cover it.
```

---

## L480

**Focal:** `Value& Value::operator[](int index)`  
**Source:** [allhjson/hjson_value.cpp:480-511](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L480-L511)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator[](int index) {
  if ((prv->type == Type::Undefined)) {

    throw index_out_of_bounds("Index out of bounds.");
  
  } else if ((prv->type == Type::Vector) || (prv->type == Type::Map)) {

    if (index < 0 || index >= size()) {
      throw index_out_of_bounds("Index out of bounds.");
    }

    if ((prv->type == Type::Vector)) {

      return prv->v[0][index];
    
    } else if ((prv->type == Type::Map)) {

      {
        auto it = prv->m->m.find(prv->m->v[index]);
        assert(it != prv->m->m.end());
        return it->second;
      }
    
    }
  
  } else {

    throw type_mismatch("Must be of type Undefined, Vector or Map for that operation.");
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Reachability: after the outer Vector||Map and the first Vector branch, the Map comparison cannot be false in a valid execution.
```

---

## L595

**Focal:** `Value operator+(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:595-622](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L595-L622)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 8, *not an LLVM coverage measurement*

### Focal method

```cpp
Value operator+(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d + b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i + b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    throw type_mismatch("The values must be of the same type for this operation.");
  }

  if ((a.prv->type == Type::Double)) {

    return a.prv->d + b.prv->d;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i + b.prv->i;
  
  } else if ((a.prv->type == Type::String)) {

    return *a.prv->s + *b.prv->s;
  
  }

  throw type_mismatch("The values must be of type Double, Int64 or String for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L624

**Focal:** `bool operator<(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:624-651](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L624-L651)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 8, *not an LLVM coverage measurement*

### Focal method

```cpp
bool operator<(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d < b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i < b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    throw type_mismatch("The values must be of the same type for this operation.");
  }

  if ((a.prv->type == Type::Double)) {

    return a.prv->d < b.prv->d;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i < b.prv->i;
  
  } else if ((a.prv->type == Type::String)) {

    return *a.prv->s < *b.prv->s;
  
  }

  throw type_mismatch("The values must be of type Double, Int64 or String for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L653

**Focal:** `bool operator>(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:653-680](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L653-L680)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 8, *not an LLVM coverage measurement*

### Focal method

```cpp
bool operator>(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d > b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i > b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    throw type_mismatch("The values must be of the same type for this operation.");
  }

  if ((a.prv->type == Type::Double)) {

    return a.prv->d > b.prv->d;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i > b.prv->i;
  
  } else if ((a.prv->type == Type::String)) {

    return *a.prv->s > *b.prv->s;
  
  }

  throw type_mismatch("The values must be of type Double, Int64 or String for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L682

**Focal:** `bool operator<=(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:682-709](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L682-L709)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 8, *not an LLVM coverage measurement*

### Focal method

```cpp
bool operator<=(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d <= b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i <= b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    throw type_mismatch("The values must be of the same type for this operation.");
  }

  if ((a.prv->type == Type::Double)) {

    return a.prv->d <= b.prv->d;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i <= b.prv->i;
  
  } else if ((a.prv->type == Type::String)) {

    return *a.prv->s <= *b.prv->s;
  
  }

  throw type_mismatch("The values must be of type Double, Int64 or String for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L711

**Focal:** `bool operator>=(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:711-738](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L711-L738)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 8, *not an LLVM coverage measurement*

### Focal method

```cpp
bool operator>=(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d >= b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i >= b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    throw type_mismatch("The values must be of the same type for this operation.");
  }

  if ((a.prv->type == Type::Double)) {

    return a.prv->d >= b.prv->d;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i >= b.prv->i;
  
  } else if ((a.prv->type == Type::String)) {

    return *a.prv->s >= *b.prv->s;
  
  }

  throw type_mismatch("The values must be of type Double, Int64 or String for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L740

**Focal:** `bool operator==(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:740-785](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L740-L785)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 13, *not an LLVM coverage measurement*

### Focal method

```cpp
bool operator==(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d == b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i == b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    return false;
  }

  if ((a.prv->type == Type::Undefined) || (a.prv->type == Type::Null)) {

    return true;
  
  } else if ((a.prv->type == Type::Bool)) {

    return a.prv->b == b.prv->b;
  
  } else if ((a.prv->type == Type::Double)) {

    return a.prv->d == b.prv->d;
  
  } else if ((a.prv->type == Type::String)) {

    return *a.prv->s == *b.prv->s;
  
  } else if ((a.prv->type == Type::Vector)) {

    return a.prv->v == b.prv->v;
  
  } else if ((a.prv->type == Type::Map)) {

    return a.prv->m == b.prv->m;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i == b.prv->i;
  
  }

  assert(!"Unknown type");

  return false;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Value-Value == compares Vector/Map backing pointer identity, not structural content; deep_equal is separate. Use Value operands on both sides to select this focal overload, not Value==bool. The unknown Type assertion is not reachable with valid Type tags.
```

---

## L792

**Focal:** `Value operator-(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:792-815](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L792-L815)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
Value operator-(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d - b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i - b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    throw type_mismatch("The values must be of the same type for this operation.");
  }

  if ((a.prv->type == Type::Double)) {

    return a.prv->d - b.prv->d;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i - b.prv->i;
  
  }

  throw type_mismatch("The values must be of type Double or Int64 for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Avoid signed int64 overflow and negating INT64_MIN in generated tests; these are undefined behavior rather than valid coverage targets.
```

---

## L817

**Focal:** `Value operator*(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:817-840](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L817-L840)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
Value operator*(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d * b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i * b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    throw type_mismatch("The values must be of the same type for this operation.");
  }

  if ((a.prv->type == Type::Double)) {

    return a.prv->d * b.prv->d;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i * b.prv->i;
  
  }

  throw type_mismatch("The values must be of type Double or Int64 for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L842

**Focal:** `Value operator/(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:842-865](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L842-L865)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
Value operator/(const Value& a, const Value& b) {
  if (a.prv->type == Type::Double && b.prv->type == Type::Int64) {
    return a.prv->d / b.prv->i;
  } else if (a.prv->type == Type::Int64 && b.prv->type == Type::Double) {
    return a.prv->i / b.prv->d;
  }

  if (a.prv->type != b.prv->type) {
    throw type_mismatch("The values must be of the same type for this operation.");
  }

  if ((a.prv->type == Type::Double)) {

    return a.prv->d / b.prv->d;
  
  } else if ((a.prv->type == Type::Int64)) {

    return a.prv->i / b.prv->i;
  
  }

  throw type_mismatch("The values must be of type Double or Int64 for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Use a nonzero integer divisor; division/remainder by zero is undefined behavior, not an expected Hjson type_mismatch outcome.
```

---

## L867

**Focal:** `Value operator%(const Value& a, const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:867-874](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L867-L874)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value operator%(const Value& a, const Value& b) {
  if (a.prv->type != b.prv->type || a.prv->type != Type::Int64) {
    throw type_mismatch("The values must be of the Int64 type for this operation.");
  }

  return a.prv->i % b.prv->i;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Use a nonzero integer divisor; division/remainder by zero is undefined behavior, not an expected Hjson type_mismatch outcome.
```

---

## L911

**Focal:** `Value& Value::operator+=(const std::string& b)`  
**Source:** [allhjson/hjson_value.cpp:911-920](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L911-L920)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator+=(const std::string& b) {
  if (prv->type != Type::String) {
    throw type_mismatch("The value must be of type String for this operation.");
  }

  *prv->s += b;

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L922

**Focal:** `Value& Value::operator+=(const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:922-957](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L922-L957)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 8, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator+=(const Value& b) {
  if (prv->type == Type::Double && b.prv->type == Type::Int64) {
    prv->d += b.prv->i;
  } else if (prv->type == Type::Int64 && b.prv->type == Type::Double) {
    prv->i += static_cast<int64_t>(b.prv->d);
  } else {
    if (prv->type != b.prv->type) {
      throw type_mismatch("The values must be of the same type for this operation.");
    }

    if ((prv->type == Type::Double)) {

      prv->d += b.prv->d;
      
    
    } else if ((prv->type == Type::Int64)) {

      prv->i += b.prv->i;
      
    
    } else if ((prv->type == Type::String)) {

      *prv->s += *b.prv->s;
      
    
    } else {

      throw type_mismatch("The values must be of type Double, Int64 or String for this operation.");
      
    
    }
  }

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Avoid signed int64 overflow and negating INT64_MIN in generated tests; these are undefined behavior rather than valid coverage targets.
```

---

## L966

**Focal:** `Value& Value::operator*=(const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:966-996](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L966-L996)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator*=(const Value& b) {
  if (prv->type == Type::Double && b.prv->type == Type::Int64) {
    prv->d *= b.prv->i;
  } else if (prv->type == Type::Int64 && b.prv->type == Type::Double) {
    prv->i = static_cast<int64_t>(prv->i * b.prv->d);
  } else {
    if (prv->type != b.prv->type) {
      throw type_mismatch("The values must be of the same type for this operation.");
    }

    if ((prv->type == Type::Double)) {

      prv->d *= b.prv->d;
      
    
    } else if ((prv->type == Type::Int64)) {

      prv->i *= b.prv->i;
      
    
    } else {

      throw type_mismatch("The values must be of type Double or Int64 for this operation.");
      
    
    }
  }

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Avoid signed int64 overflow and negating INT64_MIN in generated tests; these are undefined behavior rather than valid coverage targets.
```

---

## L998

**Focal:** `Value& Value::operator/=(const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:998-1028](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L998-L1028)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator/=(const Value& b) {
  if (prv->type == Type::Double && b.prv->type == Type::Int64) {
    prv->d /= b.prv->i;
  } else if (prv->type == Type::Int64 && b.prv->type == Type::Double) {
    prv->i = static_cast<int64_t>(prv->i / b.prv->d);
  } else {
    if (prv->type != b.prv->type) {
      throw type_mismatch("The values must be of the same type for this operation.");
    }

    if ((prv->type == Type::Double)) {

      prv->d /= b.prv->d;
      
    
    } else if ((prv->type == Type::Int64)) {

      prv->i /= b.prv->i;
      
    
    } else {

      throw type_mismatch("The values must be of type Double or Int64 for this operation.");
      
    
    }
  }

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Use a nonzero integer divisor; division/remainder by zero is undefined behavior, not an expected Hjson type_mismatch outcome.
```

---

## L1030

**Focal:** `Value& Value::operator%=(const Value& b)`  
**Source:** [allhjson/hjson_value.cpp:1030-1039](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1030-L1039)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator%=(const Value& b) {
  if (prv->type != b.prv->type || prv->type != Type::Int64) {
    throw type_mismatch("The values must be of the Int64 type for this operation.");
  }

  prv->i %= b.prv->i;

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Use a nonzero integer divisor; division/remainder by zero is undefined behavior, not an expected Hjson type_mismatch outcome.
```

---

## L1041

**Focal:** `Value Value::operator+() const`  
**Source:** [allhjson/hjson_value.cpp:1041-1059](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1041-L1059)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value Value::operator+() const {
  if ((prv->type == Type::Double)) {

    return prv->d;
  
  } else if ((prv->type == Type::Int64)) {

    return prv->i;
  
  } else {

    throw type_mismatch("The value must be of type Double or Int64 for this operation.");
    
  
  }

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1061

**Focal:** `Value Value::operator-() const`  
**Source:** [allhjson/hjson_value.cpp:1061-1079](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1061-L1079)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value Value::operator-() const {
  if ((prv->type == Type::Double)) {

    return -prv->d;
  
  } else if ((prv->type == Type::Int64)) {

    return -prv->i;
  
  } else {

    throw type_mismatch("The value must be of type Double or Int64 for this operation.");
    
  
  }

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Avoid signed int64 overflow and negating INT64_MIN in generated tests; these are undefined behavior rather than valid coverage targets.
```

---

## L1081

**Focal:** `Value& Value::operator++()`  
**Source:** [allhjson/hjson_value.cpp:1081-1101](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1081-L1101)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator++() {
  if ((prv->type == Type::Double)) {

    prv->d++;
    
  
  } else if ((prv->type == Type::Int64)) {

    prv->i++;
    
  
  } else {

    throw type_mismatch("The values must be of type Double or Int64 for this operation.");
    
  
  }

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Avoid signed int64 overflow and negating INT64_MIN in generated tests; these are undefined behavior rather than valid coverage targets.
```

---

## L1103

**Focal:** `Value& Value::operator--()`  
**Source:** [allhjson/hjson_value.cpp:1103-1123](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1103-L1123)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::operator--() {
  if ((prv->type == Type::Double)) {

    prv->d--;
    
  
  } else if ((prv->type == Type::Int64)) {

    prv->i--;
    
  
  } else {

    throw type_mismatch("The values must be of type Double or Int64 for this operation.");
    
  
  }

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Avoid signed int64 overflow and negating INT64_MIN in generated tests; these are undefined behavior rather than valid coverage targets.
```

---

## L1125

**Focal:** `Value Value::operator++(int)`  
**Source:** [allhjson/hjson_value.cpp:1125-1149](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1125-L1149)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value Value::operator++(int) {
  Value ret;

  if ((prv->type == Type::Double)) {

    ret = prv->d;
    prv->d++;
    
  
  } else if ((prv->type == Type::Int64)) {

    ret = prv->i;
    prv->i++;
    
  
  } else {

    throw type_mismatch("The values must be of type Double or Int64 for this operation.");
    
  
  }

  return ret;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Avoid signed int64 overflow and negating INT64_MIN in generated tests; these are undefined behavior rather than valid coverage targets.
```

---

## L1151

**Focal:** `Value Value::operator--(int)`  
**Source:** [allhjson/hjson_value.cpp:1151-1175](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1151-L1175)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value Value::operator--(int) {
  Value ret;

  if ((prv->type == Type::Double)) {

    ret = prv->d;
    prv->d--;
    
  
  } else if ((prv->type == Type::Int64)) {

    ret = prv->i;
    prv->i--;
    
  
  } else {

    throw type_mismatch("The values must be of type Double or Int64 for this operation.");
    
  
  }

  return ret;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Avoid signed int64 overflow and negating INT64_MIN in generated tests; these are undefined behavior rather than valid coverage targets.
```

---

## L1177

**Focal:** `Value::operator bool() const`  
**Source:** [allhjson/hjson_value.cpp:1177-1194](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1177-L1194)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 3, *not an LLVM coverage measurement*

### Focal method

```cpp
Value::operator bool() const {
  if ((prv->type == Type::Double)) {

    return !!prv->d;
  
  } else if ((prv->type == Type::Int64)) {

    return !!prv->i;
  
  } else if ((prv->type == Type::Bool)) {

    return prv->b;
  
  }

  return !empty();
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1201

**Focal:** `Value::operator double() const`  
**Source:** [allhjson/hjson_value.cpp:1201-1216](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1201-L1216)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value::operator double() const {
  if ((prv->type == Type::Double)) {

    return prv->d;
  
  } else if ((prv->type == Type::Int64)) {

    return static_cast<double>(prv->i);
  
  }

  throw type_mismatch("Must be of type Double or Int64 for that operation.");

  return 0.0;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1239

**Focal:** `Value::operator long long() const`  
**Source:** [allhjson/hjson_value.cpp:1239-1253](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1239-L1253)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
Value::operator long long() const {
  if ((prv->type == Type::Double)) {

    return static_cast<long long>(prv->d);
  
  } else if ((prv->type == Type::Int64)) {

    return prv->i;
  
  }

  throw type_mismatch("Must be of type Double or Int64 for that operation.");

  return 0;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1256

**Focal:** `Value::operator const char*() const`  
**Source:** [allhjson/hjson_value.cpp:1256-1263](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1256-L1263)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value::operator const char*() const {
  if (prv->type != Type::String) {
    throw type_mismatch("Must be of type String for that operation.");
  }

  return prv->s->c_str();
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1265

**Focal:** `Value::operator std::string() const`  
**Source:** [allhjson/hjson_value.cpp:1265-1272](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1265-L1272)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value::operator std::string() const {
  if (prv->type != Type::String) {
    throw type_mismatch("Must be of type String for that operation.");
  }

  return *prv->s;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1279

**Focal:** `bool Value::empty() const`  
**Source:** [allhjson/hjson_value.cpp:1279-1286](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1279-L1286)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
bool Value::empty() const {
  return (prv->type == Type::Undefined ||
    prv->type == Type::Null ||
    (prv->type == Type::String && prv->s->empty()) ||
    (prv->type == Type::Vector && prv->v->empty()) ||
    (prv->type == Type::Map && prv->m->m.empty()));
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1293

**Focal:** `bool Value::is_container() const`  
**Source:** [allhjson/hjson_value.cpp:1293-1296](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1293-L1296)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
bool Value::is_container() const {
  return prv->type == Type::Vector || prv->type == Type::Map;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1298

**Focal:** `bool Value::is_numeric() const`  
**Source:** [allhjson/hjson_value.cpp:1298-1301](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1298-L1301)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
bool Value::is_numeric() const {
  return prv->type == Type::Double || prv->type == Type::Int64;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1303

**Focal:** `size_t Value::size() const`  
**Source:** [allhjson/hjson_value.cpp:1303-1316](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1303-L1316)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
size_t Value::size() const {
  if ((prv->type == Type::Vector)) {

    return prv->v->size();
  
  } else if ((prv->type == Type::Map)) {

    return prv->m->m.size();
  
  }

  return 0;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1318

**Focal:** `bool Value::deep_equal(const Value& other) const`  
**Source:** [allhjson/hjson_value.cpp:1318-1363](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1318-L1363)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 9, *not an LLVM coverage measurement*

### Focal method

```cpp
bool Value::deep_equal(const Value& other) const {
  if (*this == other) {
    return true;
  }

  if (this->type() != other.type() || this->size() != other.size()) {
    return false;
  }

  if ((prv->type == Type::Vector)) {

    {
      auto itA = this->prv->v->begin();
      auto endA = this->prv->v->end();
      auto itB = other.prv->v->begin();
      while (itA != endA) {
        if (!itA->deep_equal(*itB)) {
          return false;
        }
        ++itA;
        ++itB;
      }
    }
    return true;

  
  } else if ((prv->type == Type::Map)) {

    {
      auto itA = this->begin(), endA = this->end(), itB = other.begin();
      while (itA != endA) {
        if (!itA->second.deep_equal(itB->second)) {
          return false;
        }
        ++itA;
        ++itB;
      }
    }
    return true;

  
  }

  return false;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// deep_equal on independently constructed Maps compares sorted mapped values but does not verify corresponding keys. Thus {a:1} and {b:1} can return true; avoid assuming standard JSON structural equality. Shared-pointer copies enter the initial fast equality path.
```

---

## L1365

**Focal:** `Value Value::clone() const`  
**Source:** [allhjson/hjson_value.cpp:1365-1394](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1365-L1394)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 4, *not an LLVM coverage measurement*

### Focal method

```cpp
Value Value::clone() const {
  if ((prv->type == Type::Vector)) {

    {
      Value ret;
      for (int index = 0; index < int(size()); ++index) {
        ret.push_back(operator[](index).clone());
      }
      ret.set_comments(*this);
      return ret;
    }

  
  } else if ((prv->type == Type::Map)) {

    {
      Value ret;
      for (int index = 0; index < size(); ++index) {
        ret[key(index)] = operator[](index).clone();
      }
      ret.set_comments(*this);
      return ret;
    }

  
  }

  return *this;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Source behavior: clone() of empty Vector/Map produces Undefined because no loop iteration materializes the destination; scalar clone shares ValueImpl. Do not assume independent deep copy for these cases.
```

---

## L1396

**Focal:** `void Value::clear()`  
**Source:** [allhjson/hjson_value.cpp:1396-1412](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1396-L1412)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::clear() {
  if ((prv->type == Type::Vector)) {

    prv->v->clear();
    

  
  } else if ((prv->type == Type::Map)) {

    prv->m->m.clear();
    prv->m->v.clear();
    

  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1414

**Focal:** `void Value::erase(int index)`  
**Source:** [allhjson/hjson_value.cpp:1414-1446](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1414-L1446)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::erase(int index) {
  if ((prv->type == Type::Undefined) || (prv->type == Type::Vector) || (prv->type == Type::Map)) {

    if (index < 0 || index >= size()) {
      throw index_out_of_bounds("Index out of bounds.");
    }

    if ((prv->type == Type::Vector)) {

      {
        prv->v->erase(prv->v->begin() + index);
      }
      
    
    } else if ((prv->type == Type::Map)) {

      {
        prv->m->m.erase(prv->m->v[index]);
        prv->m->v.erase(prv->m->v.begin() + index);
      }
      
    
    }
    

  
  } else {

    throw type_mismatch("Must be of type Vector or Map for that operation.");
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1448

**Focal:** `void Value::push_back(const Value& other)`  
**Source:** [allhjson/hjson_value.cpp:1448-1459](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1448-L1459)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::push_back(const Value& other) {
  if (prv->type == Type::Undefined) {
    prv->~ValueImpl();
    // Recreate the private object using the same memory block.
    new(&(*prv)) ValueImpl(Type::Vector);
  } else if (prv->type != Type::Vector) {
    throw type_mismatch("Must be of type Undefined or Vector for that operation.");
  }

  prv->v->push_back(other);
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1461

**Focal:** `void Value::move(int from, int to)`  
**Source:** [allhjson/hjson_value.cpp:1461-1509](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1461-L1509)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 12, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::move(int from, int to) {
  if ((prv->type == Type::Undefined) || (prv->type == Type::Vector) || (prv->type == Type::Map)) {

    if (from < 0 || to < 0 || from >= size() || to > size()) {
      throw index_out_of_bounds("Index out of bounds.");
    }

    if (from == to) {
      return;
    }

    if ((prv->type == Type::Vector)) {

      {
        auto it = prv->v->begin();

        prv->v->insert(it + to, it[from]);
        if (to < from) {
          ++from;
        }
        prv->v->erase(prv->v->begin() + from);
      }
      
    
    } else if ((prv->type == Type::Map)) {

      {
        auto vec = &prv->m->v;
        auto it = vec->begin();

        vec->insert(it + to, it[from]);
        if (to < from) {
          ++from;
        }
        vec->erase(vec->begin() + from);
      }
      
    
    }
    

  
  } else {

    throw type_mismatch("Must be of type Vector or Map for that operation.");
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1511

**Focal:** `std::string Value::key(int index) const`  
**Source:** [allhjson/hjson_value.cpp:1511-1525](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1511-L1525)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 4, *not an LLVM coverage measurement*

### Focal method

```cpp
std::string Value::key(int index) const {
  if ((prv->type == Type::Undefined) || (prv->type == Type::Map)) {

    if (index < 0 || index >= size()) {
      throw index_out_of_bounds("Index out of bounds.");
    }
    return prv->m->v[index];
  
  } else {

    throw type_mismatch("Must be of type Map for that operation.");
  
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1527

**Focal:** `ValueMap::iterator Value::begin()`  
**Source:** [allhjson/hjson_value.cpp:1527-1536](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1527-L1536)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
ValueMap::iterator Value::begin() {
  if (prv->type != Type::Map) {
    // Some C++ compilers might not allow comparing this to another
    // default-constructed iterator.
    return ValueMap::iterator();
  }

  return prv->m->m.begin();
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1538

**Focal:** `ValueMap::iterator Value::end()`  
**Source:** [allhjson/hjson_value.cpp:1538-1547](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1538-L1547)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
ValueMap::iterator Value::end() {
  if (prv->type != Type::Map) {
    // Some C++ compilers might not allow comparing this to another
    // default-constructed iterator.
    return ValueMap::iterator();
  }

  return prv->m->m.end();
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1549

**Focal:** `ValueMap::const_iterator Value::begin() const`  
**Source:** [allhjson/hjson_value.cpp:1549-1558](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1549-L1558)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
ValueMap::const_iterator Value::begin() const {
  if (prv->type != Type::Map) {
    // Some C++ compilers might not allow comparing this to another
    // default-constructed iterator.
    return ValueMap::const_iterator();
  }

  return prv->m->m.begin();
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1560

**Focal:** `ValueMap::const_iterator Value::end() const`  
**Source:** [allhjson/hjson_value.cpp:1560-1569](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1560-L1569)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
ValueMap::const_iterator Value::end() const {
  if (prv->type != Type::Map) {
    // Some C++ compilers might not allow comparing this to another
    // default-constructed iterator.
    return ValueMap::const_iterator();
  }

  return prv->m->m.end();
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1571

**Focal:** `size_t Value::erase(const std::string &key)`  
**Source:** [allhjson/hjson_value.cpp:1571-1592](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1571-L1592)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 4, *not an LLVM coverage measurement*

### Focal method

```cpp
size_t Value::erase(const std::string &key) {
  if (prv->type == Type::Undefined) {
    return 0;
  } else if (prv->type != Type::Map) {
    throw type_mismatch("Must be of type Map for that operation.");
  }

  size_t ret = prv->m->m.erase(key);

  if (ret > 0) {
    auto v = &prv->m->v;
    auto it = std::find(v->begin(), v->end(), key);
    if (it == v->end()) {
      assert(!"Value found in map but not in vector");
    } else {
      v->erase(it);
    }
  }

  return ret;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// The Map lookup assertion requires an invalid internal map/vector invariant and is unreachable via valid public APIs.
```

---

## L1599

**Focal:** `double Value::to_double() const`  
**Source:** [allhjson/hjson_value.cpp:1599-1656](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1599-L1656)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 9, *not an LLVM coverage measurement*

### Focal method

```cpp
double Value::to_double() const {
  if ((prv->type == Type::Undefined) || (prv->type == Type::Null)) {

    return 0.0;
  
  } else if ((prv->type == Type::Bool)) {

    return (prv->b ? 1.0 : 0.0);
  
  } else if ((prv->type == Type::Double)) {

    return prv->d;
  
  } else if ((prv->type == Type::Int64)) {

    return static_cast<double>(prv->i);
  
  } else if ((prv->type == Type::String)) {

    {
      double ret;

#if HJSON_USE_CHARCONV
      const char *pCh = prv->s->c_str();
      const char *pEnd = pCh + prv->s->size();

      auto res = std::from_chars(pCh, pEnd, ret);

      if (res.ptr != pEnd || res.ec == std::errc::result_out_of_range) {
#elif HJSON_USE_STRTOD
      const char *pCh = prv->s->c_str();
      char *endptr;
      errno = 0;

      ret = std::strtod(pCh, &endptr);

      if (errno || endptr - pCh != prv->s->size()) {
#else
      std::stringstream ss(*prv->s);

      // Make sure we expect dot (not comma) as decimal point.
      ss.imbue(std::locale::classic());

      ss >> ret;

      if (!ss.eof() || ss.fail()) {
#endif
        return 0.0;
      }

      return ret;
    }
  
  }

  throw type_mismatch("Illegal type for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Default allhjson C++11 build leaves HJSON_USE_CHARCONV and HJSON_USE_STRTOD undefined, so the stringstream #else code is active. STRTOD and CHARCONV alternatives need separately pinned builds; CHARCONV requires C++17; do not treat inactive #if code as runtime branches.
```

---

## L1658

**Focal:** `std::int64_t Value::to_int64() const`  
**Source:** [allhjson/hjson_value.cpp:1658-1716](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1658-L1716)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 9, *not an LLVM coverage measurement*

### Focal method

```cpp
std::int64_t Value::to_int64() const {
  if ((prv->type == Type::Undefined) || (prv->type == Type::Null)) {

    return 0;
  
  } else if ((prv->type == Type::Bool)) {

    return (prv->b ? 1 : 0);
  
  } else if ((prv->type == Type::Double)) {

    return static_cast<std::int64_t>(prv->d);
  
  } else if ((prv->type == Type::Int64)) {

    return prv->i;
  
  } else if ((prv->type == Type::String)) {

    {
      std::int64_t ret;

#if HJSON_USE_CHARCONV
      const char *pCh = prv->s->c_str();
      const char *pEnd = pCh + prv->s->size();

      auto res = std::from_chars(pCh, pEnd, ret);

      if (res.ptr != pEnd || res.ec == std::errc::result_out_of_range) {
#elif HJSON_USE_STRTOD
      const char *pCh = prv->s->c_str();
      char *endptr;
      errno = 0;

      ret = std::strtoll(pCh, &endptr, 0);

      if (errno || endptr - pCh != prv->s->size()) {
#else
      std::stringstream ss(*prv->s);

      // Avoid localization surprises.
      ss.imbue(std::locale::classic());

      ss >> ret;

      if (!ss.eof() || ss.fail()) {
#endif
        // Perhaps the string contains a decimal point or exponential part.
        return static_cast<std::int64_t>(to_double());
      }

      return ret;
    }
  
  }

  throw type_mismatch("Illegal type for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Default allhjson C++11 build leaves HJSON_USE_CHARCONV and HJSON_USE_STRTOD undefined, so the stringstream #else code is active. STRTOD and CHARCONV alternatives need separately pinned builds; CHARCONV requires C++17; do not treat inactive #if code as runtime branches.
```

---

## L1718

**Focal:** `std::string Value::to_string() const`  
**Source:** [allhjson/hjson_value.cpp:1718-1829](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1718-L1829)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 8, *not an LLVM coverage measurement*

### Focal method

```cpp
std::string Value::to_string() const {
  if ((prv->type == Type::Undefined)) {

    return "";
  
  } else if ((prv->type == Type::Null)) {

    return "null";
  
  } else if ((prv->type == Type::Bool)) {

    return (prv->b ? "true" : "false");
  
  } else if ((prv->type == Type::Double)) {

    {
#if HJSON_USE_CHARCONV
      std::array<char, 32> buf;

      auto res = std::to_chars(buf.data(), buf.data() + buf.size(), prv->d);

      if (res.ptr - buf.data() >= buf.size() || res.ec != std::errc()) {
        return "";
      }

      // to_chars() does not set a zero termination, which is needed by strchr().
      *res.ptr = '\0';

      // Always output a decimal point.
      if (strchr(buf.data(), '.') == nullptr) {
        if (res.ptr - buf.data() >= buf.size() - 1) {
          return "";
        }
        *(res.ptr++) = '.';
        *(res.ptr++) = '0';
      }

      return std::string(buf.data(), res.ptr);
#elif HJSON_USE_STRTOD
      char buf[32];
      int nChars = snprintf(buf, sizeof(buf), "%.15g", prv->d);

      if (nChars < 0 || nChars >= static_cast<int>(sizeof(buf))) {
        return "";
      }

      // Always output a decimal point.
      if (strchr(buf, '.') == nullptr) {
        if (nChars >= static_cast<int>(sizeof(buf)) - 1) {
          return "";
        }
        buf[nChars++] = '.';
        buf[nChars++] = '0';
      }

      return std::string(buf, nChars);
#else
      std::ostringstream oss;

      // Make sure we use dot (not comma) as decimal point.
      oss.imbue(std::locale::classic());
      oss.precision(15);

      oss << prv->d;

      // Always output a decimal point. Done like this to avoid printing more
      // decimals than needed, which would be the result of using
      // std::ios::showpoint.
      if (oss.str().find_first_of('.', 0) == std::string::npos) {
        oss << ".0";
      }

      return oss.str();
#endif
    }
  
  } else if ((prv->type == Type::Int64)) {

    {
#if HJSON_USE_CHARCONV
      std::array<char, 32> buf;

      auto res = std::to_chars(buf.data(), buf.data() + buf.size(), prv->i);

      if (res.ec != std::errc()) {
        return "";
      }

      return std::string(buf.data(), res.ptr);
#elif HJSON_USE_STRTOD
      return std::to_string(prv->i);
#else
      std::ostringstream oss;

      // Avoid localization surprises.
      oss.imbue(std::locale::classic());

      oss << prv->i;

      return oss.str();
#endif
    }
  
  } else if ((prv->type == Type::String)) {

    return *prv->s;
  
  }

  throw type_mismatch("Illegal type for this operation.");
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.

// Default allhjson C++11 build leaves HJSON_USE_CHARCONV and HJSON_USE_STRTOD undefined, so the stringstream #else code is active. STRTOD and CHARCONV alternatives need separately pinned builds; CHARCONV requires C++17; do not treat inactive #if code as runtime branches.
```

---

## L1831

**Focal:** `void Value::set_comment_before(const std::string& str)`  
**Source:** [allhjson/hjson_value.cpp:1831-1841](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1831-L1841)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::set_comment_before(const std::string& str) {
  if (!cm) {
    if (str.empty()) {
      return;
    }
    cm.reset(new Comments());
  }

  cm->m_commentBefore = str;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1843

**Focal:** `std::string Value::get_comment_before() const`  
**Source:** [allhjson/hjson_value.cpp:1843-1850](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1843-L1850)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
std::string Value::get_comment_before() const {
  if (cm) {
    return cm->m_commentBefore;
  }

  return "";
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1852

**Focal:** `void Value::set_comment_key(const std::string& str)`  
**Source:** [allhjson/hjson_value.cpp:1852-1862](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1852-L1862)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::set_comment_key(const std::string& str) {
  if (!cm) {
    if (str.empty()) {
      return;
    }
    cm.reset(new Comments());
  }

  cm->m_commentKey = str;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1864

**Focal:** `std::string Value::get_comment_key() const`  
**Source:** [allhjson/hjson_value.cpp:1864-1871](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1864-L1871)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
std::string Value::get_comment_key() const {
  if (cm) {
    return cm->m_commentKey;
  }

  return "";
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1873

**Focal:** `void Value::set_comment_inside(const std::string& str)`  
**Source:** [allhjson/hjson_value.cpp:1873-1883](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1873-L1883)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::set_comment_inside(const std::string& str) {
  if (!cm) {
    if (str.empty()) {
      return;
    }
    cm.reset(new Comments());
  }

  cm->m_commentInside = str;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1885

**Focal:** `std::string Value::get_comment_inside() const`  
**Source:** [allhjson/hjson_value.cpp:1885-1892](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1885-L1892)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
std::string Value::get_comment_inside() const {
  if (cm) {
    return cm->m_commentInside;
  }

  return "";
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1894

**Focal:** `void Value::set_comment_after(const std::string& str)`  
**Source:** [allhjson/hjson_value.cpp:1894-1904](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1894-L1904)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::set_comment_after(const std::string& str) {
  if (!cm) {
    if (str.empty()) {
      return;
    }
    cm.reset(new Comments());
  }

  cm->m_commentAfter = str;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1906

**Focal:** `std::string Value::get_comment_after() const`  
**Source:** [allhjson/hjson_value.cpp:1906-1913](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1906-L1913)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
std::string Value::get_comment_after() const {
  if (cm) {
    return cm->m_commentAfter;
  }

  return "";
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1915

**Focal:** `void Value::set_comments(const Value& other)`  
**Source:** [allhjson/hjson_value.cpp:1915-1926](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1915-L1926)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
void Value::set_comments(const Value& other) {
  if (other.cm) {
    if (!cm) {
      cm.reset(new Comments());
    }

    *cm = *other.cm;
  } else {
    clear_comments();
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L1933

**Focal:** `Value& Value::assign_with_comments(const Value& other)`  
**Source:** [allhjson/hjson_value.cpp:1933-1941](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1933-L1941)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::assign_with_comments(const Value& other) {
  // If this object is of type Undefined set_comments() will be called in the
  // assignment operator, no need to call it here.
  if (defined()) {
    set_comments(other);
  }
  return operator=(other);
}
```

### Context

```cpp
// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1943

**Focal:** `Value& Value::assign_with_comments(Value&& other)`  
**Source:** [allhjson/hjson_value.cpp:1943-1951](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1943-L1951)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
Value& Value::assign_with_comments(Value&& other) {
  // If this object is of type Undefined set_comments() will be called in the
  // assignment operator, no need to call it here.
  if (defined()) {
    cm = other.cm;
  }
  return operator=(std::move(other));
}
```

### Context

```cpp
// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L1953

**Focal:** `MapProxy::MapProxy(std::shared_ptr<ValueImpl> _parent, const std::string &_key, Value *_pTarget) : Value(_pTarget ? _pTarget->prv : std::make_shared<ValueImpl>(Type::Undefined), _pTarget ? _pTarget->cm : 0), parentPrv(_parent), key(_key), pTarget(_pTarget), wasAssigned(false)`  
**Source:** [allhjson/hjson_value.cpp:1953-1963](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1953-L1963)  
**Access:** `benchmark_local_public_header`  
**Lexical branch indicators:** 2, *not an LLVM coverage measurement*

### Focal method

```cpp
MapProxy::MapProxy(std::shared_ptr<ValueImpl> _parent, const std::string &_key,
  Value *_pTarget)
  : Value(_pTarget ? _pTarget->prv : std::make_shared<ValueImpl>(Type::Undefined),
      _pTarget ? _pTarget->cm : 0),
    parentPrv(_parent),
    key(_key),
    pTarget(_pTarget),
    wasAssigned(false)
{
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Original MapProxy declaration from hjson.h
// MapProxy is only used for temporary references to elements in a Map. It is
// not possible to store a MapProxy in a variable. It only exists to make it
// possible to check for the existence of a specific key in a Map without
// creating an empty element in the Map with that key.
class MapProxy : public Value {
  private:
  friend class Value;

  std::shared_ptr<ValueImpl> parentPrv;
  std::string key;
  Value *pTarget;
  // True if an explicit assignment has been made to this MapProxy.
  bool wasAssigned;

  MapProxy(std::shared_ptr<ValueImpl> parent, const std::string& key,
    Value *pTarget);

  // Make the copy constructor private in order to avoid accidental creation of
  // MapProxy variables like this:
  //   auto myVal = val["one"];
  MapProxy(const MapProxy&) = default;
  MapProxy(Value&&);

public:
  ~MapProxy() override;
  MapProxy& operator =(const MapProxy&);
  MapProxy& operator =(const Value&);
  MapProxy& operator =(Value&&);
  MapProxy& assign_with_comments(const MapProxy&);
  MapProxy& assign_with_comments(const Value&);
  MapProxy& assign_with_comments(Value&&);
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.

// Both constructor outcomes are reachable through public object["missing"] and object["existing"] lookups; do not copy MapProxy.
```

---

## L1971

**Focal:** `MapProxy::~MapProxy()`  
**Source:** [allhjson/hjson_value.cpp:1971-1992](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L1971-L1992)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 3, *not an LLVM coverage measurement*

### Focal method

```cpp
MapProxy::~MapProxy() {
  if (wasAssigned || !empty()) {
    if (pTarget) {
      // Can have changed due to assignment.
      pTarget->prv = this->prv;
      // In case cm was 0 but now has been created by a call to set_comment_x.
      pTarget->cm = this->cm;
    } else {
      // If the key is new we must add it to the order vector also.
      parentPrv->m->v.push_back(key);

      // We waited until now because we don't want to insert a Value object of
      // type Undefined into the parent map, unless such an object was explicitly
      // assigned (e.g. `val["key"] = Hjson::Value()`).
      // Without this requirement, checking for the existence of an element
      // would create an Undefined element for that key if it didn't already exist
      // (e.g. `if (val["key"] == 1) {` would create an element for "key").
      parentPrv->m->m.emplace(key, Value(this->prv, this->cm));
    }
  }
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original backing types from hjson_value.cpp
typedef std::vector<std::string> KeyVec;
typedef std::vector<Value> ValueVec;
typedef std::map<std::string, Value> ValueMap;

class ValueVecMap {
public:
  KeyVec v;
  ValueMap m;
};

class Value::ValueImpl {
public:
  Type type;
  union {
    bool b;
    double d;
    std::int64_t i;
    std::string *s;
    ValueVec *v;
    ValueVecMap *m;
  };

  ValueImpl();
  ValueImpl(bool);
  ValueImpl(double);
  explicit ValueImpl(std::int64_t);
  ValueImpl(const std::string&);
  ValueImpl(Type);
  ~ValueImpl();
  static void DeepClear(Value &val);
};

class Value::Comments {
public:
  std::string m_commentBefore, m_commentKey, m_commentInside, m_commentAfter;
};

// Original MapProxy declaration from hjson.h
// MapProxy is only used for temporary references to elements in a Map. It is
// not possible to store a MapProxy in a variable. It only exists to make it
// possible to check for the existence of a specific key in a Map without
// creating an empty element in the Map with that key.
class MapProxy : public Value {
  private:
  friend class Value;

  std::shared_ptr<ValueImpl> parentPrv;
  std::string key;
  Value *pTarget;
  // True if an explicit assignment has been made to this MapProxy.
  bool wasAssigned;

  MapProxy(std::shared_ptr<ValueImpl> parent, const std::string& key,
    Value *pTarget);

  // Make the copy constructor private in order to avoid accidental creation of
  // MapProxy variables like this:
  //   auto myVal = val["one"];
  MapProxy(const MapProxy&) = default;
  MapProxy(Value&&);

public:
  ~MapProxy() override;
  MapProxy& operator =(const MapProxy&);
  MapProxy& operator =(const Value&);
  MapProxy& operator =(Value&&);
  MapProxy& assign_with_comments(const MapProxy&);
  MapProxy& assign_with_comments(const Value&);
  MapProxy& assign_with_comments(Value&&);
};

// Value member declarations from hjson.h; excerpts inside class Value
  friend class MapProxy;
  class ValueImpl;
  class Comments;

  std::shared_ptr<ValueImpl> prv;
  std::shared_ptr<Comments> cm;

  Value(std::shared_ptr<ValueImpl>, std::shared_ptr<Comments>);

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// ValueImpl is incomplete in the public header; access its internal fields only where its full definition is available.
```

---

## L2018

**Focal:** `MapProxy& MapProxy::assign_with_comments(const Value& other)`  
**Source:** [allhjson/hjson_value.cpp:2018-2026](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L2018-L2026)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
MapProxy& MapProxy::assign_with_comments(const Value& other) {
  // If this object is of type Undefined set_comments() will be called in the
  // assignment operator, no need to call it here.
  if (defined()) {
    set_comments(other);
  }
  return operator=(other);
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original MapProxy declaration from hjson.h
// MapProxy is only used for temporary references to elements in a Map. It is
// not possible to store a MapProxy in a variable. It only exists to make it
// possible to check for the existence of a specific key in a Map without
// creating an empty element in the Map with that key.
class MapProxy : public Value {
  private:
  friend class Value;

  std::shared_ptr<ValueImpl> parentPrv;
  std::string key;
  Value *pTarget;
  // True if an explicit assignment has been made to this MapProxy.
  bool wasAssigned;

  MapProxy(std::shared_ptr<ValueImpl> parent, const std::string& key,
    Value *pTarget);

  // Make the copy constructor private in order to avoid accidental creation of
  // MapProxy variables like this:
  //   auto myVal = val["one"];
  MapProxy(const MapProxy&) = default;
  MapProxy(Value&&);

public:
  ~MapProxy() override;
  MapProxy& operator =(const MapProxy&);
  MapProxy& operator =(const Value&);
  MapProxy& operator =(Value&&);
  MapProxy& assign_with_comments(const MapProxy&);
  MapProxy& assign_with_comments(const Value&);
  MapProxy& assign_with_comments(Value&&);
};

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L2028

**Focal:** `MapProxy& MapProxy::assign_with_comments(Value&& other)`  
**Source:** [allhjson/hjson_value.cpp:2028-2036](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L2028-L2036)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 1, *not an LLVM coverage measurement*

### Focal method

```cpp
MapProxy& MapProxy::assign_with_comments(Value&& other) {
  // If this object is of type Undefined set_comments() will be called in the
  // assignment operator, no need to call it here.
  if (defined()) {
    cm = other.cm;
  }
  return operator=(std::move(other));
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Original MapProxy declaration from hjson.h
// MapProxy is only used for temporary references to elements in a Map. It is
// not possible to store a MapProxy in a variable. It only exists to make it
// possible to check for the existence of a specific key in a Map without
// creating an empty element in the Map with that key.
class MapProxy : public Value {
  private:
  friend class Value;

  std::shared_ptr<ValueImpl> parentPrv;
  std::string key;
  Value *pTarget;
  // True if an explicit assignment has been made to this MapProxy.
  bool wasAssigned;

  MapProxy(std::shared_ptr<ValueImpl> parent, const std::string& key,
    Value *pTarget);

  // Make the copy constructor private in order to avoid accidental creation of
  // MapProxy variables like this:
  //   auto myVal = val["one"];
  MapProxy(const MapProxy&) = default;
  MapProxy(Value&&);

public:
  ~MapProxy() override;
  MapProxy& operator =(const MapProxy&);
  MapProxy& operator =(const Value&);
  MapProxy& operator =(Value&&);
  MapProxy& assign_with_comments(const MapProxy&);
  MapProxy& assign_with_comments(const Value&);
  MapProxy& assign_with_comments(Value&&);
};

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);

// Safe construction: use Value(false), Value(0.0), Value(0) for scalar payloads. Value(Type::Bool/Double/Int64) sets only the type tag, leaving the scalar union payload uninitialized. Value(Type::Null/Undefined/Vector/Map/String) is usable for those categories.
```

---

## L2038

**Focal:** `Value Merge(const Value& base, const Value& ext)`  
**Source:** [allhjson/hjson_value.cpp:2038-2065](https://github.com/Ming191/thucnghiem/blob/d26d2e5b7644f42e8deeb461dbd45cb53c35fcf3/allhjson/hjson_value.cpp#L2038-L2065)  
**Access:** `public_header_or_external_linkage`  
**Lexical branch indicators:** 7, *not an LLVM coverage measurement*

### Focal method

```cpp
Value Merge(const Value& base, const Value& ext) {
  Value merged;

  if (!ext.defined()) {
    merged = base.clone();
  } else if (base.type() == Type::Map && ext.type() == Type::Map) {
    for (int index = 0; index < ext.size(); ++index) {
      if (base[ext.key(index)].defined()) {
        merged[ext.key(index)] = Merge(base[ext.key(index)], ext[index]);
      } else {
        merged[ext.key(index)] = ext[index].clone();
      }
    }

    for (int index = 0; index < base.size(); ++index) {
      if (!merged[base.key(index)].defined()) {
        merged[base.key(index)] = base[index].clone();
      }
    }

    merged.set_comments(ext);
  } else {
    merged = ext.clone();
  }

  return merged;
}
```

### Context

```cpp
// Original Value type enum from hjson.h
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

// Relevant public Value construction API from hjson.h; declarations inside class Value
  Value();
  Value(bool);
  Value(float);
  Value(double);
  Value(char);
  Value(unsigned char);
  Value(short);
  Value(unsigned short);
  Value(int);
  Value(const char*);
  Value(const std::string&);
  Value(Type);

// Relevant Value vector API declarations
  // -- Vector and Map specific functions
  // Removes all child elements from this Value if it is of type Vector or Map.
  // Does nothing if this Value is of any other type.
  void clear();
  // Returns the number of child elements contained in this Value if this Value
  // is of type Vector or Map. Returns 0 if this Value is of any other type.
  size_t size() const;

  // -- Vector specific function
  // Increases the size of this Vector by adding a Value at the end. Throws
  // Hjson::type_mismatch if this Value is of any other type than Vector or
  // Undefined.
  void push_back(const Value&);

// Relevant Value map API declarations
  // -- Map specific functions
  // Get key by its zero-based insertion index. Throws
  // Hjson::index_out_of_bounds if the index is out of bounds and this Value is
  // of type Undefined or Map. Throws Hjson::type_mismatch if this Value is of
  // any other type.
  std::string key(int) const;
  // Returns a reference to the Value specified by the key parameter. Throws
  // Hjson::index_out_of_bounds if this Value does not contain the specified
  // key and this Value is of type Undefined or Map. Throws
  // Hjson::type_mismatch if this Value is of any other type.
  const Value& at(const std::string& key) const;
  Value& at(const std::string& key);
  const Value& at(const char *key) const;
  Value& at(const char *key);
  // Iterations are always done in alphabetical key order. Returns a default
  // constructed iterator if this Value is of any other type than Map.
  std::map<std::string, Value>::iterator begin();
  std::map<std::string, Value>::iterator end();
  std::map<std::string, Value>::const_iterator begin() const;
  std::map<std::string, Value>::const_iterator end() const;
  // Removes the child element specified by the input key if this Value is of
  // type Map. Returns the number of erased elements (0 or 1). Throws
  // Hjson::type_mismatch if this Value is of any other type than Map or
  // Undefined.
  size_t erase(const std::string&);
  size_t erase(const char*);

// Relevant Value comment API declarations
  void set_comment_before(const std::string&);
  std::string get_comment_before() const;
  // Sets comment shown between the key and this Value. If this Value is
  // not an element in a Map, the comment is shown between the "before"
  // comment and this Value.
  void set_comment_key(const std::string&);
  std::string get_comment_key() const;
  // Sets comment shown right after "[" if this Value is a Vector, or right
  // after "{" if this Value is a Map. The comment is not shown if this Value
  // is of any other type than Vector or Map.
  void set_comment_inside(const std::string&);
  std::string get_comment_inside() const;
  // Sets comment shown after this Value.
  void set_comment_after(const std::string&);
  std::string get_comment_after() const;

  // Copies all comments from the other Hjson::Value.
  void set_comments(const Value&);
  // Removes all comments from this Value.
  void clear_comments();
  // A combination of the assignment operator (=) and set_comments(). The
  // normal assignment operator (=) will not change any comments, unless the
  // receiving Value is of type Undefined.
  Value& assign_with_comments(const Value&);
  Value& assign_with_comments(Value&&);
```

