import pytest
from src.card import BlackjackCard, RANKS, SUITS


class TestBlackjackCardInitialization:
    """Tests for valid and invalid card initialization."""

    @pytest.mark.parametrize("rank", RANKS)
    @pytest.mark.parametrize("suit", SUITS)
    def test_valid_card_creation(self, rank, suit):
        card = BlackjackCard(rank, suit)
        assert card.rank == rank
        assert card.suit == suit

    @pytest.mark.parametrize("invalid_rank", ["0", "1", "11", "JOKER", "a", 9])
    def test_invalid_rank_raises_value_error(self, invalid_rank):
        with pytest.raises(ValueError, match=f"The rank {invalid_rank} is invalid."):
            BlackjackCard(invalid_rank, "Spades")

    @pytest.mark.parametrize("invalid_suit", ["spades", "Hearts ", "Stars", ""])
    def test_invalid_suit_raises_value_error(self, invalid_suit):
        with pytest.raises(ValueError, match=f"The suit {invalid_suit} is invalid."):
            BlackjackCard("A", invalid_suit)


class TestBlackjackCardValues:
    """Tests for correct card values across number, face, and Ace cards."""

    @pytest.mark.parametrize("rank, expected_value", [
        ("2", 2),
        ("5", 5),
        ("9", 9),
        ("10", 10),
        ("J", 10),
        ("Q", 10),
        ("K", 10),
        ("A", 1),
    ])
    def test_card_values(self, rank, expected_value):
        card = BlackjackCard(rank, "Hearts")
        assert card.value == expected_value


class TestBlackjackCardStringAndRender:
    """Tests for string output and ASCII card line rendering."""

    @pytest.mark.parametrize("rank, suit, expected_str", [
        ("A", "Spades", "A♠"),
        ("10", "Hearts", "10♥"),
        ("K", "Clubs", "K♣"),
        ("5", "Diamonds", "5♦"),
    ])
    def test_str_representation(self, rank, suit, expected_str):
        card = BlackjackCard(rank, suit)
        assert str(card) == expected_str

    def test_render_lines_single_digit_rank(self):
        card = BlackjackCard("7", "Hearts")
        expected = [
            "┌───────┐",
            "│7      │",
            "│   ♥   │",
            "│      7│",
            "└───────┘",
        ]
        assert card.render_lines() == expected

    def test_render_lines_double_digit_rank(self):
        card = BlackjackCard("10", "Spades")
        expected = [
            "┌───────┐",
            "│10     │",
            "│   ♠   │",
            "│     10│",
            "└───────┘",
        ]
        assert card.render_lines() == expected


class TestBlackjackCardImmutability:
    """Tests ensuring properties are read-only."""

    def test_properties_are_read_only(self):
        card = BlackjackCard("A", "Spades")
        with pytest.raises(AttributeError):
            card.rank = "K"
        with pytest.raises(AttributeError):
            card.suit = "Hearts"
        with pytest.raises(AttributeError):
            card.value = 11