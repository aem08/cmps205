import sys,turtle 

user_order=int(sys.argv[1])
user_length=int(sys.argv[2])
turtle.speed(0)
def fractal(order,length):
    if order==0:
        turtle.forward(length)
    elif order==1:
        fractal(0,length/3)
        turtle.left(60)
        fractal(0,length/3)
        turtle.right(120)
        fractal(0,length/3)
        turtle.left(60)
        fractal(0,length/3)
    else:
        fractal(order-1,length/3)
        turtle.left(60)
        fractal(order-1,length/3)
        turtle.right(120)
        fractal(order-1,length/3)
        turtle.left(60)
        fractal(order-1,length/3)
        
def snowflake(order,length):
    fractal(order,length)
    turtle.right(120)
    fractal(order,length)
    turtle.right(120)
    fractal(order,length)

snowflake(user_order,user_length)
turtle.done()
