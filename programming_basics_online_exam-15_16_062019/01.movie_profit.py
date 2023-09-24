movie_name = input()
days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
cinema_cut = int(input())

profit_before_cut = (days * number_of_tickets * ticket_price)
profit = profit_before_cut - (profit_before_cut * cinema_cut / 100)

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
