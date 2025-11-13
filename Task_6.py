# Exercise 6: Pandas Series Creation and Indexing
#
# Part A
# Create a Pandas Series from a list of temperatures measured in Celsius
#
# Part B
# Convert the temperatures to Fahrenheit and add them as a new Series with the same index
import pandas as pd

def celsius_to_Fahrenheit(celsius):

    print("Converting the list into series")
    celsius_series = pd.Series(celsius)
    print(f"{celsius_series}\n")
    Fahrenheit = (celsius_series * 1.8) +  32
    print("Creating a new series")
    Fahrenheit_series = pd.Series(Fahrenheit)
    print(Fahrenheit_series)

celsius_to_Fahrenheit([24,29,30,31,31,18])
