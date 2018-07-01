
from deck import Card, Deck

class War():
    RANKS = "23456789TJQKA"

    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.winner = None
        self.turn = 0
        return

    def play_war(self):
        while not self.winner:
            self.next_card()
        self.announce_winner()
        return

    def next_card(self, turn_deck=None):
        if not turn_deck:
            turn_deck = Deck()
        if self.is_game_over():
            return
        self.turn += 1
        print("Turn {}".format(self.turn))
        print("Decks:\n------\nPlayer 1: {}\nPlayer 2: {}"
               .format(self.deck1, self.deck2))
        c1 = self.deck1.deal()
        c2 = self.deck2.deal()
        turn_deck.add(c1)
        turn_deck.add(c2)

        print("{}   {}\n".format(c1, c2))
        higher_card = self.determine_higher_card(c1, c2)
        if higher_card == 1:
            for card in turn_deck.cards:
                self.deck1.add(card)    # TODO more pythonic if just in turn_deck
        elif higher_card == 2:
            for card in turn_deck.cards:
                self.deck2.add(card)    # TODO more pythonic if just in turn_deck
        else:
            self.go_to_war(turn_deck)
        return

    def burn_card(self, turn_deck):
        turn_deck.add(self.deck1.deal())
        turn_deck.add(self.deck2.deal())
        return

    def determine_higher_card(self, card1, card2):
        diff = self.RANKS.index(card1.card_rank) - self.RANKS.index(card2.card_rank)
        if diff > 0:
            return 1
        elif diff < 0:
            return 2
        else:  # WAR
            return

    def go_to_war(self, turn_deck):
        self.burn_card(turn_deck)
        if self.is_game_over():
            return
        self.next_card(turn_deck=turn_deck)
        return

    def is_game_over(self):
        if len(self.deck1) == 0:
            self.winner = 2
            return True
        elif len(self.deck2) == 0:
            self.winner = 1
            return True
        return False

    def announce_winner(self):
        print("The winning player is Player {}.".format(self.winner))
        return

if __name__ == "__main__":
    deck1 = Deck()
    for card in (Card(i) for i in range(2, 10, 2)):
        deck1.add(card)
    deck1.add(Card(41))
    deck2 = Deck()
    for card in (Card(i) for i in range(3, 43, 5)):
        deck2.add(card)
    game = War(deck1, deck2)
    game.play_war()
