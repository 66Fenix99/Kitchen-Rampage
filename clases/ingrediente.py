from base_de_datos import DAO, Base_de_Datos

class Ingrediente:
    def __init__(self, nombre: str, imagen: bytes):
        self.__nombre = nombre
        self.__imagen = imagen

    @property
    def nombre(self):
        return self.__nombre

    @property
    def imagen(self):
        return self.__imagen

    @classmethod
    def obtener_url_imagen(cls, nombre):
        url = "https://www.themealdb.com/images/ingredients/"

        nombre = nombre.title()

        if " " in nombre:
            nombre = nombre.replace(" ", "%20")
        
        url = url + nombre + ".png"
        
        return url

class Ingredientes_DAO(DAO):
    @classmethod
    def leer(cls, id: int):
        ingrediente_db = Base_de_Datos.ejecutar_accion(f'SELECT * FROM Ingredientes WHERE id = {id}')
        ingrediente = Ingrediente(ingrediente_db[1], ingrediente_db[2])
        return ingrediente
    
    @classmethod
    def insertar(cls, nombre: str, imagen: bytes):
        Base_de_Datos.ejecutar_accion(f'INSERT INTO Ingredientes (nombre, imagen) VALUES ("{nombre}", {imagen})')