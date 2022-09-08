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

wn.exitonclick()
wn.mainloop()

#documentation screen is useful for organization. 
#comment requires you to added new "#" every time you go to a new line
#doc screen doesn't. 

"""


"""