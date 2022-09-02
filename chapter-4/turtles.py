import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

for i in [0, 1, 2, 3]:
  crush.forward(90)
  crush.right(90)

  
#create second turtle

squirt = turtle.Turtle()

for i in [0, 1, 2]:
  squirt.forward(90)
  squrt.right(45)


wn.exitonclick()
wn.mainloop()


