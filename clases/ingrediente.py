class Ingrediente:
    def __init__(self):
        self.__nombre = None
        self.__imagen = None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def imagen(self):
        return self.__imagen

    @classmethod
    def obtener_url_imagen(cls, nombre_ingrediente):
        url = "https://www.themealdb.com/images/ingredients/"

        nombre_ingrediente = nombre_ingrediente.title()

        if " " in nombre_ingrediente:
            nombre_ingrediente = nombre_ingrediente.replace(" ", "%20")            
        
        url = url + nombre_ingrediente
        
        return url