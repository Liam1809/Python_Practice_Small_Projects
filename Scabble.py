# In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# list comprehension to zip and create new dict
letter_to_points = {letter : point for (letter,point) in zip(letters, points)}

letter_to_points[" "] = 0
# display
# print(letter_to_points)


def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total
# Testing
# brownie_points  = score_word("BROWNIE")
# print(brownie_points)

# score a Game