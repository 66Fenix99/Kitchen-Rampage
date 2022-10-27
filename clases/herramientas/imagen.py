from io import BytesIO
from urllib.request import urlopen
from pygame.image import load

class Imagen():
    @classmethod
    def convertir_url_a_imagen(cls, imagen_url):
        imagen_string = urlopen(imagen_url).read()
        imagen_archivo = BytesIO(imagen_string)
        return imagen_archivo

    @classmethod
    def convertir_ruta_a_imagen(cls, ruta):
        imagen = load(ruta)
        return imagen