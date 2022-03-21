class Seccion:
    def __init__(self, id, seccion):
        self.id = id
        self.seccion = seccion
    
    def __str__(self):
        string = str(self.id) + str(" ") + str(self.seccion)
        return string

    def setIdseccion(self, idseccion):
        self.idseccion=idseccion

class dtEtiqueta:

    def __init__(self, tipo1, etiqueta, valor1, nombre1):
        self.tipo1 = tipo1
        self.etiqueta = etiqueta
        self.valor1 = valor1
        self.nombre1 = nombre1

    def setTipo1(self, tipo1):
        self.tipo1=tipo1

    def setValor1(self, valor1):
        self.valor1=valor1

    def setEtiqueta(self, etiqueta):
        self.etiqueta=etiqueta

    def setNombre1(self, nombre1):
        self.nombre1=nombre1

    def __str__(self):
        string = str(self.tipo1) + str(" ") + str(self.etiqueta) + str(" ") + str(self.valor1) + str(" ") + str(self.nombre1) 
        return string

class dtTexto:

    def __init__(self, tipo, valor, fondo):
        self.tipo = tipo
        self.valor = valor
        self.fondo = fondo

    
    def setTipo(self, tipo):
        self.tipo=tipo

    def setValor(self, valor):
        self.valor=valor

    def setFondo(self, fondo):
        self.fondo = fondo
       
    def __str__(self):
        string = str(self.tipo) + str(" ") + str(self.valor) + str(" ") + str(self.fondo) 
        return string

class dtGrupoR:

    def __init__(self, tipo, valor, valores):
        self.tipo = tipo
        self.valor= valor
        self.valores = valores

    def setTipo(self, tipo):
        self.tipo=tipo

    def setValor(self, valor):
        self.valor=valor

    def setValores(self, valores):
        self.valores = valores
        
    def __str__(self):
        string = str(self.tipo) + str(" ") + str(self.valor) + str(" ") + str(self.valores) 
        return string

class dtGrupoO:

    def __init__(self, tipo, valor, valores):
        self.tipo = tipo
        self.valor = valor
        self.valores = valores

    def setTipo(self, tipo):
        self.tipo=tipo

    def setValor(self, valor):
        self.valor=valor

    def setValores(self, valores):
        self.valores = valores
        
    def __str__(self):
        string = str(self.tipo) + str(" ") + str(self.valor) + str(" ") + str(self.valores) 
        return string

class dtBoton:

    def __init__(self, tipo, valor, evento):
        self.tipo = tipo
        self.valor= valor
        self.evento = evento

    def setTipo(self, tipo):
        self.tipo=tipo

    def setValor5(self, valor):
        self.valor=valor

    def setEvento(self, evento):
        self.evento = evento
        
    def __str__(self):
        string = str(self.tipo) + str(" ") + str(self.valor) + str(" ") + str(self.evento) 
        return string









    
