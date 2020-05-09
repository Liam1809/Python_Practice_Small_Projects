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