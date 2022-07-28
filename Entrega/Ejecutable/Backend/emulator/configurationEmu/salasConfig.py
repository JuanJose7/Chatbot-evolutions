from ..modelEmu.sala import Sala
from ..modelEmu.sensor import Sensor

salas = [
    Sala("Sala Norte", 0, 8, 0),
    Sala("Sala Oeste", 1, 7, 0),
    Sala("Sala Sur", 2, 6, 0),
    Sala("Sala Sorento", 3, 7, 0),
    Sala("Sala Espacio", 4, 6, 0),
]

sensores = [
    Sensor(0, "Sala 1 - Sensor 1", salas[0]),
    Sensor(0, "Sala 2 - Sensor 2", salas[1]),
    Sensor(0, "Sala 3 - Sensor 3", salas[2]),
    Sensor(0, "Sala 4 - Sensor 4", salas[3]),
    Sensor(0, "Sala 5 - Sensor 5", salas[4]),
]