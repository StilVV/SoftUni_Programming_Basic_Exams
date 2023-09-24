guests = int(input())
price_for_one = float(input())
budget = float(input())

cake = budget * 0.10

if 10 <= guests <= 15:
    price_for_one *= 0.85
elif guests > 20:
    price_for_one *= 0.75
elif 15 < guests <= 20:
    price_for_one *= 0.80

total = (price_for_one * guests) + cake

if total <= budget:
    print(f"It is party time! {budget - total:.2f} leva left.")
else:
    print(f"No party! {total - budget:.2f} leva needed.")
