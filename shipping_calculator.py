def ground_shipping(weight):
  
  if weight < 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75

  return(weight * price_per_pound + 20)

print(ground_shipping(8.4))

premium_ground_shipping = 125.00


def drone_shipping(weight):

  if weight < 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25

  return(weight * price_per_pound)

print(drone_shipping(1.5))


def cheapest_shipping_method(weight):

  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_ground_shipping

  if ground < drone and ground < premium:
    method = "standard ground"
    cost = ground
  elif drone < ground and drone < premium:
    method = "drone"
    cost = drone
  else:
    method = premium
    cost = premium

  print(
    "The cheapest option available is %.2f with %s shipping."
    % (cost, method)
    )



cheapest_shipping_method(4.8)
cheapest_shipping_method(41.5)


