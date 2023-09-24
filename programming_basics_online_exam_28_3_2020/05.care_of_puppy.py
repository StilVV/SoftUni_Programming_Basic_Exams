food = int(input()) * 1000

while True:
    eaten_food = input()

    if eaten_food != "Adopted":
        eaten_food = int(eaten_food)
    else:
        break

    food -= eaten_food

if food >= 0:
    print(f"Food is enough! Leftovers: {food} grams.")
else:
    print(f"Food is not enough. You need {abs(food)} grams more.")
