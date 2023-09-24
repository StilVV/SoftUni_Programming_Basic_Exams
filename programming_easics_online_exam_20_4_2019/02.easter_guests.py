from math import ceil
guests = int(input())
budget = float(input())

eggs_price = 0.45
easter_bread_price = 4
easter_bread = ceil(guests / 3)
eggs = guests * 2

total = (eggs * eggs_price) + (easter_bread_price * easter_bread)

if budget >= total:
    print(f"Lyubo bought {easter_bread} Easter bread and {eggs} eggs.")
    print(f"He has {budget - total:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total - budget:.2f} lv. more.")
