weight_lbs = float(input("Please enter your weight (lbs): "))
height_in = float(input("Please enter your height (inches): "))

KG_CONSTANT = 2.2046
weight_kg = weight_lbs/KG_CONSTANT

M_CONSTANT = 0.0254
height_m = height_in * M_CONSTANT

height_m_squared = height_m ** 2

BMI = weight_kg/height_m_squared

rounded_BMI = round(BMI, 2)

print("Your BMI is: ", rounded_BMI)