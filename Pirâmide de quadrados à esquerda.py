import turtle

a = turtle.Screen()
turtle.speed(0)

def quadrado(posx, posy, lado):
    turtle.showturtle()
    # posiciona
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    # desenha

    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
        turtle.hideturtle()

# Normal
# Esquerda
def pir_esquerda(n,posx, posy,lado):
    for i in range(1,n+1):
       # desenha coluna i
       # posiciona
       turtle.penup()
       turtle.goto(posx - (n-i)*lado,posy+(n-i)*lado/2)
       turtle.pendown()

       # desenha

       for j in range(1,i+1):
           quadrado(turtle.xcor(),turtle.ycor(), lado)
           turtle.sety(turtle.ycor()+lado)
           turtle.hideturtle()

quadrado(350, -300, 50)
pir_esquerda(12, 350, -300, 50)
a.exitonclick()