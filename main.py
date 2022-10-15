import math
import turtle
turtle.shape('turtle')
turtle.left(90)
turtle.speed(10)
def f (g):
    turtle.forward(g)
def b (h):
    turtle.backward(h)
def l (c):
    turtle.left(c)
def r (c):
    turtle.right(c)
def pu ():
    turtle.penup()
def pd ():
    turtle.pendown()
def sp(x):
    for i in range(x):
        r(90)
        pu()
        f(50)
        pd()
        l(90)
def crd(a, b):
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.goto(x + a, y + b)
def nach ():
    pu()
    f(200)
    l(90)
    f(500)
    pd()
    r(90)
def nW ():
    pu()
    turtle.home()
    l(180)
    f(500)
    l(90)
    f(200)
    l(180)
    pd()

def A ():
    f(200)
    r(90)
    f(100)
    r(90)
    f(200)
    b(100)
    r(90)
    f(100)
    l(90)
    f(100)
    l(180)
    sp(3)
def B ():
    f(200)
    r(90)
    f(100)
    l(90)
    pu()
    b(100)
    pd()
    for i in range(4):
        b(100)
        r(90)
    b(100)
def V ():
    f(200)
    b(200)
    r(90)
    f(90)
    l(45)
    f(10 * math.sqrt(2))
    l(45)
    f(80)
    l(45)
    f(10 * math.sqrt(2))
    l(45)
    f(90)
    r(90)
    r(90)
    f(90)
    l(45)
    f(10 * math.sqrt(2))
    l(45)
    f(80)
    l(45)
    f(10 * math.sqrt(2))
    l(45)
    f(90)
    r(90)
    b(200)
    sp(3)
def G ():
    f(200)
    r(90)
    f(100)
    l(90)
    pu()
    b(200)
    pd()
    sp(1)
def D ():
    pu()
    l(90)
    f(25)
    r(90)
    pd()
    f(25)
    r(90)
    f(150)
    r(90)
    f(25)
    b(25)
    r(90)
    f(25)
    r(90)
    f(175)
    l(90)
    f(100)
    l(90)
    f(175)
    r(180)
    pu()
    crd(175, -25)
    pd()
def E ():
    f(200)
    b(200)
    for i in range(3):
        r(90)
        f(100)
        b(100)
        l(90)
        pu()
        f(100)
        pd()
    pu()
    b(300)
    pd()
    sp(3)
def IO ():
    b(200)
    for i in range(3):
        r(90)
        f(100)
        b(100)
        l(90)
        pu()
        f(100)
        pd()
    pu()
    b(100)
    f(25)
    r(90)
    f(20)
    pd()
    for g in range(2):
        f(20)
        l(90)
        f(1)
        l(90)
        f(20)
        r(90)
        f(1)

        r(90)
        pu()
        f(40)
        r(90)
        f(2)
        l(90)
        pd()
    l(90)
    pu()
    b(25)
    crd(100, -200)
def J ():
    crd(25, 100)
    crd(-25, 100)
    crd(25, -100)
    r(90)
    f(50)
    l(90)
    f(100)
    b(200)
    f(100)
    r(90)
    f(50)
    l(90)
    crd(25, 100)
    crd(-25, -100)
    crd(25, -100)
    sp(1)
def Z ():
    r(90)
    f(90)
    l(45)
    f(10 * math.sqrt(2))
    l(45)
    f(80)
    l(45)
    f(10 * math.sqrt(2))
    l(45)
    f(90)
    r(90)
    r(90)
    f(90)
    l(45)
    f(10 * math.sqrt(2))
    l(45)
    f(80)
    l(45)
    f(10 * math.sqrt(2))
    l(45)
    f(90)
    r(90)
    pu()
    crd(150, -200)
    pd()
def I ():
    f(200)
    b(200)
    crd(100, 200)
    b(200)
    sp(1)
def IK ():
    f(200)
    b(200)
    crd(100, 200)
    b(200)
    pu()
    crd(-20, 225)
    l(90)
    pd()
    f(60)
    r(90)
    f(1)
    r(90)
    f(60)
    pu()
    crd(70, -225)
    l(90)
