# Occasionally when working with strings, you’ll find that you want to include characters that already have a special meaning in python. 
# For example let’s say I create the string
#  favorite_fruit_conversation = "He said, "blueberries are my favorite!""
# We’ll have accidentally ended the string before we wanted to by including the " character. 
# The way we can do this is by introducing escape characters. 
# By adding a backslash in front of the special character we want to escape, \", we can include it in a string.
# favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
# Now it works!
password = "theycallme\"crazy\"91\\"

print(password)

# We can also split strings using escape sequences. Escape sequences are used to indicate that we want to split by something in a string that is not necessarily a character. The two escape sequences we will cover here are

# \n Newline
# \t Horizontal Tab
# Newline or \n will allow us to split a multi-line string by line breaks and \t will allow us to split a string by tabs. \t is particularly useful when dealing with certain datasets because it is not uncommon for data points to be separated by tabs.

# Let’s take a look at an example of splitting by an escape sequence:

smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

print(smooth_chorus)