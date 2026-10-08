from src.participant import Player, Dealer
from src.deck import Deck
from typing import Literal

ActionType = Literal["hit", "stand"]

class BlackjackGame:
    def __init__(self, player: Player, dealer: Dealer, deck: Deck):
        self._player = player
        self._dealer = dealer
        self._deck = deck

    def reset_deck(self) -> None:
        self._deck.reset()

    def deal_cards(self) -> None:
        p1 = self._deck.deal()
        p2 = self._deck.deal()

        self._player.add_card(p1)
        self._player.add_card(p2)

        d1 = self._deck.deal()

        self._dealer.add_card(d1)

    def get_dealer_action(self) -> ActionType:
        if self._dealer.should_stand():
            return "stand"
        else:
            return "hit"

    def dealer_hit(self) -> None:
        card = self._deck.deal()
        self._dealer.add_card(card)

    def player_hit(self) -> None:
        card = self._deck.deal()
        self._player.add_card(card)

    def player_is_finished(self, action: ActionType) -> bool:
        if action == "stand":
            return True
        if self._player.is_bust():
            return True
        if self._player.is_blackjack():
            return True
        else:
            return False

    
    def resolve_round(self) -> None:
        if self._player.is_bust():
            self._player.lose_bet()
        elif self._dealer.is_bust():
            self._player.collect_winnings()
        elif self._player.is_blackjack() and not self._dealer.is_blackjack():
            self._player.collect_winnings()
        elif self._dealer.is_blackjack() and not self._player.is_blackjack():
            self._player.lose_bet()
        elif self._player.hand_value > self._dealer.hand_value:
            self._player.collect_winnings()
        elif self._player.hand_value < self._dealer.hand_value:
            self._player.lose_bet()
        else:
            self._player.push()



