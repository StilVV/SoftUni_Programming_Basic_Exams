numbers_for_division = int(input())
divisible_two = 0
divisible_tree = 0
divisible_four = 0
count = 0

for number in range(0, numbers_for_division):
    number_to_check = int(input())
    count += 1

    if number_to_check % 2 == 0:
        divisible_two += 1
    if number_to_check % 3 == 0:
        divisible_tree += 1
    if number_to_check % 4 == 0:
        divisible_four += 1

divisible_two = divisible_two / count * 100
divisible_tree = divisible_tree / count * 100
divisible_four = divisible_four / count * 100

print(f"{divisible_two:.2f}%")
print(f"{divisible_tree:.2f}%")
print(f"{divisible_four:.2f}%")
