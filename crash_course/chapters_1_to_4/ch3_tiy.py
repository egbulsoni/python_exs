persons = ['Nikola Tesla', 'Dad', 'Jordan Peterson']
print('------------last invitation----------')
print('{}, I invite you to my fantastic dinner!'.format(persons[0]))
print('{}, I invite you to my fantastic dinner!'.format(persons[1]))
print('{}, I invite you to my fantastic dinner!'.format(persons[2]))
print('Sorry, I ({}) couldn\'t attend your dinner'.format(persons[0]))
new_person = 'Braun'
persons[0] = new_person

print('------------last invitation----------')
print('{}, I invite you to my fantastic dinner!'.format(persons[0]))
print('{}, I invite you to my fantastic dinner!'.format(persons[1]))
print('{}, I invite you to my fantastic dinner!'.format(persons[2]))

persons.insert(0,'Ashe')
persons.insert(len(persons)//2, 'Blitzcrank')
persons.append('Twitch')

print('------------last invitation----------')
print('{}, I invite you to my fantastic dinner!'.format(persons[0]))
print('{}, I invite you to my fantastic dinner!'.format(persons[1]))
print('{}, I invite you to my fantastic dinner!'.format(persons[2]))
print('{}, I invite you to my fantastic dinner!'.format(persons[3]))
print('{}, I invite you to my fantastic dinner!'.format(persons[4]))
print('{}, I invite you to my fantastic dinner!'.format(persons[5]))

print('sorry everyone, I\'ve got only 2 seats!')
uninvited_1 = persons.pop()
uninvited_2 = persons.pop()
uninvited_3 = persons.pop()
uninvited_4 = persons.pop()
print('Hey {}, {}, {}, {}, sorry, you\'re not invited anymore!'.format(uninvited_1,uninvited_2,uninvited_3,uninvited_4))
print('Hey {} and {}, you\'re still invited'.format(persons[0],persons[1]))
del persons[1]
del persons[0]
print(persons)

