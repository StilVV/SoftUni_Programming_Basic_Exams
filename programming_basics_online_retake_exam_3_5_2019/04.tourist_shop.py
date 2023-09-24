budget = float(input())

total_price = 0
count = 0

while True:
    product_name = input()

    if product_name == "Stop":
        print(f"You bought {count} products for {total_price:.2f} leva.")
        break

    product_price = float(input())
    count += 1

    if count % 3 == 0:
        product_price -= product_price * 0.50

    total_price += product_price

    if total_price > budget:
        print("You don't have enough money!")
        print(f"You need {total_price - budget:.2f} leva!")
        break
