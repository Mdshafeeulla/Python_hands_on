# Tuple and Set Operations
#
# This exercise tests your understanding of Python's immutable and mutable collection types, along with data transformation techniques.
#
# Step 1
# Create a tuple from a list of strings
#
# Step 2
# Convert tuple to set to remove duplicates
#
# Step 3
# Return sorted list of unique elements

#The tuple is an immuatable and represented by ()
#The set is muatable but not print duplicate values and represented by {}

my_lists = ['Name','Class',1,2,3,1,'Name']
print(f"Original list:{my_lists}")
print(f"The datatype before conversion to tuple {type(my_lists)}\n")

my_tup = tuple(my_lists)
print(f"converted into tuple:{my_tup}")
print(f"The datatype after conversion to tuple {type(my_tup)}\n")

my_set = set(my_tup)
print(f"converted into set{my_set}")
print(f"The datatype is converted into set in order to remove the duplicates and print the unique values {type(my_set)}\n")

my_list = list(my_set)
print(f"converted into list{my_list}")
print(f"The datatype is converted into list {type(my_list)}")
