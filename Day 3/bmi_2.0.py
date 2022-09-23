# 🚨 Don't change the code bellow 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code bellow this line

bmi = round(weight / (height**2))
print(bmi)

if bmi < 18.5:
    print("Under weight")
if bmi > 18.5 and bmi < 25:
    print("Normal Weight")
if bmi > 25 and bmi < 30:
    print("Over weight")
if bmi > 30 and bmi < 35:
    print("Obese")
if bmi > 35:
    print("OBESO GORDÃO")
