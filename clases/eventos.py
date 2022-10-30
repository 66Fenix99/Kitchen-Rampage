from abc import ABC, abstractmethod, abstractproperty
from pygame import KEYDOWN, MOUSEBUTTONDOWN
from pygame.event import Event

class Comando:
    def __init__(self, funcion, *argumentos):
        self.__funcion = funcion
        self.__argumentos = argumentos

    def ejecutar(self):
        self.__funcion(*self.__argumentos)

class Evento:
    def __init__(self, codigo: int, informacion: Event):        
        self.__codigo = codigo
        self.__informacion = informacion

    @property
    def codigo(self):
        return self.__codigo

    @property
    def informacion(self):
        return self.__informacion

# El objeto Evento se envía al Receptor_Evento y se verifica a través del método 
# validar_emision() de este último.

class Receptor_Evento(ABC):
    def __init__(self, emisor, comandos):
        self._emisor = emisor
        self._comandos = comandos

    @abstractproperty
    def codigo(self):
        pass

    @abstractmethod
    def validar_emision(self, evento):
        pass

    def ejecutar_comandos(self):
        for comando in self._comandos:
            comando.ejecutar()

class Receptor_Click(Receptor_Evento):
    def __init__(self, emisor, comandos):
        super().__init__(emisor, comandos)
        
    @property
    def codigo(self):
        return MOUSEBUTTONDOWN

    def validar_emision(self, evento: Evento):
        click_posicion_x, click_posicion_y = evento.informacion.pos[0], evento.informacion.pos[1]
        
        # Declaramos variables para cada lado del control para que sea más legible.
        control_lado_izquierdo = self._emisor.coordenada_x
        control_lado_derecho = control_lado_izquierdo + self._emisor.ancho

        control_lado_superior = self._emisor.coordenada_y
        control_lado_inferior = control_lado_superior + self._emisor.alto

        # Se valida si las coordenadas del click están dentro del area del control.
        return control_lado_izquierdo < click_posicion_x < control_lado_derecho and control_lado_superior < click_posicion_y < control_lado_inferior

class Receptor_Tecla_Presionada(Receptor_Evento):
    def __init__(self, emisor, comandos, codigo_tecla: int):
        super().__init__(emisor, comandos)
        self.__codigo_tecla = codigo_tecla
    
    @property
    def codigo(self):
        return KEYDOWN

    def validar_emision(self, evento: Evento):
        return evento.informacion.key == self.__codigo_tecla