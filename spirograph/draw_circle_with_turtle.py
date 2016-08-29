def draw_circle_turtle(x, y, r):
    """Draws circle: positions pen, loop in steps of 5 degrees."""
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    for i in range(0, 365, 5):
        #convert from degrees(i) to radians(a)
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))


