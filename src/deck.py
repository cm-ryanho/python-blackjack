from src.card import RANKS, SUITS, SUIT_MAP, BlackjackCard
import random

class Deck:
    def __init__(self):
        self._cards = self.create_standard()
        self._cards.shuffle()

    def create_standard(self) -> list[BlackjackCard]:
        cards = []
        for suit in SUITS:
            for rank in RANKS:
                cards.append(BlackjackCard(rank=rank, suit=suit))
        return cards

    def shuffle(self) -> None:
        self._cards.random.shuffle()

    def deal(self):
        pass

    def __str__(self):
        pass