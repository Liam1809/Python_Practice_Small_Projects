# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary
# Write your sum_values function here:
def sum_values(my_dictionary):
  sum_lst = my_dictionary.values()
  sum = 0
  for element in sum_lst:
    sum += element
  return sum

# Uncomment these function calls to test your sum_values function:
# print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
# print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  sum = 0
  for key,value in my_dictionary.items():
    if key %2 == 0:
      sum += value
  return sum

# Uncomment these function calls to test your  function:
# print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
# print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary
# Write your add_ten function here:
def add_ten(my_dictionary):
  # for key,value in my_dictionary.items():
  #   my_dictionary.update({key : (value + 10)})
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary
# Uncomment these function calls to test your  function:
# print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
# print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  keys_lst = my_dictionary.keys()
  values_lst = my_dictionary.values()
  empty_lst = []
  for key in keys_lst:
    if key in values_lst:
      empty_lst.append(key)
  return empty_lst

# # Uncomment these function calls to test your  function:
# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
# print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.
# Write your max_key function here:
def max_key(my_dictionary):
  max_value = max(my_dictionary.values())
  for key in my_dictionary.keys():
    if max_value == my_dictionary[key]:
      return key
  # largest_value = 0
  # largest_key = 0
  # for key in my_dictionary.keys():
  #   if largest_value < my_dictionary[key]:
  #     largest_value = my_dictionary[key]
  #     largest_key = key
  # return largest_key
# Uncomment these function calls to test your  function:
# print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
# print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  empty = {}
  for word in words:
    empty[word] = len(word)
  return empty

# Uncomment these function calls to test your  function:
# print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
# print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}