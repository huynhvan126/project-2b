# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/10/2024
# Description: Converting temperature from C to F and rounded to 7 decimal places
print("Please enter a Celsius temperature.")
celsius = float(input())
print("The equivalent Fahrenheit temperature is:")
fahrenheit = format(((9/5)*celsius) + 32,'7f') #limit to 7 decimal places
print(fahrenheit)