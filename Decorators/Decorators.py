# 1. Functions are objects

# define function
def add_five(num):
    print(num + 5)
    
# call function
add_five
print(add_five)
print(add_five(5))

# 2. Functions within functions

# define function
def add_five(num):
    def add_two(num):
        return num + 2
    num_plus_two = add_two(num)
    print(num_plus_two + 3)
# call function
# add_two(7)
# getting error
add_five(10)
# should print 15

# 3. Returning functions from functions

def get_math_functions(operation): # + or -
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    if operation == "+":
        return add
    elif operation == "-":
        return sub
    
add_function = get_math_functions("+")
sub_function = get_math_functions("-")
print(add_function)
print(sub_function)
# should return add/sub function object
print(add_function(4, 6))
# should print 10
print(sub_function(4, 2))
# should print 2

# 4. Decorating a function

def title_decorator(print_name_function):
    def wrapper():
        print("Hello")
        print_name_function()
    return wrapper
    
def print_my_name():
    print("Liam")
    
decorated_function = title_decorator(print_my_name)

decorated_function()

# 5. Decorators

def title_decorator(print_name_function):
    def wrapper():
        print("Hello")
        print_name_function()
    return wrapper
 
@title_decorator   
def print_my_name():
    print("Liam")
    
print_my_name()

# 6. Decorators w/ parameters

def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Hello")
        print_name_function(*args, **kwargs)
    return wrapper
 
@title_decorator   
def print_my_name(name, age = 50, **info):
    print(name + " is " + str(age) + " years old.")
    for key, value in info.items():
        print(key, value)
    
info = {"ocuppation" : "student"}
print_my_name("Liam", age = 20, **info)