clients = int(input())

total = 0

for client in range(clients):
    product_count = 0
    client_product_price = 0

    while True:
        product = input()

        if product == "Finish":
            break

        elif product == "basket":
            client_product_price += 1.50
            product_count += 1
        elif product == "wreath":
            client_product_price += 3.80
            product_count += 1
        elif product == "chocolate bunny":
            client_product_price += 7
            product_count += 1

    if product_count % 2 == 0:
        client_product_price *= 0.80

    total += client_product_price
    print(f"You purchased {product_count} items for {client_product_price:.2f} leva.")

print(f"Average bill per client is: {total / clients:.2f} leva.")
