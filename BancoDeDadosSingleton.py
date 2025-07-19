import sqlite3

class MetaSingleton(type):
    """
    Metaclass implementing the Singleton pattern.
    Ensures only one instance of any class using this metaclass exists.
    """
    _instances = {}

    @classmethod
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DataBase(metaclass=MetaSingleton):
    """
    Singleton class managing a single SQLite database connection.
    """
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """
        Create a new connection and cursor if none exists.
        Return the cursor to perform DB operations.
        """
        if self.connection is None:
            self.connection = sqlite3.connect("banco.db")
            self.cursor = self.connection.cursor()
        return self.cursor

db1 = DataBase()
cursor1 = db1.connect()

db2 = DataBase()
cursor2 = db2.connect()

print(f"db1 id: {id(db1)}")
print(f"db2 id: {id(db2)}")
print(f"cursor1 id: {id(cursor1)}")
print(f"cursor2 id: {id(cursor2)}")
print(f"Same db instance? {"Yes" if db1 is db2 else "No"}")
print(f"Same cursor instance? {"Yes" if cursor1 is cursor2 else "No"}")

"""
Pattern Explanation:

Singleton Pattern:
-> Ensures a class has only one instance and provides a global access point to it.
-> Avoids drawbacks of global variables by controllings instantiation.

Monostate Pattern:
-> Different instances share the same state.
-> In Singleton, typically the instance itself is unique (id same).
"""