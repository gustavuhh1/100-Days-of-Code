# Don't Change the code bellow
print("Welcome to Python pizza Deliveries!")
size = input("What size pizza do you want? S, M, L ? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
# Don't Change the code above

# Write your code below this line

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

# Verificação de complementos
order = ""
if add_pepperoni == "Y":
    order += "[add_pepperoni]"
else:
    order += "[-]"
if extra_cheese == "Y":
    order += "[Extra_cheese]"
else:
    order += "[-]"


print(f"Order: {size} - {order} - Total_bill: {bill}")
