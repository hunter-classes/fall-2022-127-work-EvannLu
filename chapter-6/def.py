import turtle


#define function "square". However, not used.
def square(t):
    #draws a square
  for i in range(4):
        t.forward(50)
        t.right(90)


wn = turtle.Screen()
crush = turtle.Turtle()

#use function
square(crush)

#second turtle
squirt = turtle.Turtle()

#move turtle to a new place
squirt.penup()
squirt.goto(100, 100)
squirt.pendown()
squirt.color("red")
squirt.width(5)
squirt.right(45)

square(squirt)


#Third

def square2(t,x,y,w,color,sidelen):

#documentation screen is useful for organization. 
#comment requires you to added new "#" every time you go to a new line
#doc screen doesn't. 
  
    """
    t - turtle
    x,y - location
    w - width
    color - color to draw in
    sidelen - length of each side
    return:
        nothing    
    """
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()

    for i in range(4):
        t.forward(50)
        t.right(90)
square2(crush,150,150,5,"blue",4)
squirt = turtle.Turtle()
squirt.penup()
squirt.goto(100,100)
squirt.pendown()
squirt.color("red")
squirt.width(5)
square(squirt)

wn.exitonclick()
wn.mainloop()
