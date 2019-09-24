#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
#create spider bofy
spider.pensize(40)
spider.circle(20)
#create spider body
spider.penup()
spider.goto(20,30)
spider.pendown()
spider.circle(5)
#create spider legs 
legs = 8
place = 70
angle = 360 / legs
spider.pensize(5)
number = 0
while (number < legs):
  spider.goto(0,20)
  spider.setheading(place*number-30/2)
  spider.setheading(place*number+30/2)
  spider.forward(place)
  number = number + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()