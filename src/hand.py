class Hand:
    """Represents a hand in Blackjack."""
    def __init__(self):
        """Initializes a card list."""
        self.cards = []
        
    @property
    def value(self):
        """Calculates the value of a hand and returns it."""
        value = 0
        aces = 0
        for card in self.cards:
            if card.rank == "A":
                aces += 1
            value += card.value

        while (value > 21 and aces > 0):
            value -= 10
            aces -= 1
        
        return value

    def add_card(self, card):
        """Adds 1 card to the hand."""
        self.cards.append(card)

    def is_bust(self):
        return self.value > 21

    def is_blackjack(self):
        return (len(self.cards) == 2 and self.value == 21)
            
    def render(self):
        """Prints the cards in the hand side by side."""
        columns = []
        for card in self.cards:
            suit = card.SUIT_MAP[card.suit]
            columns.append([
                "┌───────┐",
                f"│{card.rank:<7}│",
                "│       │",
                f"│{suit:^7}│",
                "│       │",
                f"│{card.rank:>7}│",
                "└───────┘",
            ])

        for row in zip(*columns):
            print("  ".join(row))

    def __len__(self):
        return len(self.cards)

        
        

        


        

        












