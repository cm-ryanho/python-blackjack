from src.card import BlackjackCard
from src.hand import Hand


class Player:
    def __init__(self, hand: Hand):
        self._hand = hand
        self._balance = 0
        self._bet = 0

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, balance: int) -> None:
        if balance < 0:
            raise ValueError("The balance must be positive")
        self._balance = balance

    def add_card(self, card: BlackjackCard) -> None:
        self._hand.add_card(card)

    def clear_hand(self) -> None:
        self._hand.reset()

    @property
    def bet(self) -> int:
        return self._bet
        
    @bet.setter
    def bet(self, bet: int) -> None:
        if bet <= 0:
            raise ValueError(f"{bet} is invalid")
        self._bet = bet