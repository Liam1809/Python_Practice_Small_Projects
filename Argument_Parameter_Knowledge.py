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