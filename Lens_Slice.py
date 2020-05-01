toppings = ["peppeeroni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushtooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
# Find the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas =len(toppings)
print("We sell " + str(num_pizzas) + " differeent kinds of pizza!") 
pizzas = list(zip(toppings, prices))
print(pizzas)
# Sort pizzas so that the pizzas with the lowest prices are at the start of the list.
pizzas.sort(key = lambda x : x[1])
# Store the first element of pizzas in a variable called cheapest_pizza.
cheapest_pizza = pizzas[0]
# Get the last item of the pizzas list and store it in a variable called priciest_pizza.
priciest_pizza = pizzas[-1]
# Slice the pizzas list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizzas[:3]
print(three_cheapest)
# Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)