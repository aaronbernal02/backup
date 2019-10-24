from turtle import *

myTurtle = Turtle()
screen = myTurtle.getscreen()
myTurtle.forward(200)

def printname():
	name = screen.textinput("name", "What is your name?")
	myTurtle.write(name, move=True, align="Left", font=("Ariel", 40, "normal"))
	screen.listen()

def goForward():
    myTurtle.forward(10)

screen.onkey(printname, "p")	

screen.listen()
screen.mainloop()
