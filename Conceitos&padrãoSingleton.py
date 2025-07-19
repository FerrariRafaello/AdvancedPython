"""
Demonstration of the Singleton Design Pattern in Python with explanation of SOLID principles.

Key concepts illustrated:
- Singleton Pattern: Ensures a class has only one instance and provides a global access point.
- Lazy Instatiation: Defers creation of the instance until it is needed.
- Use of classmethods and special methods (__new__) for control over instantiation.
"""

class Singleton:
    """
    Basic Singleton implementation using '__new__".
    This ensures only one instance of the class is created.
    """
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
    
class LazySingleton:
    """
    Singleton with lazy instantiation using a class method.
    The instance is only created upon the first request.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating LazySingleton instance...")
            cls._instance = super().__new__(cls)
        else:
            print("LazySingleton instance already created.")
        return cls._instance

    def __init__(self):
        # Initialization logic here, if needed.
        pass
    
    @classmethod
    def get_instance(cls):
        """
        Returns the single instance of the class,
        creating it if it doesn't exist yet.
        """
        if cls._instance is None:
            cls._instance = LazySingleton()
        return cls._instance
    
def main():
    print("Testing Singleton:")
    s1 = Singleton()
    s2 = Singleton()
    print(f"Singleton instances s1 and s2 are the same object: {s1 is s2}")

    print("Testing LazySingleton:")
    l1 = LazySingleton()
    l2 = LazySingleton()
    print(f"LazySingleton instances l1 and l2 are the same object: {l1 is l2}")

if __name__ == "__main__":
    main()