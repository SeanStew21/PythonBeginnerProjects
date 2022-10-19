'''
    Guess my number game

    computer generates a random number
    user tries to guess the number
    keep track of how many guesses were correct
    if player enters a negative number, game over
    display the totals of guesses right
'''
import random

randomNum = 0
userNumber = 1
guessedRight = 0
guessedWrong = 0

while userNumber > 0:
    randNum = random.randint(1,10)
    print("I am thinking of a number between 1 and 10")

    print("For testing purposes, the number I picked was", randNum)
    userNumber = int(input("What is your guess? Enter negative number to quit:"))

    if userNumber == randNum:
        print("You guessed it!")
        guessedRight += 1
    elif userNumber > 10:
        print("You guessed too high!")
        guessedWrong += 1
    elif userNumber < 0:
        print("Thank your for playing!")
    else:
        print("You guessed incorrectly")
        guessedWrong += 1

print("You guessed ", guessedRight, " correctly.")
print("You guessed ", guessedWrong, " incorrectly.")
