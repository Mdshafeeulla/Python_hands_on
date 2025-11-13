# Exercise 6: Pandas Series Creation and Indexing
#
# Part A
# Create a Pandas Series from a list of temperatures measured in Celsius
#
# Part B
# Convert the temperatures to Fahrenheit and add them as a new Series with the same index
import pandas as pd

temp_in_celsius = [24,32,24,28,31]
celsius_series = pd.Series(temp_in_celsius)
print(f"The temperature in celsius \n{celsius_series}")

def celsius_to_fehrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

fahrenheit_series = celsius_series.apply(celsius_to_fehrenheit)
print(f"The temperature in fahrenheit\n")

print(fahrenheit_series)
