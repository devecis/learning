"""
Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random interger between 0 - 100 inclusive
Then asks the user to guess what number has been chosen
Each time the user enters a guess, the program indicates one of the following:
- Too High
- Too Low
- Just right
If the user guesses correctly, the program exits. Otherwises , the user is asked to try agian
The program exits after the user guess correctly
Give user 3 tries
"""


from os import system, name
from time import sleep
import random

def clear():  # Used to clear the screen after session
    if name == 'nt':
        _ = system('cls')
        
answer = random.randint(1, 100) #picking as number between 1 and 100

def guessing_game():  #the guessing game. The user input is in here instead of main because the user has to do it 3 times
    for i in range(3):
        user_guess = int(input("Guess a number between 1 - 100, you only get 3 tries. "))
        if user_guess == answer:
            print(f"Right! The answer is {user_guess}")
            break
        elif user_guess < answer:
            print(f"Your guess of {user_guess} is too low!")
        elif user_guess > answer:
                print(f"Your guess of {user_guess} is too high!")
                  

def main():
    guessing_game()
    sleep(2)
    clear()

if __name__ == "__main__":
    main()