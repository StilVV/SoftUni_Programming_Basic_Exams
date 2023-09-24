budget = float(input())
pay = 0

while True:
    actor_name = input()
    if actor_name == "ACTION":
        break

    if len(actor_name) > 15:
        budget -= budget * 0.20
    else:
        pay_actor = float(input())
        budget -= pay_actor

    if budget < 0:
        print(f"We need {pay - budget:.2f} leva for our actors.")
        break

if budget > 0:
    print(f"We are left with {budget:.2f} leva.")