def K ():
    f(200)
    b(100)
    crd(100, 100)
    crd(-100, -100)
    crd(100, -100)
    sp(1)
def L ():
    f(200)
    b(200)
    l(90)
    f(25)
    b(25)
    r(90)
    f(200)
    r(90)
    f(100)
    r(90)
    f(200)
    l(180)
    sp(1)
def M ():
    f(200)
    crd(50, -100)
    crd(50, 100)
    b(200)
    sp(1)
def N ():
    f(200)
    b(100)
    r(90)
    f(100)
    l(90)
    f(100)
    b(200)
    sp(1)
def O ():
    for i in range(2):
        f(200)
        r(90)
        f(100)
        r(90)
    sp(3)
def P ():
    f(200)
    r(90)
    f(100)
    r(90)
    f(200)
    l(180)
    sp(1)
def R ():
    f(200)
    for i in range(4):
        r(90)
        f(100)
    pu()
    crd(150, -200)
    pd()
def S ():
    f(200)
    r(90)
    f(100)
    b(100)
    r(90)
    f(200)
    l(90)
    f(100)
    l(90)
    sp(1)
def T ():
    pu()
    crd(50, 0)
    pd()
    f(200)
    l(90)
    f(50)
    b(100)
    f(50)
    l(90)
    f(200)
    l(180)
    sp(2)
def Y ():
    crd(100, 200)
    pu()
    crd(-100, 0)
    pd()
    crd(50, -100)
    pu()
    crd(100, -100)
    pd()
def F ():
    r(90)
    f(75)
    b(75)
    l(90)
    f(200)
    r(90)
    f(150)
    r(90)
    f(200)
    r(90)
    f(75)
    r(90)
    f(240)
    b(280)
    f(40)
    sp(2)
def X ():
    crd(100, 200)
    pu()
    crd(-100, 0)
    pd()
    crd(100, -200)
    sp(1)
def TS ():
    f(200)
    b(200)
    r(90)
    f(100)
    l(90)
    f(200)
    b(200)
    r(90)
    f(30)
    r(90)
    f(30)
    b(30)
    l(90)
    b(30)
    l(90)
    sp(1)
def CH ():
    pu()
    f(100)
    pd()
    f(100)
    b(100)
    r(90)
    f(100)
    l(90)
    f(100)
    b(200)
    sp(1)
def SH ():
    f(200)
    b(200)
    r(90)
    f(75)
    l(90)
    f(200)
    b(200)
    r(90)
    f(75)
    l(90)
    f(200)
    b(200)
    sp(1)
def SH2 ():
    f(200)
    b(200)
    r(90)
    f(75)
    l(90)
    f(200)
    b(200)
    r(90)
    f(75)
    l(90)
    f(200)
    b(200)
    r(90)
    f(30)
    r(90)
    f(30)
    b(30)
    l(90)
    b(30)
    l(90)
    sp(1)
def tvZ():
    f(200)
    b(100)
    r(90)
    f(100)
    r(90)
    f(100)
    r(90)
    f(100)
    r(90)
    f(200)
    l(90)
    f(40)
    b(40)
    r(90)
    b(200)
    sp(3)
def YI():
    f(200)
    b(100)
    r(90)
    f(75)
    r(90)
    f(100)
    r(90)
    f(75)
    r(90)
    pu()
    crd(110, 0)
    pd()
    f(200)
    b(200)
    sp(1)
def myagZ ():
    f(200)
    b(100)
    r(90)
    f(100)
    r(90)
    f(100)
    r(90)
    f(100)
    r(90)
    sp(3)
def AE ():
    r(90)
    f(100)
    l(90)
    f(100)
    l(90)
    f(100)
    b(100)
    r(90)
    f(100)
    l(90)
    f(100)
    b(100)
    r(90)
    b(200)
    sp(1)
def U ():
    f(200)
    b(100)
    r(90)
    f(50)
    l(90)
    b(100)
    for i in range(2):
        f(200)
        r(90)
        f(100)
        r(90)
    sp(3)
def YA ():
    crd(100, 100)
    for i in range(4):
        f(100)
        l(90)
    b(100)
    sp(1)
nach()
# буквы
# P()
# I()
# T()
# O()
# N()
turtle.done()