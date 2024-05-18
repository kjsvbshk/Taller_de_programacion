from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app= Ursina()
jugador = FirstPersonController(position=(5,0,10))

class Escenario_3D(Button):
    def __init__(self,position=(0,0,0),escala=(10,10),textura='white_cube'):
        super().__init__(
            position = position,
            parent = scene,
            model = 'cube',
            origin_y = 0.5,
            collider = 'box',
            texture = textura,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = escala
        )

class mano(Entity):
    #posicion armas x y 
    x_inicio = 0
    y_inicio = -0.4
    image_speed = 0.4
    image_index = 0#imagen estatica

    textura_mano = Texture('assets/arma.png')
    def __init__(self):
        super().__init__(            
            parent = camera.ui,
            model = 'cube',
            texture = self.textura_mano,
            scale = (0.7,0.7),
            color = color.white,
            rotation = Vec3(0,0,0),#mover arma
            position = Vec2(self.x_inicio,self.y_inicio),#posicion x,y
            )

        
nivel = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 2, 2, 2, 5, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0 ],
    [0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 5, 2, 2, 2, 2, 5, 0, 6, 3, 3, 3, 6, 0, 0, 0, 0 ],
    [0, 0, 0, 4, 1, 1, 1, 4, 4, 4, 5, 2, 2, 2, 2, 5, 0, 6, 3, 3, 3, 6, 0, 0, 0, 0 ],
    [0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 4, 6, 3, 3, 3, 6, 0, 0, 0, 0 ],
    [0, 0, 0, 4, 1, 1, 1, 4, 4, 4, 5, 2, 2, 2, 2, 5, 1, 6, 3, 3, 3, 6, 0, 0, 0, 0 ],
    [0, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 6, 3, 6, 5, 5, 5, 5, 5 ],
    [4, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 5 ],
    [4, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 5 ],
    [4, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 5 ],
    [4, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 5 ],
    [4, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 5 ],
    [4, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 5 ],
    [0, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1, 4, 4, 4, 5, 5, 2, 5, 5, 5, 5, 5, 5 ],
    [0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 0, 0, 0, 0 ],
    [0, 0, 0, 4, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 2, 2, 2, 5, 0, 0, 0, 0 ],
    [0, 0, 0, 4, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 2, 2, 5, 0, 0, 0, 0 ],
    [0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 2, 2, 5, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
]

techo = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
]

def crear_mapa(nivel1,nivel2):
    largo = len(nivel1)
    ancho = len(nivel1[0])
    #crear espacio
    for i in range(largo):
        piso = nivel1[i]
        nivel = nivel2[i]
        for j in range(ancho):
        #crear el suelo y techo
            if piso[j] == 0:
                #crear techo 
                Escenario_3D(position=(j,8,i),escala=(1,1),textura='assets/lava2.jpg')
                #crear suelo
                Escenario_3D(position=(j,0,i),escala=(1,1),textura='assets/suelo2.jpg')
        #crear paredes
            if piso[j] > 0:
                #crear pared a la altula correspondiente
                Escenario_3D(position=(j,piso[j],i),escala=(1,piso[j]))
            if nivel[j]>0:
                #crear pared a la altula correspondiente
                Escenario_3D(position=(j,piso[j]+nivel[j],i),escala=(1,nivel[j]),textura='sala.jpg')
                # if j ==0 or j ==ancho-1 or i ==0 or i==largo-1:
                #     Escenario_3D(position=(j,piso[j]+nivel[j],i),escala=(1,nivel[i]))

crear_mapa(techo,nivel)
arma = mano()
app.run()