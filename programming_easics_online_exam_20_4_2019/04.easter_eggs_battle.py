eggs_first = int(input())
eggs_second = int(input())

while True:
    winner = input()

    if winner == "End":
        print(f"Player one has {eggs_first} eggs left.")
        print(f"Player two has {eggs_second} eggs left.")
        break

    elif winner == "one":
        eggs_second -= 1
    elif winner == "two":
        eggs_first -= 1

    if eggs_first == 0:
        print(f"Player one is out of eggs. Player two has {eggs_second} eggs left.")
        break
    elif eggs_second == 0:
        print(f"Player two is out of eggs. Player one has {eggs_first} eggs left.")
        break
