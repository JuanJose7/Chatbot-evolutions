import json

class Operation:

    # init method or constructor
    def __init__(self,
                 name,
                 oppathlist,
                 showkeyboard,
                 indexsala,
                 fieldJson
                 ):
        self.name = name
        self.oppathlist = oppathlist
        self.indexsala = indexsala
        self.showKeyboard = showkeyboard
        self.fieldjson = fieldJson

    def prettyOutput (self, jsonstring):

        if None != self.fieldjson:
            prettyoutput = "########################\n"
            jsondict = json.loads(jsonstring)

            for field in self.fieldjson:
                value = jsondict[field]
                prettyoutput += str(field).capitalize() + ": " + str(value) + "\n"

            prettyoutput += "########################\n"
            return prettyoutput
        else:
            return jsonstring