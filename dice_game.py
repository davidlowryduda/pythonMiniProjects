#!/usr/bin/env python
# encoding: utf-8

"""
Suppose two players are playing with a single d-sided die. The first player rolls
it n times, where he chooses n while rolling. Then he keeps his highest roll R
and on which roll N it occurred (e.g. 6 on the 2nd roll).

Player 2 has n rolls to try to outright beat the first player. Player 2 wins if
he gets a higher overall roll, or if he ties player One's highest roll at an
earlier indexed roll (< N).

What should player 1's strategy be for different d?
"""
import random

class Die(object):
    """A simple d-sided die."""

    def __init__(self, numsides):
        self.numsides = numsides

    def roll(self):
        """Roll the die, yielding an integer from 1 to `numsides`"""
        return random.randint(1, self.numsides)

    def set_sides(self, sides):
        """Choose a new die with `sides` number of sides"""
        self.numsides = sides

class Game(object):

    def __init__(self, numsides, numrolls):
        self.gamedie = Die(numsides)
        self.numrolls = numrolls
        print "The game has begun!"

    def play(self):
        # [roll, index]
        playerone_best = [0,0]
        playerone_rolls = 0
        for r in range(self.numrolls):
            playerone_rolls += 1
            roll = self.gamedie.roll()
            if roll > playerone_best[0]:
                playerone_best = [roll, playerone_rolls]

        playertwo_best = [0,0]
        playertwo_rolls = 0
        for r in range(self.numrolls):
            playertwo_rolls += 1
            roll = self.gamedie.roll()
            if roll > playertwo_best[0]:
                playertwo_best = [roll, playertwo_rolls]

        print "Player one best: " + str(playerone_best)
        print "Player two best: " + str(playertwo_best)
        winner = self.determine_winner(playerone_best, playertwo_best)
        print "The winner is player " + str(winner)
        return winner

    def determine_winner(self, one, two):
        if one[0] > two[0]:
            return 1
        elif one[0] < two[0]:
            return 2
        else:
            if one[1] < two[1]:
                return 1
            return 2
