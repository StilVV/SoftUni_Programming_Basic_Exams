import math, sys
number_of_easter_cake = int(input())

max_sugar = -sys.maxsize
max_flour = - sys.maxsize
sugar_used = 0
flour_used = 0

for easter_cake in range(number_of_easter_cake):
    sugar = int(input())
    flour = int(input())

    sugar_used += sugar
    flour_used += flour

    if sugar > max_sugar:
        max_sugar = sugar

    if flour > max_flour:
        max_flour = flour

sugar_pack = math.ceil(sugar_used / 950)
flour_pack = math.ceil(flour_used / 750)

print(f"Sugar: {sugar_pack}")
print(f"Flour: {flour_pack}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
