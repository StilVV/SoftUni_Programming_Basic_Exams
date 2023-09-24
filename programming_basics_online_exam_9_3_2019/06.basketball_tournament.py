all_games = 0
win_games = 0
lost_games = 0

while True:
    tournament_name = input()
    count = 0

    if tournament_name == "End of tournaments":
        break

    desi_team = 0
    enemy_team = 0

    tournament_games = int(input())
    all_games += tournament_games

    for match in range(tournament_games):
        count += 1
        desi_team = int(input())
        enemy_team = int(input())

        if desi_team > enemy_team:
            win_games += 1
            print(f"Game {count} of tournament {tournament_name}: win with {desi_team - enemy_team} points.")
        else:
            lost_games += 1
            print(f"Game {count} of tournament {tournament_name}: lost with {enemy_team - desi_team} points.")

win_rate = (win_games / all_games) * 100
lost_rate = (lost_games / all_games) * 100

print(f"{win_rate:.2f}% matches win")
print(f"{lost_rate:.2f}% matches lost")
