from src.card import Card

class Deck:
    """Represents a standard 52-card playing deck. Contains objects from the Card class"""
 
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self):
        """Initializes a standard 52-card deck"""
        self.cards = [Card(rank, suit) for suit in self.SUITS for rank in self.RANKS]

    def shuffle(self):
        """Shuffles the list of cards in the deck"""
        pass

    def deal(self):
        """Pops a card from the deck and returns it"""
        pass

    def __len__(self):
        """Returns the number of cards left in the deck"""
        pass

    def __str__(self):
        """Prints the deck in a readable format"""
        ...