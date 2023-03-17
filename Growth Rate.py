init_pop = int(input("Enter the initial number of organisms: "))

growth_rate = float(input("Enter the rate of growth (a real number > 1): "))

while(growth_rate <= 1):
    print("Invalid growth rate. Please try again.")
    growth_rate = float(input("Enter the rate of growth (a real number > 1): "))

num_hours = int(input("Enter the number of hours to achieve the rate of growth: "))

total_hours = int(input("Enter the total hours of growth: "))

total_pop = init_pop

hours = 1

while (hours < total_hours):
    init_pop *= growth_rate
    total_pop += init_pop
    hours += num_hours
    if (num_hours == total_hours):
        break
print("The total population is: " + str(init_pop))
