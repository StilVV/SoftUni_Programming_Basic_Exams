player_name = input()

points = 301
nok_throws = 0
ok_throws = 0

while True:
    tmp_points = 0
    sector = input()
    if sector == "Retire":
        print(f"{player_name} retired after {nok_throws} unsuccessful shots.")
        break
        
    throw_points = int(input())

    if sector == "Single":
        tmp_points = throw_points
    elif sector == "Double":
        tmp_points = throw_points * 2
    elif sector == "Triple":
        tmp_points = throw_points * 3

    if tmp_points <= points:
        ok_throws += 1
        points -= tmp_points
    else:
        nok_throws += 1

    if points == 0:
        print(f"{player_name} won the leg with {ok_throws} shots.")
        break
