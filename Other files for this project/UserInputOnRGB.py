# imports
from os import system, name
import time
import turtle
import random

# Variables
m,n = 0,0

#Normal RGB vars
r,g,b = 0,0,0
r1,r2,b1,b2,g1,g2 = 0,0,0,0,0,0
#rgbc (rgb choice)
rgbc = 0

#rgb tuple
RGBList = ("red", "green", "blue")
# for uChoice() function
test = None

t = turtle.Screen()
tt = turtle.Turtle()
t.bgcolor('black')
t.setup(width=1920,height=1080)
t.tracer(1)
tt.shape('square')
t.colormode(255)
tt.width(2) #width of the drawing pen
tt.shapesize(stretch_len=200,stretch_wid=50000)

def uChoice(choice):
    print("Please write which of the RGB Values you want to change:\nRed, Green and/or blue. If you dont want to change a value, write 'next'")
    choice = input()
    uInput = choice.lower().split()
    #if choice is 'next'
    if choice != "next":
        test = True
    else:
        #if choice is not next
        test = False
        return choice
    if choice == "random":
        smth = randVals()
        print(smth)

    while test == True:
        while choice.lower() not in RGBList:
            if choice == "":
                print("not an rgb color")
            choice = input()
            uInput = choice.lower().split()
        for rgb in uInput:
            if rgb in RGBList:
                print(f"Editing the lowest interval of '{choice}'")
                minVal, maxVal = ecVal(m,n)
                print(f"Editing the highest interval of '{choice}'")
                #maxVal = changeVal()
                return choice, minVal, maxVal

def randVals():
    print(f"Generating random numbers")
    time.sleep(0.5)
    while True:
        list = [random.randint(0,255) for x in range(3)] 
        tt.color(list[0], list[1], list[2])
        print (list)
    return list

def ecVal(a,b):
    a = changeVal()
    b = changeVal()
    while a > b:
        print(f"ERROR: Min value is greater than max value\nMin val: '{a}'\nMax val: '{b}'")
        a = changeVal()
        b = changeVal()
    return a,b

def changeVal():
    uInput = int(input())
    while uInput < 0 or uInput > 255:
        if uInput > 255:
            print("ERROR: Int out of range\nMax int '255'")
        if uInput < 0:
            print("ERROR: Int out of range\nLowest int '0'")
        uInput = int(input())
    return uInput

def idfk():
    global r1,r2,b1,b2,g1,g2
    this = uChoice(rgbc)
    if this[0] == RGBList[0]:
        print(f"Changed 'RED' to value '{this[1]}'")
        print(this)
        r1 = this[1]
        r2 = this[2]
        return r1, r2
    elif this[0] == RGBList[1]:
        print(f"Changed 'GREEN' to value '{this[1]}'")
        print(this)
        g1 = this[1]
        g2 = this[2]
        return g1, g2 
    elif this[0] == RGBList[2]:
        print(f"Changed 'BLUE' to value '{this[1]}'")
        print(this)
        b1 = this[1]
        b2 = this[2]
        return b1, b2
    else:
        while True:
            x = random.randint(r1,r2)
            y = random.randint(g1,g2)
            z = random.randint(b1,b2)
            print(x,y,z)
            tt.color(x,y,z)

def cls():
    _ = system('cls')

cls()
while True:
    idfk()