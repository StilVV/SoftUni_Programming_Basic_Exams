"""01. Oscars ceremony"""
# hall_rent = int(input())
#
# statuettes = hall_rent * 0.70
# catering = statuettes * 0.85
# voiceover = catering / 2
# total = hall_rent + statuettes + catering + voiceover
#
# print(f"{total:.2f}")
######################################################################################################################
"""02. Godzilla vs. Kong"""
# budget = float(input())
# extras = int(input())
# cloths_price = float(input())
#
# decor = budget * 0.10
#
# if extras > 150:
#     cloths_price *= 0.90
#
# total = (extras * cloths_price) + decor
#
# if budget >= total:
#     print(f"Action!")
#     print(f"Wingard starts filming with {budget - total:.2f} leva left.")
# else:
#     print(f"Not enough money!")
#     print(f"Wingard needs {total - budget:.2f} leva more.")
#######################################################################################################################
"""03. Oscars week in cinema"""
# movie_name = input()
# type_of_hall = input()
# tickets = int(input())
#
# ticket_price = 0
#
# if movie_name == "A Star Is Born":
#     if type_of_hall == "normal":
#         ticket_price = 7.50
#     elif type_of_hall == "luxury":
#         ticket_price = 10.50
#     elif type_of_hall == "ultra luxury":
#         ticket_price = 13.50
#
# elif movie_name == "Bohemian Rhapsody":
#     if type_of_hall == "normal":
#         ticket_price = 7.35
#     elif type_of_hall == "luxury":
#         ticket_price = 9.45
#     elif type_of_hall == "ultra luxury":
#         ticket_price = 12.75
#
# elif movie_name == "Green Book":
#     if type_of_hall == "normal":
#         ticket_price = 8.15
#     elif type_of_hall == "luxury":
#         ticket_price = 10.25
#     elif type_of_hall == "ultra luxury":
#         ticket_price = 13.25
#
# elif movie_name == "The Favourite":
#     if type_of_hall == "normal":
#         ticket_price = 8.75
#     elif type_of_hall == "luxury":
#         ticket_price = 11.55
#     elif type_of_hall == "ultra luxury":
#         ticket_price = 13.95
#
# print(f"{movie_name} -> {tickets * ticket_price:.2f} lv.")
######################################################################################################################
"""04. Cinema Voucher"""
# voucher_price = int(input())
#
# movie_tickets = 0
# product_bought = 0
# price = 0
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     product = command
#
#     if len(product) > 8:
#         ticket_price = ord(product[0]) + ord(product[1])
#         if voucher_price >= ticket_price:
#             voucher_price -= ticket_price
#             movie_tickets += 1
#         else:
#             break
#     else:
#         product_price = ord(product[0])
#         if voucher_price >= product_price:
#             voucher_price -= product_price
#             product_bought += 1
#         else:
#             break
#
# print(movie_tickets)
# print(product_bought)
######################################################################################################################
"""05. Movie Ratings"""
# from sys import maxsize
# total_movies = int(input())
#
# all_ratings = 0
# highest_rating = -maxsize
# highest_rating_name = ""
# lowest_rating = maxsize
# lowest_rating_name = ""
#
# for movie in range(total_movies):
#     movie_name = input()
#     movie_rating = float(input())
#
#     if movie_rating > highest_rating:
#         highest_rating = movie_rating
#         highest_rating_name = movie_name
#
#     elif movie_rating < lowest_rating:
#         lowest_rating = movie_rating
#         lowest_rating_name = movie_name
#
#     all_ratings += movie_rating
#
# print(f"{highest_rating_name} is with highest rating: {highest_rating:.1f}")
# print(f"{lowest_rating_name} is with lowest rating: {lowest_rating:.1f}")
# print(f"Average rating: {all_ratings / total_movies:.1f}")
######################################################################################################################
"""06. Cinema Tickets"""
# movie_name = input()
#
# student_ticket = 0
# standard_ticket = 0
# kid_ticked = 0
#
# while movie_name != "Finish":
#     available_seats = int(input())
#     reserved_seats = 0
#
#     for seat in range(available_seats):
#         type_of_ticket = input()
#
#         if type_of_ticket == "End":
#             break
#
#         if available_seats <= reserved_seats:
#             break
#
#         elif type_of_ticket == "student":
#             student_ticket += 1
#         elif type_of_ticket == "standard":
#             standard_ticket += 1
#         elif type_of_ticket == "kid":
#             kid_ticked += 1
#
#         reserved_seats += 1
#
#     capacity = reserved_seats / available_seats * 100
#     print(f"{movie_name} - {capacity:.2f}% full.")
#
#     movie_name = input()
#
# total_tickets = standard_ticket + student_ticket + kid_ticked
#
# print(f"Total tickets: {total_tickets}")
# print(f"{(student_ticket / total_tickets) * 100:.2f}% student tickets.")
# print(f"{(standard_ticket / total_tickets) * 100:.2f}% standard tickets.")
# print(f"{(kid_ticked / total_tickets) * 100:.2f}% kids tickets.")
