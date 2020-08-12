import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    cube = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    cube.shape("turtle")
    # Set your turtle's speed using .speed(2)
    cube.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    cube.color('green')

    cube.shapesize(10)

    # Move your turtle forward using .forward(100)
    cube.forward(100)
    # TEST    Did your turtle move forward?
    
    # Move your turtle left or right using .left(90) or .right(90)
    cube.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    for i in range(4):
        cube.left(90)
        cube.forward(100)

    # TEST    Did your turtle draw a square?
        
    # Move your turtle to a new place on the screen using .goto(x, y)
    cube.goto(90,50)
    # x=0 and y=0 is the center of the screen
    cube.begin_fill()
    # Have your turtle draw a circle using .circle(radius, steps=30)
    cube.circle(radius=100, steps=30)
    # TEST    Did your turtle draw a circle?
    
    # Add color to your shape by adding .begin_fill() before drawing the circle

    # and .end_fill() below
    cube.end_fill()
    # Draw 3 more shapes with different fill colors!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
