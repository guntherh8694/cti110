#Price List with totals
#2/25/2022
#CTI-110-P2HW1 - Total Purchases
#Heather Gunther


item_1 = float(input('Enter the price of item #1: '))
item_2 = float(input('Enter the price of item #2: '))
item_3 = float(input('Enter the price of item #3: '))
item_4 = float(input('Enter the price of item #4: '))
item_5 = float(input('Enter the price of item #5: '))

sub_total = item_1 +  item_2 + item_3 + item_4 + item_5

sales_tax = sub_total * 0.07

total = sub_total + sales_tax

print('-------Results-------')
print('Subtotal:', end=' ')
print(f'{sub_total:.2f}')

print('Sales tax:', end=' ')
print(f'{sales_tax:.2f}')

print('Total:', end=' ')
print(f'{total:.2f}')


#Create input statements for 5 different items, remembering to use the float data type.
#Create formula for sub_total
#Create formula for sales_tax
#Create formula for total
#Using format specification inside the replacement fields in the ‘Results’ section, determines how many places past the decimal the outputted number will print.  
