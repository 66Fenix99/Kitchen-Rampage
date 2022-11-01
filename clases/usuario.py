from base_de_datos import DAO, Base_de_Datos
from platillo import Platillos_DAO

class Usuario:
    def __init__(self, nombre: str, contraseña: str):
        self.__nombre = nombre
        self.__contraseña = contraseña
 
    @property
    def nombre(self):
        return self.__nombre
 
    @property
    def contraseña(self):
        return self.__contraseña

class Usuarios_DAO(DAO):
    @classmethod
    def leer(cls, id: int):
        usuario_db = Base_de_Datos.ejecutar_comandos(f'SELECT * FROM Usuarios WHERE id = {id}')[0]
        usuario = Usuario(usuario_db[1], usuario_db[2])
        return usuario

    @classmethod
    def insertar(cls, nombre: str, contraseña: str):
        Base_de_Datos.ejecutar_comandos(f'INSERT INTO Usuarios (nombre, contraseña) VALUES ("{nombre}", "{contraseña}")')

class RecetasDesbloqueadas(DAO):
    @classmethod
    def leer(cls, id_usuario: int):
        id_platillos_db = Base_de_Datos.ejecutar_comandos(f'SELECT idPlatillo FROM RecetasDesbloqueadas WHERE idUsuario = {id_usuario}')

        platillos = []
        for id_platillo_db in id_platillos_db:
            platillo = Platillos_DAO.leer(id_platillo_db)
            platillos.append(platillo)

        return platillos

    @classmethod
    def insertar(cls, id_platillo: int, id_usuario: int):
        Base_de_Datos.ejecutar_comandos(f'INSERT INTO RecetasDesbloqueadas (idPlatillo, idUsuario) VALUES ({id_platillo}, {id_usuario})')