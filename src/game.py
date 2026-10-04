from src.deck import Deck
from src.player import Player, Dealer
import time
import sys

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(name = "j")
        self.dealer = Dealer()

    def play(self):
        while True:
            self.play_round()
            print(f"YOUR BALANCE: {self.player.balance}")
            choice = input("DO YOU WANT TO PLAY AGAIN [Y/N]: ")
            if choice == "N":
                break
            self.reset_game()
        print("THANK YOU FOR PLAYING")

    def reset_game(self):
        self.deck.reset()
        self.player.hand.clear()
        self.dealer.hand.clear()

    def play_round(self):
        bet = self.player.get_bet()

        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())

        if self.player.hand.is_blackjack():
            self.render_state()
            self.player.balance += int(2.5*bet)
            print("BLACKJACK!!!")
            return

        self.render_state()

        while self.player.hand.value <= 20:
            action = self.player.choose_action()
            time.sleep(1)
            if action == "hit":
                self.player.hand.add_card(self.deck.deal())
                self.render_state()
                if self.player.hand.value > 21:
                    print(f"BUST!!! YOU LOSE {bet} BUCKS")
                    return
                elif self.player.hand.value == 21:
                    self.player.balance += 2*bet
                    print("YOU WIN!!!")
                    return
            else:
                break

        while self.dealer.choose_action() == "hit":
            time.sleep(1)
            self.dealer.hand.add_card(self.deck.deal())
            self.render_state()

            if self.dealer.hand.value > 21:
                self.player.balance += 2*bet
                print("DEALER BUSTS!!! YOU WIN!!!")
                return

        # showdown
        if self.player.hand.value > self.dealer.hand.value:
            self.player.balance += 2*bet
            print("YOU WIN!!!")
            return
        elif self.player.hand.value == self.dealer.hand.value:
            self.player.balance += bet
            print("PUSH...")
            return
        else:
            print(f"YOU LOSE {bet} BUCKS!!")
            return
            
            
            

    def render_state(self):
        print("Dealer's cards: ")
        self.dealer.hand.render()
        print("Your cards:")
        self.player.hand.render()


game = Game()

game.play()
