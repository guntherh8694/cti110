current_price = int(input())
last_months_price = int(input())

price_change = current_price - last_months_price

monthly_mortgage = (current_price * 0.051) / 12

print('This house is ', end='$')
print(current_price, end='. ')
print('The change is ', end='$')
print(price_change, 'since last month.')
print('The estimated monthly mortgage is ', end='$')

print(f'{monthly_mortgage:.2f}', end='')
print('.')
