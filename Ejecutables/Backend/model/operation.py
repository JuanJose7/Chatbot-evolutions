import urllib
from urllib.parse import urlparse


class Operation:

    # init method or constructor
    def __init__(self,
                 path):

        parseResult = urlparse(path)

        self.path = parseResult.path
        self.query = parseResult.query
        self.operation = parseResult.path
        self.scheme = parseResult.scheme
        self.id = None

        if (self.query != ""):
            parseQuery = urllib.parse.parse_qs(parseResult.query)
            self.id = parseQuery.get("id")[0]

    def checkIsError(self):
        if (((self.operation == "/sala") or
             (self.operation == "/canEnter") or
             (self.operation == "/porcentajeOcupacion")) and
                self.id is None):
            return True
