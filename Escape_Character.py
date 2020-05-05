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

