buffet = (
    'lasagna',
    'fried chicken',
    'mashed potatoes',
    'breadsticks',
    'sundaes'
)

print("Today's menu includes:")

for food in buffet:
    print(food)

# Attempting to alter a tuple returns an error
# buffet[3] = "Texas toast"

buffet = ('lasagna', 'fried chicken', 'sweet corn', 'Texas toast', 'sundaes')

print("\nThe revised menu includes:")

for food in buffet:
    print(food)