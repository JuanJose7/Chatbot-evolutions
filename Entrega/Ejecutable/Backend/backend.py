import http.server
import socketserver
import threading

from Backend.configurationBackend.configurationBackend import PORT
from Backend.model.operation import Operation
from emulator.emulator import Emulator

emulator = Emulator()


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.respond()

    def do_POST(self):
        self.respond()

    def createBody(self, operation):

        ## check error
        if operation.checkIsError():
            return None

        ## API define
        body = None
        if operation.operation == "/sala":
            body = emulator.salasManager.infoSalaJson(int(operation.id))
        if operation.operation == "/infoTotalSalas":
            body = emulator.salasManager.infoTotalSalaJson()
        elif operation.operation == "/currentOcupation":
            body = emulator.salasManager.currentOcupacionJson()
        elif operation.operation == "/lessOcupation":
            body = emulator.salasManager.lessOcupacionJson()
        elif operation.operation == "/maxOcupation":
            body = emulator.salasManager.maxOcupacionJson()
        elif operation.operation == "/canEnter":
            body = emulator.salasManager.canEnter(int(operation.id))
        elif operation.operation == "/info":
            body = emulator.salasManager.info()
        elif operation.operation == "/salaFavorita":
            body = emulator.salasManager.favoritaSalaJson()
        elif operation.operation == "/porcentajeOcupacion":
            body = emulator.salasManager.salaPorcentajeOcupacionJson(int(operation.id))

        return body

    def respond(self):
        print("Route ", self.path)
        operation = Operation(self.path)

        bodyResult = self.createBody(operation)
        if bodyResult is None:
            self.send_response(500)
            self.send_header('Content-type', 'text/json')
            self.end_headers()

        elif bodyResult.status:
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            self.wfile.write(bytes(bodyResult.description, "UTF-8"))

        else:
            self.send_response(302)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            self.wfile.write(bytes(bodyResult.description, "UTF-8"))


def emulatorexecute():
    emulator.execute()

hilo = threading.Thread(target=emulatorexecute)
hilo.start()

httpd = socketserver.TCPServer(('', PORT), Handler)
httpd.serve_forever()
