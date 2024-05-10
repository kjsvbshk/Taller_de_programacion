from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app= Ursina()

class Escenario_3D(Button):
    sprite_index=''
    def __init__(self,position=(0,0,0),escala=(0,0)):
        super().__init__(
            position = position,
            parent = scene,
            model = 'cube',
            origin_y = 0.5,
            collider = 'box',
            texture = load_texture('assets/fondo.jpg'),
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = escala,

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

        



ini_techos = [
    [0] * 24 for _ in range(40)
]

ini_nivel = [
    [0] * 24 for _ in range(40)
]


def crear_mapa(nivel1,nivel2):
    largo = len(nivel1)
    ancho = len(nivel1[0])
    x_inicio = ancho/2

    #crear espacio
    for i in range(largo):
        piso = nivel2[i]
        techo = nivel1[i]

        #crear el suelo
        cajax = Escenario_3D(position=(x_inicio,0,i),escala=(ancho,1))

        #crear bloques
        for x in range(ancho):
            if piso[x] > 0:
                cajax=Escenario_3D(position=(x,piso[x],i),escala=(1,piso[x]))
            if techo[x]>0:
                cajax=Escenario_3D(position=(x,techo[x],i),escala=(1,1))
crear_mapa(ini_nivel,ini_techos)
jugador = FirstPersonController()
arma = mano()
app.run()