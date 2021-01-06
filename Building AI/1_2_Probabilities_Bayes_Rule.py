"""
This script is playing around with probabilities. 
1. Printing different sentences given probabilities.
2. Generating random numbers and counting occurences of a sequence
3. Using some data, calculating probabilities and predicting an outcome
4. Using Bayes Rule to predict an outcome
"""

import numpy as np
import random

# 1. Printing different sentences given probabilities.

def main1():
    """
    This function prints "I love" followed by one word:
   'dogs' with 80% probability
   'cats' with 10% probability and
   'bats' with 10% probability.
    """
    p = random.random()
    
    if p < 0.8: 
        favourite = "dogs"  # change this
    elif p < 0.9:
        favourite = "cats"
    else:
        favourite = "bats"

    print("I love " + favourite) 

main1()


# 2. Generating random numbers and counting occurences of a sequence

def generate(p1):
    """
    This function generates 10000 random zeros and ones as sequence
    where the probability of a one is p1.
    """
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    """
    This function counts the number of occurrences of 5 consecutive ones
    ("11111") in the sequence.
    """
    n = 0
    for i in range(len(seq)-1):
        if sum(seq[i:i+5])==5:
            n += 1
    return n

def main2(p1):
    seq = generate(p1)
    return count(seq)

print(main2(2/3))


# 3. Using some data, calculating probabilities and predicting an outcome

# Fishing in the Nordics

# Data of each country
countries = np.array(['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden'])
populations = np.array([5615000, 5439000, 324000, 5080000, 9609000])
male_fishers = np.array([1822, 2575, 3400, 11291, 1731])
female_fishers = np.array([69, 77, 400, 320, 26])

# total values of all countries
fishers_male_total = sum(male_fishers) # total number of male fishers
fishers_female_total = sum(female_fishers) # total number of female fishers

def guess(winner_gender):
    """
    This function gets the gender and finds the country with the highest chance
    of being the winner.
    """
    if winner_gender == 'female':
        fishers = female_fishers
        fishers_total = fishers_female_total
    else:
        fishers = male_fishers
        fishers_total = fishers_male_total

    # probability winner is a male or female fisher for each country
    arr = fishers/fishers_total * 100
    # index to find country with highest probability = guess of country
    index = np.where(arr == np.amax(arr)) 
    guess = countries[index] # country result = numpy.where(arr == numpy.amax(arr))
    biggest = arr[index] # fraction of fishers and total fishers

    return (*guess, biggest)  

def main3():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main3()

# 4. Using Bayes Rule to predict an outcome

def bot8(pbot, p8_bot, p8_human):
    """
    This function uses Bayes Rule to calculate how much likely a name with
    an 8-digit code is a bot. Bayes Rule -> p(A|B) = p(B|A) * p(A) / p(B)
    and with p(B) = p(A)*p(B|A) + (1-p(A))*p(B|(notA))
    """
    p8 = p8_bot * pbot + p8_human * (1-pbot)
    pbot_8 = p8_bot * pbot / p8
    print(pbot_8)

# probabilities
pbot = 0.1 # being a bot
p8_bot = 0.8 # having 8-digit code given that it's a bot
p8_human = 0.05 # having a 8-digit code given that it's a human

bot8(pbot, p8_bot, p8_human)
