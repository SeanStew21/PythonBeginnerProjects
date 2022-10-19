'''

    Author: Sean
    Purpose: Looping practice

'''
'''
#Bug Collector

bugs = 0
total = 0

while total < 6:
    bugs += int(input('Enter number of bugs collected today: '))
    total += 1


print('Total bugs collected: ', bugs)
'''

#Calories burned

caloriesPerMinute = 4.2
caloriesBurned = 0.0
minutes = 10

while minutes <= 30:
    caloriesBurned = caloriesPerMinute * minutes
    print('You burned ', caloriesBurned, ' calories.')
    print('You ran for ', minutes, ' minutes.')
    minutes += 5
    

