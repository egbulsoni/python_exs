# ex 4.10

# >>> if x == 5
# SyntaxError: invalid syntax

# The error occurs because of lack of semi-colon
from typing import List

x = 5
if x == 5:
    print("funcionou")

# >>> print 'hello'
# SyntaxError: invalid syntax

# Print is a function, and should include parenthesis as such:
print('hello')

# >>> lst = [4;5;6]
# SyntaxError: invalid syntax
# The error occurs because python's syntax for separating values in a list uses simple commas
lst = [4, 5, 6]

# >>> for i in range(10):
# print(i)
# SyntaxError: expected an indented block
# Problem here is, print should be indented in order to be recognized as a nested expression
# python can infer this for us because of the usage of a variable outside the expected scope

for i in range(10):
    print(i)


# ex 4.8

def words_only(filename):
    'returns the number of words in file filename'
    infile = open(filename, 'r')
    content = infile.read()  # read the file into a string
    infile.close()
    word_list = content.translate({ord('!'): None, ord(','): None, ord('.'): None, ord(':'): None,
                                   ord(';'): None, ord('?'): None})

    return word_list.split(' ')  # split file into list of words


print(words_only('example.txt'))


def my_grep(filename, word):
    infile = open(filename, 'r')
    content = infile.read()  # read the file into a string
    infile.close()
    counter = 0
    content = content.split('\n')
    wanted = []
    for line in content:
        if word in line:
            counter += 1
            wanted.append(line)

    print('{} lines contains {} string'.format(counter, word))
    for line in wanted:
        print(line)


my_grep('example.txt', 'the')
my_grep('example.txt', 'everyone')
my_grep('example.txt', 'for')
