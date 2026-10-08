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
        print("Start of a new round in 3... 2.... 1.... start!")
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
                print("Dealer's turn")
                dealer_action_loop(game)
                game.resolve_round()

        new_balance = game.get_player_balance()
        if new_balance > balance:
            print(f"You won {new_balance - balance} euro!")
        elif new_balance < balance:
            print(f"You lost {balance - new_balance} euro.")
        else:
            print("Push, you get your bet back.")

        # continue playing?
        play_again = input("do you want to play another round? [y/n]: ").strip().lower()
        if not play_again == "y":
            print(f"Thanks for playing, your remaining balance: {game.get_player_balance()}")
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
    while game.get_dealer_action() == "hit":
        game.dealer_hit()
        display_cards(game)
    

def get_player_action() -> ActionType:
    while True:
        user_input = input("What do you want to do [hit/stand]: ").strip().lower()
        if user_input in ["hit", "stand"]:
            return user_input



def display_cards(game: BlackjackGame):
    print("Player: ")
    print(game.render_player_hand())
    print("Dealer: ")
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