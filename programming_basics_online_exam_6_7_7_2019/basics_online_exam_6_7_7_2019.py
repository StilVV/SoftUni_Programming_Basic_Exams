# import math
# number_of_people = int(input())
# entrance_price = float(input())
# sun_lounger_price = float(input())
# umbrella_price = float(input())
#
# sun_lounger = math.ceil(number_of_people * 0.75)
# umbrella = math.ceil(number_of_people * 0.50)
#
# final_price = (sun_lounger * sun_lounger_price) +\
#               (umbrella_price * umbrella) +\
#               (number_of_people * entrance_price)
# print(f"{final_price:.2f} lv.")

""" 02. Family Trip """
# budget = float(input())
# number_of_nights = int(input())
# price_for_night = float(input())
# add_expanses = int(input())
#
# add_expanses_persenteg = budget * add_expanses / 100
#
# if number_of_nights > 7:
#     price_for_night -= price_for_night * 0.05
#
# total = number_of_nights * price_for_night + add_expanses_persenteg
# if total <= budget:
#     print(f"Ivanovi will be left with {budget - total:.2f} leva after vacation.")
# else:
#     print(f"{total - budget:.2f} leva needed.")

""" 03. Coffee Machine """
# drink = input()
# sugar = input()
# number_of_drinks = int(input())
#
# price = 0
#
# if drink == "Espresso":
#     if sugar == "Without":
#         price = 0.90
#     elif sugar == "Normal":
#         price = 1
#     elif sugar == "Extra":
#         price = 1.20
#
# elif drink == "Cappuccino":
#     if sugar == "Without":
#         price = 1
#     elif sugar == "Normal":
#         price = 1.20
#     elif sugar == "Extra":
#         price = 1.60
#
# elif drink == "Tea":
#     if sugar == "Without":
#         price = 0.50
#     elif sugar == "Normal":
#         price = 0.60
#     elif sugar == "Extra":
#         price = 0.70
#
# total = price * number_of_drinks
#
# if sugar == "Without":
#     total -= total * 0.35
#
# if drink == "Espresso" and number_of_drinks >= 5:
#     total -= total * 0.25
#
# if total > 15:
#     total -= total * 0.20
#
# print(f"You bought {number_of_drinks} cups of {drink} for {total:.2f} lv.")

""" 03. Travel Agency """
# city = input()
# type_of_stay = input()
# vip = input()
# days = int(input())
#
# is_valid = 0
# price_per_night = 0
#
# if city == "Bansko" or city == "Borovets":
#     if type_of_stay == "noEquipment":
#         price_per_night = 80
#         if vip == "yes":
#             price_per_night -= price_per_night * 0.05
#     elif type_of_stay == "withEquipment":
#         price_per_night = 100
#         if vip == "yes":
#             price_per_night -= price_per_night * 0.10
#     else:
#         is_valid = 1
#
# elif city == "Varna" or city == "Burgas":
#     if type_of_stay == "noBreakfast":
#         price_per_night = 100
#         if vip == "yes":
#             price_per_night -= price_per_night * 0.07
#     elif type_of_stay == "withBreakfast":
#         price_per_night = 130
#         if vip == "yes":
#             price_per_night -= price_per_night * 0.12
#     else:
#         is_valid = 1
# else:
#     is_valid = 1
#
# total = days * price_per_night
#
# if days > 7:
#     days += 1
#
# if days < 1:
#     print("Days must be positive number!")
# elif is_valid == 1:
#     print("Invalid input!")
# else:
#     print(f"The price is {total:.2f}lv! Have a nice time!")

""" 04. Club """
# target = float(input())
# cocktail = ""
# number_of_drinks = 0
#
# club_income = 0
#
# while True:
#     cocktail = input()
#
#     if cocktail == "Party!":
#         print(f"We need {target - club_income:.2f} leva more.")
#         break
#
#     number_of_drinks = int(input())
#     price = len(cocktail)
#     order = price * number_of_drinks
#
#     if order % 2 != 0:
#         order -= order * 0.25
#
#     club_income += order
#
#     if target <= club_income:
#         print("Target acquired.")
#         break
#
# print(f"Club income - {club_income:.2f} leva.")

