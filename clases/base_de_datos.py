from abc import ABC, abstractclassmethod
import sqlite3

class Base_de_Datos:
    @classmethod
    def crear(cls):
        cls.ejecutar_comandos(
            'CREATE TABLE IF NOT EXISTS Usuarios (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre TEXT, contraseña TEXT)',
            'CREATE TABLE IF NOT EXISTS Platillos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre TEXT, paisOrigen TEXT, receta TEXT, imagen BLOB)',
            'CREATE TABLE IF NOT EXISTS Ingredientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre TEXT, imagen BLOB)',
            'CREATE TABLE IF NOT EXISTS RecetasDesbloqueadas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, idPlatillo INTEGER, idUsuario INTEGER, FOREIGN KEY (idPlatillo) REFERENCES Platillos(id), FOREIGN KEY(idUsuario) REFERENCES Usuarios(id))',
            'CREATE TABLE IF NOT EXISTS RecetaIngredientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, idPlatillo INTEGER, idIngrediente INTEGER, cantidad DECIMAL, FOREIGN KEY(idPlatillo) REFERENCES Platillos(id), FOREIGN KEY(idIngrediente) REFERENCES Ingredientes(id))',
        )

    @classmethod
    def ejecutar_comandos(cls, *comandos: str):
        resultado = []
        conexion = sqlite3.connect("./recursos/base de datos/kitchen_rampage.db")
        cursor = conexion.cursor()
        for comando in comandos:
            cursor.execute(comando)
            resultado = [*resultado, *cursor.fetchall()]
        conexion.commit()
        conexion.close()
        return resultado

class DAO(ABC):
    @abstractclassmethod
    def leer(cls):
        pass

    @abstractclassmethod
    def insertar(cls):
        pass
#     def insertar_platillos(self):
#         conn = sqlite3.connect('kitchenrampage.db')
#         cur = conn.cursor()
#         for letra in abecedario:
#             if letra=="q" or letra=="u" or letra=="x" or letra=="z":
#                 continue
#             respuesta = get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letra}").json()
#             for comida in respuesta["meals"]:
#                 nombre=comida["strMeal"]
#                 instrucciones=comida["strInstructions"]
#                 foto=comida["strMealThumb"]
#                 cur.execute("INSERT INTO Platillos (nombrePlatillo, instrucciones, imagen) values (?, ?, ?)",
#                 (nombre, instrucciones,foto))
#             conn.commit()

#     def insertar_ingredientes_bdd(self):
#         ing=Ingrediente()
#         conn = sqlite3.connect('kitchenrampage.db')
#         cur = conn.cursor()
#         respuesta = get(f"https://www.themealdb.com/api/json/v1/1/list.php?i=list").json()
#         for ingrediente in respuesta["meals"]:
#             ingrediente=ingrediente["strIngredient"]
#             url_foto=ing.obtener_url_imagen(ingrediente)
#             cur.execute("INSERT INTO Ingredientes (nombre,imagen) values (?,?)",
#                     (ingrediente,url_foto))
#         conn.commit()
        
#     def crear_usuario(self,nombre,contraseña):
#         conn = sqlite3.connect('kitchenrampage.db')
#         cur = conn.cursor()
#         cur.execute("INSERT INTO Usuarios (nombre, contraseña) values (?, ?)",
#                 (nombre, contraseña))
#         conn.commit()
 
#     def select_comidas(self):
#         conn = sqlite3.connect('kitchenrampage.db')
#         cur = conn.cursor()
#         cur.execute(''' SELECT * FROM Platillos;''')
#         data=cur.fetchall()
#         if len(data)==0:
#                 print(f"\033[1;31m No hay registros aún \x1b[0m ")
#         else:
#             print(f"\033[1;33m ID-Nombre-Instrucciones-Imagen \x1b[0m")
#             for row in cur.execute('SELECT id as "ID", nombrePlatillo as "Nombre", instrucciones as "Instrucciones", imagen as "URL" from Platillos'):  
#                 print(row)
 
 
#     def select_recetas_bdd(self):
#         conn = sqlite3.connect('kitchenrampage.db')
#         cur = conn.cursor()
#         cur.execute(''' SELECT * FROM RecetasDesbloqueadas;''')
#         data=cur.fetchall()
#         if len(data)==0:
#                 print(f"\033[1;31m No hay registros aún \x1b[0m ")
#         else:
#             print(f"\033[1;33m ID-Nombre-Usuario \x1b[0m")
#             for row in cur.execute('SELECT id as "ID", idPlatillo as "idPlatillo",idUsuario as "idUsuario"  FROM RecetasDesbloqueadas'):  
#                 print(row)


#     def select_ingredientes_bdd(self):
#         conn = sqlite3.connect('kitchenrampage.db')
#         cur = conn.cursor()
#         cur.execute(''' SELECT * FROM Ingredientes;''')
#         data=cur.fetchall()
#         if len(data)==0:
#                 print(f"\033[1;31m No hay registros aún \x1b[0m ")
#         else:
#             print(f"\033[1;33m ID-Nombre-Foto \x1b[0m")
#             for row in cur.execute('SELECT id as "ID", nombre as "Nombre", imagen as "Imagen" from Ingredientes'):  
#                 print(row)
 
#     def desbloquear_receta(self,nombreplatillo,usuario):
#         pass
 
# class Usuario:
#     def __init__(self, nombre: str, contraseña: str):
#         self.__nombre = nombre
#         self.__contraseña = contraseña
 
#     @property
#     def nombre(self):
#         return self.__nombre
 
#     @property
#     def contraseña(self):
#         return self.__contraseña
 
 


