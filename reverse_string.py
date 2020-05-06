# Write your reverse_string function here:
def reverse_string(word):
  string = ""
  # op1
  # lst = []
  # for element in word:
  #   lst += element
  # lst.reverse()
  # for element in lst:
  #   string += element
  # return string
  # op2
  for i in range(len(word) -1, -1, -1):
    string += word[i]
  return string
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print