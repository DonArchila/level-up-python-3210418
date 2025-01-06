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

    # Generate random numbers
    random_numbers = np.random.randint(1, sides+1, (rolls, n))
    outcomes = np.sum(random_numbers, axis=1)
    unique_outcomes, counts = np.unique(outcomes, return_counts=True)
    prob_outcomes = counts/rolls

    print("OUTCOME\tPROBABILITY")
    for i in range(len(unique_outcomes)):
        print(f"{unique_outcomes[i]}\t{prob_outcomes[i]:0.2f}%")
    return

if __name__ == "__main__":
    roll_dice(4, 6, 8)