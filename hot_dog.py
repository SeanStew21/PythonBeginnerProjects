'''
    Author: Sean Steward
    Date February 25, 2019
    Purpose: Hot Dog Cookout Calculator

'''

#Main Module

#Declare
numOfPeople = 0
hotDogs = 10
Buns = 8


#input data module
    #how many people attending
numOfPeople = int(input("Enter the amount of people attending cookout:"))
    #number of hot dogs people recieve
givenFood = int(input("Enter amount of hot dogs each person will get:"))

#perform calculations module
    #calculate how many hot dogs needed
totHotDogsNeeded = numOfPeople * givenFood
print("You need ", totHotDogsNeeded, " total hot dogs.")
buyDogs = totHotDogsNeeded / hotDogs
buyBuns = totHotDogsNeeded / Buns

#output data module

#if totHotDogsNeeded > 0 and totHotDogsNeeded < 10:
print(buyDogs)
