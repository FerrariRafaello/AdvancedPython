# Delegation Pattern Example:
"""
Delegation is a programming pattern where the responsibility 
for implementing an operation is passed to a different object.
In other words, an object delegates certain behavior to another.
"""

class A:
    def do_something(self):
        print("Doing something in A")

    def another_method(self):
        print("Another method in A")

    def some_method(self, name):
        print(f"Name received: {name}")

class B:
    def __init__(self) -> None:
        self.a = A()  # instance of A to delegate to

    # Explicit delegation
    def do_something(self):
        return self.a.do_something()

    def another_method(self):
        return self.a.another_method()

    # Use __getattr__ to delegate any other attribute/method calls automatically
    def __getattr__(self, name):
        return getattr(self.a, name)

# Usage
b = B()
b.do_something()  # Calls A.do_something() via delegation
b.some_method("python")  # Delegated via __getattr__

# ------------------------------------------

# Iterating multiple sequences simultaneously using zip()

x = [1, 2, 3]
y = [4, 5, 6]

for i, j in zip(x, y):
    print(i, j)

# Creating zipped list of formatted strings
c = zip([f"{i}, {j}" for i, j in zip(y, x)])
print(list(c))

# ------------------------------------------

# Memory optimization with __slots__ to reduce instance dict overhead

class Person:
    __slots__ = ['name', 'age', 'weight']  # limits attributes to these only

    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, weight={self.weight})"

# Usage
p = Person("Alice", 30, 65.5)
print(p)
