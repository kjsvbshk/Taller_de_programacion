from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
jugador = FirstPersonController(position=(5, 0, 10))
sky = Sky(texture='assets/sky.jpg')

class Escenario_3D(Button):
    def __init__(self, position=(0, 0, 0), escala=(0, 0), textura='white_cube'):
        super().__init__(
            position=position,
            parent=scene,
            model='cube',
            origin_y=0.5,
            collider='box',
            texture=textura,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=escala
        )

class Mano(Entity):
    x_inicio = 0
    y_inicio = -0.4
    image_speed = 4  # Ajusta esta variable para cambiar la velocidad de los frames
    image_index = 0
    textura_mano = Texture('assets/sprite_shot.png')

    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture=self.textura_mano,
            scale=(0.4, 0.4),  # Escala ajustada
            color=color.white,
            rotation=Vec3(0, 0, 0),
            position=Vec2(self.x_inicio, self.y_inicio),
        )
        self.frames = [Vec4(0, 0, 0.3 + i*0.2, 0.28) for i in range(10)] + [Vec4(0 + i*0.2, 0.25, 0.3 + i*0.2, 0.5) for i in range(9)]
        self.texture_scale = Vec2(1, 1)
        self.active = False

    def on_click(self):
        self.active = True

    def update(self):
        if self.active:
            self.image_index = (self.image_index + time.dt * self.image_speed) % len(self.frames)
            current_frame = self.frames[int(self.image_index)]
            self.texture_offset = Vec2(current_frame.x, current_frame.y)
            self.texture_scale = Vec2(current_frame.z - current_frame.x, current_frame.w - current_frame.y)
            self.scale = Vec3(self.texture_scale.x*1,self.texture_scale.y*1,1)  # Ajusta la escala para que coincida con el tamaño del frame
            if int(self.image_index) == len(self.frames) - 1:
                self.active = False
                self.image_index = 0

# Obtener textura almacenada de acuerdo al valor
def obtener_texturas(altura):
    return texturas_nivel.get(altura, 'assets/default_texture.jpg')

def crear_mapa(nivel1, nivel2):
    largo = len(nivel1)
    ancho = len(nivel1[0])
    for i in range(largo):
        piso = nivel1[i]
        nivel = nivel2[i]
        for j in range(ancho):
            if piso[j] == 0:
                Escenario_3D(position=(j, 0, i), escala=(1, 1), textura='assets/suelo3.png')
                Escenario_3D(position=(j, 8, i), escala=(1, 1), textura='assets/techo.png')
            if piso[j] > 0:
                bloque = Escenario_3D(position=(j, piso[j], i), escala=(1, piso[j]))
                textura_horizontal_scale = 10 if piso[j] == 1 else 9
                bloque.texture_scale = (textura_horizontal_scale, piso[j])
            if nivel[j] > 0:
                bloque = Escenario_3D(position=(j, piso[j] + nivel[j], i), escala=(1, nivel[j]), textura=obtener_texturas(nivel[j]))
                textura_horizontal_scale = 2 if nivel[j] == 1 else 1
                bloque.texture_scale = (textura_horizontal_scale, nivel[j])

# Definición de texturas
texturas_nivel = {
    1: 'assets/suelo2.jpg',
    2: 'assets/suelo2.jpg',
    3: 'assets/suelo2.jpg',
    4: 'assets/paredes2.jpg',
    5: 'assets/paredes2.jpg',
    6: 'assets/paredes2.jpg',
    7: 'assets/paredes2.jpg',
    8: 'assets/pared3.jpg',
}

nivel = [
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 2, 2, 2, 2, 7, 0, 7, 7, 7, 7, 7, 0, 0, 0, 8 ],
    [8, 0, 0, 7, 7, 7, 7, 7, 0, 0, 7, 2, 2, 2, 2, 7, 0, 7, 3, 3, 3, 7, 0, 0, 0, 8 ],
    [8, 0, 0, 7, 1, 1, 1, 7, 7, 7, 7, 2, 2, 2, 2, 7, 0, 7, 3, 3, 3, 7, 0, 0, 0, 8 ],
    [8, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 7, 7, 7, 3, 3, 3, 7, 0, 0, 0, 8 ],
    [8, 0, 0, 7, 1, 1, 1, 7, 7, 7, 7, 2, 2, 2, 2, 7, 1, 7, 3, 3, 3, 7, 0, 0, 0, 8 ],
    [8, 7, 7, 7, 1, 1, 1, 7, 7, 7, 7, 7, 2, 2, 7, 7, 7, 7, 7, 3, 7, 7, 7, 7, 7, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 7, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 7, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 7, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 7, 2, 2, 2, 2, 2, 2, 2, 8 ],
    [8, 7, 7, 7, 1, 1, 1, 7, 7, 7, 7, 7, 1, 1, 7, 7, 7, 7, 7, 2, 7, 7, 7, 7, 7, 8 ],
    [8, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 7, 0, 0, 0, 8 ],
    [8, 0, 0, 7, 1, 1, 1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 2, 7, 0, 0, 0, 8 ],
    [8, 0, 0, 7, 1, 1, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 2, 2, 2, 7, 0, 0, 0, 8 ],
    [8, 0, 0, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 2, 2, 2, 7, 0, 0, 0, 8 ],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 0, 0, 0, 8 ],
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

mano = Mano()
mano.on_click = mano.on_click  # Asigna la función de clic

def input(key):
    if key == 'left mouse down':
        mano.on_click()

app.run()
