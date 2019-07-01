"""Week 3, Exercise 3.
Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    
    is_none = False
    is_num = True
    num = input(message)

# Check that the input is not NONE
    while is_none == False:
      if num == None:
        print('Please input a number ')
        num = input(message)
      else:
        is_num = False
        is_none = True
        

    while is_num == False:
        try:
            int(num)
            is_num = True
        except Exception:
            print('This is not a number, Please try again ')
            num = input(message)
        

    return num


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

    print('Welcome to the guessing game !')
    print('Lets start by picking the range for the number')

    lower = not_number_rejector(str('Please pick the lower bound '))
    
    print('You enetered ' + str(lower))

    upper = not_number_rejector(str('Please pick a number for the upper bound '))

    small = False 
    
    while small == False:
      if int(upper) > int(lower) + 1:
        print('Cool')
        small = True
      else:
        upper = not_number_rejector(str('Please select a numer higer than ' + str(int(lower) + 1) + ' '))
    
    print('Please guess a number between ' + str(lower) + ' and ' + str(upper))

    guessed_num = not_number_rejector(str("Please guess a number between {} and {} ".format(lower, upper)))

    bounds = False
    
    while bounds == False:
      if int(guessed_num) > int(lower) and int(guessed_num) < int(upper):
        bounds = True
      else:
        print ("Not inside the bounds")
        guessed_num = not_number_rejector(str("Please guess a number between {} and {} ".format(lower, upper)))
     
    num_selected = random.randint(int(lower) +1 , int(upper) -1)

    is_correct = False

    while is_correct == False:
      print('Your guess is {}'.format(guessed_num))
      if int(guessed_num) == int(num_selected):
        is_correct = True
      elif int(guessed_num) < int(num_selected):
        print('Sorry the number {} is too small'.format(guessed_num))
        guessed_num = not_number_rejector(str("Please guess another number between {} and {} ".format(lower, upper)))
      else:
        print('Sorry the number {} is too big'.format(guessed_num))
        guessed_num = not_number_rejector(str("Please guess another number between {} and {} ".format(lower, upper)))



    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())