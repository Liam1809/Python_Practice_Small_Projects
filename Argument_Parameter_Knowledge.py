# A parameter is a variable in the definition of a function.
# An argument is the value being passed into a function call.
# A function definition begins with def and contains the entire following indented block.
# And function calls are the places a function is invoked, with parentheses, after its definition
# Let’s see this in a block of code:

# # The "def" keyword is the start of a function definition
# def function_name(parameter1, parameter2):
#   # The placeholder variables used inside a function definition are called parameters
#   print(parameter1)
#   return parameter2
# # The outdent signals the end of the function definition

# # "Arguments" are the values passed into a function call
# argument1 = "argument 1"
# argument2 = "argument 2"

# # A function call uses the functions name with a pair of parentheses
# # and can return a value
# return_val = function_name(argument1, argument2)
# In the above code we defined the function function_name that takes two parameters, parameter1 and parameter2. We then create two variables with the values "argument 1" and "argument 2" and proceed to call function_name with the two arguments.

# Some of this terminology can be used inconsistently between schools, people, and businesses. Some people don’t differentiate between “parameter” and “argument” when speaking. It’s useful here because we’re going to be looking at a lot of behavior that looks very similar in a function definition and a function call, but will be subtly different. But the distinction is sometimes unnecessary, so don’t get too hung up if something is called a “parameter” that should be an “argument” or vice versa.


# None: It's Nothing!
# How do you define a variable that you can’t assign a value to yet? You use None.

# None is a special value in Python. It is unique (there can’t be two different Nones) and immutable (you can’t update None or assign new attributes to it).

# none_var = None
# if none_var:
#   print("Hello!")
# else:
#   print("Goodbye")

# # Prints "Goodbye"
# None is falsy, meaning that it evaluates to False in an if statement, which is why the above code prints “Goodbye”. None is also unique, which means that you can test if something is None using the is keyword.

# # first we define session_id as None
# session_id = None

# if session_id is None:
#   print("session ID is None!")
#   # this prints out "session ID is None!"

# # we can assign something to session_id
# if active_session:
#   session_id = active_session.id

# # but if there's no active_session, we don't send sensitive data
# if session_id is not None:
#   send_sensitive_data(session_id)
# Above we initialize our session_id to None, then set our session_id if there is an active session. Since session_id could either be None we check if session_id is None before sending our sensitive data.

# Default Return
# What does a function return when it doesn’t return anything? This sounds like a riddle, but there is a correct answer. A Python function that does not have any explicit return statement will return None after completing. This means that all functions in Python return something, whether it’s explicit or not. For example:

# def no_return():
#   print("You've hit the point of no return")
#   # notice no return statement

# here_it_is = no_return()

# print(here_it_is)
# # Prints out "None"
# Above we defined a function called no_return() and saved the result to a variable here_it_is. When we print() the value of here_it_is we get None, referring to Python’s None. It’s possible to make this syntax even more explicit — a return statement without any value returns None also.

# def fifty_percent_off(item):
#   # Check if item.cost exists
#   if hasattr(item, 'cost'):
#     return item.cost / 2

#   # If not, return None 
#   return

# sale_price = fifty_percent_off(product)

# if sale_price is None:
#   print("This product is not for sale!")
# Here we have implemented a function that returns the cost of a product with “50% Off” (or “half price”). We check if the item passed to our function has a cost attribute. If it exists, we return half the cost. If not, we simply return, which returns None.

# When we plug a product into this function, we can expect two possibilities: the first is that the item has a cost and this function returns half of that. The other is that item does not have a listed cost and so the function returns None. We can put error handling in the rest of our code, if we get None back from this function that means whatever we’re looking at isn’t for sale!

# store the result of this print() statement in the variable prints_return
prints_return = print("What does this print function return?")

# print out the value of prints_return
print(prints_return)

# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]

list_sort_return = sort_this_list.sort()
# print out the value of list_sort_return

print(list_sort_return)


# Default Arguments
# Function arguments are required in Python. So a standard function definition that defines two parameters requires two arguments passed into the function.

# # Function definition with two required parameters
# def create_user(username, is_admin):
#   create_email(username)
#   set_permissions(is_admin)

# # Function call with all two required arguments
# user1 = create_user('johnny_thunder', True)

# # Raises a "TypeError: Missing 1 required positional argument"
# user2 = create_user('djohansen')
# Above we defined our function, create_user, with two parameters. We first called it with two arguments, but then tried calling it with only one argument and got an error. What if we had sensible defaults for this argument?

# Not all function arguments in Python need to be required. If we give a default argument to a Python function that argument won’t be required when we call the function.

# # Function defined with one required and one optional parameter
# def create_user(username, is_admin=False):
#   create_email(username)
#   set_permissions(is_admin)

# # Calling with two arguments uses the default value for is_admin
# user2 = create_user('djohansen')
# Above we defined create_user with a default argument for is_admin, so we can call that function with only the one argument 'djohansen'. It assumes the default value for is_admin: False. We can make both of our parameters have a default value (therefore making them all optional).

# # We can make all three parameters optional
# def create_user(username=None, is_admin=False):
#   if username is None:
#     username = "Guest"
#   else:
#     create_email(username)
#   set_permissions(is_admin)

# # So we can call with just one value
# user3 = create_user('ssylvain')
# # Or no value at all, which would create a Guest user
# user4 = create_user()
# Above we define the function with all optional parameters, if we call it with one argument that gets interpreted as username. We can call it without any arguments at all, which would only use the default values.



# Using Keyword and Positional Arguments
# Not all of your arguments need to have default values. But Python will only accept functions defined with their parameters in a specific order. The required parameters need to occur before any parameters with a default argument.

# # Raises a TypeError
# def create_user(is_admin=False, username, password):
#   create_email(username, password)
#   set_permissions(is_admin)
# In the above code, we attempt to define a default argument for is_admin without defining default arguments for the later parameters: username and password.

# If we want to give is_admin a default argument, we need to list it last in our function definition:

# # Works perfectly
# def create_user(username, password, is_admin=False):
#   create_email(username, password)
#   set_permissions(is_admin)