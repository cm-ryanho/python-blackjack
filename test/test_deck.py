import pytest
from src.deck import Deck
from src.card import SUITS, RANKS, BlackjackCard
import random

class TestDeck:
    def setup_method(self, method):
        self.deck = Deck()

    def teardown_method(self, method):
        del self.deck

    def test_create_standard(self):
        # Should return a list of BlackjackCards
        cards = self.deck.create_standard()

        assert len(cards) == 52
        assert len(cards) == len(SUITS) * len(RANKS)

        assert all(isinstance(card, BlackjackCard) for card in cards)

        # No duplicates, and every rank/suit combination is present
        combos = {(card.rank, card.suit) for card in cards}
        expected = {(rank, suit) for suit in SUITS for rank in RANKS}
        assert len(combos) == len(cards)
        assert combos == expected

        # Each suit has one card of every rank
        for suit in SUITS:
            ranks_in_suit = [card.rank for card in cards if card.suit == suit]
            assert sorted(ranks_in_suit) == sorted(RANKS)



    def test_create_standard_returns_new_list(self):
        first = self.deck.create_standard()
        second = self.deck.create_standard()
        assert first is not second

    def test_init_creates_full_deck(self):
        assert len(self.deck) == 52

    # --- deal ---

    def test_deal_returns_card(self):
        card = self.deck.deal()
        assert isinstance(card, BlackjackCard)

    def test_deal_reduces_length_by_one(self):
        self.deck.deal()
        assert len(self.deck) == 51

        self.deck.deal()
        assert len(self.deck) == 50



    def test_deal_from_empty_deck_raises(self):
        for _ in range(52):
            self.deck.deal()

        with pytest.raises(ValueError, match="There are no cards to deal."):
            self.deck.deal()

    # --- reset ---

    def test_reset_restores_full_deck(self):
        for _ in range(10):
            self.deck.deal()
        assert len(self.deck) == 42

        self.deck.reset()
        assert len(self.deck) == 52

    def test_reset_after_empty_allows_dealing_again(self):
        for _ in range(52):
            self.deck.deal()

        self.deck.reset()
        assert isinstance(self.deck.deal(), BlackjackCard)

    def test_reset_calls_shuffle(self, monkeypatch):
        calls = []
        monkeypatch.setattr(self.deck, "shuffle", lambda: calls.append(1))

        self.deck.reset()
        assert len(calls) == 1

    # --- shuffle ---

    def test_shuffle_changes_order(self):
        # Chance of an identical order is 1 in 52!, so this is safe to assert.
        # Seeding makes the result deterministic anyway.
        random.seed(42)
        before = [(c.rank, c.suit) for c in self.deck._cards]
        self.deck.shuffle()
        after = [(c.rank, c.suit) for c in self.deck._cards]

        assert before != after

    # --- dunder methods ---

    def test_len(self):
        assert len(self.deck) == 52
        self.deck.deal()
        assert len(self.deck) == 51

    def test_len_empty(self):
        for _ in range(52):
            self.deck.deal()
        assert len(self.deck) == 0

    def test_str(self):
        expected = str([str(card) for card in self.deck._cards])
        assert str(self.deck) == expected

    def test_str_empty_deck(self):
        for _ in range(52):
            self.deck.deal()
        assert str(self.deck) == "[]"