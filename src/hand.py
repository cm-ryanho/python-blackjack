from src.card import BlackjackCard

class Hand:
    def __init__(self):
        self._cards = []

    @property
    def value(self):
        total = 0
        aces = 0
        for card in self._cards:
            if card.rank == "A":
                aces += 1
                total += 11
            else:
                total += card.value

        while total > 21 and aces > 0:
            aces -= 1
            total -= 10
        return total

    def is_blackjack(self) -> bool:
        return (len(self) == 2 and self.value == 21)

    def is_bust(self) -> bool:
        return self.value > 21

    def add_card(self, card: BlackjackCard) -> None:
        self._cards.append(card)

    def reset(self) -> None:
        self._cards = []

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        cards = []
        for card in cards:
            cards.append(str(card))
        return str(cards)