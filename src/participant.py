from src.card import BlackjackCard
from src.hand import Hand

class Participant:
    def __init__(self, hand: Hand):
        self._hand = hand

    @property
    def hand_value(self) -> int:
        return self._hand.value

    def clear_hand(self) -> None:
        self._hand.reset()

    def add_card(self, card: BlackjackCard) -> None:
        self._hand.add_card(card)

    def is_blackjack(self) -> bool:
        return self._hand.is_blackjack()
    
    def is_bust(self) -> bool:
        return self._hand.is_bust()

class Player(Participant):
    def __init__(self, hand: Hand):
        super().__init__(hand)
        self._balance = 0
        self._bet = 0

    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, value: int) -> None:
        if value < 0:
            raise ValueError("You cannot deposit a negative value")
        self._balance += value
        
    def place_bet(self, bet:int) -> None:
        if bet <= 0:
            raise ValueError("The bet must be positive")
        if bet > self._balance:
            raise ValueError(f"The bet {bet} is larger than the balance {self._balance}")
        self._balance -= bet
        self._bet += bet

    def _clear_bet(self) -> None:
        self._bet = 0
        
    def lose_bet(self) -> None:
        self._clear_bet()

    def collect_winnings(self) -> None:
        if self.is_bust():
            raise ValueError("The hand is bust.")
        if self.is_blackjack():
            self._balance += int(self._bet *2.5)
        else:
            self._balance += int(self._bet *2)
        self._clear_bet()

    def push(self) -> None:
        self._balance += self._bet
        self._clear_bet()

    @property
    def bet(self) -> int:
        return self._bet

class Dealer(Participant):
    STAND_VALUE = 17

    def should_stand(self) -> bool:
        if self.hand_value >= self.STAND_VALUE:
            return True
        else:
            return False

        