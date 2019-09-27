
# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 4
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 4 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  ladybug.penup()
  ladybug.goto(xpos - 1 , ypos + 25)
  ladybug.pendown()
  ladybug.circle(1)
  ladybug.penup()
  ladybug.goto(xpos + 35, ypos + 40)
  ladybug.pendown()
  ladybug.circle(4)
num_dots = num_dots + 1
  # position next dots
  ladybug.penup()

#make ladybug legs 
w = 6
y = 70
z = 360 / w
x.pensize(5)
n = 0
while (n < w):
  ladybug.goto(0,0)
  ladybug.setheading(z*n)
  ladybug.forward(y)
  n = n + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()