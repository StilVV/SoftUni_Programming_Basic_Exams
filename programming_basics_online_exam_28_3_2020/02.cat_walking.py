minutes_walk = int(input())
number_of_walks = int(input())
calories = int(input())

calories_per_minutes = (minutes_walk * 5) * number_of_walks

if calories_per_minutes >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_per_minutes}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_per_minutes}.")
    