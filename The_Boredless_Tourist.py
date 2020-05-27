# The Boredless Tourist
# Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. 
# We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by. 
# Let’s get started!

# Now let’s create some data that we’re going to use to test the functionality that we create for The Boredless Tourist.

# The first is our list of destinations that we’re going to be using.

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# test get_destination_index()
# print(get_destination_index("Los Angeles, USA"))
# should print 2
# print(get_destination_index("Paris, France"))
# should print 0
# get_destination_index("Hyderabad, India")

# Travelling To Faraway Lands

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# test get_traveler_location()
# test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)