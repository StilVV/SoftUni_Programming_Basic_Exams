days = int(input())

total_win = 0
total_lost = 0
total_money = 0

for day in range(days):
    win = 0
    lost = 0
    money = 0

    while True:
        sport = input()

        if sport == "Finish":
            break

        win_lost = input()

        if win_lost == "win":
            win += 1
            money += 20
        elif win_lost == "lose":
            lost += 1

    if win > lost:
        money *= 1.10

    total_win += win
    total_lost += lost
    total_money += money

if total_win > total_lost:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
