yearly_price = int(input())

shoes = yearly_price * 0.60
outfit = shoes * 0.80
basket_ball = outfit / 4
accessories = basket_ball / 5

total_price = shoes + outfit + basket_ball + accessories

print(f"{yearly_price + total_price:.2f}")
