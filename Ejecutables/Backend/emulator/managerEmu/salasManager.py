import sys
from ..configurationEmu.emulatorConfig import infoConfig
from ..configurationEmu.emulatorConfig import errores
from ..configurationEmu.salasConfig import salas, sensores
from ..configurationEmu.emulatorConfig import ConfigEmu
from ..modelEmu.result import Result

class SalasManager:

    def __init__(self, salasfield):
        self.salas = salasfield
        for index in range(0, len(self.salas) - 1):
            sala = self.salas[index]
            sala.sensor = sensores[index]

    def detectarMovimiento(self, idSala):
        salaAux = self.salas[idSala]
        salaAux.ocupacion = salaAux.ocupacion + 1

    def getPeopleNumber(self, idSala):
        return self.salas[idSala].ocupacion

    def infoSalaJson(self, idSala):
        if 0 <= idSala < ConfigEmu.MAX_SALAS:
            return Result(True, str(self.salas[idSala].toJson()))
        else:
            return Result(False, errores[1])

    def infoTotalSalaJson(self):
        return Result(True, self.toJsonSalas(self.salas))

    def canEnter(self, idSala):
        if 0 <= idSala < ConfigEmu.MAX_SALAS:
            return Result(True, str("{\"canEnterSala\": " + str(not self.salas[idSala].isFull()).lower() + "}"))
        else:
            return Result(False, errores[1])

    def currentOcupacionJson(self):
        ocupacion = 0
        for salaAux in self.salas:
            ocupacion = ocupacion + salaAux.ocupacion
        return Result(True, str("{\"currentOcupacion\": " + str(ocupacion) + "}"))

    def lessOcupacionJson(self):
        ocupacion = sys.maxsize
        sala = None
        for salaAux in self.salas:
            if salaAux.ocupacion < ocupacion:
                ocupacion = salaAux.ocupacion
                sala = salaAux

        if sala is not None:
            return Result(True, str(sala.toJson()))
        else:
            return Result(False, errores[0])

    def maxOcupacionJson(self):
        ocupacion = -sys.maxsize
        sala = None
        for salaAux in self.salas:
            if salaAux.ocupacion > ocupacion:
                ocupacion = salaAux.ocupacion
                sala = salaAux
        if sala is not None:
            return Result(True, str(sala.toJson()))
        else:
            return Result(False, errores[0])

    def favoritaSalaJson(self):
        total = -sys.maxsize
        sala = None
        for salaAux in self.salas:
            if salaAux.contadorTotal > total:
                total = salaAux.contadorTotal
                sala = salaAux

        if sala is not None:
            return Result(True, str(sala.toJson()))
        else:
            return Result(False, errores[0])

    def salaPorcentajeOcupacionJson(self, porcentaje):
        if 0 <= porcentaje <= 100:
            sala = None
            for salaAux in self.salas:
                if ((salaAux.ocupacion / salaAux.capacidad) * 100) <= porcentaje:
                    sala = salaAux
                    break

            if sala is not None:
                return Result(True, str(sala.toJson()))
            else:
                return Result(False, errores[0])
        else:
            return Result(False, errores[2])

    def toJsonSalas(self, salas):
        resultjson = "["
        for salaAux in salas:
            resultjson = resultjson + salaAux.toJson() + ","
        resultjson = resultjson[:-1] + "]"

        return str(resultjson)

    def info(self):
        return Result(True, str(infoConfig))

    def printStatus(self):
        for salaAux in self.salas:
            print(salaAux)
