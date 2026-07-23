pizza_names = ['four-cheese', 'canadian', 'pepperoni']

for pizza in pizza_names:
    print(f"I could really go for a {pizza.title()} pizza right about now.")

print("\nI'll eat nearly any type of pizza, so long as there's no pineapple!")

friend_pizzas = pizza_names[:]
pizza_names.append('sicilian')
friend_pizzas.append('seafood')

print("\nMy favorite pizzas are:")

for pizza in pizza_names:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza.title())