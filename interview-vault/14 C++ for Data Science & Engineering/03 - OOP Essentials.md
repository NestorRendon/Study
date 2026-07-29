# OOP Essentials

**Prev:** [[02 - C++ Core Cheatsheet]] · **Next:** [[04 - STL Containers and Algorithms]]

---

## In plain English

**Class** = data + methods bundled together. **Encapsulation** hides internals; **inheritance** reuses code; **polymorphism** calls the right method at runtime.

---

## Minimal class

```cpp
class Detector {
public:
    Detector(int threshold) : thresh_(threshold) {}
    bool predict(const std::vector<float>& x) const {
        return score(x) > thresh_;
    }
private:
    int thresh_;
    float score(const std::vector<float>& x) const;
};
```

| Keyword | Role |
|---------|------|
| `public` | API for users |
| `private` | Implementation detail |
| `const` method | Does not modify object state |

---

## Inheritance & virtual

```cpp
class Model {
public:
    virtual ~Model() = default;           // always virtual dtor if polymorphic
    virtual float infer(const float* in) = 0;  // pure virtual = interface
};

class LinearModel : public Model {
public:
    float infer(const float* in) override { return w_ * in[0] + b_; }
private:
    float w_, b_;
};
```

**Interview:** virtual dispatch lets you swap models without changing client code.

---

**Next:** [[04 - STL Containers and Algorithms]]
