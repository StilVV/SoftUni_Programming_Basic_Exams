actor_name = input()
academy_points = float(input())
number_of_evaluators = int(input())

for jury in range(0, number_of_evaluators):
    name_of_judge = input()
    point_of_judge = float(input())

    given_points = (len(name_of_judge) / 2) * point_of_judge

    academy_points += given_points

    if academy_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break

if academy_points < 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!")
