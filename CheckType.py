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

# The type() command returns the namespace and class for the object provided. For classes defined in the local file, the namespace will be reported as __main__. For classes imported from other modules, the namespace reported will be the same as the module. The following code example shows, the results from type() on objects created from two different modules.

from collections import OrderedDict

mycoll = OrderedDict()

print(type(mycoll))
# <class 'collections.OrderedDict'>


from calendar import Calendar

mycal = Calendar()

print(type(mycal))
# <class 'calendar.Calendar'>