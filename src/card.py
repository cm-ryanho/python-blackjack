class Card:
    """A single playing card from a standard 52-card deck.

    A card is immutable after creation: rank and suit are read-only.
    Blackjack value is exposed via the `value` property.

    Attributes:
        rank (str): The card's rank, one of "2"-"10", "J", "Q", "K", "A".
        suit (str): The card's suit, one of "Spades", "Hearts", "Diamonds", "Clubs".

    Example:
        >>> card = Card("K", "Hearts")
        >>> print(card)
        K♥
        >>> card.value
        10
    """

    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank: str, suit: str):
        """Creates a card

        Args:
            rank: Card's rank, must be in 'Card.RANKS'.
            suit: Card's suit, must be in 'Card.SUITS'.

        Raises:
            ValueError: If `rank` or `suit` is not valid.
        """
        self._rank = rank
        self._suit = suit

        if self._rank not in Card.RANKS:
            raise ValueError("Invalid Rank")
        if self._suit not in Card.SUITS:
            raise ValueError("Invalid Suit")
    
    def __str__(self):
        """Returns Card's rank and suit, example: K♠ """
        pass

    @property
    def rank(self) -> str:
        """Returns card's rank."""
        return self._rank
    
    @property
    def suit(self) -> str:
        """Returns card's suit."""
        return self._suit
    
    @property
    def value(self) -> int:
        """Returns value of card.

        "J", "Q", "K", return 10. "A" returns 11.
        "2-10" return "face value".

        """
        pass


            



