from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def operation(self):
        pass


class Adaptee:
    def specific_operation(self):
        return "sare 2tai"


class Adapter(Target, Adaptee):
    # override
    def operation(self):
        return f"3tai be {self.specific_operation()}"


def client(adapter):
    print(adapter.operation())


if __name__ == "__main__":
    adapter = Adapter()
    client(adapter)


def my_fun(*args):
    print(args)


my_fun(2, 12, "ashkan")


def f(name="ashkan", age=12):
    print(name, age)


my_dict = {
    "name": "asghar",
    "age": 15
}

my_tuple = ("mehrdad", 54)
f(**my_dict)
f(*my_tuple)
f()
f("doost dokhtar mehrdad!")
f("shaghayegh", 62)
