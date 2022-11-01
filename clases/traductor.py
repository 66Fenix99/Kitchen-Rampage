from translate import Translator

class Traductor(Translator):
    def __init__(self, idioma_origen: str, idioma_salida: str):
        super().__init__(to_lang = idioma_origen, from_lang = idioma_salida)        

    def traducir(self, texto_a_traducir):
        return super().translate(texto_a_traducir)