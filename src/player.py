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
        
    def place_bet(self, bet:int):
        if bet <= 0:
            raise ValueError("The bet must be positive")
        if bet > self._balance:
            raise ValueError(f"The bet {bet} is larger than the balance {self._balance}")
        self._balance -= bet
        self._bet += bet

    def add_card(self, card: BlackjackCard) -> None:
        self._hand.add_card(card)

    def clear_hand(self) -> None:
        self._hand.reset()

    @property
    def bet(self) -> int:
        return self._bet

    @property
    def hand_value(self) -> int:
        return self._hand.value