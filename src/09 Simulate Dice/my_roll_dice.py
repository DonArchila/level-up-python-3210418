# `roll_dice()`, that takes a variable number of input arguments 
# representing the number of sides on an arbitrary number of dice, 
# its and its output should print a table of the probability 
# for each possible outcome.

import numpy as np

def roll_dice(*args, rolls=1_000_000):
    n = len(args)
    sides = np.array(args)
    total_sides = np.sum(sides)
    prob = sides/total_sides
    print("Sum of dice:", total_sides)
    print("Number of dice:", n)
    print("Number of sides on each dice:", sides)
    print("Probability of each outcome:")

    # roll each dice rolls times and count the number of times each outcome occurs
    outcomes = np.zeros(total_sides - n + 1)
    for _ in range(rolls):
        outcome = np.sum([np.random.randint(1, sides[i] + 1) for i in range(n)])
        outcomes[outcome - n] += 1

    # print the probability of each outcome
    for i, outcome in enumerate(outcomes):
        print(f"{i + n}: {outcome/rolls:.2%}")

if __name__ == "__main__":
    roll_dice(4, 6, 8)