southern_states = [
    'texas',
    'florida',
    'georgia',
    'north Carolina',
    'virginia',
    'tennessee',
    'maryland',
    'south carolina',
    'alabama',
    'louisiana',
    'kentucky',
    'oklahoma',
    'arkansas',
    'mississippi',
    'west virginia',
    'delaware'
]

print("The Southern states of the U.S. are:")
print(southern_states)

print(f"\nThe Southern state with the largest population is {southern_states[0].title()}.")
print(f"The Southern state with the smallest population is {southern_states[-1].title()}.")

# Fix that errant capitalization
southern_states[3] = "north carolina"

southern_states.append("hawaii")
southern_states.insert(7, "idaho")

print("\nWait, the list suddenly looks faulty:")
print(southern_states)

del southern_states[17]
southern_states.pop(7)

print("\nThere, now it looks back to normal:")
print(southern_states)

is_it_even_a_real_state = "tennessee"
southern_states.remove(is_it_even_a_real_state)

print("\nOops, temporarily dropped a state:")
print(southern_states)

print(f"\nSorry, {is_it_even_a_real_state.title()}!")
southern_states.insert(5, is_it_even_a_real_state)

print("\nOur list temporarily sorted alphabetically:")
print(sorted(southern_states))

print("\nOur list temporarily sorted reverse-alphabetically:")
print(sorted(southern_states, reverse=True))

southern_states.reverse()

print("\nOur list sorted in reverse order:")
print(southern_states)

southern_states.sort()

print("\nOur list permanently stored alphabetically:")
print(southern_states)

southern_states.sort(reverse=True)

print("\nOur list permanently stored reverse-alphabetically:")
print(southern_states)

print(f"\nNo matter how they are sorted, there are {len(southern_states)} states in the South.")