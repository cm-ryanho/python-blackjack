from src.game import BlackjackGame
from src.participant import Player, Dealer
from src.hand import Hand
from src.deck import Deck
from typing import Literal

ActionType = Literal["hit", "stand"]


def main():
    game = initialize_game()
    game.player_deposit(100)


    while True:
        balance = game.get_player_balance()
        if balance <= 0:
            print("You are not that rich buddy")
            break
        

        game.reset_round()
        player_bet = get_bet(balance)
        
        game.place_bet(player_bet)



        game.deal_cards()

        display_cards(game)

        # game loop
        # player loop
        if game.player_is_blackjack():
            game.resolve_round()
            print("BLACKJACK")
            continue
        else:
            player_action_loop(game)

            if not game.player_is_bust():
        # dealer action loop
                dealer_action_loop(game)
                game.resolve_round()

        # continue playing?
        play_again = input("do you want to play another round? [y/n]: ").strip().lower()
        if not play_again == "y":
            print(f"Thanks for playing, your remaining balance: {game.get_player_balance}")
            break
    
def get_bet(balance: int) -> int:
    while True:
        try:
            print(f"Balance is {balance}")
            bet = int(input(f"What is your bet: "))
            if bet > balance:
                print("Your not that rich buddy.")
                continue
            if bet <= 0:
                print("No")
                continue
            return bet
        except ValueError:
            continue


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
        
            elif game.player_is_finished(player_action):
                return
def dealer_action_loop(game: BlackjackGame):
    print("Dealers turn")
    while game.get_dealer_action() == "hit":
        print("Dealer gets ")
        game.dealer_hit()
        display_cards(game)
    

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