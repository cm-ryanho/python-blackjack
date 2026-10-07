SUIT_MAP = {"Hearts": "♥", "Spades": "♠", "Clubs": "♣", "Diamonds": "♦"}
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        self.__rank = rank


    @property
    def suit(self):
        return self.__suit

    @self.setter
    def suit(self, suit):
        self.__suit = suit