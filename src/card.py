SUIT_MAP = {"Hearts": "♥", "Spades": "♠", "Clubs": "♣", "Diamonds": "♦"}
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank


    @property
    def suit(self):
        return self._suit

