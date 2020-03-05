import random
import turtle

#variables
ColorArr = [
    'blue',
    'red',
    'yellow',
    'purple',
    'gray',
    'white',
    'green',
    'brown',
    'orange',
    'pink',
    'violet',
]

def get255Input():
    uInputMin = int(input())
    while uInputMin > 255 or uInputMin < 0:
        print("int not 0-255")
        uInputMin = int(input())
    return uInputMin

#function to get an input from user and return the input
def getInput():
    uInput = input()
    #As long as the users input is not in the color array, repeat
    while uInput.lower() not in ColorArr:
        print("Invalid color name")
        uInput = input()
    #Return the user's input
    return uInput.lower()

#while True:
    #main code
    #In python, if you call a function within print(), the function will run. This means that we can call the function twice, and it'll return the user's value and print it
    #print(getInput(), getInput())
    