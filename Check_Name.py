# Write your check_for_name function here:
def check_for_name(sentence, name):
  words = sentence.split()
  if words[-1].lower() == name.lower():
      return True
  return False
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False