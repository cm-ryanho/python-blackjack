from typing import Literal

SUIT_MAP = {"Hearts": "♥", "Spades": "♠", "Clubs": "♣", "Diamonds": "♦"}
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
SuitType = Literal["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
RankType = Literal["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class BlackjackCard:
    def __init__(self, rank: RankType, suit:SuitType):
        if rank not in RANKS:
            raise ValueError(f"The rank {rank} is invalid.")
        elif suit not in SUITS:
            raise ValueError(f"The suit {suit} is invalid.")
        
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return f"{self._rank}{SUIT_MAP[self._suit]}"

    @property
    def value(self) -> int:
        if self._rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return int(self._rank)
        elif self._rank in ["J", "Q", "K"]:
            return 10
        else:
            return 1

    @property
    def rank(self):
        return self._rank


    @property
    def suit(self):
        return self._suit

