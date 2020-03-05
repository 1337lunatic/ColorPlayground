import turtle
import random
import time
from userinputTest import get255Input

t = turtle.Screen()
tt = turtle.Turtle()
t.bgcolor('black')
t.setup(width=1920,height=1080)
t.tracer(1)
tt.shape('square')
t.colormode(255)
tt.width(2) #width of the drawing pen
tt.shapesize(stretch_len=200,stretch_wid=50000)


#Shortest amount of code to draw random colors
def randintarr():
    #Creates an array with 3 elements where all 3 elements has random values.
    list = [random.randint(0,255) for x in range(3)]
    print (list) #Doesnt need to be here. only for debugging
    #Returns elements from list
    return (list[0], list[1], list[2])


#Draw random colors with delays inbetween.
def forlooptest():
    #Gets the lowest user value and the highest user value
    min = get255Input()
    max = get255Input()
    #Error check: if max val is less than min val.
    while max < min:
        print(f'invalid values: "max val: {max}" is less than "min val: {min}"')
        min = get255Input()
        max = get255Input()

    #This runs after the min and max values are correctly entered by the user.
    while True:
        a = random.randint(min, max)
        # time0.sleep(0.01)
        b = random.randint(min, max)
        # time.sleep(0.01)
        c = random.randint(min, max)
        # time.sleep(0.01)
        tt.color(a,b,c)
        print(a,b,c)
    return (a, b, c)

while True:
    t.update
    # forlooptest()
    tt.color(randintarr())