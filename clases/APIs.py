from abc import ABC, abstractclassmethod
from string import ascii_lowercase as abecedario
from requests import get as consultar
from ingrediente import Ingrediente
from imagen import Imagen
from platillo import Platillo

class API(ABC):

    @abstractclassmethod
    def chequear_conexion_exitosa(cls):
        pass

    @abstractclassmethod
    def devolver_informacion(cls, parametros: None):
        pass


class TheMealDB(API):

    __url = "http://www.themealdb.com/api/json/v1/1/search.php"

    @classmethod
    def chequear_conexion_exitosa(cls):
        respuesta = consultar(cls.__url)
        if respuesta.status_code == 200:
            return True
        return False

    @classmethod
    def devolver_informacion(cls, parametros: None):
        respuesta = consultar(cls.__url).json()
        return respuesta

    @classmethod
    def devolver_lista_platillos(cls):
        lista_platillos = []
        parametros = {}
        
        for letra in abecedario:
            parametros["f"] = letra
            respuesta = cls.devolver_informacion(parametros)
            lista_platillos_api = respuesta["meals"]

            if lista_platillos_api:
                for platillo_api in lista_platillos_api:
                    lista_platillos.append(cls.crear_platillo(platillo_api))                    
        
        return lista_platillos

    @classmethod
    def crear_lista_ingredientes(cls, platillo_api):
        lista_ingredientes = []

        for clave in platillo_api:
            if "strIngredient" in clave:
                ingrediente_api = platillo_api[clave]

                if ingrediente_api:
                    ingrediente_nuevo = cls.crear_ingrediente(ingrediente_api)
                    lista_ingredientes.append(ingrediente_nuevo)
        
        return lista_ingredientes

    @classmethod
    def crear_platillo(cls, platillo_api):
        lista_ingredientes = cls.crear_lista_ingredientes(platillo_api)

        platillo_nuevo = Platillo(platillo_api["strMeal"], platillo_api["strArea"], lista_ingredientes, platillo_api["strInstructions"], platillo_api["strMealThumb"])
        
        return platillo_nuevo

    @classmethod
    def crear_ingrediente(cls, ingrediente_api):
        imagen_ingrediente_url = Ingrediente.obtener_url_imagen(ingrediente_api)
        imagen_ingrediente = Imagen.convertir_url_a_imagen(imagen_ingrediente_url)
        return imagen_ingrediente

print(TheMealDB.chequear_conexion_exitosa())