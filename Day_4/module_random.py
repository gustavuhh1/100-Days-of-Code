import random

random_int = random.randint(1, 10)
print(random_int)

# 0.0000000 - 0.99999999...
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

states_of_brazil = ["Ceara", "Piaui", "Rio de Janeiro",
                    "Sao paulo", "brasilia", "rn", "Rondonia"]

states_of_brazil[1] = "MG"

states_of_brazil.append("bahia")

print(states_of_brazil[3:7])
