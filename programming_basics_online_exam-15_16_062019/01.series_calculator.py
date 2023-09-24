series_name = input()
seasons = int(input())
episodes = int(input())
duration = float(input())

commercials = duration * 0.20
duration_with_commercials = duration + commercials
special_episodes = seasons * 10

time_needed = duration_with_commercials * episodes * seasons + special_episodes

print(f"Total time needed to watch the {series_name} series is {int(time_needed)} minutes.")
