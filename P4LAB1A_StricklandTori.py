import turtle
wn = turtle.Screen()         
wn.bgcolor("lightblue")
wn.title("Tori & Trent")

tori = turtle.Turtle()       
tori.color("purple")
tori.pensize(5)

trent = turtle.Turtle()       

tori.forward(80)             
tori.left(120)
tori.forward(80)
tori.left(120)
tori.forward(80)
tori.left(120)               

tori.right(180)              
tori.forward(80)             

trent.forward(50)            
trent.left(90)
trent.forward(50)
trent.left(90)
trent.forward(50)
trent.left(90)
trent.forward(50)
trent.left(90)

wn.mainloop()




