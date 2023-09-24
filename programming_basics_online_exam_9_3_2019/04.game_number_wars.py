first_player_name = input()
second_player_name = input()

player_one_points = 0
player_two_points = 0
winner_name = ""
winner_points = 0

while True:
    fist_number = input()
    if fist_number == "End of game":
        print(f"{first_player_name} has {player_one_points} points")
        print(f"{second_player_name} has {player_two_points} points")
        break

    fist_number = int(fist_number)
    second_number = int(input())

    if fist_number > second_number:
        player_one_points += (fist_number - second_number)
    elif fist_number < second_number:
        player_two_points += second_number - fist_number
    else:
        fist_number = int(input())
        second_number = int(input())
        if fist_number > second_number:
            winner_points = player_one_points
            winner_name = first_player_name
        elif fist_number < second_number:
            winner_name = second_player_name
            winner_points = player_two_points

        print("Number wars!")
        print(f"{winner_name} is winner with {winner_points} points")
        break
