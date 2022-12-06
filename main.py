import random
import turtle
turtle.colormode(255)

import colorgram
# Extract 6 colors from an image.
# colors = colorgram.extract('img.png', 25)
# #print(colors)
#
# my_rgb_colors = []
# for i in colors:
#     color = (i.rgb.r, i.rgb.g, i.rgb.b)
#     my_rgb_colors.append(color)

# print(my_rgb_colors)

color_list = [(195, 163, 118), (121, 37, 31), (167, 188, 158), (48, 96, 118), (177, 88, 58), (169, 152, 30), (123, 33, 41),
 (60, 41, 42), (118, 161, 173), (106, 78, 89), (65, 135, 107), (32, 62, 46), (58, 42, 41), (22, 71, 90), (191, 96, 69),
 (24, 75, 94), (179, 149, 153), (215, 196, 118), (106, 149, 72), (181, 200, 177), (211, 183, 178)]


tommy = turtle.Turtle()
turtle.colormode(255)
tommy.penup()
tommy.shape("turtle")
tommy.setx(-200)
tommy.sety(-200)
tommy.hideturtle()

for i in range(10):
    for j in range(10):
        tommy.dot(30, random.choice(color_list))
        tommy.forward(50)
    tommy.setheading(90)
    tommy.forward(50)
    tommy.setheading(180)
    tommy.forward(10 * 50)
    tommy.setheading(0)




screen = turtle.Screen()
screen.exitonclick()