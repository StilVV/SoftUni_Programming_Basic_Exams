flour_price = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs = int(input())
maya = int(input())

sugar_price = (flour_price * 0.75)
eggs_price = (flour_price * 1.10) * eggs
maya_price = (sugar_price * 0.20) * maya

total = (sugar_price * kg_sugar) + eggs_price + maya_price + (kg_flour * flour_price)

print(f"{total:.2f}")