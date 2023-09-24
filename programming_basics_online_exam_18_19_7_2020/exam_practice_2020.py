# import math
""" 01. Agency Profit """
# company_name = input()
# adult_tickets = int(input())
# kids_tickets = int(input())
# net_adult_price = float(input())
# service_price = float(input())
#
# kid_ticket_price = net_adult_price * 0.3 + service_price
# adult_tickets_price = net_adult_price + service_price
# total = kid_ticket_price * kids_tickets + adult_tickets_price * adult_tickets
# profit = total * 0.2
#
# print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")

"""" 02. Add Bags """
# overweight_price = float(input())
# weight = float(input())
# days = int(input())
# number_of_suitcases = int(input())
#
# suitcases_price = 0
#
# if weight < 10:
#     suitcases_price = overweight_price * 0.20
#     if days > 30:
#         suitcases_price += suitcases_price * 0.10
#     elif days < 7:
#         suitcases_price += suitcases_price * 0.40
#     else:
#         suitcases_price += suitcases_price * 0.15
#
# elif weight > 20:
#     suitcases_price = overweight_price
#     if days > 30:
#         suitcases_price += suitcases_price * 0.10
#     elif days < 7:
#         suitcases_price += suitcases_price * 0.40
#     else:
#         suitcases_price += suitcases_price * 0.15
#
# else:
#     suitcases_price = overweight_price * 0.50
#     if days > 30:
#         suitcases_price += suitcases_price * 0.10
#     elif days < 7:
#         suitcases_price += suitcases_price * 0.40
#     else:
#         suitcases_price += suitcases_price * 0.15
#
# print(f"The total price of bags is: {(suitcases_price * number_of_suitcases):.2f} lv.")

"""" 03. Aluminum Joinery """
# number_aluminum = int(input())
# type_aluminum = input()
# delivery = input()
#
# aluminum_price = 0
#
#
# if number_aluminum <= 10:
#     print("Invalid order")
# else:
#     if type_aluminum == "90X130":
#         aluminum_price = 110
#         if 30 <= number_aluminum <= 60:
#             aluminum_price -= aluminum_price * 0.05
#         elif number_aluminum > 60:
#             aluminum_price -= aluminum_price * 0.08
#
#     elif type_aluminum == "100X150":
#         aluminum_price = 140
#         if 40 <= number_aluminum <= 80:
#             aluminum_price -= aluminum_price * 0.06
#         elif aluminum_price > 80:
#             aluminum_price -= aluminum_price * 0.10
#
#     elif type_aluminum == "130X180":
#         aluminum_price = 190
#         if 20 <= number_aluminum <= 50:
#             aluminum_price -= aluminum_price * 0.07
#         elif number_aluminum > 50:
#             aluminum_price -= aluminum_price * 0.12
#
#     elif type_aluminum == "200X300":
#         aluminum_price = 250
#         if 25 >= number_aluminum <= 50:
#             aluminum_price -= aluminum_price * 0.09
#         elif number_aluminum > 50:
#             aluminum_price -= aluminum_price * 0.14
#
#     total = aluminum_price * number_aluminum
#
#     if delivery == "With delivery":
#         total += 60
#
#     if number_aluminum > 99:
#         total -= total * 0.04
#
#     print(f"{total:.2f} BGN")

"""" 04. Balls """
# numbers_of_balls = int(input())
# 
# total_points = 0
# red = 0
# orange = 0
# yellow = 0
# white = 0
# black = 0
# count = 0
# 
# while numbers_of_balls > 0:
#     numbers_of_balls -= 1
#     colors_of_balls = input()
# 
#     if colors_of_balls == "red":
#         red += 1
#         total_points += 5
#     elif colors_of_balls == "orange":
#         orange += 1
#         total_points += 10
#     elif colors_of_balls == "yellow":
#         yellow += 1
#         total_points += 15
#     elif colors_of_balls == "white":
#         white += 1
#         total_points += 20
#     elif colors_of_balls == "black":
#         black += 1
#         total_points /= 2
#     else:
#         count += 1
#         continue
# 
# print(f"Total points: {math.floor(total_points)}")
# print(f"Red balls: {red}")
# print(f"Orange balls: {orange}")
# print(f"Yellow balls: {yellow}")
# print(f"White balls: {white}")
# print(f"Other colors picked: {count}")
# print(f"Divides from black balls: {black}")

"""" 05. Best Player """
# best_player = ""
# best_score = 0
# hat_trick = 0
# player_name = ""
#
# while best_score <= 10:
#     player_name = input()
#     if player_name == "END":
#         break
#     number_of_goals = int(input())
#     if number_of_goals > best_score:
#         best_player = player_name
#         best_score = number_of_goals
#         if number_of_goals >= 3:
#             hat_trick = 1
#     if number_of_goals >= 10:
#         break
#
# print(f"{best_player} is the best player!")
#
# if hat_trick > 0:
#     print(f"He has scored {best_score} goals and made a hat-trick !!!")
# else:
#     print(f"He has scored {best_score} goals.")

""" 06. Barcode Generator """
"""START TRY"""
# upper_limit = int(input())
# down_limit = int(input())
#
# for a in range(upper_limit, down_limit):
#     for b in str(a):
#         if int(b) % 2 == 0:
#             break
#     else:
#         print(f"{a}", end=" ")
""""END TRY"""
num_1 = (input())
num_2 = (input())

num_1_digit_4 = int(num_1[3])
num_1_digit_3 = int(num_1[2])
num_1_digit_2 = int(num_1[1])
num_1_digit_1 = int(num_1[0])

num_2_digit_4 = int(num_2[3])
num_2_digit_3 = int(num_2[2])
num_2_digit_2 = int(num_2[1])
num_2_digit_1 = int(num_2[0])

for digit_1 in range(num_1_digit_1, num_2_digit_1 + 1):
    if digit_1 % 2 == 0:
        continue
    for digit_2 in range(num_1_digit_2, num_2_digit_2 + 1):
        if digit_2 % 2 == 0:
            continue
        for digit_3 in range(num_1_digit_3, num_2_digit_3 + 1):
            if digit_3 % 2 == 0:
                continue
            for digit_4 in range(num_1_digit_4, num_2_digit_4 + 1):
                if digit_4 % 2 == 0:
                    continue
                print(f"{digit_1}{digit_2}{digit_3}{digit_4} ", end="")
