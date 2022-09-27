# 🚨 Don't change the code bellow 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code bellow this line

bmi = round(weight / (height**2))
print(bmi)

if bmi < 18.5:
    print("Vai comer diabo")
if bmi > 18.5 and bmi < 25:
    print("ta susu")
if bmi > 25 and bmi < 30:
    print("Vai da uma corridinha")
if bmi > 30 and bmi < 35:
    print("Parar o Bigmac ai rei")
if bmi > 35:
    print("OBESO GORDÃO")
