# Exercise 5: NumPy Array Manipulation
#
# Matrix Creation
# Using NumPy, create a 5×5 matrix with values ranging from 1 to 25
#
# Diagonal Extraction
# Extract the diagonal elements from your generated matrix
#
# Calculation
# Calculate the sum of the extracted diagonal elements

import numpy as np

#creating an array of numbers from 1 to 25
arr = np.arange(1,26)
print(f"The array of numbers from 1 to 25{arr}\n")
matrix = arr.reshape(5,5)
print(f"The matrix with 5 rows and columns{matrix}\n")

dig = matrix.diagonal()
print(f"The array of diagonal elements{dig}\n")
print(f"The sum of diagonal elements")
print(dig.sum())