from math import floor

tournaments = int(input())
starting_points = int(input())

final_points = 0 + starting_points
avr_points = 0
win_rate = 0

for player in range(tournaments):
    stage_of_tournament = input()

    if stage_of_tournament == "W":
        final_points += 2000
        win_rate += 1
    elif stage_of_tournament == "F":
        final_points += 1200
    elif stage_of_tournament == "SF":
        final_points += 720

avr_points = floor((final_points - starting_points) / tournaments)
win_rate = (win_rate / tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {avr_points}")
print(f"{win_rate:.2f}%")
