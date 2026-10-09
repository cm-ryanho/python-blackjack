import pytest
from src.deck import Deck

class TestDeck:
    def setup_method(self, method):
        self.deck = Deck()

    def teardown_method(self, method):
        del self.deck

    def test_create_standard(self):
        pass

    def test_reset(self):
        pass

    def test_deal(self):
        pass

    def test_len(self):
        pass

    def test_shuffle(self):
        pass    