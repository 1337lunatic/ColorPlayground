#Abbreviation dictionary
#EC = Error Check(ing), clrm = Color mode, uInput = User Input, r g b = Red Green Blue, rx gx bx = Redx Greenx Bluex, randRGB = Random RGB, val = Value, grRGBval = Generate RGB values

#libraries
import random
import turtle

#Turtle variables
t = turtle.Screen()
tt = turtle.Turtle()
t.bgcolor('black')
t.setup(width=1920,height=1080)
t.tracer(1)
tt.shape('square')
t.colormode(255)
tt.width(2) #width of the drawing pen
tt.shapesize(stretch_len=200,stretch_wid=50000)

#Create variables. Assigning all variables to 0, because they need to be ints
r1,r2,b1,b2,g1,g2 = 0,0,0,0,0,0
rx1,rx2,bx1,bx2,gx1,gx2 = 0,0,0,0,0,0
#Function for input, and EC the input
def clrm():
    #Make uInput an int instead of str
    uInput = int(input())
    #Error handling
    while uInput < 0 or uInput > 255:
        #if the uInput is greater than 255(max rgb val.), print this
        if uInput > 255:
            print("ERROR: Int out of range\nMax int '255'")
        #If the uInput is lesser than 0, (Lowest rgb val.), print this
        if uInput < 0:
            print("ERROR: Int out of range\nLowest int '0'")
        uInput = int(input())
    return uInput

#This function makes it possible to compare 2 values with the use of 1 function. the functions could be moved to another .py file to make this file have less code
#Function to make it possible to have a min & max val. function has 2 parameters (min,max)
def randRGB(a,b):
    a = clrm()
    b = clrm()
    while a > b:
        print(f"ERROR: Min value is greater than max value\nMin val: '{a}'\nMax val: '{b}'")
        a = clrm()
        b = clrm()
    return a,b

#Generates the random numbers with user input
def grRGBval():
    #Generates random numbers within the min,max vals specified by the user inputs
    x = random.randint(r1,r2)
    y = random.randint(g1,g2)
    z = random.randint(b1,b2)
    print(x,y,z)
    tt.color(x,y,z)

#Run before the while loop runs
print("please write 2 integers, on seperate lines, from 0-255 for r(Red)")
#Using tuples to assing the randRGB values to r1,r2
r1,r2 = randRGB(rx1,rx2)
print("please write 2 integers, on seperate lines, from 0-255 for g(Green)")
g1,g2 = randRGB(gx1,gx2)
print("please write 2 integers, on seperate lines, from 0-255 for b(Blue)")
b1,b2 = randRGB(bx1,bx2)

while True:
    #Run the loop
    grRGBval()