from pygame import Surface
from pygame.transform import scale
from .eventos import Evento, Receptor_Evento

class Control(Surface):
    def __init__(self, ancho: int, alto: int):
        super().__init__((ancho, alto))
        self._ancho = ancho
        self._alto = alto
        self._color = None
        self._imagen_fondo = None
        self._coordenada_x = None
        self._coordenada_y = None
        self._contenedor = None
        self._receptores_eventos = []

    def establecer_tamaño(self, ancho: int, alto: int):
        scale(self, (ancho, alto), self)
        self._ancho = ancho
        self._alto = alto
        self.establecer_imagen(self._imagen_fondo)

    def establecer_color(self, color: str):
        self._color = color

    def establecer_imagen(self, imagen: Surface):
        self._imagen_fondo = scale(imagen, (self._ancho, self._alto))

    def _establecer_contenedor(self, contenedor: Surface):
        self._contenedor = contenedor   

    def _establecer_coordenadas(self, coordenada_x: int, coordenada_y: int):
        self._coordenada_x = coordenada_x
        self._coordenada_y = coordenada_y

    def _renderizar(self):
        self.fill(self._color)
        self.blit(self._imagen_fondo, (0,0))

        if self._contenedor:
            self._contenedor.renderizar()

    def agregar_receptor(self, receptor: Receptor_Evento):
        self._receptores_eventos.append(receptor)

    def evaluar_evento(self, evento: Evento):
        for receptor in self._receptores_eventos:
            if receptor.codigo == evento.codigo:
                if receptor.validar_emision(evento):
                    receptor.ejecutar_comandos()
                    return True
        return False

    @property
    def coordenada_x(self):
        return self._coordenada_x

    @property
    def coordenada_y(self):
        return self._coordenada_y

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto


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
        control_hijo._establecer_coordenadas(coordenada_x, coordenada_y)
        self._controles_hijos.append(control_hijo)
        self._renderizar(control_hijo)

    def establecer_tamaño(self, ancho: int, alto: int):
        super().establecer_tamaño(ancho, alto)
        self._establecer_tamaño_en_hijos(ancho, alto)

    def _establecer_tamaño_en_hijos(self, ancho: int, alto: int):
        porcentajes_diferencia = self._calcular_diferencias_tamaño(ancho, alto)
        porcentaje_diferencia_ancho = porcentajes_diferencia[0]
        porcentaje_diferencia_alto = porcentajes_diferencia[1]

        for control_hijo in self._controles_hijos:
            ancho_nuevo = control_hijo.ancho + control_hijo.ancho * porcentaje_diferencia_ancho / 100
            alto_nuevo = control_hijo.alto + control_hijo.alto * porcentaje_diferencia_alto / 100
            coordenada_x_nueva = control_hijo.coordenada_x + control_hijo.coordenada_x * porcentaje_diferencia_ancho / 100
            coordenada_y_nueva = control_hijo.coordenada_y + control_hijo.coordenada_y * porcentaje_diferencia_alto / 100

            control_hijo._establecer_coordenadas(coordenada_x_nueva, coordenada_y_nueva)
            control_hijo.establecer_tamaño(ancho_nuevo, alto_nuevo)
            control_hijo.renderizar()

    def _calcular_diferencias_tamaño_coordenadas(self, ancho: int, alto: int):
        diferencia_ancho = ancho - self._ancho
        diferencia_alto = alto - self._alto
        
        porcentaje_diferencia_ancho = diferencia_ancho * 100 / self._ancho
        porcentaje_diferencia_alto = diferencia_alto * 100 / self._alto

        return [porcentaje_diferencia_ancho, porcentaje_diferencia_alto]

    # Si se le pasa un control hijo al método renderizador se renderiza solo ese hijo,
    # en el caso contrario se renderizan todos.
    
    def renderizar(self, control_hijo: Control = None):
        if control_hijo:
            self.blit(control_hijo, (control_hijo.coordenada_x, control_hijo.coordenada_y))
        else:
            self.fill(self._color)
            self.blit(self._imagen_fondo, (0,0))
            for control_hijo in self._controles_hijos:
                self.blit(control_hijo, (control_hijo.coordenada_x, control_hijo.coordenada_y))

        if self._contenedor:
            self._contenedor.renderizar()