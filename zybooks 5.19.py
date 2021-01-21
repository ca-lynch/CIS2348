# Cody Lynch
# 1954220

# Outputs available services and prices
print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12')
print()
# Gets desired services from user
service1 = input('Select first service:\n')
service2 = input('Select second service:\n')
# Matches services with prices
oil_change = int(35)
tire_rot = int(19)
car_wash = int(7)
car_wax = int(12)
# Builds and outputs an itemized service invoice
print('\nDavy\'s auto shop invoice\n')
if service1 == 'Oil change':
    service1 = oil_change
    print('{} ${}'.format('Service 1: Oil change,', oil_change))
elif service1 == 'Tire rotation':
    service1 = tire_rot
    print('{} ${}'.format('Service 1: Tire rotation,', tire_rot))
elif service1 == 'Car wash':
    service1 = car_wash
    print('{} ${}'.format('Service 1: Car wash,', car_wash))
elif service1 == 'Car wax':
    service1 = car_wax
    print('{} ${}'.format('Service 1: Car wax,', car_wax))
elif service1 == '-':
    service1 = 0
    print('Service 1: No service')
else:
    print('Error: Requested service is not recognized')
if service2 == 'Oil change':
    service2 = oil_change
    print('{} ${}'.format('Service 2: Oil change,', oil_change))
elif service2 == 'Tire rotation':
    service2 = tire_rot
    print('{} ${}'.format('Service 2: Tire rotation', tire_rot))
elif service2 == 'Car wash':
    service2 = car_wash
    print('{} ${}'.format('Service 2: Car wash,', car_wash))
elif service2 == 'Car wax':
    service2 = car_wax
    print('{} ${}'.format('Service 2: Car wax,', car_wax))
elif service2 == '-':
    service2 = 0
    print('Service 2: No service')
else:
    print('Error: Requested service is not recognized')
print()
# Calculates and outputs total price of services
total = service1 + service2
print('{} ${}'.format('Total:', total))
