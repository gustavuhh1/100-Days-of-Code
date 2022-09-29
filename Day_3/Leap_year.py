# Don't change code below
year = int(input("Which year do you want to check? "))
# Don't change code above

# Write your code below this line

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year.")
        else:
            print("Not a leap year.")
    else:
        print("100")
else:
    print("Not a leap year.")
