def show_points(alien_color):
    if alien_color == 'green':
        print('you just earned 5 points!')
    elif alien_color == 'yellow':
        print('you just earned 10 points')
    elif alien_color == 'red':
        print('you just earned 15 points')
    else:
        print('enter a valid alien: green, red, yellow')
    return 0

def stage_of_life(age):
    if age < 2:
        print('baby')
    elif age < 4:
        print('toddler')
    elif age < 13:
        print('kid')
    elif age < 20:
        print('teenager')
    elif age < 65:
        print('adult')
    else:
        print('elder')

c = 'green'
d = 'yellow'
show_points(c)
show_points(d)

fruits = ['watermelon', 'avocado', 'passion fruit']

if 'banana' in fruits:
    print('let\'s make a banana split.')

if 'strawberry' in fruits:
    print('those are nice with condensed milk.')

if 'avocado' in fruits:
    print('in brazil, we\'d rather have those with sugar.')

if 'dragon fruit' in fruits:
    print('that\'s not so common in Brazil.')

if 'watermelon' in fruits:
    print('there are huge ammounts of water in those.')
