# Input Processing
# Given a list of integers, write a function to identify even numbers
#
# Transformation
# Return a new list containing only the even numbers
#
# Output Format
# Sort the results in descending order

def is_even(num):
    if num % 2 == 0:
        print(f"The given number {num} is a even number ")
    else:
        print(f"The given number {num} is a odd number ")

is_even(4)
is_even(5)

#As we know the logic behind if it is divisble by 2.
#And we get a remainder as 0 then it is even