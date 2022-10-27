from pygame import MOUSEBUTTONDOWN, KEYDOWN, QUIT, K_F11
from pygame.event import get
from sys import exit
from clases.graficos.controles import *
from clases.graficos.eventos import *

class Juego:
    def __init__(self, ventana: Ventana):
        self.__juego_activo = True
        self.__ventana = ventana
        self.__jugador = None
        self.__eventos_admitidos = [MOUSEBUTTONDOWN, KEYDOWN, QUIT]
    
    def iniciar_juego(self):
        while self.__juego_activo:
            for evento_pygame in get(self.__eventos_admitidos):
                if evento_pygame.type == QUIT:
                    self.cerrar_juego()
                else:
                    evento_recibido = Evento(evento_pygame.type, evento_pygame)
                    self.__ventana.pantalla_actual.evaluar_evento(evento_recibido)
            self.__ventana.actualizar()

    def cerrar_juego(self):
        self.__juego_activo = False
        quit()
        exit()


menu_inicio = Pantalla(500,500,"Bienvenido al menú principal")
ventana_nueva = Ventana(500,500, menu_inicio)
menu_inicio.agregar_receptor(Receptor_Tecla_Presionada(menu_inicio, [Comando(ventana_nueva.establecer_vista)], K_F11))

juego_uno = Juego(ventana_nueva)

juego_uno.iniciar_juego()