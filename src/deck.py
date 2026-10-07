from src.card import RANKS, SUITS, SUIT_MAP, BlackjackCard

class Deck:
    def __init__(self):
        self._cards = self.create_standard()

    def create_standard(self) -> list[BlackjackCard]:
        cards = []
        for suit in SUITS:
            for rank in RANKS:
                cards.append(BlackjackCard(rank=rank, suit=suit))
        return cards

    def shuffle(self):
        pass

    def deal(self):
        pass

    def __str__(self):
        pass