import random


class Dice:
    def __init__(self):
        self.dice = [0]*5
        self.rollAll()


def roll(self, which):
    for pos in which:
        self.dice[pos] = random.randrange(1, 7)


def rollAll(self):
    self.roll(range(5))


def values(self):
    return self.dice[:]


def score(self):

    # Create the counts list
    counts = [0]*7
    for value in self.dice:
        counts[value] = counts[value] + 1
        # score the hand
        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        # [6]のコードを原文ママで記載
        elif not (2 in counts) and (counts == 0 or counts == 0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0
