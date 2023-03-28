# реализовать метакласс, позволяющий создавать всегда один и тот же объект класса

class IdenticalObjects(type):

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class MyClass(metaclass=IdenticalObjects):
    pass


obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
print(obj1 is obj2)
print(obj1 is obj3)
print(obj3 is obj2)
