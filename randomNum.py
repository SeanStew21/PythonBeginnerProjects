'''

    generate a random number
    have user guess the number
'''
import random #Brings in random module for computer to randomly guess a number

randNum = 0
userNumber = 0
randNum = random.randint(1,10)

print ("I am thinking of a number between 1 and 10")
#print(randNum) #checking to make sure random module works

userNumber = int(input("What is your guess? "))

if (userNumber == randNum):
    print ("You guessed correctly!")
elif (userNumber == ''):
    print("A character not a number.")
else:
    print('Nope!')