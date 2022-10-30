from translate import Translator

class Traductor(Translator):
    def __init__(self, traducir_de, traducir_a):
        super().__init__(to_lang=traducir_a, from_lang=traducir_de)        

    def traducir(self, texto_a_traducir):
        return super().translate(texto_a_traducir)