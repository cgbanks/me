"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    def randomgame():

      print('Welcome to the guessing game!')
      print('Pick the bounds')
      lower = input('Enter a lower bound : ')
      upper = input('Enter a upper bound : ')
      if lower or upper != int:
        print('Interger only')
      else:
        print('Ok, you have chosen {lower} and {upper} as your bounds, guess a number'.format(lower, upper)
      lower = int(lower)
      upper = int(upper)

      actualNumber = random.randint(lower, upper)

      guessed = False

      while not guessed:
        guessed_number = int(input('Number guess : '))
        print('You have guessed {}').format(guessed_number)
        if guessed_number == actualNumber:
          print('Well done! That is it!')
          guessed = True
        elif guessed_number > upper or guessed_number < lower:
          print('You fool! Know your bounds')
          guessed = False
        elif guessed_number > actualNumber:
          print ('Too high!')
          guessed = False
        else guessed_number < actualNumber:
          print ('Too low!')
          guessed = False
        
      return "You got it!"

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
