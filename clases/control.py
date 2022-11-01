from pygame import Surface
from pygame.transform import scale
from eventos import Evento, Receptor_Evento

class Control(Surface):
    def __init__(self, ancho: int, alto: int):
        super().__init__((ancho, alto))
        self._ancho_absoluto = ancho
        self._alto_absoluto = alto
        self._ancho_relativo = ancho
        self._alto_relativo = alto
        self._coordenada_x_absoluta = None
        self._coordenada_y_absoluta = None
        self._coordenada_x_relativa = None
        self._coordenada_y_relativa = None
        self._color = "#000000"
        self._imagen_fondo = Surface((0,0))
        self._contenedor = None
        self._receptores_eventos = []

    def _establecer_tamaño_relativo(self, ancho, alto):
        self._ancho_relativo = ancho
        self._alto_relativo = alto

    def establecer_color(self, color: str):
        self._color = color

    def establecer_imagen(self, imagen: Surface):
        self._imagen_fondo = scale(imagen, (self._ancho_absoluto, self._alto_absoluto))

    def _establecer_contenedor(self, contenedor: Surface):
        self._contenedor = contenedor   

    def establecer_coordenadas(self, coordenada_x: int, coordenada_y: int):
        self._coordenada_x_absoluta = coordenada_x
        self._coordenada_y_absoluta = coordenada_y

    def _establecer_coordenadas_relativas(self, coordenada_x: int, coordenada_y: int):
        self._coordenada_x_relativa = coordenada_x
        self._coordenada_y_relativa = coordenada_y

    def renderizar(self):
        self.fill(self._color)
        self.blit(self._imagen_fondo, (0,0))

        if self._contenedor:
            self._contenedor.renderizar()

    def agregar_receptor(self, receptor: Receptor_Evento):
        self._receptores_eventos.append(receptor)

    def limpiar_receptores(self):
        self._receptores_eventos.clear()

    def evaluar_evento(self, evento: Evento):
        for receptor in self._receptores_eventos:
            if receptor.codigo == evento.codigo:
                if receptor.validar_emision(evento):
                    receptor.ejecutar_comandos()
                    return True
        return False

    @property
    def coordenada_x(self):
        return self._coordenada_x_relativa

    @property
    def coordenada_y(self):
        return self._coordenada_y_relativa

    @property
    def ancho(self):
        return self._ancho_relativo

    @property
    def alto(self):
        return self._alto_relativo

# Se denomina "control hijo" a los controles que estén dentro de un contenedor.

class Contenedor(Control):
    def __init__(self, ancho: int, alto: int):
        super().__init__(ancho, alto)
        self._controles_hijos = []

    def evaluar_evento(self, evento: Evento):
        if not super().evaluar_evento(evento):
            return self._evaluar_evento_en_hijos(evento)
        else:
            return True

    def _evaluar_evento_en_hijos(self, evento: Evento):
        evento_recibido = False
        for control_hijo in self._controles_hijos:
            if control_hijo.evaluar_evento(evento):
                evento_recibido = True
        return evento_recibido

    def agregar_control_hijo(self, control_hijo: Control, coordenada_x: int, coordenada_y: int):
        control_hijo._establecer_contenedor(self)
        control_hijo.establecer_coordenadas(coordenada_x, coordenada_y)
        control_hijo._establecer_coordenadas_relativas(coordenada_x, coordenada_y)
        self._controles_hijos.append(control_hijo)
        self.renderizar(control_hijo)

    def eliminar_control_hijo(self, control_hijo: Control):
        self._controles_hijos.remove(control_hijo)

    def _establecer_tamaño_relativo(self, ancho: int, alto: int):
        self._establecer_tamaño_relativo_en_hijos(ancho, alto)
        super()._establecer_tamaño_relativo(ancho, alto)
    
    def _establecer_tamaño_relativo_en_hijos(self, ancho: int, alto: int):
            porcentajes_diferencia = self._calcular_diferencias_tamaño_coordenadas(ancho, alto)
            porcentaje_diferencia_ancho = porcentajes_diferencia[0]
            porcentaje_diferencia_alto = porcentajes_diferencia[1]

            for control_hijo in self._controles_hijos:
                ancho_relativo = control_hijo.ancho + control_hijo.ancho * porcentaje_diferencia_ancho / 100
                alto_relativo = control_hijo.alto + control_hijo.alto * porcentaje_diferencia_alto / 100
                coordenada_x_relativa = control_hijo.coordenada_x + control_hijo.coordenada_x * porcentaje_diferencia_ancho / 100
                coordenada_y_relativa = control_hijo.coordenada_y + control_hijo.coordenada_y * porcentaje_diferencia_alto / 100

                control_hijo._establecer_coordenadas_relativas(coordenada_x_relativa, coordenada_y_relativa)
                control_hijo._establecer_tamaño_relativo(ancho_relativo, alto_relativo)

    def _calcular_diferencias_tamaño_coordenadas(self, ancho: int, alto: int):
        diferencia_ancho = ancho - self._ancho_relativo
        diferencia_alto = alto - self._alto_relativo
        
        porcentaje_diferencia_ancho = diferencia_ancho * 100 / self._ancho_relativo
        porcentaje_diferencia_alto = diferencia_alto * 100 / self._alto_relativo

        return [porcentaje_diferencia_ancho, porcentaje_diferencia_alto]

    # Si se le pasa un control hijo al método renderizador se renderiza solo ese hijo,
    # en el caso contrario se renderizan todos.
    
    def renderizar(self, control_hijo: Control = None):
        if control_hijo:
            self.blit(control_hijo, (control_hijo._coordenada_x_absoluta, control_hijo._coordenada_y_absoluta))
        else:
            self.fill(self._color)
            self.blit(self._imagen_fondo, (0,0))
            for control_hijo in self._controles_hijos:
                self.blit(control_hijo, (control_hijo._coordenada_x_absoluta, control_hijo._coordenada_y_absoluta))

        if self._contenedor:
            self._contenedor.renderizar()