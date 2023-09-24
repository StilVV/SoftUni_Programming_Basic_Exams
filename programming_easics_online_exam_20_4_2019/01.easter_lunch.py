kozunaci = int(input()) * 3.20
eggs_kora = int(input())
cookies = int(input()) * 5.40

eggs_kora_price = eggs_kora * 4.35
eggs_paint = ((eggs_kora * 12) * 0.15)

total = eggs_paint + cookies + kozunaci + eggs_kora_price

print(f"{total:.2f}")
