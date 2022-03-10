import turtle

def clicked(x,y): 
    print("Clicked!")
    t.speed(0)
    t.pu()
    t.goto(x,y)
    t.write(str(x)+","+str(y))

def tangentcircles(t,number_of_circles=10,fit_to_window=True, color=True):
    t.goto(0,-screen.window_height()/2)
    r = 8
    t.hideturtle()
    t.down()
    colors = ["green","violet"]
    colindex = 0 
    for i in range(1,number_of_circles+1,1): 
        colindex %= len(colors)
        t.circle(r * i)
        if color: 
            colindex += 1
            t.color(colors[colindex-1])
        if fit_to_window:
            if ((r*i) == (screen.window_height()/2)):  
                break 

def cocentriccircles(t,number_of_circles:50):
    for i in range(50):
        t.circle(r * i)
        t.up()
        t.sety((r * i)*(-1))
        t.down()

def spiralcircles(t,number_of_circles=20, fit_to_window=True,color=False):
    t.color("white")
    r = 10
    t.hideturtle()
    t.down()
    for i in range(1,number_of_circles+1,1):
        t.circle(r+i,45)
        ''' 
        if fit_to_window: 
            if ((r +1) == (screen.window_height()/2)):
                return
        ''' 


t = turtle.Turtle()
t.hideturtle()
#t.up()
screen = turtle.getscreen()
print(f"{screen.window_width()},{screen.window_height()}")
screen.bgcolor("black")
t.color("White")
t.fd(100)
screen.onclick(clicked)
screen.mainloop()
