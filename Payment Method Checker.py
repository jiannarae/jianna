# AUTHOR: JIANNA DELOS REYES
# 8 - CAMIA
# 9-17-2026
# PAYMENT METHOD CHECKER

valid_payment =["cash", "gcash", "card"]

payment = input("Enter your mode of payment: ").lower()

if payment in valid_payment:
    print("Valid Payment Method")
else:
    print("Invalid Payment Method")