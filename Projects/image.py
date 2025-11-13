#this is my turtle 
import turtle 
turtle.Screen().bgcolor("pink")
t = turtle.Turtle()
t.speed(10)

#these are the colors i used 
t.goto(0,0)
colors = ["black","dark blue","crimson"]

#this is my design/directions
for i in range (150): 
    t.color(colors[ i % 3])

    t.forward (100)
    t.left (90) 
    t.forward (80)
    t.left (45) 
    t.forward (75)
    t.left (50)    
    t.forward (105)
    t.left (95) 
    t.forward (85)
    t.left (55) 
    t.forward (85)
    t.left (60)


turtle.exitonclick()