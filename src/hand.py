class Hand:
    def __init__(self):
        self._cards = []

    @property
    def value(self):
        pass

    def is_blackjack(self) -> bool:
        pass

    def is_bust(self) -> bool:
        pass

    def add_card(self) -> None:
        pass

    def reset(self) -> None:
        pass