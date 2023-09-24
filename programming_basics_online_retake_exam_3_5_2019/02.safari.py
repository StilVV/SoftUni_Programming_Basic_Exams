budget = float(input())
fuel = float(input())
day = input()

fuel_price = fuel * 2.10
tour_guide = 100

price = fuel_price + tour_guide

if day == "Saturday":
    price -= price * 0.10
elif day == "Sunday":
    price -= price * 0.20

if budget >= price:
    print(f"Safari time! Money left: {budget - price:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {price - budget:.2f} lv.")
