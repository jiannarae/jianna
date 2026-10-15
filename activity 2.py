# GLOBAL VARIABLES
sum = 0
difference = 0

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

def calculate_sum():
    # LOCAL VARIABLES
    global sum
    sum = number_1 + number_2

def calculate_difference():
    # LOCAL VARIABLES
    global difference
    difference = number_1 - number_2

# GLOBAL VARIABLES
calculate_sum()
calculate_difference()

print(f"Sum: {sum}")
print(f"Difference: {difference}")
