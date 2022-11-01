from base_de_datos import DAO, Base_de_Datos
from typing import List
from pygame import Surface
from ingrediente import Ingrediente, Ingredientes_DAO

class Platillo:
    def __init__(self, nombre: str, pais_origen: str, ingredientes: List[Ingrediente], receta: str, imagen: Surface):
        self.__nombre = nombre
        self.__pais_origen = pais_origen
        self.__ingredientes = ingredientes
        self.__receta = receta
        self.__imagen = imagen
        self.__tiempo_platillo = len(self.__lista_ingredientes) * 3
        self.__porcentajes_puntos = []
        self.__porcentajes_puntos.append(self.__tiempo_platillo * 0.25)
        self.__porcentajes_puntos.append(self.__tiempo_platillo * 0.50)
        self.__porcentajes_puntos.append(self.__tiempo_platillo * 0.75)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def pais_origen(self):
        return self.__pais_origen

    @property
    def ingredientes(self):
        return self.__ingredientes

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

class Platillos_DAO(DAO):
    @classmethod
    def leer(cls, id: int = None):
        if id:
            platillos_db = Base_de_Datos.ejecutar_accion(f'SELECT * FROM Platillos WHERE id = {id}')
        platillos_db = Base_de_Datos.ejecutar_accion(f'SELECT * FROM Platillos')

        platillos = []
        for platillo_db in platillos_db:
            ingredientes = RecetaIngredientes_DAO.leer(platillo_db[0])
            platillo = Platillo(platillo_db[1], platillo_db[2], ingredientes, platillo_db[3], platillo_db[4])
            platillos.append(platillo)
        
        return platillos

    @classmethod
    def insertar(cls, nombre: str, receta: str, imagen: bytes):
        Base_de_Datos.ejecutar_accion(f'INSERT INTO Platillos (nombre, instrucciones, imagen) VALUES ("{nombre}", "{receta}", "{imagen}")')

class RecetaIngredientes_DAO(DAO):
    @classmethod
    def leer(cls, id_platillo: int):
        id_ingredientes_db = Base_de_Datos.ejecutar_accion(f'SELECT idIngrediente FROM RecetaIngredientes WHERE idPlatillo = {id_platillo}')

        ingredientes = []
        for id_ingrediente_db in id_ingredientes_db:
            ingrediente = Ingredientes_DAO.leer(id_ingrediente_db)
            ingredientes.append(ingrediente)

        return ingredientes

    @classmethod
    def insertar(cls, id_platillo: int, id_ingrediente: int):
        Base_de_Datos.ejecutar_accion(f'INSERT INTO RecetaIngredientes (idPlatillo, idIngrediente) VALUES ({id_platillo}, {id_ingrediente})')        