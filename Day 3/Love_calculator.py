# Don't Chance the code bellow
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n ")
name2 = input("What is their name? \n ")
# Don't change the code above

# Write your code below this line
name1.lower()
name2.lower()
concat = name1 + name2
print(concat)

# t r u e / l o v e
t = concat.count("t")
r = concat.count("r")
u = concat.count("u")
e = concat.count("e")

sum1 = t+r+u+e

l = concat.count("l")
o = concat.count("o")
v = concat.count("v")
e = concat.count("e")

sum2 = l+o+v+e

x = str(sum1)+str(sum2)
y = int(x)
print(y)

if (y < 10) or (y > 90):
    print(f"Your love score is {y}, you go together like coke and mentos.")
elif (y >= 40) and (y <= 50):
    print(f"your score is {y}, you are alright together.")
else:
    print(f"Your score is {y}")
