from src.game import BlackjackGame
from src.participant import Player, Dealer
from src.hand import Hand
from src.deck import Deck
from typing import Literal
import time

ActionType = Literal["hit", "stand"]


def main():
    game = initialize_game()
    game.player_deposit(100)

    while True:
        balance = game.get_player_balance()  

        game.reset_round()
        print("A NEW ROUND HAS STARTED!!!")

        time.sleep(1)
        # Prints the remaining balance and prompts for a bet
        player_bet = get_bet(balance)
        
        game.place_bet(player_bet)

        game.deal_cards()

        time.sleep(1)
        display_cards(game)

        # Game loop
        # Player loop
        if game.player_is_blackjack():
            game.resolve_round()
            print("BLACKJACK")
            
            time.sleep(1)
            new_balance = game.get_player_balance()
            print(f"You won {new_balance - balance} euros!")

            # Ask for playing again
            if not play_again():
                print(f"Thanks for playing, your remaining balance: {game.get_player_balance()}")
                break
            continue
        else:
            player_action_loop(game)

        if not game.player_is_bust():
            # Dealer action loop
            time.sleep(1)
            print("Dealer's turn")
            dealer_action_loop(game)
            game.resolve_round()

        new_balance = game.get_player_balance()
        if new_balance > balance:
            time.sleep(1)
            print(f"You won {new_balance - balance} euros!")
        elif new_balance < balance:
            time.sleep(1)
            print(f"You just gave {balance - new_balance} to the house.")
        else:
            time.sleep(1)
            print("Push, you get your bet back.")

        # At the end if the player is broke, break.
        if new_balance <= 0:
            time.sleep(1)
            print(f"Gambling is bad.")
            break

        # Continue playing?
        if not play_again():
            print(f"Thanks for playing, your remaining balance: {game.get_player_balance()}")
            break

def play_again() -> bool:
    while True:
        play_again = input("do you want to play another round? [y/n]: ").strip().lower()
        if play_again == "y":
            return True
        elif play_again == "n":
            return False
                    
def get_bet(balance: int) -> int:
    while True:
        try:
            print(f"Your balance is: {balance}")
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
            time.sleep(1)
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
        time.sleep(1)
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