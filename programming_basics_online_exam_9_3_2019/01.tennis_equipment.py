import  math
tennis_rocket_price = float(input())
tennis_rockets = int(input())
sneakers = int(input())

sneakers_price = tennis_rocket_price / 6
equipment = (tennis_rockets * tennis_rocket_price) + (sneakers_price * sneakers)
others = equipment * 0.20
his_pay = (others + equipment) / 8
spomsors = (others + equipment) - his_pay

print(f"Price to be paid by Djokovic {math.floor(his_pay)}")
print(f"Price to be paid by sponsors {math.ceil(spomsors)}")
