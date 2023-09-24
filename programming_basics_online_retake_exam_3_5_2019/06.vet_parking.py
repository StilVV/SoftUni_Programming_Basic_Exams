number_of_days = int(input())
hours = int(input())

total_price = 0

for day in range(0, number_of_days):
    price = 0
    for hour in range(0, hours):
        if day % 2 == 0 and hour % 2 != 0:
            price += 1.25
        elif day % 2 != 0 and hour % 2 == 0:
            price += 2.50
        else:
            price += 1

    total_price += price
    print(f"Day: {day + 1} - {price:.2f} leva")

print(f"Total: {total_price:.2f} leva")
