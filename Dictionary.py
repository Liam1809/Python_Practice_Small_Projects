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