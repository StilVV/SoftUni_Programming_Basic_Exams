bitcoin = int(input())
yoan = float(input())
comission = float(input())

bitcoin_rate = 1168 * bitcoin
dollar = 1.76
euro = 1.95
yoan_rate = (0.15 * yoan) * dollar

all = (bitcoin_rate + yoan_rate) / euro
comission_all = all * comission / 100
print(f"{all - comission_all:.2f}")

