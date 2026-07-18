cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse-sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

cars.reverse()

print("\nHere is the reversed list:")
print(cars)

cars.sort()

print("\nHere is the permanently sorted list:")
print(cars)

cars.sort(reverse=True)

print("\nHere is the permanently reverse-sorted list:")
print(cars)

print("\nThe length of the list is:")
print(len(cars))