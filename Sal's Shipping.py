Premium_Ground_Shipping = 125.0
def cost_ground_shipping(weight):
  if weight <= 2:
    return weight * 1.5 + 20
  elif weight > 2 and weight <= 6:
    return weight * 3 + 20
  elif weight > 6 and weight <= 10:
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20
def cost_drone_shipping(weight):
  if weight <= 2:
    return weight * 4.5 
  elif weight > 2 and weight <= 6:
    return weight * 9 
  elif weight > 6 and weight <= 10:
    return weight * 12 
  else:
    return weight * 14.25
def cheapest_shipping(weight):
  if cost_ground_shipping(weight) <  cost_drone_shipping(weight) and cost_ground_shipping(weight) < Premium_Ground_Shipping:
    print("You should ship using ground shipping, it will cost " + str(cost_ground_shipping(weight)))
  elif cost_drone_shipping(weight) < cost_ground_shipping(weight) and cost_drone_shipping(weight) < Premium_Ground_Shipping:
    print("You should ship using drone shipping, it will cost " + str(cost_drone_shipping(weight)))
  else:
        print("You should ship using Premium_Ground_Shipping, it will cost " + str(Premium_Ground_Shipping))                                                                                       
print("What is the cheapest method of shipping a 4.8 pound package and how much would it cost?")
cheapest_shipping(4.8)
print("What is the cheapest method of shipping a 41.5 pound package and how much would it cost?")
cheapest_shipping(41.5)

