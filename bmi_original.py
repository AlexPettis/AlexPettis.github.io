"""
Program: bmi.py
Author: Ed Hassler
Last date modified: 1/31/2022
The purpose of this program is to compute an individual's Body Mass Index (BMI)
based on their height in inches and weight in pounds.
"""
import math

LBS_PER_KG = 2.2046
INCHES_PER_METER = 39.3701


def main():
    weight_lbs = float(input("Please enter weight (pounds): "))
    height_in = float(input("Please enter height (inches): "))
    weight_kg = weight(weight_lbs)
    height_m = height(height_in)
    bmi_value = bmi(weight_kg, height_m)
    print("BMI is", bmi_value)

def weight(weight_lbs):
    weight_kg = weight_lbs / LBS_PER_KG
    return weight_kg

def height(height_in):
    height_m = height_in / INCHES_PER_METER
    return height_m

def bmi(weight_kg, height_m):
    bmi = weight_kg / height_m**2
    return bmi

if __name__ == "__main__":
    main()