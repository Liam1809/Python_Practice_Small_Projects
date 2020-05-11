# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# Notice that:

# A dictionary begins and ends with curly braces ({ and }).
# Each item consists of a key (i.e., “oatmeal”) and a value (i.e., 3)
# Each key: value pair (i.e., "oatmeal": 3 or "avocado toast": 6) is separated by a comma (,)
# It’s considered good practice to insert a space () after each comma, but your code will still run without the space.
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)

# each key has its own value, no two keys have the same value ==> override value
dictionary = {"key_1": "value_1", "key_1": "value_2", "key_2": "value_2"}
print(dictionary) # {'key_1': 'value_2', 'key_2': 'value_2'}


#  the keys can be numbers as well. For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:
# subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
# Values can be any type. You can use a string, a number, a list, or even another dictionary as the value associated with a key!
# students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
# The list ["Aaron", "Delila", "Samson"], which is the value for the key "software design", represents the students in that class.

# You can also mix and match key and value types. For example:

# person = {"name": "Shuri", "age": 18, "siblings": ["T'Chaka", "Ramonda"]}

# You can create an empty dictionary using either of the two methods shown here.

# locations = {}
# # OR
# locations = dict()
# To add values to the dictionary you can use the index syntax (square brackets) or call the update() function on the dictionary and pass data to be populated into the dictionary. The update method can be used to populate multiple key/values to the dictionary. The syntax for these is shown below.

# locations['Paris'] = 100
# locations.update({"London": 75})
# locations.update({"New York": 83, "Vancouver" : 110})

# print(locations)
# # {'Paris': 100, 'London': 75, 'New York': 83, 'Vancouver': 110}

# We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary. If we try to, we will get a TypeError. For example:

# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# will yield:

# TypeError: unhashable type: 'list'
# The word “unhashable” in this context means that this ‘list’ is an object that can be changed. Dictionaries in Python rely on each key having a hash value, a specific identifier for the key. If the key can change, that hash value would not be reliable. So the keys must always be unchangeable, hashable data types, like numbers or strings.

# a tuple is a hashable value and can be used as a dictionary key. A tuple would be useful as a key when storing values associated with a grid or some other coordinate type system. The following code example shows a dictionary with keys representing a simple x,y grid system.

coordinates = { (0,0) : 100, (1,1) : 200}
coordinates[(1,0)] = 150
coordinates[(0,1)] = 125

print(coordinates)
# {(0, 0): 100, (1, 1): 200, (1, 0): 150, (0, 1): 125}

# Add A Key
# To add a single key : value pair to a dictionary, we can use the syntax:

# my_dict["new_key"] = "new_value"
# For example, if we had our menu object from the first exercise:

# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# and we wanted to add a new item, "cheesecake" for 8 dollars, we could use:

# menu["cheesecake"] = 8
# Now, menu looks like:

# {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

# Add Multiple Keys
# If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

# Looking at our sensors object from the first exercise:

# sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
# If we wanted to add 3 new rooms, we could use:

# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
# which would add all three items to the sensors dictionary. Now, sensors looks like:

#  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper" : 138475, "stringQueen" : 85739})
print(user_ids)

# Overwrite Values
# we cannot overwrite key
# We know that we can add a key by using syntax like:

# menu['avocado toast'] = 7
# which will create a key 'avocado toast' and set the value to 7. But what if we already have an 'avocado toast' entry in the menu dictionary?

# In that case, our value assignment would overwrite the existing value attached to the key 'avocado toast'.

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
# would yield:

# {"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# Notice the value of "oatmeal" has now changed to 5.

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)

# List Comprehensions to Dictionaries
# Let’s say we have two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:

# names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# heights = [61, 70, 67, 64]
# Python allows you to create a dictionary using a list comprehension, with this syntax:

# students = {key:value for key, value in zip(names, heights)}
# #students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
# Remember that zip() combines two lists into a zipped list of pairs. This list comprehension:

# Takes a pair from the zipped list of pairs from names and heights
# Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
# Creates a key : value item in the students dictionary
# Repeats steps 1-3 for the entire list of pairs
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for (key,value) in zipped_drinks}

# duplicates treated as update in zip
cities = ["New York", "London", "Sydney", "New York"]
temps = [ 85, 81, 65, 99]

weather = { key:value for key,value in zip(cities, temps)}

print(weather)
# {'New York': 99, 'London': 81, 'Sydney': 65}

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for (song,playcount) in zip(songs, playcounts)}
print(plays)
plays["Purple Haze"] = 1
plays.update({"Respect" : 94})

