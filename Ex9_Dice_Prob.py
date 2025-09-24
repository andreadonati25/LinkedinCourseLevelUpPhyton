import random
import collections

def dice_probability(*dices, num_trials = 1000000):
    counts = collections.Counter()
    for _ in range(num_trials):
        counts[sum((random.randint(1, sides) for sides in dices))] += 1

    for result in range(len(dices), sum(dices) + 1):
        print(f"{result}\t{counts[result] * 100 / num_trials :0.2f}%")


dice_probability(6, 4, 6)