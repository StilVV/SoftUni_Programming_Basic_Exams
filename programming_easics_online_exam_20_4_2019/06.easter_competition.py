from sys import maxsize
number_of_easter_cake = int(input())

max_points = -maxsize
max_chef = ""

for easter_cake in range(number_of_easter_cake):
    chef_name = input()
    current_points = 0

    while True:
        rating = input()

        if rating != "Stop":
            rating = int(rating)
            current_points += rating
        else:
            print(f"{chef_name} has {current_points} points.")
            if current_points > max_points:
                max_points = current_points
                max_chef = chef_name
                print(f"{chef_name} is the new number 1!")
            break

print(f"{max_chef} won competition with {max_points} points!")
