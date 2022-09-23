# Tip calculator
print("Welcome to the tip calculator.")
# Data
total = float(input("What was the total bill?" '$'))
percentage = int(
    input("what percetage tip would you like to give? 10, 12, pr 15? "))
peoples = input("how many people to split the bill? ")

percentage /= 100
percentage += 1
total *= percentage
division = total / int(peoples)
division = round(division, 2)
print(f"Each person should pay {division} ")

# COMPLETED