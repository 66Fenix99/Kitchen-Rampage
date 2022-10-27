from unittest.result import failfast
from pygame import *
from sys import exit
from clases.controles.controles import Ventana, Pantalla, Boton
from clases.controles.eventos import Evento, Tecla_Presionada, Comando, Click
from clases.herramientas.pyvidplayer import Video
from clases.herramientas.imagen import Imagen

class Juego:
    def __init__(self, ventana):
        self.__juego_activo = True
        self.__ventana = ventana
        self.__jugador = None
        self.__eventos_admitidos = [MOUSEBUTTONDOWN, KEYDOWN, QUIT]
    
    def iniciar_juego(self):
        while self.__juego_activo:
            for evento_pygame in event.get(self.__eventos_admitidos):
                if evento_pygame.type == QUIT:
                    self.cerrar_juego()
                else:
                    evento_recibido = Evento(evento_pygame.type, evento_pygame)
                    self.__ventana.evaluar_evento(evento_recibido)
            self.__ventana.actualizar()

    def cerrar_juego(self):
        self.__juego_activo = False
        quit()
        exit()

    def mostrar_intro(self):
        pass