library = {"The Best Songs" : plays, "Sunday Feelings" : {}}

print(library)


# Try/Except KeyError
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
# caffeine_level["matcha"] = 30
try:
  print(caffeine_level["matcha"])
except KeyError as key:
  print("Unknown "+ str(key) + " Caffeine Level")
  
  
#   Safely Get a Key
# We saw in the last exercise that we had to add a key:value pair to a dictionary in order to avoid a KeyError. This solution is not sustainable. We can’t predict every key a user may call and add all of those placeholder values to our dictionary!

# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default:

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
print(building_heights.get("Shanghai Tower"))

#this line will return None:
print(building_heights.get("My House"))

# You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary:

print(building_heights.get('Shanghai Tower', 0))
# 632
print(building_heights.get('Mt Olympus', 0))
# 0
print(building_heights.get('Kilimanjaro', 'No Value'))
# 'No Value'

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# Delete a Key
# Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this dictionary mapping ticket numbers to prizes:

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
# When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize has been given away. We can use .pop() to do this. Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary:

raffle.pop(320291, "No Prize")
# "Gift Basket"
print(raffle)
# {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
raffle.pop(100000, "No Prize")
# "No Prize"
print(raffle)
# {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
raffle.pop(872921, "No Prize")
# "Concert Tickets"
print(raffle)
# {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}
# .pop() works to delete items from a dictionary, when you know the key value.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)

# Get All Keys
# Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a math class and their grades:

# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
# We want to get a roster of the students in the class, without including their grades. We can do this with the built-in list() function:

# >>> list(test_scores)
# ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
# Dictionaries also have a .keys() method that returns a dict_keys object. A dict_keys object is a view object, which provides a look at the current state of the dicitonary, without the user being able to modify anything. The dict_keys object returned by .keys() is a set of the keys in the dictionary. You cannot add or remove elements from a dict_keys object, but it can be used in the place of a list for iteration:

# for student in test_scores.keys():
#   print(student)
# will yield:

# "Grace"
# "Jeffrey"
# "Sylvia"
# "Pedro"
# "Martin"
# "Dina"

# The main diff is that .keys() method is a view of the dictionary object. That means when you update the dictionary, the object dict_keys will shows the updated value.

# If you use the list then the list will create a snapshot of keys present at the time of assignment and it will not be in sync with dictionary updates.

# Ex:

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
lessons = num_exercises.keys()
lesson_lst = list(num_exercises)
print(users)
print(lessons)
print(lesson_lst)
num_exercises.update({"exception":3})
print(lessons)
print(lesson_lst)

# Get All Values
# Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!) with all of the values in the dictionary. It can be used in the place of a list for iteration:

# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# for score_list in test_scores.values():
#   print(score_list)
# will yield:

# [80, 72, 90]
# [88, 68, 81]
# [80, 82, 84]
# [98, 96, 95]
# [78, 80, 78]
# [64, 60, 75]
# There is no built-in function to get all of the values as a list, but if you really want to, you can use:

# list(test_scores.values())
# However, for most purposes, the dict_list object will act the way you want a list to act.

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for number in num_exercises.values():
     total_exercises += number

print(total_exercises)
print(list(num_exercises.values()))

cities = {"Los Angeles": 3971883,
          "San Diego": 1394928,
          "San Jose": 1026908}

print(sum(cities.values()))
print(max(cities.values()))
print(min(cities.values()))

# Get All Items
# You can get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list object. Each element of the dict_list returned by .items() is a tuple consisting of:

# (key, value)
# so to iterate through, you can use this syntax:

# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

# for company, value in biggest_brands.items():
#   print(company + " has a value of " + str(value) + " billion dollars. ")
# which would yield this output:

# Apple has a value of 184 billion dollars.
# Google has a value of 141.7 billion dollars.
# Microsoft has a value of 80 billion dollars.
# Coca-Cola has a value of 69.7 billion dollars.
# Amazon has a value of 64.8 billion dollars.

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, age in pct_women_in_occupation.items():
  print("Women make up " +  str(age)  + " percent of " + occupation + "s")
  
letters = { "A": 10, "B": 20, "C": 30, "D": 40 }
# access tuple data 
for data in letters.items():
    print(data[0])
    print(data[1])
    
import random
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

#empty dict
spread = {}
value_tarot = list(tarot.keys())
# print(value_tarot)
for element in ["past", "present", "future"]:
   spread[element] = tarot.pop(random.choice(value_tarot))
# display
for key, value in spread.items():
  print("Your {key} is the {value} card.".format(key = key, value = value))
