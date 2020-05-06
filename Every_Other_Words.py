# Write your every_other_letter function here:
def every_other_letter(word):
  lst = ""
  for i in range(0,len(word),2):
     lst += word[i]
  return lst
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 