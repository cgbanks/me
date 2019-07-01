# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0

    num_correct = False

    while num_correct == False:

        num_list = list(range(low,high))

        index = int(len(num_list) / 2)
        #print("index {} low {} high {}".format(index,low,high))

        guess = num_list[index]

        if guess == actual_number:
            print(guess)
            print('you got it ')
            num_correct = True
        elif guess < actual_number:
            print(guess)
            low = int(guess) +1
            tries += 1
        else:
            print(guess)
            high = int(guess) 
            tries += 1


    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
