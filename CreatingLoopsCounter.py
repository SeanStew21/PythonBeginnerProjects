'''
    Creating Loops

    Repeating code until a certain condition is met



playAgain = 'y'
howMany = 0

while playAgain == 'y':
    print("You are inside the loop!")
    playAgain = input("Do you want to play again?")
    howMany += 1
    
print("Thank you for playing!")
print("You were here ",howMany, " iterations.")
'''

playAgain = 'y'
sum = 0
userNum = 0

while playAgain == 'y':
    userNum = int(input("Enter a number"))
    #sum = sum + userNum or
    sum += userNum
    playAgain = input("Want to enter in another number?")
print("Your sum is ", sum)
