import math
wall_length = float(input("Please enter the length of the wall (ft): "))
wall_height = float(input("Please enter the height of the wall (ft): "))
wall_area = float(wall_length * wall_height)

door_count = int(input("Please enter the number of doors: "))
door_allowance = door_count * 14

window_count = int(input("Please enter the number of windows: "))

window_allowance = window_count * 8.5

total_area = wall_area - door_allowance - window_allowance

gallons = total_area / 350

gallons_rounded_up = math.ceil(gallons)

paint_price = float(input("Please enter the price per gallon of paint: "))

cost = float(gallons * paint_price)

print("Gallons of paint needed: " + str(gallons_rounded_up))

rounded_cost = round(cost, 2)

print("Cost of paint: $" + str(rounded_cost))