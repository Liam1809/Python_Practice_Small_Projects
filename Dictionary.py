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
