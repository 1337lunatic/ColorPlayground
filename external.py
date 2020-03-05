import turtle
import random

tt = turtle.Turtle()
t = turtle.Screen()
t.tracer(0) #if set to 1, it will show each entity being drawn before starting the actual program
t.colormode(255) #sets the colormode to rgb values instead of 0-1
arr = ['red', #color array
        'blue',
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

class turtel():
    tem = turtle.Turtle() #Sets turtle
    #variables
    testa = None
    randmax = 255
    randmin = 0
    a = 'a'
    r = 0 #define rgb
    g = 0
    b = 0
    r1 = r
    g1 = g
    b1 = b
    speed = 0 #forwardspeed
    colorspeed = 1 #speed of which the color is changing

    def __init__(self, r = 0, g = 0, b = 0): #sets defaults of rgb
        self.r = r
        self.g = g
        self.b = b
        self.tem.up() #item.penup()
        self.tem.color(self.r,self.g,self.b) #sets color
        self.tem.shapesize(stretch_len=200,stretch_wid=500) #size of the shape
        self.tem.setheading(random.choice(arrheading)) #random pos from heading array
    
    def checkcords(self):
        if self.tem.xcor() < -20 or self.tem.xcor() > 40 or self.tem.ycor() > 20 or self.tem.ycor() < -40: #if shape hits xy cords, reverse their position
            a = self.tem.heading()
            a += 180 
            if a >= 360: #if heading is more than 360 degrees after it has been plussed with 180, then delete 360 degrees off of heading
                a -= 360
            self.tem.seth(a) #set the new heading
    
    def goforward(self):
        self.checkcords() #checks cords before moving
        self.tem.forward(self.speed) #sets itself to speed of variable

    def randh(self): #random heading position.
        self.tem.seth(random.choice(arrheading))

    #This function cuts around 40~ lines of code per cyclecolor
    def cyclefunc(self): #Function for cycling through colors
        if self.r <= self.r1: #checks if r is less than or equals to r1
            self.r += self.colorspeed #if it is below r1, then self.r add self.colorspeed
            if self.r >= self.r1: #if r is more than or equals to r1
                self.r = self.r1 #set r to r1
        if self.r >= self.r1: #checks if r is more than or equals to r1
            self.r -= self.colorspeed #if r is above r1, then subtract r
            if self.r <= self.r1: #if r is less than or equals to r
                self.r = self.r1 #set r to r1

        if self.g <= self.g1: #add green
            self.g += self.colorspeed
            if self.g >= self.g1:
                self.g = self.g1
        if self.g >= self.g1: #subtract green
            self.g -= self.colorspeed
            if self.g <= self.g1:
                self.g = self.g1

        if self.b <= self.b1: #add blue
            self.b += self.colorspeed
            if self.b >= self.b1:
                self.b = self.b1
        if self.b >= self.b1: #subtract blue    
            self.b -= self.colorspeed
            if self.b <= self.b1:
                self.b = self.b1


    #quick way to make it random
    def cyclerand(self):
        self.r = random.randint(self.randmin, self.randmax)
        self.g = random.randint(self.randmin, self.randmax)
        self.b = random.randint(self.randmin, self.randmax)
        self.tem.color(self.r,self.g,self.b)
        print(self.r,self.g,self.b)


    #Playing around with cyclefunc(). 
    def cyclered(self): #cycles through all forms of red
        self.cyclefunc() #this function calculates everything
        if self.a == 'a': #255,160,122
            self.r1,self.g1,self.b1 = 255,160,122
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'b'
        if self.a == 'b':#250,128,144
            self.r1,self.g1,self.b1 = 250,128,144
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'c'
        if self.a == 'c': #233,150,122
            self.r1,self.g1,self.b1 = 233,150,122
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'd'           
        if self.a == 'd': #240,128,128
            self.r1,self.g1,self.b1 = 240,128,128
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'e'           
        if self.a == 'e': #205,92,92
            self.r1,self.g1,self.b1 = 205,92,92
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'f'            
        if self.a == 'f': #220,20,60
            self.r1,self.g1,self.b1 = 220,20,60
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'g'           
        if self.a == 'g': #178,34,34
            self.r1,self.g1,self.b1 = 178,34,34
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'h'           
        if self.a == 'h': #255,99,71
            self.r1,self.g1,self.b1 = 255,99,71
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'i'           
        if self.a == 'i': #255,69,0
            self.r1,self.g1,self.b1 = 255,69,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'j'            
        if self.a == 'j': #128,0,0
            self.r1,self.g1,self.b1 = 128,0,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'k'
        if self.a == 'k': #138,0,0
            self.r1,self.g1,self.b1 = 138,0,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'a'
        self.tem.color(self.r,self.g,self.b)
        print(self.r, self.g, self.b)

    def cyclegreen(self): #Cycles through green colors
        self.cyclefunc()
        if self.a == 'a': #0,255,0
            self.r1,self.g1,self.b1 = 0,255,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'b'
        if self.a == 'b': #127,255,0
            self.r1,self.g1,self.b1 = 127,255,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'c'
        if self.a == 'c': #173,255,47
            self.r1,self.g1,self.b1 = 173,255,47
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'd'
        if self.a == 'd': #124,252,0 
            self.r1,self.g1,self.b1 = 124,252,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'e'
        if self.a == 'e': #152,251,152
            self.r1,self.g1,self.b1 = 152,251,152
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'f'
        if self.a == 'f': #154,205,50
            self.r1,self.g1,self.b1 = 154,205,50
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'g'
        if self.a == 'g': #50,205,50
            self.r1,self.g1,self.b1 = 50,205,50
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'h'
        if self.a == 'h': #143,188,143
            self.r1,self.g1,self.b1 = 143,188,143
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'i'
        if self.a == 'i': #60,179,113
            self.r1,self.g1,self.b1 = 60,179,113
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'j'
        if self.a == 'j': #32,178,170
            self.r1,self.g1,self.b1 = 32,178,170
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'k'
        if self.a == 'k': #107,142,35
            self.r1,self.g1,self.b1 = 107,142,35
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'l'
        if self.a == 'l': #46,139,87
            self.r1,self.g1,self.b1 = 46,139,87
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'm'
        if self.a == 'm': #34,139,34
            self.r1,self.g1,self.b1 = 34,139,34
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'n'
        if self.a == 'n': #128,128,0
            self.r1,self.g1,self.b1 = 128,128,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'o'
        if self.a == 'o': #0,128,0
            self.r1,self.g1,self.b1 = 0,128,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'p'
        if self.a == 'p': #85,107,47
            self.r1,self.g1,self.b1 = 85,107,48

            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'q'
        if self.a == 'q': #30,100,0
            self.r1,self.g1,self.b1 = 30,100,0
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'a'
        self.tem.color(self.r,self.g,self.b)
        print(self.r, self.g, self.b)

    def cycleblue(self):
        self.cyclefunc()
        if self.a == 'a': #240,248,255
            print('cycleblue')
            self.r1,self.g1,self.b1 = 240,248,255
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'b'
        if self.a == 'b': #240,248,255
            self.r1,self.g1,self.b1 = 240,248,255
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'c'
        if self.a == 'c': #230,230,250
            self.r1,self.g1,self.b1 = 230,230,250
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'd'                    
        if self.a == 'd': #176,224,230
            self.r1,self.g1,self.b1 = 176,224,230
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'e'
        if self.a == 'e': #173,216,230 
            self.r1,self.g1,self.b1 = 173,216,230
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'f'
        if self.a == 'f': #135,206,250
            self.r1,self.g1,self.b1 = 135,206,250
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'g'
        if self.a == 'g': #135,206,235
            self.r1,self.g1,self.b1 = 135,206,235
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'h'
        if self.a == 'h': #0,191,255
            self.r1,self.g1,self.b1 = 0,191,255
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'i'
        if self.a == 'i': #176,196,222
            self.r1,self.g1,self.b1 = 176,196,222
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'j'
        if self.a == 'j': #30,144,255
            self.r1,self.g1,self.b1 = 30,144,255
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'k'
        if self.a == 'k': #100,149,237
            self.r1,self.g1,self.b1 = 100,149,237
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'l'
        if self.a == 'l': #70,130,180
            self.r1,self.g1,self.b1 = 70,130,80
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'm'
        if self.a == 'm': #95,158,160
            self.r1,self.g1,self.b1 = 95,158,160
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'n'
        if self.a == 'n': #123,104,238
            self.r1,self.g1,self.b1 = 123,104,238
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'o'
        if self.a == 'o': #106,90,205
            self.r1,self.g1,self.b1 = 106,90,205
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'p' 
        if self.a == 'p': #72,61,139
            self.r1,self.g1,self.b1 = 72,61,139
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'q'
        if self.a == 'q': #65,105,225
            self.r1,self.g1,self.b1 = 65,105,255
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'r'    
        if self.a == 'r': #0,0,255
            self.r1,self.g1,self.b1 = 0,0,255
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 's'    
        if self.a == 's': #0,0,205
            self.r1,self.g1,self.b1 = 0,0,205
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 't'     
        if self.a == 't': #0,0,139
            self.r1,self.g1,self.b1 = 0,0,139
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'v'  
        if self.a == 'v': #0,0,128
            self.r1,self.g1,self.b1 = 0,0,128
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'w'     
        if self.a == 'w': #138,43,226
            self.r1,self.g1,self.b1 = 138,43,226
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'x'
        if self.a == 'x': #75,0,130
            self.r1,self.g1,self.b1 = 75,0,130
            if self.r == self.r1 and self.g == self.g1 and self.b == self.b1:
                self.a = 'a'
        self.tem.color(self.r,self.g,self.b)
        print(self.r, self.g, self.b)

    #Learning how to cycle through colors
    def changecolor(self): #changes color 0-255
        self.r += self.colorspeed #variable
        if self.r >= 255: #if self.x is greater than 255 do this:
            self.r = 255 #makes it stay at 255
            self.g += self.colorspeed
        if self.g >= 255: 
            self.g = 255
            self.b += self.colorspeed
        if self.b >= 255: 
            self.r, self.g, self.b = 0,0,0 #reset colors
        self.tem.color(self.r,self.g,self.b) #sets the turtle color to rgb values
        print(self.r, self.g, self.b)

    #Doing the reverse of changecolor
    def changecolorrev(self): #reversed changecolor.
        self.r -= self.colorspeed
        if self.r <= 0:
            self.r = 0
            self.g -= self.colorspeed
        if self.g <= 0:
            self.g = 0
            self.b -= self.colorspeed
        if self.b <= 0:
            self.r, self.g, self.b = 255,255,255
        self.tem.color(self.r,self.g,self.b)
        print(self.r, self.g, self.b)

#arrays and loops
arrheading = [] #array for turtle.setheading()
for i in range(360): #array with 0-359
    arrheading.append(i) #appends to array

arrtt = [] #array turtle.Turtle()
for i in range(1): #amount of turtles we want
    arrtt.append(turtel(i,i,i)) #appends turtel() with i,i,i as rgb

def test(): #main func for epilepsy.py
    for i in arrtt: #check class for info
        i.goforward()
        #i.cyclegreen()
        # i.cyclered()
        i.cyclerand()
        i.randh()
        #i.changecolorrev()

#This was the first couple of ideas that came to mind. putting this into a class would make this better -- upd 2/7/20. or just make it less ugly lol
#keypress check & def's
def wk(): #w key 
    tt.setheading(90)
    tt.forward(100)

def ak(): #a key
    tt.setheading(180)
    tt.forward(100)

def sk(): #s key
    tt.setheading(270)
    tt.forward(100)

def dk(): # d key
    tt.setheading(0)
    tt.forward(100)

#reset canvas
def rk():
    tt.clear() #clears all
    t.bgcolor('black') #sets bg to black

#testing random coords
xrandmin = -1000 #xy min,max oords
xrandmax = 1000
yrandmin = -520
yrandmax = 520

xrand, yrand = random.randint(xrandmin, xrandmax), random.randint(yrandmin, yrandmax)  #sets axrand to a random number between xrandmin/min

#forloop funcs
def pk(): #p key for left 
    for i in range(10):
        tt.pendown()
        tt.setheading(270)
        tt.forward(10)
        tt.setheading(90)
        tt.forward(20)
        tt.setheading(180)
        tt.forward(55)
        tt.shape('arrow')
        tt.color(random.choice(arr))
        if i == 9 or i == 4: #nested if-statements.
            if tt.xcor() < -1000 or tt.xcor() > 1000 or tt.ycor() > 520 or tt.ycor() < -520: #changes pos to new pos after for loop has ended
                xrand = random.randint(xrandmin, xrandmax)
                yrand = random.randint(yrandmin, yrandmax) 
                tt.setx(xrand)
                tt.sety(yrand)

def ok(): #o key for right
    for i in range(10):
        tt.pendown()
        tt.width(2)
        tt.setheading(270)
        tt.forward(10)
        tt.setheading(90)
        tt.forward(20)
        tt.setheading(0)
        tt.forward(55)
        tt.color(random.choice(arr))
        if i == 9 or i == 4: #nested if-statements.
            if tt.xcor() < -1000 or tt.xcor() > 1000 or tt.ycor() > 520 or tt.ycor() < -520: #changes pos to new pos after for loop has ended
                xrand = random.randint(xrandmin, xrandmax)
                yrand = random.randint(yrandmin, yrandmax) 
                tt.setx(xrand)
                tt.sety(yrand)

def ik(): #i key up left
    for i in range(10):
        tt.pendown()
        tt.setheading(0)
        tt.forward(10)
        tt.setheading(180)
        tt.forward(20)
        tt.setheading(90)
        tt.forward(55)
        tt.color(random.choice(arr))
        if i == 9 or i == 4: #nested if-statements.
            if tt.xcor() < -1000 or tt.xcor() > 1000 or tt.ycor() > 520 or tt.ycor() < -520: #changes pos to new pos after for loop has ended    
                xrand = random.randint(xrandmin, xrandmax)
                yrand = random.randint(yrandmin, yrandmax) 
                tt.setx(xrand)
                tt.sety(yrand)

def uk(): #u key up right
    for i in range(10):
        tt.pendown()
        tt.setheading(180)
        tt.forward(10)
        tt.setheading(0)
        tt.forward(20)
        tt.setheading(90)
        tt.forward(55)
        tt.color(random.choice(arr))
        if i == 9 or i == 4: #nested if-statements.
            if tt.xcor() < -1000 or tt.xcor() > 1000 or tt.ycor() > 520 or tt.ycor() < -520: #changes pos to new pos after for loop has ended    
                xrand = random.randint(xrandmin, xrandmax)
                yrand = random.randint(yrandmin, yrandmax) 
                tt.setx(xrand)
                tt.sety(yrand)

def lk(): #l key for rightdown
    for i in range(10):
        tt.pendown()
        tt.setheading(90)
        tt.forward(10)
        tt.setheading(270)
        tt.forward(20)
        tt.setheading(0)
        tt.forward(55)
        tt.color(random.choice(arr))
        if i == 9 or i == 4: #nested if-statements.
            if tt.xcor() < -1000 or tt.xcor() > 1000 or tt.ycor() > 520 or tt.ycor() < -520: #changes pos to new pos after for loop has ended
                xrand = random.randint(xrandmin, xrandmax)
                yrand = random.randint(yrandmin, yrandmax)                 
                tt.setx(xrand)
                tt.sety(yrand)

def kk(): #k key for down right
    for i in range(10):
        tt.pendown()
        tt.setheading(90)
        tt.forward(10)
        tt.setheading(270)
        tt.forward(20)
        tt.setheading(180)
        tt.forward(55)
        tt.color(random.choice(arr))
        if i == 9 or i == 4: #nested if-statements.
            if tt.xcor() < -1000 or tt.xcor() > 1000 or tt.ycor() > 520 or tt.ycor() < -520: #changes pos to new pos after for loop has ended
                xrand = random.randint(xrandmin, xrandmax)
                yrand = random.randint(yrandmin, yrandmax) 
                tt.setx(xrand)
                tt.sety(yrand)

def jk(): #j key for downleft
    for i in range(10):
        tt.pendown()
        tt.setheading(0)
        tt.forward(10)
        tt.setheading(180)
        tt.forward(20)
        tt.setheading(270)
        tt.forward(55)
        tt.color(random.choice(arr))
        if i == 9 or i == 4: #nested if-statements.
            if tt.xcor() < -1000 or tt.xcor() > 1000 or tt.ycor() > 520 or tt.ycor() < -520: #changes pos to new pos after for loop has ended
                xrand = random.randint(xrandmin, xrandmax)
                yrand = random.randint(yrandmin, yrandmax) 
                tt.setx(xrand)
                tt.sety(yrand)

def hk(): #h key for downright
    for i in range(10):
        tt.pendown()
        tt.setheading(180)
        tt.forward(10)
        tt.setheading(0)
        tt.forward(20)
        tt.setheading(270)
        tt.forward(55)
        tt.color(random.choice(arr))
        if i == 9 or i == 4: #nested if-statements.
            if tt.xcor() < -1000 or tt.xcor() > 1000 or tt.ycor() > 520 or tt.ycor() < -520: #changes pos to new pos after for loop has ended
                xrand = random.randint(xrandmin, xrandmax)
                yrand = random.randint(yrandmin, yrandmax) 
                tt.setx(xrand)
                tt.sety(yrand)    

t.listen() #Listens for input
t.onkeypress(wk, 'w') #WASD
t.onkeypress(ak, 'a')
t.onkeypress(sk, 's')
t.onkeypress(dk, 'd')

#reset key
t.onkeypress(rk, 'r')

#forloop up-keys 
t.onkeypress(pk, 'p') #left up
t.onkeypress(ok, 'o') #right up

t.onkeypress(ik, 'i') #upleft
t.onkeypress(uk, 'u') #upright

#forloop down-keys
t.onkeypress(lk, 'l') #right down
t.onkeypress(kk, 'k') #left down

t.onkeypress(jk, 'j') #downleft
t.onkeypress(hk, 'h') #downright