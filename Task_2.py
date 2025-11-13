# Input Processing
# Given a list of integers, write a function to identify even numbers
#
# Transformation
# Return a new list containing only the even numbers
#
# Output Format
# Sort the results in descending order

def is_even(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            print(f"The given number {num} is a even number ")
            evens.append(num)
        else:
            print(f"The given number {num} is a odd number ")
    print(f"This are the even numbers {evens}" )

is_even([1,2,3,4])

#As we know the logic behind if it is divisble by 2.
#And we get a remainder as 0 then it is even