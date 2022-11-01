from email.mime import image
from io import BytesIO
from urllib.request import urlopen
from pygame.image import load

class Imagen:
    @classmethod
    def convertir_url_a_bytes(cls, imagen_url):
        return urlopen(imagen_url).read()

    @classmethod
    def convertir_bytes_a_superficie(cls, bytes: bytes):
        imagen_archivo = BytesIO(bytes)
        return load(imagen_archivo)

    @classmethod
    def convertir_ruta_a_imagen(cls, ruta):
        return load(ruta)