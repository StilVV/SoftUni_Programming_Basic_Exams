minutes_needed = int(input()) * 60
seconds_needed = int(input())
distance = float(input())
seconds_for_100 = int(input())

time_needed = minutes_needed + seconds_needed
time_delly = (distance / 120) * 2.5
his_time = (distance / 100) * seconds_for_100 - time_delly

if his_time <= time_needed:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {his_time:.3f}.")
else:
    print(f"No, Marin failed! He was {his_time - time_needed:.3f} second slower.")
    