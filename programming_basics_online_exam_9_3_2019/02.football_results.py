first_game = input().split(":")
second_game = input().split(":")
third_game = input().split(":")

win = 0
lost = 0
drawn = 0

if first_game[0] > first_game[1]:
    win += 1
elif first_game[0] == first_game[1]:
    drawn += 1
elif first_game[0] < first_game[1]:
    lost += 1

if second_game[0] > second_game[1]:
    win += 1
elif second_game[0] == second_game[1]:
    drawn += 1
elif second_game[0] < second_game[1]:
    lost += 1

if third_game[0] > third_game[1]:
    win += 1
elif third_game[0] == third_game[1]:
    drawn += 1
elif third_game[0] < third_game[1]:
    lost += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn} games.")
