# C++ Core Cheatsheet

**Prev:** [[01 - Why C++ in the DS Stack]] · **Next:** [[03 - OOP Essentials]]

---

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    // types
    int x = 42;
    double pi = 3.14;
    bool ok = true;
    std::string s = "hello";

    // io
    std::cout << s << "\n";

    // control flow
    if (x > 0) { /* ... */ }
    for (int i = 0; i < 10; ++i) { }
    for (auto& v : vec) { v *= 2; }  // range-for

    // functions
    auto add = [](int a, int b) { return a + b; };  // lambda

    return 0;
}
```

---

## Headers you should know

| Header | For |
|--------|-----|
| `<vector>` | Dynamic array |
| `<string>` | Strings |
| `<map>` / `<unordered_map>` | Dictionaries |
| `<algorithm>` | sort, find, transform |
| `<memory>` | `unique_ptr`, `shared_ptr` |
| `<thread>` | Concurrency |

---

## const & references (interview favorite)

```cpp
void foo(const std::vector<int>& v);  // read-only, no copy
void bar(std::vector<int>&& v);       // move semantics
```

---

**Next:** [[03 - OOP Essentials]]
