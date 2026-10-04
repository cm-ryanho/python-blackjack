from src.card import Card
import random

class Deck:
    """Represents a standard 52-card playing deck. Contains objects from the Card class"""
 
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self):
        """Initializes a standard 52-card deck"""
        self.reset()

    def shuffle(self):
        """Shuffles the list of cards in the deck"""
        random.shuffle(self.cards)

    def deal(self):
        """Pops a card from the deck and returns it.

        Returns the last card in the deck if the deck is not empty and None if empty
        """
        if self.cards:
            return self.cards.pop()
        return None

    def reset(self):
        """Completely resets the deck back to the 52-card standard deck and shuffles it.
        
        This works on the Deck object itself. It returns nothing.
        """
        self.cards = [Card(rank, suit) for suit in self.SUITS for rank in self.RANKS]
        self.shuffle()

    def __len__(self):
        """Returns the number of cards left in the deck"""
        return len(self.cards)

    def __str__(self):
        """Returns the deck in a readable format whenever set to str"""
        spades = []
        hearts = []
        clubs = []
        diamonds = []
        for card in self.cards:
            if card.suit == "Spades":
                spades.append(card.rank)
            elif card.suit == "Hearts":
                hearts.append(card.rank)
            elif card.suit == "Diamonds":
                diamonds.append(card.rank)
            else:
                clubs.append(card.rank)

        return f"""
♠: {" ".join(spades)}
♥: {" ".join(hearts)}
♦: {" ".join(diamonds)}
♣: {" ".join(clubs)}"""