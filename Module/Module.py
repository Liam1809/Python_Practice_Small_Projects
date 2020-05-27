

# Import Decimal below:
from decimal import Decimal
# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# Import random below:
import random
# Create random_list below:
random_list = []

# Create randomer_number below:
random_list = [random.randint(1,101) for number in range(101)]
randomer_number = random.choice(random_list)
# Print randomer_number below:
print(randomer_number)

# Aliasing calendar as c
import calendar as c 
print(c.month_name[9])

# Three different ways to import modules: # First way
# import module
# module.function()
#  Second way
#   from module import function
#   function()
#   Third way
#   from module import *
#   function()

# DATETIME module
from datetime import datetime
birthday = datetime(1999, 9, 18, 22, 30, 12)

print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.weekday())
# current datetime
print(datetime.now())
# subtract
print(datetime(1999, 9, 18) - datetime(2020, 5, 8))

#https://docs.python.org/3/library/datetime.html

# parsing a string using strptime 
parsed_string = datetime.strptime("Sep 18, 1999", "%b %d, %Y")
print(parsed_string.month)
print(parsed_string.day)
print(parsed_string.year)
# rendering a date as av string using strftime
date_now = datetime.strftime(datetime.now(), "%d %b, %Y")
print(date_now)