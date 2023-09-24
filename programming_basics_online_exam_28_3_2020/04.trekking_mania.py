groups = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for group in range(groups):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group

all_people = musala + monblan + k2 + kilimanjaro + everest
musala_rate = (musala / all_people) * 100
monblan_rate = (monblan / all_people) * 100
kilimanjaro_rate = (kilimanjaro / all_people) * 100
k2_rate = (k2 / all_people) * 100
everest_rate = (everest / all_people) * 100

print(f"{musala_rate:.2f}%")
print(f"{monblan_rate:.2f}%")
print(f"{kilimanjaro_rate:.2f}%")
print(f"{k2_rate:.2f}%")
print(f"{everest_rate:.2f}%")
