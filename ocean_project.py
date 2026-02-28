#ocean project

import turtle
import random
alex = turtle.Turtle()
alex.speed(0)
alex.shape("turtle")
screen = turtle.Screen()
screen.bgcolor("#6fd8dc")

# ocean background 
def stripe(alex, y, color, size):
    alex.penup()
    alex.goto(-350, y)
    alex.pendown()
    alex.color(color)
    alex.pensize(size)
    alex.goto(350, y)

stripe(alex, 250, "#5ab9d1", 100)       # differemt shades of blue to create a gradient effect
stripe(alex, 100, "#3d8ed2", 200)
stripe(alex, -65, "#3E72D2", 200)
stripe(alex, -270, "#3D6AC6", 250)


# sand 

sandy = turtle.Turtle()
sandy.shape("turtle")
sandy.color("#fbe3bc")
sandy.penup()
sandy.goto(-350, -350)
sandy.pendown()
sandy.pensize(70)
sandy.goto(350, -350)

sandy.pensize(1) 
sandy.speed(0)

# rocks

rocky = turtle.Turtle()
rocky.shape("circle")
rocky.penup()
rocky.hideturtle()
rocky.speed(0)

rock_colors = [
    "#4e5166",
    "#7c90a0",
    "#b5aa9d",
    "#b9b7a7",
    "#747274"
]

for i in range(20):

    x = random.randint(-320, 320)       # rocks are randomly placed across the ocean floor
    y = random.randint(-340, -300)

    rocky.goto(x, y)

    rocky.color(random.choice(rock_colors))     # rocks are randomly colored from the rock_colors list

    rocky.shapesize(
        random.uniform(0.8, 2),       # height between 0.8 and 2 
        random.uniform(1.5, 3)         # width between 1.5 and 3
    )

    rocky.stamp()

#seaweed

sweedy = turtle.Turtle()
sweedy.shape("turtle")
sweedy.color("#2e8b57")
sweedy.penup()
sweedy.goto(-300, -350)
sweedy.pendown()
sweedy.pensize(17)  
sweedy.goto(-300, -270)         # squiggly seaweed left
sweedy.forward(40)
sweedy.left(90)
sweedy.forward(40)
sweedy.left(90)
sweedy.forward(30)
sweedy.right(90)
sweedy.forward(30)

sweedy.penup()                 # straight seaweed large left
sweedy.goto(-350, -350)            
sweedy.pendown()
sweedy.goto(-350, -270)
sweedy.forward(100)

sweedy.penup()               # straight seaweed small left
sweedy.goto(-230, -350)
sweedy.pendown()
sweedy.goto(-230, -275)

sweedy.penup()               # squiggly seaweed right
sweedy.goto(300, -350)
sweedy.pendown()
sweedy.goto(300, -270)
sweedy.forward(30)
sweedy.left(90)
sweedy.forward(40)
sweedy.right(90)
sweedy.forward(30)
sweedy.right(90)
sweedy.forward(30)
sweedy.left(90)
sweedy.forward(30)

sweedy.penup()               # straight seaweed large right
sweedy.goto(250, -350)
sweedy.pendown()
sweedy.goto(250, -275)

sweedy.penup()
sweedy.goto(340, -350)       # straight seaweed small right
sweedy.pendown()
sweedy.goto(340, -230)

sweedy.hideturtle()
alex.hideturtle()
sandy.hideturtle()
sweedy.hideturtle()

# starfish

star = turtle.Turtle()
star.hideturtle()
star.speed(0)
star.penup()
star.pensize(8)

def draw_starfish(star, x, y, size=25, color= "#f05895"):
    star.penup()
    star.goto(x, y)
    star.setheading(0)
    star.color(color)
    star.pendown()

    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.goto(x, y)  
    star.end_fill()

    star.penup()

draw_starfish(star, -150, -330, size=30, color="#f05895")
draw_starfish(star, 100, -320, size=20, color="#f9a1c1")
draw_starfish(star, 200, -310, size=25, color="#e2629a") 
draw_starfish(star, -250, -300, size=15, color="#f27582")
draw_starfish(star, 50, -290, size=35, color="#f27582")

# bubbles

bub = turtle.Turtle()
bub.speed(0)
bub.shape("circle")
bub.penup()
bub.hideturtle()

bubble_colors = [
    "#e7eff1",
    "#caf0f1",
    "#c3edef",
    "#b0e1ef",
    "#b8e9ed"
]

for i in range(40):

    x = random.randint(-350, 350)
    y = random.randint(-270, 350)

    bub.goto(x, y)

    bub.color(random.choice(bubble_colors))    # bubbles are randomly colored from the bubble_colors list

    size = random.uniform(0.3, 0.7)   # small circles
    bub.shapesize(size, size)

    bub.stamp()

# fish

fish = turtle.Turtle()
fish.speed(0)
fish.pensize(2)
fish.hideturtle()

fish_colors = ["#e85b26", "#ee9c80", "#f9b6b6","#ffcc00","#f5ff69", "#ecb172", "#d05f4c"]


def draw_fish(fish, body_height=4, tail_len=12):

    fish.setheading(0)   
    start_x, start_y = fish.pos()

    # tail
    fish.begin_fill()
    fish.setheading(180)     
    fish.forward(tail_len)
    fish.left(120)
    fish.forward(tail_len)
    fish.left(120)
    fish.forward(tail_len)
    fish.end_fill()

    # Move fish to the right of the tail to start drawing the body
    fish.penup()
    fish.goto(start_x + 5, start_y)
    fish.setheading(0)
    fish.pendown()

    # body
    fish.begin_fill()
    fish.circle(body_height, 180)
    fish.circle(body_height, 180)
    fish.end_fill()

    fish.penup()
    fish.goto(start_x, start_y)
    fish.setheading(0)

    # eye
    fish.penup()
    fish.goto(start_x + body_height * 1.1, start_y + body_height * 1.0)
    fish.dot(4, "black")


# draw many fish
fish.penup()

for _ in range(30):
    fish.goto(random.randint(-300, 300), random.randint(-150, 200))
    fish.color(random.choice(fish_colors))
    fish.pendown()
    draw_fish(fish, body_height=random.randint(8,9), tail_len=random.randint(14, 16))
    fish.penup()

# hide turtles 
alex.hideturtle()
sandy.hideturtle()
sweedy.hideturtle()
fish.hideturtle()


turtle.done()