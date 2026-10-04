from src.hand import Hand

class Player:
    def __init__(self, balance=100):
        self.balance = balance
        self.hand = Hand()

    @staticmethod    
    def choose_action():
        while True:
            action = input("Choose your action ['hit'/'stand']: ").strip().lower()
            if action == "hit" or action == "stand":
                return action
            
    def get_bet(self):
        while True:
            try:
                bet = int(input("Choose your bet: "))
                if bet > self.balance:
                    print("You are not that rich buddy!")
                    continue
                elif bet <= 0:
                    print("That doesn't work")
                    continue
                self.balance -= bet
                return bet
            except ValueError:
                print("Fill in an integer!")
            

class Dealer(Player):
    def __init__(self):
        super().__init__(balance=0)

    def choose_action(self):
        if self.hand.value < 17:
            return "hit"
        else:
            return "stand"