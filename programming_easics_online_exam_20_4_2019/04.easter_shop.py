eggs = int(input())

sold_eggs = 0

while True:
    buy_fill = input()

    if buy_fill == "Close":
        print(f"Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break

    number_of_eggs = int(input())

    if buy_fill == "Fill":
        eggs += number_of_eggs

    elif buy_fill == "Buy":
        if number_of_eggs > eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs}.")
            break
        eggs -= number_of_eggs
        sold_eggs += number_of_eggs

