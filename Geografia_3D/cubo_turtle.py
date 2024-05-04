from turtle import *

def dibujar_linea(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)
    

    ultima_posicion = [x2,y2]

    return ultima_posicion

def dibujar_cubo(x, y,tam): #no existe aun el valor de z

    #cara lateral
    [x_final,y_final] = dibujar_linea(x,y,x+tam/2,y+tam/2)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final,y_final+tam)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final-tam/2,y_final-tam/2)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final,y_final-tam)

    #reposicionar 
    [x_final,y_final] = dibujar_linea(x_final,y_final,x-tam,y_final)
    #segunda cara lateral
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final,y_final+tam)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final+tam/2,y_final+tam/2)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final,y_final-tam)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final-tam/2,y_final-tam/2)

    #reposicionar
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final,y_final+tam)

    #cara superior e inferior
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final+tam,y_final)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final+tam/2,y_final+tam/2)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final-tam,y_final)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final,y_final-tam)
    [x_final,y_final] = dibujar_linea(x_final,y_final,x_final+tam,y_final)

dibujar_cubo(0,0,100)
dibujar_cubo(390,240,100)
dibujar_cubo(-390,240,100)
dibujar_cubo(-390,-240,100)
dibujar_cubo(390,-240,100)


done()