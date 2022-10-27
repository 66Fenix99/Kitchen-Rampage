from pygame import SHOWN, display, FULLSCREEN, Surface
from .control import Contenedor, Control
from pygame import display
from pygame.time import Clock
from pygame.font import get_fonts, SysFont
from pygame.transform import scale

class Pantalla(Contenedor):
    def __init__(self, ancho: int, alto: int, titulo: str):
        super().__init__(ancho, alto)
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo

class Ventana():
    def __init__(self, ancho: int, alto: int, pantalla: Pantalla):
        self = display.set_mode((ancho, alto), self.__estado_vista)
        self.__ancho = ancho
        self.__alto = alto
        self.__estado_vista = SHOWN
        self.__FPS = 25
        self.__reloj = Clock()
        self.__pantalla_actual = pantalla

    def establecer_tamaño(self, ancho: int, alto: int):
        self.__ancho = ancho
        self.__alto = alto

        self.__pantalla_actual.establecer_tamaño(ancho, alto)

    def establecer_vista(self):
        if self.__estado_vista == SHOWN:
            self.__estado_vista = FULLSCREEN
        else:
            self.__estado_vista = SHOWN
        
        self = display.set_mode((self.__ancho, self.__alto), self.__estado_vista)

    def establecer_FPS(self, FPS: int):
        self.__FPS = FPS

    def establecer_pantalla(self, pantalla: Pantalla):
        self.__pantalla_actual = pantalla
        self.__pantalla_actual._establecer_contenedor(self)
        self.__pantalla_actual._establecer_coordenadas(0,0)
        display.set_caption(pantalla.titulo)

    def establecer_icono(self, icono: Surface):
        display.set_icon(icono)

    def renderizar(self):
        self.__pantalla_actual.renderizar()
        self.blit(self.__pantalla_actual, (0,0))
        self.__reloj.tick(self.__FPS)
        display.update()

    @property
    def estado_vista(self):
        return self.__estado_vista
    
    @property
    def FPS(self):
        return self.__FPS

    @property
    def pantalla_actual(self):
        return self.__pantalla_actual

class Boton(Control):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
        self.__imagen = None
        self.__texto = ""
        self.__fuente = SysFont("arial", 10)
        self.__color_texto = "#ffffff"

    def agregar_imagen(self, imagen):
        imagen = scale(imagen, (self._ancho, self._alto))
        self.__imagen = imagen
        self.redibujar()

    def agregar_texto(self, texto):
        self.__texto = texto
        self.redibujar()

    def cambiar_fuente(self, fuente, grosor = 10):        
        self.__fuente = SysFont(fuente, grosor)

    def cambiar_color_texto(self, color):
        self.__color = color
        self.redibujar()

    def redibujar(self):
        if self.__imagen:
            self.blit(self.__imagen, (0,0))
        if self.__texto:
            texto_superficie = self.__fuente.render(self.__texto, True, self.__color_texto)

            posicion_texto_x = self._ancho / 2 - texto_superficie.get_size()[0] / 2
            posicion_texto_y = self._alto / 2 - texto_superficie.get_size()[1] / 2

            self.blit(texto_superficie, (posicion_texto_x, posicion_texto_y))

class Picture_Box(Control):
    def __init__(self, ancho, alto, imagen):
        super().__init__(ancho, alto)
        scale(imagen, (self._ancho, self._alto), imagen)

    def cambiar_imagen(self, imagen):
        scale(imagen, (self._ancho, self._alto), imagen)
        self.blit(imagen, (0,0))