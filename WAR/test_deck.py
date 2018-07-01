import unittest
import random

from deck import Card, Deck
from war import War

RANKS = "23456789TJQKA"
SUITS = "SCDH"

class CardTests(unittest.TestCase):
    def test_representations(self):
        """Testing the various input representations for cards."""
        c1 = Card(2)
        c2 = Card("2D")
        c3 = Card(("2", "D"))
        c4 = Card("5H")

        self.assertEqual(c1, c2)
        self.assertEqual(c2, c3)
        self.assertNotEqual(c1, c4)

    def test_suit_and_rank(self):
        rank = RANKS[random.randint(0, len(RANKS) - 1)]
        suit = SUITS[random.randint(0, len(SUITS) - 1)]

        c1 = Card(rank+suit)
        c2 = Card((rank, suit))
        self.assertEqual(rank, c1.card_rank)
        self.assertEqual(rank, c2.card_rank)
        self.assertEqual(suit, c1.card_suit)
        self.assertEqual(suit, c2.card_suit)
        self.assertEqual(c1.card_value, c2.card_value)


#class WarTests(unittest.TestCase):
#    def test_basic(self):
#        war = War()


if __name__ == "__main__":
    unittest.main(verbosity=1)
