days = int(input())
all_food = float(input())

biscuits = 0
dog_food = 0
cat_food = 0

for lunch in range(1, days + 1):
    dog_eat = int(input())
    cat_eat = int(input())

    dog_food += dog_eat
    cat_food += cat_eat

    if lunch % 3 == 0:
        biscuits += (dog_eat + cat_eat) * 0.10

all_food_eaten = dog_food + cat_food
all_food_rate = all_food_eaten / all_food * 100
dog_rate = (dog_food / all_food_eaten) * 100
cat_rate = (cat_food / all_food_eaten) * 100

print(f"Total eaten biscuits: {biscuits:.0f}gr.")
print(f"{all_food_rate:.2f}% of the food has been eaten.")
print(f"{dog_rate:.2f}% eaten from the dog.")
print(f"{cat_rate:.2f}% eaten from the cat.")
