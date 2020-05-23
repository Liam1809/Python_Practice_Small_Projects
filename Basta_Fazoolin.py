# This project invloving classes properties
# Basta Fazoolin'
# You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

# Making the Menus
# At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids.
class Menu():
  # constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # string repr
  def __repr__(self):
    return "{name} menu available from {start_time} to {end_time}".format(name = self.name, start_time = self.start_time, end_time = self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for key,value in purchased_items.items():
      if key in self.items:
        total += value * self.items[key]
    return "Total Price is {total}$".format(total = total)

# Making menus
brunch_dict = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_dict = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_dict = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_dict = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

# making instantiated of class Menu
brunch = Menu("brunch", brunch_dict, 1100, 1600)
early_bird = Menu("early_bird", early_bird_dict, 1500, 1800)
dinner = Menu("dinner", dinner_dict, 1700, 2300)
kids = Menu("kids", kids_dict, 1100, 2100)

# display menus
print("- Menus schedule")
print(brunch)
print(early_bird)
print(dinner)
print(kids)

# Brunch order
print("- Brunch order")
brunch_order = {"pancakes" : 1, "home fries" : 1, "coffee" : 2}
for key, value in brunch_order.items():
  print("{order} order of {dish}".format(order = value, dish = key))
# total price for Brunch order
print(brunch.calculate_bill(brunch_order))

# early-bird order
print("- Early-bird order")
early_bird_order = {"salumeria plate" : 3, "mushroom ravioli (vegan)": 2}
for key, value in early_bird_order.items():
  print("{order} order of {dish}".format(order = value, dish = key))
# total price for early-bird order
print(early_bird.calculate_bill(early_bird_order))

# Basta Fazoolin’ with my Heart has seen tremendous success with the family market, which is fantastic because when you’re at Basta Fazoolin’ with my Heart with family, that’s great!

# We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.
class Franchise():
  # constructor
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  # string rep
  def __repr__(self):
    return self.address

  def available_menus(self, time):
    avalable_menus = []
    for menu in menus:
      if time in range(menu.start_time, menu.end_time + 1):
        avalable_menus.append(menu)
    return avalable_menus
     
# a list of menu
menus = [brunch, early_bird, dinner, kids]
# instances
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
#
print("Flagship store is located at " + str(flagship_store))
print("New installment is located at " + str(new_installment))

# at flagship store
# available menus at 12 noon
print("- available menus")
print(*flagship_store.available_menus(1200), sep = "\n")
# at new_installment
# available menus at 5pm
print("- available menus")
print(*new_installment.available_menus(1700), sep = "\n")

