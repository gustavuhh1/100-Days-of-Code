# Don't change code below 🚨
height = int(input("what is your height in cm? ")) 
age = int(input("What is your age? "))
# Don't change code up 🚨

if height < 120:
    print("Welcome to The Rollercoaster, Happy fun!")
    if age > 12:
        print("you need pay 12$")
    elif age > 16:
        print("you need pay 16$")
    else:
        print("you need pay 18$")
else:
    print("you don't have height for entry in rollercoaster")