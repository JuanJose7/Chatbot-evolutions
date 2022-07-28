infoConfig = "{ \
    \"hora-apertura\": \"8:00\", \
    \"hora-cierre\": \"20:00\", \
    \"nombre\": \"Go-fit\", \
    \"direccion\": \"Calle Gran via\", \
    \"mensualidad\": 25, \
    \"n-salas\": 5, \
    \"ocupacionTotal\": 100 \
}"

errores = {
    0: "{\"errorCode\":" + str(0) + ", \"description\": \"Sala no encontrada\"}",
    1: "{\"errorCode\":" + str(1) + ", \"description\": \"Identificador de sala no válido \"}",
    2: "{\"errorCode\":" + str(2) + ", \"description\": \"Parámetro enviado no reconocido\"}"
}

class ConfigEmu:
    RELOJ = 15
    ENTER = 0
    EXIT = 1
    MAX_SALAS = 5
    MAX_SENSOR = 5
