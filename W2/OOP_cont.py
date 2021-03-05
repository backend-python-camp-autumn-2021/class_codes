# class A:
#     pass

# class B(A):
#     pass


# b = B()

# print("b is sinstance A: ", isinstance(b, A))
# print("B is subclass A: ", issubclass(B, A))
# print("A is subclass B: ", issubclass(A, B))

# print(isinstance(object, type))
# print(isinstance(type, object))
# print(issubclass(type, object))
# print(issubclass(object, type))


# print(issubclass(A, type))
# print(isinstance(A, type))
# print(issubclass(A, object))
# print(isinstance(A, object))


# class MetaA(type):
#     name = 'ALi'

# class TestMeta(metaclass=MetaA):
#     pass


# obj = TestMeta()

# print(TestMeta.name)


# class A:
#     def arian(self):
#         print("salam Pedar!")


# class B(A):
#     def arian(self):
#         print("salam Pesar")
#         super().arian()


# b = B()
# b.arian()


class MetaBaKelas(type):
    def __call__(self, *args, **kwargs):
        print("manam meta BaKelas")
        return super().__call__(*args, **kwargs)


class BaKelass(metaclass=MetaBaKelas):
    def __init__(self):
        print("manam init")

    @classmethod
    def __new__(cls, *args, **kwargs):
        print("manam new!")
        return super().__new__(*args, **kwargs)

    def __call__(self, name):
        print(f"manam call {name}")


obj = BaKelass()
# obj("ashkan")
# obj("mehrdad")
# obj("shahgayegh")
