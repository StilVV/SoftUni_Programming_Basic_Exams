movie_name = input()
type_of_package = input()
number_of_tickets = int(input())

addons = 0

if movie_name == "John Wick":
    if type_of_package == "Drink":
        addons = 12
    elif type_of_package == "Popcorn":
        addons = 15
    else:
        addons = 19

elif movie_name == "Star Wars":
    if type_of_package == "Drink":
        addons = 18
    elif type_of_package == "Popcorn":
        addons = 25
    elif type_of_package == "Menu":
        addons = 30
    if number_of_tickets >= 4:
        addons -= addons * 0.30

elif movie_name == "Jumanji":
    if type_of_package == "Drink":
        addons = 9
    elif type_of_package == "Popcorn":
        addons = 11
    elif type_of_package == "Menu":
        addons = 14
    if number_of_tickets == 2:
        addons -= addons * 0.15

total_price = number_of_tickets * addons

print(f"Your bill is {total_price:.2f} leva.")


