class Platillo:
    def __init__(self):
        self.__nombre = None
        self.__pais_origen = None
        self.__lista_ingredientes = None
        self.__receta = None
        self.__imagen = None
        self.__tiempo_platillo = None
        self.__porcentajes_puntos = None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def pais_origen(self):
        return self.__pais_origen

    @property
    def lista_ingredientes(self):
        return self.__lista_ingredientes

    @property
    def receta(self):
        return self.__receta

    @property
    def imagen(self):
        return self.__imagen

    @property
    def tiempo_platillo(self):
        return self.__tiempo_platillo

    @property
    def porcentajes_puntos(self):
        return self.__porcentajes_puntos

    def obtener_tiempo_platillo(self):
        return len(self.__lista_ingredientes) * 3

    def obtener_porcentajes_puntos(self):
        lista_porcentajes = []
        lista_porcentajes.append(self.__tiempo_platillo * 0.25)
        lista_porcentajes.append(self.__tiempo_platillo * 0.50)
        lista_porcentajes.append(self.__tiempo_platillo * 0.75)
        return lista_porcentajes