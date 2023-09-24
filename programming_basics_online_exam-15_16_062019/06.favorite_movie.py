movie_name = input()

win_points = 0
win_movie = ""
count = 0

while movie_name != "STOP":
    count += 1
    points = 0
    for letter in range(0, len(movie_name)):
        points += ord(movie_name[letter])

        if 90 >= ord(movie_name[letter]) >= 65:
            points -= len(movie_name)
        elif 122 >= ord(movie_name[letter]) >= 97:
            points -= len(movie_name) * 2

    if points >= win_points:
        win_movie = movie_name
        win_points = points

    if count >= 7:
        print("The limit is reached.")
        break
    movie_name = input()

print(f"The best movie for you is {win_movie} with {win_points} ASCII sum.")