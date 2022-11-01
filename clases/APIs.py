from abc import ABC, abstractclassmethod
from string import ascii_lowercase as abecedario
from requests import get
from ingrediente import Ingredientes_DAO
from imagen import Imagen
from platillo import Platillos_DAO, RecetaIngredientes_DAO
from traductor import Traductor

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
        respuesta = get(cls.__url)
        return respuesta.status_code == 200

    @classmethod
    def consultar(cls, parametros: None):
        return get(cls.__url, parametros).json()

    @classmethod
    def llenar_base_de_datos(cls):
        platillos_json = cls.obtener_platillos_json()
        for platillo_json in platillos_json:
            Platillos_DAO.insertar(platillo_json["strMeal"], platillo_json[""])

    @classmethod
    def obtener_platillos_json(cls):
        platillos_json = []
        parametros = {}
        
        for letra in abecedario:
            parametros["f"] = letra
            respuesta = cls.devolver_informacion(parametros)
            if respuesta["meals"]:
                platillos_json = [*platillos_json, *respuesta["meals"]]

        return platillos_json

    @classmethod
    def obtener_ingredientes_json(cls, platillo_api):
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
print(TheMealDB.devolver_platillos_json()[0])