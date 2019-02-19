Tax=0.13

meal_cost = float(input('Enter the cost of your meal:'))
tax_amount= meal_cost * 0.13
tip_amount= meal_cost * 0.18
grand_total= meal_cost + tax_amount + tip_amount
print(f'Meal:{meal_cost}')
print(f'Tax:{tax_amount}')
print(f'Tip:{tip_amount}')
print(f'Total:{grand_total}')
