from src.game import BlackjackGame
from src.participant import Player, Dealer
from src.hand import Hand
from src.deck import Deck

def main():
    game = initialize_game()

    game.deal_cards()

    game.rende


def initialize_game() -> BlackjackGame:
    player_hand = Hand()
    dealer_hand = Hand()

    player = Player(player_hand)
    dealer = Dealer(dealer_hand)

    deck = Deck()

    game = BlackjackGame(player, dealer, deck)

    return game


if __name__ == "__main__":
    main()