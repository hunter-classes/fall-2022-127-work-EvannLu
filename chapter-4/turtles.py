#set up alex
import turtle           
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2]:
  alex.forward(80)
  alex.left(120)

#repeat four times
for i in [0, 1, 2, 3]:      
    alex.forward(50)
    alex.left(90)

#create second turtle
squirt = turtle.Turtle()

for i in [0, 1, 2]:
    squirt.forward(90)
    squirt.right(45)

wn.exitonclick()
wn.mainloop()
