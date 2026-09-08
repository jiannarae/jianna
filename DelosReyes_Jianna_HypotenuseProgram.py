import math

# Ask the user for the lengths of the 2 shorter sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

# Square a & b
a_squared = math.pow(a,2)
b_squared = math.pow(b,2)

# Add
sum_of_squares = a_squared + b_squared

# Calculate the hypotenuse
c = math.sqrt(sum_of_squares)

# Results
print(f"The distance between the two points is: , {c:.2f}")