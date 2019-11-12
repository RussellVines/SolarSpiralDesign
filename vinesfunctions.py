import turtle

bob=turtle.Turtle()
turtle.bgcolor("black")
turtle.colormode(255)
bob.speed(0)


def square(distance):
    for times in range(4):
        bob.forward(distance)
        bob.left(90)

def triangle(distance):
    for times in range(3):
        bob.forward(distance)
        bob.left(120)

def pentagon(distance):
    for times in range(5):
        bob.forward(distance)
        bob.left(72)
    
def hexagon(distance):
    for times in range(6):
        bob.forward(distance)
        bob.left(60)
    
def octagon(distance):
    for times in range(8):
        bob.forward(distance)
        bob.left(45)
        

def decagon(distance):
    for times in range(10):
        bob.forward(distance)
        bob.left(36)

def polygon(sides,distance,c):
    bob.color(c)
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()  

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance,color,width):
    bob.color(color)
    bob.width(width)
    bob.begin_fill()
    for times in range(5):
        bob.left(144)
        bob.forward(distance)
    bob.end_fill()

def explosion(distance,color):
    bob.color(color)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.left(135)
    bob.end_fill()

def figure1(distance,size,color):
    bob.color(color)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()

    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    
    
def monster(color):
    bob.color(color)

    bob.begin_fill()
    bob.left(90)
    bob.forward(100)
    bob.circle(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(135)
    bob.forward(25)
    bob.right(90)
    bob.forward(25)
    bob.left(90)
    bob.forward(25)
    bob.right(90)
    bob.forward(25)
    bob.left(90)
    bob.forward(25)
    bob.right(90)
    bob.forward(25)
    bob.end_fill()

def fadingtriangle():
    turtle.tracer(False)
    for times in range(50):
        c= (250 - times * 5, 250 - times *5, 0)
        polygon(3, 250 - times * 8, c)
    turtle.tracer(True)

def tile():
    for times in range(4):
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        bob.left(90)

    bob.left(180)
    
    for times in range(4):
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        bob.left(90)
        
    bob.left(90)

    for times in range(4):
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        bob.left(90)

    bob.right(180)

    for times in range(4):
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        bob.left(90)

def rowtile(c):
    for times in range(4):
        bob.forward(8)
        tile(c)
        bob.forward(200)


def spike(distance):
    for times in range (20):
        bob.width(times*1.05)
        bob.forward(distance)
        bob.left(10)

def spike9(distance):
    for times in range(11):
        c= times * 12
        bob.color(0,c,c)
        bob.width(times*1.05)
        bob.forward(distance)
        bob.left(10)

def spikeflower(distance):
    turtle.tracer(False)
    for times in range(11):
        c= times * 20
        bob.color(0,c,c)
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 37)
    turtle.tracer(True)

def design1():
    turtle.tracer(False)
    for times in range(5):
        spikeflower(times*4)
        bob.right(180)
    turtle.tracer(True)

def spikeflower4(distance):
    turtle.tracer(False)
    for times in range(11):
        c= times * 20
        bob.color(0,c,c)
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 40)
    turtle.tracer(True)

def spikeflower3(distance):
    turtle.tracer(False)
    for times in range(11):
        c= times * 20
        bob.color(0,0,c)
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 36)
    turtle.tracer(True)

def spikeflower5(distance):
    turtle.tracer(False)
    for times in range(11):
        c= times * 20
        bob.color(c,c,0)
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 45)
    turtle.tracer(True)



def spike2(distance):
    for times in range (25):
        bob.width(3)
        bob.forward(distance)
        bob.left(21)

def spike3(distance):
    turtle.tracer(False)
    for times in range(11):
        c= times * 20
        bob.color(0,c,c)
        spike(distance)
        bob.penup()
        jump(100,100)
        bob.pendown()
        bob.left(times * 36)
    turtle.tracer(True)




def spike4(distance):
    turtle.tracer(False)
    for times in range(11):
        c= times * 20
        bob.color(0,c,c)
        spike(distance)
        bob.penup()
        jump(-100,100)
        bob.pendown()
        bob.left(times * 36)
    turtle.tracer(True)


def spike5(distance):
    turtle.tracer(False)
    for times in range(11):
        c= times * 20
        bob.color(0,c,c)
        spike(distance)
        bob.penup()
        jump(100,-100)
        bob.pendown()
        bob.left(times * 36)
    turtle.tracer(True)

def spike6(distance):
    turtle.tracer(False)
    for times in range(11):
        c= times * 20
        bob.color(0,c,c)
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 36)
    turtle.tracer(True)


def spiral1():
    colors=["red","green","blue","yellow","purple","orange","aquamarine","indigo","violet"]

    turtle.tracer(False)
    for times in range (251) :
        bob.pencolor(colors[times%9])
        bob.width(times/100)
        bob.forward(times*1.05)
        bob.left(59)
    turtle.tracer(True)
    
def flower(distance):
    turtle.tracer(False)
    for times in range(15):
        c= times * 18
        bob.color(0,c,0)
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 45)

def flower2(distance):
    colors=["red", "purple", "blue", "green", "orange", "yellow"]
    turtle.tracer(False)
    for times in range(15):
        bob.pencolor(colors[times%6])
        c= times * 18
        bob.color(0,c,0)
        spike(distance)
        bob.penup()
        jump(200,200)
        bob.pendown()
        bob.left(times * 45)
        
def flower3(distance):
    colors=["red", "purple", "blue", "green", "orange", "yellow"]
    turtle.tracer(False)
    for times in range(15):
        bob.pencolor(colors[times%6])
        c= times * 18
        bob.color(0,c,0)
        spike(distance)
        bob.penup()
        jump(200,-200)
        bob.pendown()
        bob.left(times * 45)

def flower4(distance):
    colors=["red", "purple", "blue", "green", "orange", "yellow"]
    turtle.tracer(False)
    for times in range(15):
        bob.pencolor(colors[times%6])
        c= times * 18
        bob.color(0,c,0)
        spike(distance)
        bob.penup()
        jump(-200,-200)
        bob.pendown()
        bob.left(times * 45)

def flower5(distance):
    colors=["red", "purple", "blue", "green", "orange", "yellow"]
    turtle.tracer(False)
    for times in range(15):
        bob.pencolor(colors[times%6])
        c= times * 18
        bob.color(0,c,0)
        spike(distance)
        bob.penup()
        jump(-200,200)
        bob.pendown()
        bob.left(times * 45)

def circleLoop():
    for times in range(25):
        bob.color("red")
        bob.circle(times+2)
        bob.penup()
        bob.forward(10)
        bob.pendown()

def circlespiral():
    turtle.tracer(False)
    bob.color("red")
    bob.width(2)
    for times in range(20):
        bob.goto(0,0)
        spike9(40)
        spike9(30)
    turtle.tracer(True)
