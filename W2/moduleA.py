a = 10
print("hello")


class PropTest:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname

    @property
    def fullname(self):
        print("in property method")
        return self._fullname

    @fullname.setter
    def fullname(self, data):
        print("in setter")
        temp = data.split(" ")
        if len(temp) > 1:
            self.firstname = temp[0]
            self.lastname = temp[1]
        self._fullname = data


obj = PropTest("nane", "ghsemi")


# obj.fullname = "akbar ghasemi"

print(obj.fullname)
