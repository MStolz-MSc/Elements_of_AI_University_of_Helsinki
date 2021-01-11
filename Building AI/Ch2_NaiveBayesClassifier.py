'''
Exercise 10: Naive Bayes Classifier
Throwing a die ten times and deciding after if it was a loaded or a normal die.
'''
import numpy as np

# probabilities of the dies
p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # loaded

def roll(loaded):
    """
    This function creates a sequence by rolling a die that is either loaded
    or normal.
    """
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1 
    for roll in sequence:
        print("rolled %d" % roll)
        
    return sequence

def bayes(sequence):
    """
    This function uses Bayes Rule to update the odds by calculating the
    likelihood r and multiplying it on the odds.
    Returns True if odds > 1 (loaded die) or else False (normal die)
    """
    odds = 1.0              # start with odds 1:1
    for roll in sequence:   
        r = p2[roll-1]/p1[roll-1]
        odds *= r 
        print(odds)

    if odds > 1:
        return True
    else:
        return False

sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
