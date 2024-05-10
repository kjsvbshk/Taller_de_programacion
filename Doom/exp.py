from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Escenario_3D(Button):
    sprite_index = ''
    def __init__(self, position=(0,0,0), scale=(1,1,1), **kwargs):
        super().__init__(
            position=position,
            parent=scene,
            model='cube',
            origin_y=0.5,
            collider='box',
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=scale,
            **kwargs
        )

class mano(Entity):
    #posicion armas x y 
    x_inicio = 0
    y_inicio = -0.4
    image_speed = 0.4
    image_index = 0#imagen estatica

    textura_mano = load_texture('assets/arma.png')
    def __init__(self):
        super().__init__(            
            parent=camera.ui,
            model='cube',
            texture=self.textura_mano,
            scale=(0.7,0.7),
            color=color.white,
            rotation=Vec3(0,0,0),#mover arma
            position=Vec3(self.x_inicio, self.y_inicio, 0),#posicion x,y
        )

ini_techos = [
    [0] * 24 for _ in range(20)
]

ini_nivel = [
    [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def crear_mapa(nivel1, nivel2):
    largo = len(nivel1)
    ancho = len(nivel1[0])
    x_inicio = ancho / 2

    # Crear espacio
    for i in range(largo):
        piso = nivel2[i]
        techo = nivel1[i]

        # Crear el suelo y el techo
        for x in range(ancho):
            if piso[x] > 0:
                suelo = Escenario_3D(position=(x, piso[x] / 2, i), scale=(1, piso[x], 1))
            if techo[x] > 0:
                techo = Escenario_3D(position=(x, techo[x] + 0.5, i), scale=(1, 1, 1))

def crear_habitacion(x, z):
    # Crear habitación
    for i in range(x, x + 5):
        for j in range(z, z + 5):
            if i == x or i == x + 4 or j == z or j == z + 4:
                suelo = Escenario_3D(position=(i, 0, j), scale=(1, 1, 1))

def crear_pasillo(x, z, longitud, orientacion):
    if orientacion == 'horizontal':
        for i in range(x, x + longitud):
            suelo = Escenario_3D(position=(i, 0, z), scale=(1, 1, 1))
    elif orientacion == 'vertical':
        for j in range(z, z + longitud):
            suelo = Escenario_3D(position=(x, 0, j), scale=(1, 1, 1))

def crear_puertas():
    for i in range(0, 10):
        puerta1 = Escenario_3D(position=(i, 0, 2), scale=(1, 1, 1))
        puerta2 = Escenario_3D(position=(i, 0, 7), scale=(1, 1, 1))

crear_mapa(ini_nivel, ini_techos)
crear_habitacion(1, 1)
crear_habitacion(1, 6)
crear_habitacion(7, 1)
crear_habitacion(7, 6)
crear_pasillo(3, 1, 4, 'horizontal')
crear_pasillo(1, 3, 4, 'vertical')
crear_pasillo(3, 6, 4, 'horizontal')
crear_puertas()
jugador = FirstPersonController()
arma = mano()
app.run()
