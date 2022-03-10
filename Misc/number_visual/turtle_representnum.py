import random 
from turtle import *
''' Using turtle to represent lists and sort them
Note: 
    - We only care about the relative differences between number (no need to display values)
    - Get help with a function, ie. help(generate_random_list)
    - global variables: unsortedlist, forwardlist, backwardlist, sortedlist, t, screen
TODO: 
    - Fix bug when switching from drawing circle to bar
    - Scale the numbers with the screen (?)
    - Have a "sub window for drawing" within the window 
        - Turtle draws border 
        - Barcharts dont go beyond the height of it
        - (idea) Numbers can scale
    - Menu for setting parameters of graphs (need more Tkinter?)
        - Part of top-lvl menu
        - color, bottom_line_color, speed_number, shape, visible turtle, border
''' 

t = None 
screen = None 

def bubble_sort(alist):
    """ Bubble sort a list (lowest->greatest)
    """ 
    modlist = alist.copy() # if we use alist, we will modify the list we pass through
    for i in range(len(modlist)-1,0,-1):
        for j in range(i):
            if modlist[j] > modlist[j + 1]:
                temp = modlist[j] # swap 
                modlist[j] = modlist[j + 1]
                modlist[j + 1] = temp
    print("Bubble ran") 
    return(modlist)
                
def generate_random_list(size=10,numrange=10):
    """ Generate a random list 
    Note: If the `size` or `numrange` isn't passed in, we use a default of 10 
    """
    random_list = []
    for num in range(size): 
        random_list.append(random.randint(1,numrange))
    print(random_list)
    return(random_list)

def generate_circlelines(numlist, color="White", ends=False): 
    """ Shows a circle-line representation of the numbers 
    """ 
    t.penup()
    t.color(color)
    t.speed(0) # fastest
    spacing = 360/len(numlist) # angles
    track = 0
    home = (0,0) 
    for num in numlist:
        t.goto(home) # 0,0
        t.pendown()
        t.setheading(spacing*track)
        t.forward(num*40) 
        if ends: 
            t.stamp()
        track += 1 
    t.penup()

def generate_barchart_drawing(
                                home, numlist, bottom_line=False,
                                color="White", bottom_line_color="White",
                                speed_number=10, ends=False): 
    """ Shows a barchart representation of the numbers 
    """ 
    t.penup()
    spacing = 25 
    track = 0 # cant use list index because values arent necessarily unique 
    t.goto(home)
    t.speed(speed_number)
    t.pencolor(color) 
    for num in numlist:
        t.forward(track * spacing)
        t.left(90)
        t.pendown()
        t.forward(num*100)
        if ends:
            t.stamp()
        t.penup()
        t.goto(home)
        t.setheading(0)
        track += 1
    if bottom_line:
        t.goto(home) 
        t.pencolor(bottom_line_color)
        t.pendown()
        t.forward(len(numlist) * spacing)
    t.penup()

def generate_menu() -> None: 
    """ Draws a menu that we can use to interact with
    """
    global unsortedlist, forwardlist, backwardlist, sortedlist, screen
    home =(-screen.window_width()/2, -screen.window_height()/4) # bottom left of screen
    rainbow = ["red", "orange", "yellow", "green", "blue", "violet"] # unicorn specs
    col_index = 0 
    interactive = True
    while interactive:
        t.penup()
        col_index %= len(rainbow)
        prompt = "Choice:\n(1) Barchart\n(2) Circlelines\n(3) Clear screen\n(4) Quit program\n"
        topchoice = textinput("Chart Selection", prompt)
        if topchoice == "1":
            choice = textinput("Barchart", "Generate barchart? ([yes|no])\n").lower()
            if choice in ['y','yes']: 
                inputnumber = int(numinput("User Input", "Size of list: ", 10,
                                    minval=1, maxval=40))
                unsortedlist = generate_random_list(inputnumber)
                generate_barchart_drawing(home, unsortedlist, color=rainbow[col_index])
                col_index += 1 
                generate_barchart_drawing(home, bubble_sort(unsortedlist))
                col_index += 1
        if topchoice == "2":
            choice = textinput("Circlelines", "Generate circlelines? ([yes|no])\n").lower()
            if choice in ['y','yes']: 
                inputnumber = int(numinput("User Input", "Size of list: ", 10, minval=1, maxval=500))
                numrange = int(numinput("User Input", "Number range: ", 10, minval=1, maxval=30))
                unsortedlist = generate_random_list(inputnumber,numrange)
                generate_circlelines(unsortedlist, color=rainbow[col_index])
                col_index += 1
                generate_circlelines(bubble_sort(unsortedlist), color=rainbow[col_index])
                col_index += 1
        if topchoice == "3": 
            screen.clear()
            screen.bgcolor("Black")
        if topchoice is None or topchoice in ['n','no','4']: 
            interactive = False

if __name__ == "__main__":
    screen = Screen() # screen size determied by current canvas width & height
    screen.bgcolor("Black")
    title("Representing sorting numbers with turtle")
    t = Turtle()
    t.pen(pencolor="orange", speed=10, fillcolor="orange", pensize=4, shown=False, pendown=False)
    t.shape("arrow") # turtle, arrow, circle, classic, triangle, square
    generate_menu() 
    screen.mainloop()