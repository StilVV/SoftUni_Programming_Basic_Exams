budget = float(input())
place = input()
season = input()
days = int(input())

price = 0

if place == "Dubai":
    if season == "Winter":
        price = 45000
    elif season == "Summer":
        price = 40000

elif place == "Sofia":
    if season == "Winter":
        price = 17000
    elif season == "Summer":
        price = 12500

elif place == "London":
    if season == "Winter":
        price = 24000
    elif season == "Summer":
        price = 20250

total = days * price

if place == "Dubai":
    total -= total * 0.30
elif place == "Sofia":
    total += total * 0.25

if budget >= total:
    print(f"The budget for the movie is enough! We have {budget - total:.2f} leva left!")
else:
    print(f"The director needs {total - budget:.2f} leva more!")
