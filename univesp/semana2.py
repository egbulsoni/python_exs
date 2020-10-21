class Point:
    # 'class that represents points in the plane'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, xcoord):
        # 'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        # 'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        # 'return a tuple with x and y coordinates of the point'
        return self.x, self.y

    def move(self, dx, dy):
        # 'change the x and y coordinates by dx and dy'
        self.x += dx
        self.y += dy

    def getx(self):
        return self.x


class Test:
    version = 1.02


class Rectangle:
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

    def set_size(self, width=0, length=0):
        self.width = width
        self.length = length

    def perimeter(self):
        return self.width * 2 + self.length * 2

    def area(self):
        return self.width * self.length


class Animal:
    # 'represents an animal'
    def __init__(self, animal='animal', sound='make sounds'):
        self.spec = animal
        self.lang = sound

    def set_species(self, species):
        # 'sets the animal species'
        self.spec = species

    def set_language(self, language):
        # 'sets the animal language'
        self.lang = language

    def speak(self):
        # 'prints a sentence by the animal'
        print('I am a {} and I {}.'.format(self.spec, self.lang))


from random import shuffle


class Card:
    # 'represents a playing card'
    def __eq__(self, other):
        return (self.get_rank() is other.get_rank()) and (self.get_suit() is other.get_suit())

    def __repr__(self):
        return '{0} of {1}'.format(str(self.get_rank()), str(self.get_suit()))

    def __init__(self, rank, suit):
        # 'initialize rank and suit of playing card'
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        # 'return rank'
        return self.rank

    def get_suit(self):
        # 'return suit'
        return self.suit


class Deck:
    # 'represents a deck of 52 cards'
    # ranks and suits are Deck class variables
    # ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    # suits is a set of 4 Unicode symbols representing the 4 suits
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __len__(self):
        len(self.deck)

    def __repr__(self):
        card_list = ''
        for card in self.deck:
            card_list += repr(card) + ' '
        return card_list

    def __eq__(self, other):
        return self.ranks == other.ranks

    def __init__(self, ranks={'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}):
        # 'initialize deck of 52 cards'
        self.ranks = ranks
        self.deck = []  # deck is initially empty
        for suit in Deck.suits:  # suits and ranks are Deck
            for rank in self.ranks:  # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank, suit))

    def deal_card(self):
        # 'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        # 'shuffle the deck'
        shuffle(self.deck)


deck = Deck(['1', '2', '3', '4'])
