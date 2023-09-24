time_for_shoot = int(input())
number_of_scenes = int(input())
time_for_scene = int(input())

preparation = (time_for_shoot * 0.15)
total_time_needed = number_of_scenes * time_for_scene + preparation

if time_for_shoot >= total_time_needed:
    print(f"You managed to finish the movie on time! You have {time_for_shoot - total_time_needed:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {total_time_needed - time_for_shoot:.0f} minutes.")
