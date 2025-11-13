# Exercise 1: Python Basics and Data Types
# Write a Python program to check if a given number is prime.
#
# Requirements
# Input: An integer
# Output: True if prime, False otherwise
#
# Skills Tested
# Control flow structures
# Boolean logic
# Algorithm efficiency

import math

def is_prime(n: int):
    if n < 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    print(limit)

    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    print("The given number is prime")

print(is_prime(4))

# The logic behind this is a number is prime if it is divisible by 1 and itself
#A for loop is used to iterate from 3 to sqrt of the number
#We are doing the sqrt in order to avoid computation
#As we know that sqrt of even is even and odd is odd