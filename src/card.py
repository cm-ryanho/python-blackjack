SUIT_MAP = {"Hearts": "♥", "Spades": "♠", "Clubs": "♣", "Diamonds": "♦"}
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Card:
    def __init__(self, rank:str, suit:str):
        if rank not in RANKS:
            raise ValueError(f"The rank {rank} is invalid.")
        elif suit not in SUITS:
            raise ValueError(f"The suit {suit} is invalid.")
        
        self._rank = rank
        self._suit = suit

    @property
    def value(self) -> int:
        if self.rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return int(self.rank)
        elif self.rank in ["J", "Q", "K"]:
            return 10
        else:
            return 1

    @property
    def rank(self):
        return self._rank


    @property
    def suit(self):
        return self._suit

