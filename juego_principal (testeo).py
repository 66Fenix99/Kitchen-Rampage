import pygame
from pygame import *
import sys
fps = 60
pygame.init()


info = pygame.display.Info()
width = info.current_w
height = info.current_h

ventana = pygame.display.set_mode((info.current_w, info.current_h-50), RESIZABLE)


# color_principal = "#fff4bf"



# pantalla_principal = pygame.Surface((infoObject.current_w, infoObject.current_h))
# pantalla_principal.fill(color_principal)

ventana = pygame.display.set_mode((width, height))

# imagen = pygame.image.load("recursos/imagenes/kitchen-rampage-logo.png")
# imagen = pygame.transform.scale(imagen, (info.current_w, info.current_h-50))
# # imagen = pygame.transform.scale(imagen, (500, 500))
# # pantalla_principal.blit(imagen, (0, 0))
# ventana.blit(imagen, (0,0))
# activo = True

# reloj = pygame.time.Clock()

# # rectangulo = pygame.draw.
pantalla_completa = True

activo = True

while activo:
    for evento in pygame.event.get([MOUSEBUTTONDOWN, KEYDOWN, QUIT]):
        print(evento.type)
        if evento.type == pygame.QUIT:
            activo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos[0], evento.pos[1])
        if evento.type == pygame.KEYDOWN:
            tecla = evento.key
            if evento.key == K_F11:
                pantalla_completa = not pantalla_completa
                if pantalla_completa:
                    ventana = pygame.display.set_mode((info.current_w, info.current_h), FULLSCREEN)
                else:
                    ventana = pygame.display.set_mode((info.current_w, info.current_h-50), RESIZABLE)
    pygame.display.update()

# pygame.quit()




        # video = Video("recursos/videos/introduccion.mp4")
        # video.set_size((self.__ventana.ancho, self.__ventana.alto))
        # video_activo = True
        # while video_activo:
        #     video.draw(self.__ventana.referencia_ventana_pygame, (0,0))
        #     for evento_pygame in event.get(KEYDOWN):
        #         video_activo = False
        #     self.__ventana.actualizar()


# from mailbox import NoSuchMailboxError


# class Persona:
#     def __init__(self, nombre):
#         self.__nombre = nombre

# persona_nueva = Persona("juan")








# fondo_imagen = Imagen.convertir_ruta_a_imagen("recursos/imagenes/wood-background.jpg")
# fondo_imagen_dos = Imagen.convertir_ruta_a_imagen("recursos/imagenes/wood-background-2.jpeg")

# boton_prueba = Boton(500,500)
# boton_prueba.cambiar_fuente("calibri", 60)
# boton_prueba.agregar_imagen(fondo_imagen)
# boton_prueba.agregar_texto("Hola Mundo")
# boton_prueba.agregar_receptor(
#     Click(boton_prueba, [Comando(boton_prueba.agregar_imagen, fondo_imagen_dos)]))

# pantalla_prueba = Pantalla(800,600,"Menú principal | Kitchen Rampage")
# pantalla_prueba.colorear("#fff4bf")
# pantalla_prueba.agregar_control_hijo(boton_prueba, 50, 50)

# print(boton_prueba.coordenada_x, boton_prueba.coordenada_y)
# ventana_nueva = Ventana(800,600, pantalla_prueba)

# ventana_nueva.agregar_receptor(
#     Tecla_Presionada(K_F11, ventana_nueva, [Comando(ventana_nueva.cambiar_vista)])
#     )

# juego_nuevo = Juego(ventana_nueva)

# juego_nuevo.iniciar_juego()











# print(isinstance(persona_nueva, Persona))
# import pygame
# import sys

# pygame.init()
# display = pygame.display.set_mode((400,300))

# print(pygame.font.get_fonts())
# miFuente = pygame.font.SysFont("verdana", 20)
# miTexto = miFuente.render("Hola Mundo", True, ("#ffffff"))

# while True:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit

#     display.blit(miTexto, (0,0))

#     pygame.display.update()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit