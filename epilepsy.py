import turtle
import random
from turtle import *
from external import *

t = turtle.Screen()
tt = turtle.Turtle() 
t.title('Epilepsy') #title name
t.bgcolor('black') #background color
t.setup(width=1920, height=1080)  #res
t.tracer(1000)#uncomment this aswell as add t.update() in loop to cause mayhem
tt.hideturtle() #hides turtle
tt.width(2)

#loop
while True:
    t.update() 
    test()
