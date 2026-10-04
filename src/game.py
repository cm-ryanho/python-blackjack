from src.deck import Deck
from src.player import Player, Dealer

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(name = input("What's your name: "))
        self.dealer = Dealer()

    def play(self):
        while True:
            self.play_round()


    def play_round(self):
        bet = self.player.get_bet()

        self.player.hand.add_card(self.deck.deal())
        self.player.hand.render()


game = Game()

game.play_round()
