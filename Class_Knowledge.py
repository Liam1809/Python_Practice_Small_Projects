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

# class Facade:
#       pass

# facade_1 = Facade()
# facade_1_type = type(facade_1)
# print(facade_1_type)

# Class Variables
# When we want the same data to be available to every instance of a class we use a class variable. A class variable is a variable that’s the same for every instance of the class.

# You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.

# class Musician:
#   title = "Rockstar"

# drummer = Musician()
# print(drummer.title)
# # prints "Rockstar"
# Above we defined the class Musician, then instantiated drummer to be an object of type Musician. We then printed out the drummer’s .title attribute, which is a class variable that we defined as the string “Rockstar”.

# If we defined another musician, like guitarist = Musician() they would have the same .title attribute.

# Methods
# Methods are functions that are defined as part of a class. The first argument in a method is always the object that is calling the method. Convention recommends that we name this first argument self. Methods always have at least this one argument.

# We define methods similarly to functions, except that they are indented to be part of the class.

# class Dog:
#   dog_time_dilation = 7

#   def time_explanation(self):
#     print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

# pipi_pitbull = Dog()
# pipi_pitbull.time_explanation()
# # Prints "Dogs experience 7 years for every 1 human year."
# Above we created a Dog class with a time_explanation method that takes one argument, self, which refers to the object calling the function. We created a Dog named pipi_pitbull and called the .time_explanation() method on our new object for Pipi.

# Notice we didn’t pass any arguments when we called .time_explanation(), but were able to refer to self in the function body. When you call a method it automatically passes the object calling the method as the first argument.

# Methods with Arguments
# Methods can also take more arguments than just self:

# class DistanceConverter:
#   kms_in_a_mile = 1.609
#   def how_many_kms(self, miles):
#     return miles * self.kms_in_a_mile

# converter = DistanceConverter()
# kms_in_5_miles = converter.how_many_kms(5)
# print(kms_in_5_miles)
# # prints "8.045"
# Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers. Notice again that even though how_many_kms takes two arguments in its definition, we only pass miles, because self is implicitly passed (and refers to the object converter).

# Constructors
# There are several methods that we can define in a Python class that have special behavior. These methods are sometimes called “magic”, because they behave differently from regular methods. Another popular term is dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

# The first dunder method we’re going to use is the __init__ method (note the two underscores before and after the word “init”). This method is used to initialize a newly created object. It is called every time the class is instantiated.

# Methods that are used to prepare an object being instantiated are called constructors. The word “constructor” is used to describe similar features in other object-oriented programming languages but programmers who refer to a constructor in Python are usually talking about the __init__ method.

# class Shouter:
#   def __init__(self):
#     print("HELLO?!")

# shout1 = Shouter()
# # prints "HELLO?!"

# shout2 = Shouter()
# # prints "HELLO?!"
# Above we created a class called Shouter and every time we create an instance of Shouter the program prints out a shout. Don’t worry, this doesn’t hurt the computer at all.

# Pay careful attention to the instantiation syntax we use. Shouter() looks a lot like a function call, doesn’t it? If it’s a function, can we pass parameters to it? We absolutely can, and those parameters will be received by the __init__ method.

# class Shouter:
#   def __init__(self, phrase):
#     # make sure phrase is a string
#     if type(phrase) == str:

#       # then shout it out
#       print(phrase.upper())

# shout1 = Shouter("shout")
# # prints "SHOUT"

# shout2 = Shouter("shout")
# # prints "SHOUT"

# shout3 = Shouter("let it all out")
# # prints "LET IT ALL OUT"
# Above we’ve updated our Shouter class to take the additional parameter phrase. When we created each of our objects we passed an argument to the constructor. The constructor takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.

# Instance Variables
# We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has? This is because each instance of a class can hold different kinds of data.

# The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

# Let’s say that we have the following class definition:

# class FakeDict:
#   pass
# We can instantiate two different objects from this class, fake_dict1 and fake_dict2, and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.

# fake_dict1 = FakeDict()
# fake_dict2 = FakeDict()

# fake_dict1.fake_key = "This works!"
# fake_dict2.fake_key = "This too!"

# # Let's join the two strings together!
# working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
# print(working_string)
# # prints "This works! This too!"

# CLASS VARIABLES:
# A class variable needs the "creating a variable step " as you call it, in the intended block of the Class. If it is called later by any object using the syntax object.variable, it will yield the same data for every instance/object of the class.
# INSTANCE VARIABLES:
# Although an instance variable uses the same attribute notation used for accessing class variables (object.variable ) it does so in order to assign data to the object. The data now is not shared by all instances of the class, they re specific to the object they are attached to.