""" 04. Renovation """
# height = int(input())
# weight = int(input())
# door_windows = int(input())
#
# square = (height * weight) * 4
# total_square = square - (square * door_windows) / 100
#
# painted = 0
# while True:
#     user_input = input()
#     if user_input == "Tired!":
#         print(f"{total_square - painted:.0f} quadratic m left." )
#         break
#     else:
#         user_input = int(user_input)
#         painted += user_input
#
#         if painted > total_square:
#             print(f"All walls are painted and you have {painted - total_square:.0f} l paint left!")
#             break
#         elif painted == total_square:
#             print(f"All walls are painted! Great job, Pesho!")
#             break

""" 05. PC Game Shop """
# number_of_sold_games = int(input())
# hearthstone = 0
# fornite = 0
# overwatch = 0
# others = 0
#
# for i in range(0, number_of_sold_games):
#     game_name = input()
#     if game_name == "Hearthstone":
#         hearthstone += 1
#     elif game_name == "Fornite":
#         fornite += 1
#     elif game_name == "Overwatch":
#         overwatch += 1
#     else:
#         others += 1
#
# hearthstone_of_all = hearthstone / number_of_sold_games * 100
# fornite_of_all = fornite / number_of_sold_games * 100
# overwatch_of_all = overwatch / number_of_sold_games * 100
# others_of_all = others / number_of_sold_games * 100
#
# print(f"Hearthstone - {hearthstone_of_all:.2f}%")
# print(f"Fornite - {fornite_of_all:.2f}%")
# print(f"Overwatch - {overwatch_of_all:.2f}%")
# print(f"Others - {others_of_all:.2f}%")

"""" 05. Football Tournament """
# team_name = input()
# number_of_games = int(input())
#
# win = 0
# loses = 0
# draw = 0
# win_rate = 0
# points = 0
#
# if number_of_games == 0:
#     print(f"{team_name} hasn't played any games during this season.")
#
# else:
#     for i in range(0, number_of_games):
#         outcome_of_games = input()
#
#         if outcome_of_games == "W":
#             win += 1
#             points += 3
#         elif outcome_of_games == "D":
#             draw += 1
#             points += 1
#         elif outcome_of_games == "L":
#             loses += 1
#
#     win_rate = win / number_of_games * 100
#
#     print(f"{team_name} has won {points} points during this season.")
#     print("Total stats:")
#     print(f"## W: {win}")
#     print(f"## D: {draw}")
#     print(f"## L: {loses}")
#     print(f'Win rate: {win_rate:.2f}%')

""" 06. Name Game """
# import sys
#
# name = input()
#
# max_score = -sys.maxsize
# winner_name = ""
#
# while name != "Stop":
#     current_score = 0
#
#     for letter in name:
#         number = input()
#         if int(number) == ord(letter):
#             current_score += 10
#         else:
#             current_score += 2
#         if current_score >= max_score:
#             max_score = current_score
#             winner_name = name
#     name = input()
#
# print(f'The winner is {winner_name} with {max_score} points!')

""" 06. The Most Powerful Word """
import sys
word = input()
winner_points = -sys.maxsize
winner_word = ""

while word != "End of words":
    current_points = 0

    for letter in word:
        current_points += ord(letter)

    if word[0] == "a" or word[0] == "A":
        current_points *= len(word)
    elif word[0] == "e" or word[0] == "E":
        current_points *= len(word)
    elif word[0] == "i" or word[0] == "I":
        current_points *= len(word)
    elif word[0] == "o" or word[0] == "O":
        current_points *= len(word)
    elif word[0] == "u" or word[0] == "U":
        current_points *= len(word)
    elif word[0] == "y" or word[0] == "Y":
        current_points *= len(word)
    else:
        current_points /= len(word)

    if current_points >= winner_points:
        winner_points = current_points
        winner_word = word

    word = input()

print(f"The most powerful word is {winner_word} - {winner_points}")
