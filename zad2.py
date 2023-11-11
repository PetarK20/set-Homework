n = int(input())
parking = []

for i in range(n):
    action,car = input().split(',')
    if action == 'IN':
        parking.append(car.strip())
    elif action == 'OUT':
        parking.remove(car.strip())

if not len(parking):
    print("Parking is empty")
else:
    print(parking)
