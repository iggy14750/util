#!/usr/bin/python3

"""
Inspired by the problem discussed in the Veritasium video,
"The Most Controversial Problem in Philosophy",
at one point, he discusses running the numbers himself,
and they don't turn out how I would expect.
So, I have decided to run the numbers myself.

                 -- (Tails) -- Monday wakeup
                /
Coin Flip (1/2)- 
                \-- (Heads) -- Monday wakeup -- Tuesday wakeup
"""
import random
import sys

class CoinFlipStats:
    def __init__(self):
        self.flips = 0
        self.heads = 0
        self.tails = 0
        self.tails_mondays = 0
        self.heads_mondays = 0
        self.heads_tuesdays = 0
        self.days = 0

    def __str__(self):
        # TODO: Could print in a more tabular format,
        # including right-justifying numbers
        return ""\
            + "Flips:              {}\n".format(self.flips)\
            + "Heads:              {}\n".format(self.heads)\
            + "Tails:              {}\n".format(self.tails)\
            + "Total Days:         {}\n".format(self.days)\
            + "Tails Mondays:      {}\n".format(self.tails_mondays)\
            + "Heads Mondays:      {}\n".format(self.heads_mondays)\
            + "Heads Mondays:      {}\n".format(self.heads_tuesdays)

def main():
    # TODO: Do we want to seed random with the time?
    if len(sys.argv) < 2:
        print("Usage: python3 {} <Number of Flips>".format(sys.argv[0]))
        sys.exit(1)

    flips = int(sys.argv[1])
    stats = CoinFlipStats()

    for _ in range(flips):
        stats.flips += 1
        if flip_is_heads():
            stats.heads += 1
            stats.heads_mondays += 1
            stats.heads_tuesdays += 1
            stats.days += 2 # <--- cruicial difference here
        else:
            stats.tails += 1
            stats.tails_mondays += 1
            stats.days += 1

    # Now print out results
    print(stats)

def flip_is_heads():
    heads = True
    tails = False
    coin = [heads, tails]
    return random.choice(coin)

if __name__ == "__main__":
    main()

