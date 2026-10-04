class Card:
"""A single playing card from a standard 52-card deck.

    A card is immutable after creation: rank and suit are read-only.
    Blackjack value is exposed via the `value` property.

    Attributes:
        rank (str): The card's rank, one of "2"-"10", "J", "Q", "K", "A".
        suit (str): The card's suit, one of "Spades", "Hearts", "Diamonds", "Clubs".

    Example:
        >>> card = Card("K", "♥")
        >>> print(card)
        K♥
        >>> card.value
        10
    """

    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]





