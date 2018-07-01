
from collections import deque

class Deck:
    """
    A Deck is a deque. The left of the deque is the bottom of the deck. The
    right of the deck is the top. So pop() is like deal().
    """
    def __init__(self):
        self.cards = deque()
        return

    def deal(self):
        """Return top card of deck."""
        return self.cards.pop()

    def add(self, card):
        """Add `card` to bottom of deck."""
        self.cards.appendleft(card)
        return

    def __repr__(self):
        return " ".join(repr(card) for card in self.cards)

    def __len__(self):
        return len(self.cards)


class Card:
    """
    A card is an integer from 0 to 51. Cards 0,1,2,3 are the 2s of spades,
    clubs, diamonds, and hearts (in that order), and so on.
    """
    RANKS = "23456789TJQKA"
    SUITS = "SCDH"

    def __init__(self, inp):
        if type(inp) == int:
            self.card_value = inp
            self.card_rank = self.rank(inp)
            self.card_suit = self.suit(inp)
        elif type(inp) == str:
            self.card_rank = inp[0]
            self.card_suit = inp[1]
            self.card_value = self.value(inp[0], inp[1])
        elif type(inp) == tuple:
            self.card_rank, self.card_suit = inp
            self.card_value = self.value(*inp)
        else:
            raise ValueError("Invalid input.")
        return

    def rank(self, num):
        """Return the rank (2 -- A) of the card."""
        index = num // 4
        return self.RANKS[index]

    def suit(self, num):
        """Return the suit (S, C, D, H) of the card."""
        index = num % 4
        return self.SUITS[index]

    def value(self, rank, suit):
        """Construct the value from the rank and suit."""
        rank_index = self.RANKS.index(str(rank))
        suit_index = self.SUITS.index(str(suit))
        return rank_index*13 + suit_index

    def __str__(self):
        return str(self.card_rank) + str(self.card_suit)

    def __repr__(self):
        return str(self.card_rank) + str(self.card_suit)

    def __eq__(self, other):
        return (other.card_rank == self.card_rank) and (other.card_suit == self.card_suit)
