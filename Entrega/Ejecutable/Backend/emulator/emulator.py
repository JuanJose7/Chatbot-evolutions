
import time

from random import randrange

from Backend.emulator.configurationEmu.emulatorConfig import ConfigEmu
from Backend.emulator.configurationEmu.salasConfig import sensores, salas
from Backend.emulator.managerEmu.salasManager import SalasManager


class Emulator:

    # init method or constructor
    def __init__(self):

        self.salasManager = SalasManager(Emulator.warmup(salas))

    @staticmethod
    def warmup(salas):
        for index in range(0, len(salas) - 1):
            sala = salas[index]
            ranNum = randrange(sala.capacidad)
            sala.ocupacion = ranNum
            sala.contadorTotal = ranNum

        return salas

    def executeaccion(self, sensorNumber, accion):
        sensores[sensorNumber].executeaccion(accion)
        self.salasManager.printStatus()

    def candoaccion(self, sensorNumber, accion):
        sensor = sensores[sensorNumber]
        if sensor.canDoAccion(accion):
            self.printstatusaccion(accion, sensorNumber)
            return True
        else:
            self.printerroraccion(accion, sensor)
            return False

    def printstatusaccion(self, accion, sensor):
        if (accion == ConfigEmu.ENTER):
            print("ENTRAR - Sensor " + str(sensor))
        else:
            print("SALIR - Sensor " + str(sensor))

    def printerroraccion(self, accion, sensor):
        print("ERROR - Accion " + str(accion) + " - Sensor " + str(sensor.id))

    def numbersensor(self):
        salaNumber = randrange(ConfigEmu.MAX_SENSOR)
        return salaNumber

    def enterorexit(self):
        typeEnter = randrange(2)
        return typeEnter

    def getPeopleSala(self, numerosala):
        return self.salasManager.getPeopleNumber(numerosala)

    def job(self):
        sensorNumber = self.numbersensor()
        accion = self.enterorexit()
        if self.candoaccion(sensorNumber, accion):
            self.executeaccion(sensorNumber, accion)

    def execute(self):
        while True:
            self.job()
            time.sleep(ConfigEmu.RELOJ)
