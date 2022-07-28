from ..configurationEmu.emulatorConfig import ConfigEmu
import json

class Sala:
    # init method or constructor
    def __init__(self,
                 nombre,
                 id,
                 capacidad,
                 ocupacion):
        self.nombre = nombre
        self.id = id
        self.capacidad = capacidad
        self.ocupacion = ocupacion
        self.contadorTotal = 0
        self.sensor = None

    def aumentarOcupacion(self):
        self.ocupacion = self.ocupacion + 1
        self.contadorTotal = self.contadorTotal + 1

    def disminuirOcupacion(self):
        self.ocupacion = self.ocupacion - 1

    def isFull(self):
        return self.ocupacion == self.capacidad

    def __str__(self):
        return self.nombre + "\n     Id: " + str(self.id) + "     Capacidad: " + str(
            self.capacidad) + "     Ocupacion: " + str(self.ocupacion) + "     Contador Total: " + str(self.contadorTotal)

    def canDoAccion(self, accion):
        if accion == ConfigEmu.ENTER:
            if self.ocupacion < self.capacidad:
                return True
            else:
                return False
        else:
            if self.ocupacion == 0:
                return False
            else:
                return True

    def executeAccion(self, accion):
        if (accion == ConfigEmu.ENTER):
            self.aumentarOcupacion()
        else:
            self.disminuirOcupacion()

    def toJson(self):
        return "{\"nombre\":\"" + str(self.nombre) + "\"," \
               "\"id\": " + str(self.id) + ", " \
               "\"capacidad\": " + str(self.capacidad) + "," \
               "\"ocupacion\":" + str(self.ocupacion) + ", " \
               "\"contadorTotal\":" + str(self.contadorTotal) + "}"

