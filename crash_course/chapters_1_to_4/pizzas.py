pizzas = ['4 queijos', 'atum com mussarela', 'frango com catupiry', 'gostosona', 'marguerita', 'roma', 'bacon']
for pizza in pizzas:
    print('I like {} pizza!'.format(pizza))
like = """ I fucking love pizza, whether it has
cheese, or champignon, pizza is fucking great
PRAISE THE PIZZAS"""
print(like)

print('the first three items in the list are ' + str(pizzas[:3]))
middle_left = len(pizzas)//2 - 1

middle_right = middle_left + 3
print('three items from the middle of the list are: ' + str(pizzas[middle_left:middle_right]))

last_3 = len(pizzas) - 3

print('The last three items are: ' + str(pizzas[last_3:]))

friend_pizzas = pizzas[:]
pizzas.append('escarola')
print('my fav pizzas are: ')
for pizza in pizzas:
    print(pizza)
print('my friend\'s fav pizzas are: ')
for pizza in friend_pizzas:
    print(pizza)


animals = ['cat', 'dog', 'rabbit']
for animal in animals:
    print(f'a {animal} would make a great pet')
print('those animals are mammals!')
