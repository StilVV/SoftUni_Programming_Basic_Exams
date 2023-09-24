from math import floor
record_in_seconds = float(input())
distance = float(input())
time_for_meter = float(input())

delay = floor(distance / 50) * 30
george_time = delay + (time_for_meter * distance)

if george_time < record_in_seconds:
    print(f"Yes! The new record is {george_time:.2f} seconds.")
else:
    print(f"No! He was {george_time - record_in_seconds:.2f} seconds slower.")
