import turtle
wn = turtle.Screen()
crush = turtle.Turtle

#define function "square". However, not used. 
def square(t):
  #draws a square
  for i in range(4):
    t.foward(50)
    t.right(90)

#use function
square(crush)

squirt = turtle.Turtle()
squirt.penup()
squirt.goto(100,100)
squirt.pendown
squirt.color("red")
squirt.width(5)
square(squirt)

wn.exitonclick()
wn.mainloop()