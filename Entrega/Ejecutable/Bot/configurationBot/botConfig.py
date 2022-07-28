from Bot.model.operation import Operation

API_TOKEN = '5260264151:AAFmQ04QpQJ-epSw22C_qOJP0Qhaf2GUAnw'
URL_NGROK = 'http://4843-92-189-94-207.ngrok.io'

salas = [
    'Sala Norte',
    'Sala Oeste',
    'Sala Sur',
    'Sala Sorento',
    'Sala Espacio'
]


operaciones = [
    Operation('Gente en la sala', 'sala', True, -1, ["nombre", "id", "capacidad", "ocupacion", "contadorTotal"]),
    Operation('Ocupación Total', 'currentOcupation', False, -1, ["currentOcupacion"]),
    Operation('Sala menos ocupación', 'lessOcupation', False, -1, ["nombre", "id", "capacidad", "ocupacion", "contadorTotal"]),
    Operation('Sala mayor ocupación', 'maxOcupation', False, -1, ["nombre", "id", "capacidad", "ocupacion", "contadorTotal"]),
    Operation('¿Puedo entrar a una sala?', 'canEnter', True, -1, ["canEnterSala"]),
    Operation('Información general del gimnasio', 'info', False, -1, ["hora-apertura", "hora-cierre", "nombre", "direccion", "mensualidad", "n-salas", "ocupacionTotal"]),
    Operation('Sala favorita de la gente', 'salaFavorita', False, -1, ["nombre", "id", "capacidad", "ocupacion", "contadorTotal"]),
    Operation('Porcentaje de sala', 'porcentajeOcupacion', True, 40, ["nombre", "id", "capacidad", "ocupacion", "contadorTotal"]),
    Operation('Información de TODAS las salas', 'infoTotalSalas', False, -1, None),
]