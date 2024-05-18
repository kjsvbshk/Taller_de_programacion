from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app= Ursina()
jugador = FirstPersonController(position=(5,0,10))
sky = Sky(texture='assets/sky.jpg')

class Escenario_3D(Button):
    def __init__(self,position=(0,0,0),escala=(0,0),textura='white_cube'):
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
    textura_mano = Texture('assets/gun.png')

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


#obtener textura almacenada de acuerdo al valor
def obtener_texturas(altura):
    return texturas_nivel.get(altura, 'assets/default_texture.jpg')

def crear_mapa(nivel1,nivel2):
    largo = len(nivel1)
    ancho = len(nivel1[0])
    #crear espacio
    for i in range(largo):
        piso = nivel1[i]
        nivel = nivel2[i]

        for j in range(ancho):
            # Crear el suelo y techo
            if piso[j] == 0:
                # Crear suelo
                Escenario_3D(position=(j,0,i), escala=(1,1), textura='assets/suelo.jpg')
            # Crear paredes
            if piso[j] > 0:
                # Crear pared a la altura correspondiente
                bloque = Escenario_3D(position=(j,piso[j],i), escala=(1,piso[j]))
                # Ajustar la textura
                textura_horizontal_scale = 1 if piso[j] == 1 else 0.5  # Escala horizontal según el nivel de la pared
                bloque.texture_scale = (textura_horizontal_scale, piso[j])  # Ajustar la escala horizontal y vertical
            if nivel[j] > 0:
                # Crear pared a la altura correspondiente
                bloque = Escenario_3D(position=(j,piso[j]+nivel[j],i), escala=(1,nivel[j]), textura=obtener_texturas(nivel[j]))
                # Ajustar la textura
                textura_horizontal_scale = 1 if nivel[j] == 1 else 0.5  # Escala horizontal según el nivel de la pared
                bloque.texture_scale = (textura_horizontal_scale, nivel[j])  # Ajustar la escala horizontal y vertical

#Definicion de texturas
texturas_nivel={
    1: 'assets/suelo.jpg',
    2: 'assets/suelo.jpg',
    3: 'assets/paredes.jpg',
    4: 'assets/paredes.jpg',
    5: 'assets/paredes.jpg',
    6: 'assets/paredes.jpg',
    7: 'assets/paredes.jpg',
    8: 'assets/sala.jpg',
}

nivel = [
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 2, 2, 2, 5, 0, 6, 6, 6, 6, 6, 0, 0, 0, 8 ],
    [8, 0, 0, 4, 4, 4, 4, 4, 0, 0, 5, 2, 2, 2, 2, 5, 0, 6, 3, 3, 3, 6, 0, 0, 0, 8 ],
    [8, 0, 0, 4, 1, 1, 1, 4, 4, 4, 5, 2, 2, 2, 2, 5, 0, 6, 3, 3, 3, 6, 0, 0, 0, 8 ],
    [8, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 4, 6, 3, 3, 3, 6, 0, 0, 0, 8 ],
    [8, 0, 0, 4, 1, 1, 1, 4, 4, 4, 5, 2, 2, 2, 2, 5, 1, 6, 3, 3, 3, 6, 0, 0, 0, 8 ],
    [8, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 6, 3, 6, 5, 5, 5, 5, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1, 4, 4, 4, 5, 5, 2, 5, 5, 5, 5, 5, 8 ],
    [8, 0, 0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 0, 0, 0, 8 ],
    [8, 0, 0, 4, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 2, 2, 2, 5, 0, 0, 0, 8 ],
    [8, 0, 0, 4, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 2, 2, 5, 0, 0, 0, 8 ],
    [8, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 2, 2, 5, 0, 0, 0, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 8 ],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8 ]
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

crear_mapa(techo,nivel)
arma = mano()
app.run()