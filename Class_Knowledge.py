# Class
# A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data. Define a class using the class keyword. PEP 8 Style Guide for Python Code recommends capitalizing the names of classes to make them easier to identify.

# class CoolClass:
#   pass
# In the above example we created a class and named it CoolClass. We used the pass keyword in Python to indicate that the body of the class was intentionally left blank so we don’t cause an IndentationError. We’ll learn about all the things we can put in the body of a class in the next few exercises.

# Instantiation
# A class doesn’t accomplish anything simply by being defined. A class must be instantiated. In other words, we must create an instance of the class, in order to breathe life into the schematic.

# Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined CoolClass as follows:

# cool_instance = CoolClass()
# Above, we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable cool_instance for safe-keeping so we can access our instance of CoolClass at a later time.


# Garbage Collection
# Python (like many other languages) will detect that an object is no longer being used and perform what is called “garbage collection”. During the process, unused objects are released to free up resources. When a variable is assigned to an instance and then assigned to a different instance, the prior assignment will be a candidate for “garbage collection” provided that no other variable is pointing to it. The following code example shows that the instance originally assigned to my_obj is destroyed when the variable is assigned to a new instance.

# class TestClass:
#     def __init__(self, id):
#         self.id = id
#         print("Creating object id = " + str(self.id))

#     def __del__(self):
#         print("Deleting object id = " + str(self.id))

# print("Instantiating object 1")
# my_obj = TestClass(1)

# print("Instantiating object 2")
# my_obj2 = TestClass(2)

# print("Instantiating object 3")
# my_obj = TestClass(3)

# # Wait for 10 seconds to show that object 1 is destroyed before the program ends
# from time import sleep
# sleep(10)

# Object-Oriented Programming
# A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.

# Instantiation takes a class and turns it into an object, the type() function does the opposite of that. When called with an object, it returns the class that the object is an instance of.

# print(type(cool_instance))
# # prints "<class '__main__.CoolClass'>"
# We then print out the type() of cool_instance and it shows us that this object is of type __main__.CoolClass.

# In Python __main__ means “this current file that we’re running” and so one could read the output from type() to mean “the class CoolClass that was defined here, in the script you’re currently running.”

class Facade:
      pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)
