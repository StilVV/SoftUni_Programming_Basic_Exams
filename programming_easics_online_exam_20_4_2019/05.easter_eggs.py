number_of_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0

for i in range(number_of_eggs):
    paint = input()

    if paint == "red":
        red_eggs += 1
    elif paint == "orange":
        orange_eggs += 1
    elif paint == "blue":
        blue_eggs += 1
    elif paint == "green":
        green_eggs += 1

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")

if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
    print(f"Max eggs: {red_eggs} -> red")
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    print(f"Max eggs: {orange_eggs} -> orange")
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    print(f"Max eggs: {blue_eggs} -> blue")
else:
    print(f"Max eggs: {green_eggs} -> green")
