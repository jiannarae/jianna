sum = 0
difference = 0

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

def calculate_sum():
    global sum
    sum = number_1 + number_2

def calculate_difference():
    global difference
    difference = number_1 - number_2

calculate_sum()
calculate_difference()

print(f"Sum: {sum}")
print(f"Difference: {difference}")
