duration_of_contract = input()
type_of_contract = input()
mobile_internet = input()
moths_for_par = int(input())

price_per_month = 0

if duration_of_contract == "one":
    if type_of_contract == "Small":
        price_per_month = 9.98
    elif type_of_contract == "Middle":
        price_per_month = 18.99
    elif type_of_contract == "Large":
        price_per_month = 25.98
    elif type_of_contract == "ExtraLarge":
        price_per_month = 35.99

elif duration_of_contract == "two":
    if type_of_contract == "Small":
        price_per_month = 8.58
    elif type_of_contract == "Middle":
        price_per_month = 17.09
    elif type_of_contract == "Large":
        price_per_month = 23.59
    elif type_of_contract == "ExtraLarge":
        price_per_month = 31.79

if mobile_internet == "yes":
    if price_per_month <= 10:
        price_per_month += 5.50
    elif price_per_month > 30:
        price_per_month += 3.85
    else:
        price_per_month += 4.35

final_price = (price_per_month * moths_for_par)

if duration_of_contract == "two":
    final_price -= final_price * 0.0375

print(f"{final_price:.2f} lv.")
