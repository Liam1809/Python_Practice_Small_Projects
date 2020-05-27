# A string is a list of characters.
# A character can be selected from a string using its index string_name[index]. These indices start at 0.
# A ‘slice’ can be selected from a string. These can be between two indices or can be open-ended, selecting all of the string from a point.
# Strings can be concatenated to make larger strings.
# len() can be used to determine the number of characters in a string.
# Strings can be iterated through using for loops.
# Iterating through strings opens up a huge potential for applications, especially when combined with conditional statements.
def username_generator(first_name, last_name):
      if len(first_name) <= 3 and len(last_name) <= 4:
         username = first_name + last_name
      elif len(first_name) <= 3:
         username = first_name + last_name[:4]
      elif len(last_name) <= 4:
         username = first_name[:3] + last_name
      else:
         username = first_name[:3] + last_name[:4]
      return username
# print(username_generator("Liam", "Ha"))
def password_generator(username):
  password = ""
  for i in range(len(username)):
    password += username[i -1]
  return password
# print(password_generator("AbeSimp"))