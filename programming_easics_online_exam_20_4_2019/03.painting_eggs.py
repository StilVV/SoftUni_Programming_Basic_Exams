egg_size = input()
egg_color = input()
number_of_batch = int(input())

price = 0

if egg_size == "Large":
    if egg_color == "Red":
        price = 16
    elif egg_color == "Green":
        price = 12
    elif egg_color == "Yellow":
        price = 9

elif egg_size == "Medium":
    if egg_color == "Red":
        price = 13
    elif egg_color == "Green":
        price = 9
    elif egg_color == "Yellow":
        price = 7

elif egg_size == "Small":
    if egg_color == "Red":
        price = 9
    elif egg_color == "Green":
        price = 8
    elif egg_color == "Yellow":
        price = 5

total = price * number_of_batch
cost = total * 0.35

print(f"{total - cost:.2f} leva.")
