import math
import time
from turtle import *

speed(0)
pensize(5)
tracer(50)
penup()
goto(0,0)
color("black")

screen = Screen()
width = screen.window_width()
height = screen.window_height()

C1 = None
C2 = None

def dibujar_linea(x1, y1, x2, y2):
    goto(x1, y1)
    pendown()
    goto(x2, y2)
    penup()
    

    ultima_posicion = [x2,y2]

    return ultima_posicion

#cara frontal
def cara():
    global C1
    dibujar_linea(C1[0][0],C1[0][1],C1[1][0],C1[1][1])
    dibujar_linea(C1[1][0],C1[1][1],C1[2][0],C1[2][1])
    dibujar_linea(C1[2][0],C1[2][1],C1[3][0],C1[3][1])
    dibujar_linea(C1[3][0],C1[3][1],C1[0][0],C1[0][1])
#cara trasera
def cara_2():
    global C2
    dibujar_linea(C2[0][0],C2[0][1],C2[1][0],C2[1][1])
    dibujar_linea(C2[1][0],C2[1][1],C2[2][0],C2[2][1])
    dibujar_linea(C2[2][0],C2[2][1],C2[3][0],C2[3][1])
    dibujar_linea(C2[3][0],C2[3][1],C2[0][0],C2[0][1])



def vertice_frontal(x,y,t):
    global C1
    C1 = [
        [x+t/2,y+t/2],#veritce 1
        [x+t/2,y-t/2],#vertice 2
        [x-t/2,y-t/2],#veritce 3
        [x-t/2,y+t/2]#vertice 4
    ]
def vertice_tracero(x,y,t):
        global C2
        C2 = [
        [x+t/2,y+t/2],#veritce 1
        [x+t/2,y-t/2],#vertice 2
        [x-t/2,y-t/2],#veritce 3
        [x-t/2,y+t/2]#vertice 4
    ]

def vertice_techo(x,y,t):
     global C1
     C1 = [
        [x+t/2,y+t/2],#veritce 1
        [x+t/2,y-t/2],#vertice 2
        [x-t/2,y-t/2],#veritce 3
        [x-t/2,y+t/2]#vertice 4
     ]

def vertice_base():
     global C1
     global C2

     for i in range(0,4):
        dibujar_linea(C1[i][0],C1[i][1],C2[i][0],C2[i][1])

#calcular nuevas coordenadas después de la rotación
def rotar_puntos(cx, cy, angulo,c):
    rad = angulo*(math.pi/180) #convertir a radian

    for rows in range(4):
         x_inicial = c[rows][0]-cx
         y_inicial = c[rows][1]-cy

         x_nuevo =  x_inicial*math.cos(angulo) - y_inicial*math.sin(angulo)+cx
         y_nuevo =  x_inicial*math.sin(angulo) + y_inicial*math.cos(angulo)+cy
         
         c[rows] = [x_nuevo,y_nuevo]


def dibujar_cubo():
     global C1,C2
     
     angulo_inicial=1

     angulo_inicial += 1

     rotar_puntos(x,y,angulo_inicial,C1)
     cara()

     rotar_puntos(x+t/2,y+t/2,angulo_inicial,C2)
     cara_2()

     vertice_base()
     
     #actualizar pantalla
     update()

     #ajustar la velocidad
     time.sleep(0.09)



x,y,t = 0,0,200
vertice_frontal(x,y,t)
vertice_tracero(x+t/2,y+t/2,t)

angulo_inicial = 1

def movimiento(pendiente_x=1,pendiente_y=0):
     global x,y

     x += pendiente_x * 10
     y += pendiente_y * 10

     if x > width / 2 - 100:
        x = width / 2 - 100
     elif x < -width / 2 + 100:
        x = -width / 2 + 100

     if y > height / 2 - 100:
        y = height / 2 - 100
     elif y < -height / 2 + 100:
        y = -height / 2 + 100



direccion_x = 1
direccion_y = 1
lim = True

while True:
     clear()
     dibujar_cubo()
     
     if(x >=width/2-100 and lim):
          direccion_x = -1
          lim = False
     if (x<=-width/2+100 and not lim):
          direccion_x = 1
          lim = True
     if (y>=height/2-100 and lim):
          direccion_y = -1
          lim = False
     if (y<=-height/2+100 and not lim):
          direccion_y = 1
          lim = True
     movimiento(direccion_x,direccion_y)
     

done()