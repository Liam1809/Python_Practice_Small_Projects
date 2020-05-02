# Tuples are another kind of data Structure allowing to store multiple data types inside of it
#Tuples are immutable which means it cannot be changed once it is created
my_info = ("Liam", 20, "Programmer")

for element in my_info:
    print(element)
    
print(my_info)
# my_info[0] = "Lam"
# print(my_info[0]) --> cannot print since tuple is immutable

# unpacking a tuple
name, age, occupation = my_info
print(name)
print(age)
print(occupation)

# how to create one element tuple
# using TRAILING COMMA
one_element_tuple = (4,)
print(one_element_tuple)