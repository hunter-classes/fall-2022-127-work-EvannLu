import turtle
wn = turtle.Screen()
drunk = turtle.Turtle()

drunk.penup()
drunk.forward(60)
drunk.pendown()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    drunk.left(angle)
    drunk.forward(100)

#drunk.heading() gives the degree the drunk was facing at the end of the program
print("The pirate's final heading was", drunk.heading())

wn.exitonclick()