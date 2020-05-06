# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  empty = ""
  if word.find(start) == -1 or word.find(end) == -1:
    return word
  else:
    a = word.find(start)
    b = word.find(end)
    lst = word[a:b]
    for element in lst:
      if element not in empty and element in lst:
        empty += element
  return empty

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"