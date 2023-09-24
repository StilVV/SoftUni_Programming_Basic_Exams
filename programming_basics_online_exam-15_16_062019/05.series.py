budget = float(input())
number_of_series = int(input())

for i in range(0, number_of_series):
    series_name = input()
    price_of_series = float(input())

    if series_name == "Thrones":
        price_of_series -= price_of_series * 0.50
    elif series_name == "Lucifer":
        price_of_series -= price_of_series * 0.40
    elif series_name == "Protector":
        price_of_series -= price_of_series * 0.30
    elif series_name == "TotalDrama":
        price_of_series -= price_of_series * 0.20
    elif series_name == "Area":
        price_of_series -= price_of_series * 0.10

    budget -= price_of_series

if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
