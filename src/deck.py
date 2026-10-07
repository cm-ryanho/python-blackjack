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
        if len(self) == 0:
            raise ValueError("There are no cards to deal.")
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        pass