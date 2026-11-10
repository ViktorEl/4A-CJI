import turtle

pero = turtle.Turtle()
canvas = turtle.Screen()

# základna domu
pero.color('blue')
pero.fillcolor('blue')
pero.begin_fill()
pero.forward(100)
pero.left(90)
pero.forward(100)
pero.left(90)
pero.forward(100)
pero.left(90)
pero.forward(100)
pero.end_fill()

# strecha
pero.back(100)
pero.left(90)
pero.color('red')
pero.fillcolor('red')
pero.begin_fill()

pero.forward(100)
pero.left(120)
pero.forward(100)
pero.left(120)
pero.forward(100)
pero.end_fill()

pero.color('blue')
pero.left(30)
pero.forward(100)
pero.left(90)



canvas.mainloop()







