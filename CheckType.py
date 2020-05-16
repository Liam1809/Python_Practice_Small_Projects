a_string = "Cool String"
an_int = 12

print(type(a_string))
# prints "<class 'str'>"

print(type(an_int))
# prints "<class 'int'>"

class TestClass:
    def __init__(self):
        self.value = 0

    def getVal(self):
        return self.value

mylist = [1,2,3]
mydict = { "A": 1, "B": 2}
myobj = TestClass()

print(type(mylist))
# <class 'list'>
print(type(mydict))
# <class 'dict'>
print(type(myobj))
# <class '__main__.TestClass'>