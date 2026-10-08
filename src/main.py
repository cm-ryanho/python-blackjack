from src.game import BlackjackGame
from src.participant import Player, Dealer
from src.hand import Hand
from src.deck import Deck
from typing import Literal

ActionType = Literal["hit", "stand"]


def main():
    game = initialize_game()

    game.deal_cards()

    display_cards(game)

    player_action_loop(game)

    
    


def player_action_loop(game: BlackjackGame):
    #player action loop
    while True:
        player_action = get_player_action()
        if player_action == "stand":
            return
        else:
            game.player_hit()
            display_cards(game)

            if game.player_is_bust():
                game.resolve_round()
                print("BUST")
                return
            
            elif game.player_is_blackjack():
                game.resolve_round()
                print("BLACKJACK")
                return

            elif game.player_is_finished(player_action):
                return

        

def get_player_action() -> ActionType:
    while True:
        user_input = input("What do you want to do [hit/stand]: ").strip().lower()
        if user_input in ["hit", "stand"]:
            return user_input



def display_cards(game: BlackjackGame):
    print(game.render_player_hand())
    print(game.render_dealer_hand())

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