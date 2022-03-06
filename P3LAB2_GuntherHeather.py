desired_service = input('Enter desired auto service:')

print()

print('You entered:', desired_service)

if desired_service == 'Oil change': 
    print("Cost of oil change: $35")

elif desired_service == 'Tire rotation': 
    print("Cost of tire rotation: $19")
    
elif desired_service == 'Car wash': 
    print("Cost of car wash: $7")
    
else: 
    print("Error: Requested service is not recognized")