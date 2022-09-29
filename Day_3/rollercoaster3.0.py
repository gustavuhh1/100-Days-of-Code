# Don't change code below 🚨
height = int(input("what is your height in cm? "))
age = int(input("What is your age? "))
# Don't change code up 🚨
ticket = 0
if height > 120:
    print("Welcome to The Rollercoaster, Happy fun!")
    if age < 12:
        print("Child tickets are $5")
        ticket = 5
    elif age <= 18:
        print("Youth tickets are $7")
        ticket = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets are $12")
        ticket = 12

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        ticket += 3

    print(f"Your final bill is {ticket}")

else:
    print("Sorry, you have to grow taller before you can ride")
