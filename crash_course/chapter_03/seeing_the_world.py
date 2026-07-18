locations = ['miami', 'akihabara', 'yongsan', 'avalon', 'new orleans']

print("Locations I would like to visit:")
print(locations)

print("\nThose locations sorted alphabetically:")
print(sorted(locations))

print("\nAnd the original order:")
print(locations)

print("\nThose locations sorted reverse-alphabetically:")
print(sorted(locations, reverse=True))

print("\nAnd the original order:")
print(locations)

locations.reverse()

print("\nThose locations in reversed order:")
print(locations)

locations.reverse()

print("\nAnd back in the original order:")
print(locations)

locations.sort()

print("\nThose locations permanently stored alphabetically:")
print(locations)

locations.sort(reverse=True)

print("\nThose locations permanently stored reverse-alphabetically:")
print(locations)