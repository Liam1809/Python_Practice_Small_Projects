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


# Keyword Arguments
# When we call a function in Python, we need to list the arguments to that function to match the order of the parameters in the function definition. We don’t necessarily need to do this if we pass keyword arguments.

# We use keyword arguments by passing arguments to a function with a special syntax that uses the names of the parameters. This is useful if the function has many optional default arguments or if the order of a function’s parameters is hard to tell. Here’s an example of a function with a lot of optional arguments.

# # Define a function with a bunch of default arguments
# def log_message(logging_style="shout", message="", font="Times", date=None):
#   if logging_style == 'shout':
#     # capitalize the message
#     message = message.upper()
#   print(message, date)

# # Now call the function with keyword arguments
# log_message(message="Hello from the past", date="November 20, 1693")
# Above we defined log_message(), which can take from 0 to 4 arguments. Since it’s not clear which order the four arguments might be defined in, we can use the parameter names to call the function. Notice that in our function call we use this syntax: message="Hello from the past". The key word message here needs to be the name of the parameter we are trying to pass the argument to.

# Don't Use Mutable Default Arguments
# When writing a function with default arguments, it can be tempting to include an empty list as a default argument to that function. Let’s say you have a function called populate_list that has two required arguments, but it’s easy to see that we might want to give it some default arguments in case we don’t have either list_to_populate or length every time. So we’d give it these defaults:

# def populate_list(list_to_populate=[], length=1):
#   for num in range(length):
#     list_to_populate.append(num)
#   return list_to_populate
# It’s reasonable to believe that list_to_populate will be given an empty list every time it’s called. This isn’t the case! list_to_populate will be given a new list once, in its definition, and all subsequent function calls will modify the same list. This will happen:

# returned_list = populate_list(length=4)
# print(returned_list)
# # Prints [0, 1, 2, 3] -- this is expected

# returned_list = populate_list(length=6)
# print(returned_list)
# # Prints [0, 1, 2, 3, 0, 1, 2, 3, 4, 5] -- this is a surprise!
# When we call populate_list a second time we’d expect the list [0, 1, 2, 3, 4, 5]. But the same list is used both times the function is called, causing some side-effects from the first function call to creep into the second. This is because a list is a mutable object.

# A mutable object refers to various data structures in Python that are intended to be mutated, or changed. A list has append and remove operations that change the nature of a list. Sets and dictionaries are two other mutable objects in Python.

# It might be helpful to note some of the objects in Python that are not mutable (and therefore OK to use as default arguments). int, float, and other numbers can’t be mutated (arithmetic operations will return a new number). tuples are a kind of immutable list. Strings are also immutable — operations that update a string will all return a completely new string.

def update_order(new_item, current_order=[]):
      current_order.append(new_item)
      return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)


# Using None as a Sentinel
# So if we can’t use a list as a default argument for a function, what can we use? If we want an empty list, we can use None as a special value to indicate we did not receive anything. After we check whether an argument was provided we can instantiate a new list if it wasn’t.

# def add_author(authors_books, current_books=None):
#   if current_books is None:
#     current_books = []

#   current_books.extend(authors_books)
#   return current_books
# In the above function, we accept current_books a value expected to be a list. But we don’t require it. If someone calls add_author() without giving an argument for current_books, we supply an empty list. This way multiple calls to add_author won’t include data from previous calls to add_author.

# Unpacking Multiple Returns
# A Python function can return multiple things. This is especially useful in cases where bundling data into a different structure (a dictionary or a list, for instance) would be excessive. In Python we can return multiple pieces of data by separating each variable with a comma:

# def multiple_returns(cool_num1, cool_num2):
#   sum_nums = cool_num1 + cool_num2
#   div_nums = cool_num1 / cool_num2
#   return sum_nums, div_nums
# Above we created a function that returns two results, sum_nums and div_nums. What happens when we call the function?

# sum_and_div = multiple_returns(20, 10)

# print(sum_and_div)
# # Prints "(30, 2)"

# print(sum_and_div[0])
# # Prints "30"
# So we get those two values back in what’s called a tuple, an immutable list-like object indicated by parentheses. We can index into the tuple the same way as a list and so sum_and_div[0] will give us our sum_nums value and sum_and_div[1] will produce our div_nums value.

# What if we wanted to save these two results in separate variables? Well we can by unpacking the function return. We can list our new variables, comma-separated, that correspond to the number of values returned:

# sum, div = sum_and_div(18, 9)

# print(sum)
# # Prints "27"

# print(div)
# # Prints "2"
# Above we were able to unpack the two values returned into separate variables.

# Positional Argument Unpacking
# We don’t always know how many arguments a function is going to receive, and sometimes we want to handle any possibility that comes at us. Python gives us two methods of unpacking arguments provided to functions. The first method is called positional argument unpacking, because it unpacks arguments given by position. Here’s what that looks like:

# def shout_strings(*args):
#   for argument in args:
#     print(argument.upper())

# shout_strings("hi", "what do we have here", "cool, thanks!")
# # Prints out:
# # "HI"
# # "WHAT DO WE HAVE HERE"
# # "COOL, THANKS!"
# In shout_strings() we use a single asterisk (*) to indicate we’ll accept any number of positional arguments passed to the function. Our parameter args is a tuple of all of the arguments passed. In this case args has three values inside, but it can have many more (or fewer).

# Note that args is just a parameter name, and we aren’t limited to that name (although it is rather standard practice). We can also have other positional parameters before our *args parameter. We can’t, as we’ll see, :

# def truncate_sentences(length, *sentences):
#   for sentence in sentences:
#     print(sentence[:length])

# truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
# # Prints out:
# # "What's g"
# # "Looks li"
# Above we defined a function truncate_sentences that takes a length parameter and also any number of sentences. The function prints out the first length many characters of each sentence in sentences.

from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_string = args[0]
  for arg in args[1:]:
    joined_string += '/' + arg
  return joined_string

print(myjoin(path_segment_1, path_segment_2, path_segment_3))

# Keyword Argument Unpacking
# Python doesn’t stop at allowing us to accept unlimited positional parameters, it gives us the power to define functions with unlimited keyword parameters too. The syntax is very similar, but uses two asterisks (**) instead of one. Instead of args, we call this kwargs — as a shorthand for keyword arguments.

# def arbitrary_keyword_args(**kwargs):
#   print(type(kwargs))
#   print(kwargs)
#   # See if there's an "anything_goes" keyword arg
#   # and print it
#   print(kwargs.get('anything_goes'))

# arbitrary_keyword_args(this_arg="wowzers", anything_goes=101)
# # Prints "<class 'dict'>
# # Prints "{'this_arg': 'wowzers', 'anything_goes': 101}"
# # Prints "101"
# As you can see, **kwargs gives us a dictionary with all the keyword arguments that were passed to arbitrary_keyword_args. We can access these arguments using standard dictionary methods.

# Since we’re not sure whether a keyword argument will exist, it’s probably best to use the dictionary’s .get() method to safely retrieve the keyword argument. Do you remember what .get() returns if the key is not in the dictionary? It’s None!


# Using Both Keyword and Positional Unpacking
# This keyword argument unpacking syntax can be used even if the function takes other parameters. However, the parameters must be listed in this order:

# All named positional parameters
# An unpacked positional parameter (*args)
# All named keyword parameters
# An unpacked keyword parameter (**kwargs)
# Here’s a function with all possible types of parameter:

# def main(filename, *args, user_list=None, **kwargs):
#   if user_list is None:
#     user_list = []

#   if '-a' in args:
#     user_list = all_users()

#   if kwargs.get('active'):
#     user_list = [user for user_list if user.active]

#   with open(filename) as user_file:
#     user_file.write(user_list)
# Looking at the signature of main() we define four different kinds of parameters. The first, filename is a normal required positional parameter. The second, *args, is all positional arguments given to a function after that organized as a tuple in the parameter args. The third, user_list, is a keyword parameter with a default value. Lastly, **kwargs is all other keyword arguments assembled as a dictionary in the parameter kwargs.

# A possible call to the function could look like this:

# main("files/users/userslist.txt", 
#      "-d", 
#      "-a", 
#      save_all_records=True, 
#      user_list=current_users)
# In the body of main() these arguments would look like this:

# filename == "files/users/userslist.txt"
# args == ('-d', '-a)
# user_list == current_users
# kwargs == {'save_all_records': True}
# We can use all four of these kinds of parameters to create functions that handle a lot of possible arguments being passed to them.

# the named (i.e., default) keyword argument and the **kwargs arguments can be interchanged in the function call. The only hard-and-fast rule is positional before named. But the interpreter is smart enough to sort out the named parameter from the keys in the **kwargs parameters.


#  the function remove() has three parameters: the required positional filename, the arbitrary positional args, and the arbitrary keyword kwargs.
def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()

  # Add code here to update text.
    for arg in args:
      text = text.replace(arg, "")
    for kwarg, replacement in kwargs.items():
        text = text.replace(kwarg, replacement)
    

  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))


# Passing Containers as Arguments
# Not only can we accept arbitrarily many parameters to a function in our definition, but Python also supports a syntax that makes deconstructing any data that you have on hand to feed into a function that accepts these kinds of unpacked arguments. The syntax is very similar, but is used when a function is called, not when it’s defined.

# def takes_many_args(*args):
#   print(','.join(args))

# long_list_of_args = [145, "Mexico City", 10.9, "85C"]

# # We can use the asterisk "*" to deconstruct the container.
# # This makes it so that instead of a list, a series of four different
# # positional arguments are passed to the function
# takes_many_args(*long_list_of_args)
# # Prints "145,Mexico City,10.9,85C"
# We can use the * when calling the function that takes a series of positional parameters to unwrap a list or a tuple. This makes it easy to provide a sequence of arguments to a function even if that function doesn’t take a list as an argument. Similarly we can use ** to destructure a dictionary.

# def pour_from_sink(temperature="Warm", flow="Medium")
#   set_temperature(temperature)
#   set_flow(flow)
#   open_sink()

# # Our function takes two keyword arguments
# # If we make a dictionary with their parameter names...
# sink_open_kwargs = {
#   'temperature': 'Hot',
#   'flow': "Slight",
# }

# # We can destructure them an pass to the function
# pour_from_sink(**sink_open_kwargs)
# # Equivalent to the following:
# # pour_from_sink(temperature="Hot", flow="Slight")
# So we can also use dictionaries and pass them into functions as keyword arguments with that syntax. Notice that our pour_from_sink() function doesn’t even accept arbitrary **kwargs. We can use this destructuring syntax even when the function has a specific number of keyword or positional arguments it accepts. We just need to be careful that the object we’re destructuring matches the length (and names, if a dictionary) of the signature of the function we’re passing it into.

# The default return of a function: None
# How to create default arguments to a function
# How to make sure our default arguments work the way we expect when dealing with lists.
# How to pass keyword arguments to a function
# How to unpack multiple returns from a function
# How to unpack multiple positional arguments to a function
# How to unpack multiple keyword arguments to a function
# How to pass a list as a series of arguments to a function
# How to pass a dictionary as a series of keyword arguments to a function