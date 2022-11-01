from imagen import Imagen
from controles import Ventana, Pantalla, Recuadro
from eventos import Evento, Receptor_Tecla_Presionada, Comando, Receptor_Click, Receptor_Evento
from pygame import K_4, K_F11, MOUSEBUTTONDOWN, KEYDOWN, QUIT, init
from pygame.display import Info, get_surface
import pygame.font
from pygame.event import get
from pyvidplayer import Video


class Juego:
    def __init__(self, ventana: Ventana):
        self.__juego_activo = True
        self.__ventana = ventana
        self.__jugador = None
        self.__eventos_admitidos = [MOUSEBUTTONDOWN, KEYDOWN, QUIT]
    
    def iniciar_juego(self):
        self.__ventana.renderizar()
        while self.__juego_activo:
            for evento_pygame in get(self.__eventos_admitidos):
                if evento_pygame.type == QUIT:
                    self.cerrar_juego()
                else:
                    evento_recibido = Evento(evento_pygame.type, evento_pygame)
                    self.__ventana.pantalla_actual.evaluar_evento(evento_recibido)
            self.__ventana.actualizar()

    def reproducir_video(self, ruta: str):
        self.detener_juego()
        video = Video(ruta)
        video.set_size((self.__ventana.ancho, self.__ventana.alto))
        while not self.__juego_activo:
            for evento_pygame in get(self.__eventos_admitidos):
                if evento_pygame.type == QUIT:
                    self.cerrar_juego()
                elif evento_pygame.type == KEYDOWN:
                    self.__juego_activo = True
            video.draw(get_surface(), (0,0), False)
            self.__ventana.actualizar()
        self.iniciar_juego()

    def detener_juego(self):
        self.__juego_activo = False

    def cerrar_juego(self):
        self.detener_juego()
        quit()

ventana = Ventana(800,500)
juego = Juego(ventana)
juego.reproducir_video("./recursos/videos/introduccion.mov")
juego.reproducir_video("./recursos/videos/IMG_1012.MOV")
# pygame.font.init()
# imagen_prueba = Imagen.convertir_ruta_a_imagen("./recursos/imagenes/wood-background.jpg")
# ventana_principal = Ventana(500,500)
# pantalla_menu_inicio = Pantalla(500,500,"Menú principal | Kitchen Rampage")
# pantalla_menu_inicio.establecer_imagen(imagen_prueba)
# pantalla_menu_inicio.agregar_receptor(
#     Receptor_Tecla_Presionada(
#         pantalla_menu_inicio,
#         [Comando(ventana_principal.establecer_tamaño, ventana_principal.ancho, ventana_principal.alto)],
#         K_F11
#     )
# )
# pantalla_menu_inicio.agregar_receptor(
#     Receptor_Tecla_Presionada(
#         pantalla_menu_inicio,
#         [Comando(pantalla_menu_inicio.establecer_color, "#FFFFFF"), Comando(pantalla_menu_inicio.renderizar)],
#         K_4
#     )
# )
# boton_nuevo = Recuadro(100,100)
# imagen_boton = Imagen.convertir_ruta_a_imagen("./recursos/imagenes/logo/iconoKR.png")
# boton_nuevo.establecer_imagen(imagen_boton)
# boton_nuevo.establecer_texto("Hola mundo")
# boton_nuevo.establecer_fuente("arial", 20)
# boton_nuevo.establecer_color_texto("#FF0000")
# boton_nuevo.renderizar()
# boton_nuevo.agregar_receptor(
#     Receptor_Click(
#         boton_nuevo,
#         [Comando(boton_nuevo.establecer_color, "#FF0000"),
#         Comando(boton_nuevo.renderizar)
#         ]
#     )
# )
# pantalla_menu_inicio.agregar_control_hijo(boton_nuevo, 20,20)
# ventana_principal.establecer_pantalla(pantalla_menu_inicio)
# Juego(ventana_principal).reproducir_video("./recursos/videos/introduccion.mov")