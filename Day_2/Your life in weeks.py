# 🚨 Don't change the code above 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

missing_years = int(age) - 90
missing_years = missing_years * -1
days = missing_years * 365
weeks = missing_years * 52
months = missing_years * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Completed

