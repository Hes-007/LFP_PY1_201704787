class Datos:
    def __init__(self, lexema, linea, columna, token):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.token = token

    def __str__(self):
        string = str("Lexema: ") + str(self.lexema) + str("Línea: ") + str(self.linea) + str("Columna: ") + str(self.columna) + str("Token: ") + str(self.token)
        return string

class Error:
    def __init__(self, lexema, linea, columna, descripcion):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.descripcion = descripcion

    def __str__(self):
        string = str("Línea: ") + str(self.linea) + str("Columna: ") + str(self.columna) + str("Carácter: ") + str(self.lexema) + str("Descripción: ") + str(self.descripcion)
        return string
