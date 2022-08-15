# tip calculator

# Print start message to the terminal
print("Welcome to the tip calculator!")

# Get the total bill amount in string form
total_bill = input("What was the total bill?\n$")

# Get the ip percentage
tip_percent = input("What percenatge tip would you like to give?\n")

# Get the number of people who will split the bill
num_people = input("How many people to split the bill?\n")

# Compute the total tip amount
tip_amount = float(total_bill) * (float(tip_percent) / 100)

# Compute the amount each persion should pay
total_per_person = round((float(total_bill) + tip_amount) / int(num_people), 2)

print("$" + str(total_per_person))