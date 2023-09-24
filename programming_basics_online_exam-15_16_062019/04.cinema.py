capacity = int(input())

busy = 0
income = 0
price = 0

for seat in range(0, capacity):
    people_coming = input()

    if people_coming == "Movie time!":
        print(f"There are {capacity - busy} seats left in the cinema.")
        break
    else:
        people_coming = int(people_coming)
        busy += people_coming
        if busy > capacity:
            print("The cinema is full.")
            break
        price = people_coming * 5

        if people_coming % 3 == 0:
            price -= 5

        income += price

print(f"Cinema income - {income} lv.")
