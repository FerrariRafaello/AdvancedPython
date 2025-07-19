class SharedState:
    _shared_state = {"value": 2}

    def __init__(self):
        self.__dict__ = self._shared_state
        self.x = getattr(self, "x", 1)

b1 = SharedState()
b2 = SharedState()
b1.x = 5

print("b1:\n", b1)
print("b2:\n", b2)
print("Shared dict b1:\n", b1.__dict__)
print("Shared dict b2:\n", b2.__dict__)

# ------------------------------------

class MetaClass(type):
    def __call__(cls, *args, **kwargs):
        print(f"MetaClass __call__ with args = {args}, kwargs = {kwargs}")
        return super().__call__(*args, **kwargs)

class CustomInt(metaclass=MetaClass):
    def __init__(self, x=0, y=0, extra=None):
        self.x = x
        self.y = y
        self.extra = extra

obj = CustomInt(4, 5, extra = ["rafa", "isa"])  # kwargs handled as extra parameter

print(f"CustomInt instance: x={obj.x}, y={obj.y}, extra={obj.extra}")

# -------------------------------------

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __repr__(self):
        return f"<SingletonClass id={id(self)}>"

t1 = SingletonClass()
t2 = SingletonClass()

print("t1 == t2?", t1 is t2)
print("t1:", t1)
print("t2:", t2)
