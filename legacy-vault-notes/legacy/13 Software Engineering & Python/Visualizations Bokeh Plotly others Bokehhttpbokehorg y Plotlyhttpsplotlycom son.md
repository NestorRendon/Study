# Visualizations: Bokeh, Plotly, others.: ++[Bokeh](http://bokeh.org/)++ y ++[Plotly](https://plotly.com/)++ son dos de las librerías de visualización de datos más potentes y populares basadas en Python, diseñadas específicamente para crear gráficos interactivos, modernos y orientados a la web.

-   
-   
- 
Fundamentals of Object Oriented Programming.
Packaging classes and methods into data science libraries.  
- ![Encops lotion](assets/774C40E0-4173-41F7-8CB0-5E702ADA4816.png)  
* An abstract class is a restricted, partially implemented class in object-oriented programming that cannot be instantiated directly and is designed to be inherited. It serves as a blueprint for subclasses, allowing a mix of fully implemented concrete methods and abstract methods (lacking body) that subclasses must implement.   
  
* **Key Aspects of Abstract Classes:**  
* **No Instantiation:** You cannot create an instance (object) of an abstract class using new.  
* **Abstract Methods:** They can contain methods without a body (abstract methods), which forcing subclasses to provide specific implementations.  
* **Concrete Methods:** They can also contain fully implemented methods, fields, and constructors.  
* **Inheritance:** Used to define a common, mandatory structure for derived classes (e.g., a Shape base class for Circle and Square).  
-   
* **Extend (Inheritance)**  
* **Definition:** A mechanism where a new class (subclass) inherits fields and methods from an existing class (superclass).  
* **Purpose:** To reuse code and create an "IS-A" relationship (e.g., a Dog extends Animal).  
* **Capabilities:** The subclass can add new fields/methods and use inherited ones.  
* **Keyword:** extends (Java), : (C#).   
*   
* **Override (Polymorphism)**  
* **Definition:** A feature allowing a subclass to provide a specific implementation of a method already defined in its superclass.  
* **Purpose:** To modify or specialize the behavior of an inherited method.  
* **Requirements:** The method signature (name, parameters, return type) must be the same.  
* **Polymorphism:** It enables runtime polymorphism, where the subclass method is called even if the reference is of the superclass type.   
-   
- 
Literate programming.
Reproducible research.
Error catching, context manager, generators and comprehensions, reusable methods and classes, some code optimization and profiling.  
-   
* **Using a context manager**  
*   
* with open("data.txt", "r") as f:  
*     data = f.read()  
*   
* What happens internally:  
* File is opened  
* Code block executes  
* File automatically closes  
* Equivalent behavior:  
*   
* f = open("data.txt", "r")  
* try:  
*     data = f.read()  
* finally:  
*     f.close()  
  
import time  
  
class Timer:  
  
    def __enter__(self):  
        self.start = time.time()  
        return self  
  
    def __exit__(self, exc_type, exc_value, traceback):  
        end = time.time()  
        print("Elapsed:", end - self.start)  
  
with Timer():  
    time.sleep(2)  
  
from contextlib import contextmanager.   #Using a decorator   
import time  
  
@contextmanager  
def timer():  
    start = time.time()  
    yield  
    end = time.time()  
    print("Elapsed:", end - start)  
  
  

| Concept              | Purpose                           |
| -------------------- | --------------------------------- |
| Generator            | produce values lazily using yield |
| Generator expression | compact generator syntax          |
| List comprehension   | create lists concisely            |
| Set comprehension    | create sets                       |
| Dict comprehension   | create dictionaries               |
  
**. When Generators Are Useful**  
Generators are ideal for:  
* streaming data  
* large files  
* pipelines  
* infinite sequences  
  
**1. Generators**  
**Meaning**  
A **generator** is a function that **produces values one at a time instead of computing them all at once**.  
It uses the keyword **yield**.  
This makes generators **memory efficient**, because values are generated **lazily** (only when needed).
