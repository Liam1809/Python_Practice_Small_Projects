letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  empty_lst = []
  for element in word:
    if element not in empty_lst and element in word:
      empty_lst.append(element)
  return len(empty_lst)
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# Write your count_char_x function here:
def count_char_x(word, x):
  # return word.count(x)
  count = 0
  for element in word:
    if element == x:
      count += 1
  return count
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  # op1
  # return word.count(x)
  # op2
  count = 0
  for i in range(len(word)):
    if word[i: i + len(x)] == x:
      count += 1
  return count
  # op3
  # w = word.split(x)
  # return len(w) - 1
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1