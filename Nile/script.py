from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# At The Nile our biggest concern is our consumers, and our biggest cost is delivering their goods to them. We want to develop a program that will help us minimize these costs so we can continue making everyone happy.

# First we’ll need to calculate these costs using a function that you’re going to write called calculate_shipping_cost().
# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type = "Overnight"):
  from_lat, from_long = from_coords
  to_lat, to_long = to_coords
  distance = get_distance(*from_coords, *to_coords)
  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
  return format_price(price)

# Test the function by calling 
test_function(calculate_shipping_cost)

# At The Nile, we have a joke. Without our fantastic drivers, who fulfill orders every day, we’d just be sitting with millions of toys, electronics, and clothing in warehouses to ourselves.

# Our team is important, and we want to make sure the hardest workers find their home in our careers. In order to do that, we need to figure out who the best person is for each job.
# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = driver.speed * distance
    price_for_driver = driver.salary * driver_time
    if cheapest_driver is None:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
  return cheapest_driver_price, cheapest_driver

# Test the function by calling 
test_function(calculate_driver_cost)

# Define calculate_money_made() here
def calculate_money_made(**trips):
  total_money_made = 0
  for trip_id, trip in trips.items():
    trip_revenue = trip.cost - trip.driver.cost
    total_money_made += trip_revenue
  return total_money_made

# Test the function by calling 
test_function(calculate_money_made)