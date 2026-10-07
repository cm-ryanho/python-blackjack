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
        pass

    def is_bust(self) -> bool:
        pass

    def add_card(self) -> None:
        pass

    def reset(self) -> None:
        pass