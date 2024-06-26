from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
jugador = FirstPersonController(position=(5, 0, 10))
sky = Sky(texture='assets/sky.jpg')
disparo_sonido = Audio('assets/9mm-pistol-shot-6349.mp3', autoplay=False)

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
    xInicio = 0  # Posición del arma en el eje X
    yInicio = -0.4  # Posición del arma en el eje Y
    image_speed = 0.4
    image_index = 0  # Imagen fija
    textura_mano = load_texture('assets/arma.png')
    textura_disparo = load_texture('assets/arma_disparo.png')
    texturas_recarga = [
        load_texture("assets/Paso1.png"),
        load_texture("assets/Paso2.png"),
        load_texture("assets/Paso3.png"),
        load_texture("assets/Paso4.png"),
        load_texture("assets/Paso5.png"),
        load_texture("assets/Paso1.png"),
    ]

    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            texture=self.textura_mano,
            scale=0.4,
            color=color.white,
            rotation=Vec3(0, 0, 0),  # girar el arma
            position=Vec2(self.xInicio, self.yInicio)
        )

    def disparar(self):
        # Cambiar la textura al disparar
        self.texture = self.textura_disparo
        disparo_sonido.play()  # Reproducir sonido de disparo
        # Restaurar textura después de 0.5 segundos
        invoke(self.restaurar_textura, delay=0.5)

    def recargar(self):
        for i, textura in enumerate(self.texturas_recarga):
            invoke(self.cambiar_textura, textura, delay=i * 0.1)

    def cambiar_textura(self, textura):
        self.texture = textura

    def restaurar_textura(self):
        self.texture = self.textura_mano

class Proyectil(Entity):
    def __init__(self, position=(0, 0, 0), direction=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='sphere',
            scale=0.2,
            color=color.red,
            collider='sphere'
        )
        self.direction = direction

    def update(self):
        self.position += self.direction * time.dt * 20  # Aumentar la velocidad del proyectil

        # Verificar colisión
        hit_info = self.intersects()
        if hit_info.hit:
            # Destruir el proyectil al colisionar
            destroy(self)

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

def input(key):
    if key == 'left mouse down':
        mano.disparar()
        proyectil = Proyectil(position=jugador.position + (0, 1, 0), direction=camera.forward)
    if key == 'r':
        mano.recargar()

app.run()
