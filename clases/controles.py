from pygame import SHOWN, display, FULLSCREEN, Surface
from pygame.transform import scale
from pygame.time import Clock
from pygame.font import SysFont
from control import Contenedor, Control

class Pantalla(Contenedor):
    def __init__(self, ancho: int, alto: int, titulo: str):
        super().__init__(ancho, alto)
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo

class Ventana():
    def __init__(self, ancho: int, alto: int):
        self.__referencia_ventana_pygame = display.set_mode((ancho, alto), SHOWN)
        self.__ancho = ancho
        self.__alto = alto
        self.__estado_vista = SHOWN
        self.__FPS = 25
        self.__reloj = Clock()
        self.__pantalla_actual = None

    def establecer_tamaño(self, ancho: int, alto: int):
        self.__ancho = ancho
        self.__alto = alto

        self.__referencia_ventana_pygame = display.set_mode((self.__ancho, self.__alto), self.__estado_vista)
        self.__pantalla_actual._establecer_tamaño_relativo(self.__referencia_ventana_pygame.get_size()[0], self.__referencia_ventana_pygame.get_size()[1])
        self.renderizar()

    def establecer_vista(self):
        if self.__estado_vista == SHOWN:
            self.__estado_vista = FULLSCREEN
        else:
            self.__estado_vista = SHOWN

        self.establecer_tamaño(self.__ancho, self.__alto)

    def establecer_FPS(self, FPS: int):
        self.__FPS = FPS

    def establecer_pantalla(self, pantalla: Pantalla):
        self.__pantalla_actual = pantalla
        self.__pantalla_actual._establecer_contenedor(self)
        self.__pantalla_actual.establecer_coordenadas(0,0)
        display.set_caption(pantalla.titulo)
        self.renderizar()

    def establecer_icono(self, icono: Surface):
        display.set_icon(icono)

    def renderizar(self):
        pantalla_escalada = scale(self.__pantalla_actual, (self.__referencia_ventana_pygame.get_size()[0], self.__referencia_ventana_pygame.get_size()[1]))
        self.__referencia_ventana_pygame.blit(pantalla_escalada, (0,0))

    def actualizar(self):
        self.__reloj.tick(self.__FPS)
        display.update()

    @property
    def ancho(self):
        return self.__ancho

    @property
    def alto(self):
        return self.__alto

    @property
    def estado_vista(self):
        return self.__estado_vista
    
    @property
    def FPS(self):
        return self.__FPS

    @property
    def pantalla_actual(self):
        return self.__pantalla_actual

class Recuadro(Control):
    def __init__(self, ancho: int, alto: int):
        super().__init__(ancho, alto)
        self.__texto = ""
        self.__fuente = SysFont("arial", 10)
        self.__color_texto = "#ffffff"

    def establecer_texto(self, texto):
        self.__texto = texto

    def establecer_fuente(self, fuente, grosor = 10):        
        self.__fuente = SysFont(fuente, grosor)

    def establecer_color_texto(self, color):
        self.__color_texto = color

    def renderizar(self):
        self.fill(self._color)
        self.blit(self._imagen_fondo, (0,0))
        texto_renderizado = self.__fuente.render(self.__texto, True, self.__color_texto)
        
        posicion_centrada_x = self._ancho_absoluto / 2 - texto_renderizado.get_size()[0] / 2
        posicion_centrada_y = self._alto_absoluto / 2 - texto_renderizado.get_size()[1] / 2

        self.blit(texto_renderizado, (posicion_centrada_x, posicion_centrada_y))

        if self._contenedor:
            self._contenedor.renderizar()