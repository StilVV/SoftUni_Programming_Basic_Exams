strawberries_price = float(input())
banana = float(input())
orange = float(input())
malini = float(input())
strawberries_kg = float(input())

malini_price = strawberries_price * 0.50
orange_price = malini_price - (malini_price * 0.40)
banana_price = malini_price - (malini_price * 0.80)

final_price = (malini_price * malini) + \
              (orange_price * orange) + \
              (banana_price * banana) + \
              (strawberries_price * strawberries_kg)

print(round(final_price, 2))
