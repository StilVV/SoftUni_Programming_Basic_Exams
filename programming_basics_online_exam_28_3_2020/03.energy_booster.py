fruit = input()
set_size = input()
number_of_sets = int(input())

price = 0

if set_size == "small":
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.10
    elif fruit == "Raspberry":
        price = 20

    price *= 2

elif set_size == "big":
    if fruit == "Watermelon":
        price = 28.70
    elif fruit == "Mango":
        price = 19.60
    elif fruit == "Pineapple":
        price = 24.80
    elif fruit == "Raspberry":
        price = 15.20

    price *= 5

set_price = number_of_sets * price

if 400 <= set_price <= 1000:
    set_price *= 0.85
elif set_price > 1000:
    set_price *= 0.50

print(f"{set_price:.2f} lv.")
