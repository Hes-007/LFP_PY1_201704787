from os import PathLike
from Clases.Datos import Datos, Error
from Clases.DatosFormulario import dtEtiqueta, dtTexto, dtGrupoR, dtGrupoO, dtBoton
PathLike
import re

class AnalizarFormulario:
    def __init__(self, ruta):
        self.ruta = ruta
        self.texto = ""
        self.Linea = 1
        self.contadorSecciones = 0
        self.nombreFormulario = ""
        self.ListaTokens = []
        self.ListaErrores = []
        self.ListaEtiquetas = []
        self.ListaTextos = []
        self.ListaGrupoR = []
        self.ListaGrupoO = []
        self.ListaBoton = []
        self.leerArchivo()

    def leerArchivo(self):
        archivo = open(self.ruta.name, 'r', encoding = 'utf8')
        for linea in archivo:
            self.texto+= linea
        archivo.close()
        self.texto+= "\n"
        self.analizar()
        self.buscarPalabraReservada()

    def analizar(self):
        estado = 0
        posicion = 0
        columna = 1
        string = ""
        noIdentificados="~<>!@#$%^&*()\,_+-|/¿¡?{[}]´."
        noIdentificado2="~<>!@#$%^&*()\,+-|/¿¡?{[}]´." 
        longitud = len(self.texto)
        tipo1 = None
        etiqueta = None
        valor1 = None
        nombre1 = None
        while posicion<longitud:

            caracter = self.texto[posicion]
            if estado == 0:
                if caracter == "f":
                    estado = 1
                    string+= caracter
                    posicion+= 1
                    columna+= 1

                elif caracter == " ":
                    posicion+= 1
                    columna+=1

                elif caracter == '[':
                    posicion+= 1
                    columna+=1

                elif caracter == "\n":
                    posicion+= 1
                    self.Linea+= 1
                    columna+= 1

                elif caracter == '<':
                    estado = 5
                    posicion+= 1
                    columna+=1

                elif caracter in noIdentificado2:
                    posicion+= 1
                    columna+= 1
                    aux2 = Error(caracter, self.Linea, columna, "Carácter Inválido")
                    self.ListaErrores.append(aux2)

                else:
                    if caracter == ":":
                        estado = 6
                        aux2 = Error("\n", self.Linea, columna, "Se esperaba")
                        self.ListaErrores.append(aux2)
                    posicion+= 1

            elif estado == 1:
                if string == "formulario":
                    estado = 2
                    aux = Datos("formulario", self.Linea, columna, "Palabra Reservada")
                    self.ListaTokens.append(aux)
                    string = ""
                
                elif re.search(r"[a-z]", caracter):
                    string+=caracter
                    posicion+= 1
                    columna+=1
                else:
                    if caracter == '~>>':
                        estado = 2
                        aux = Error(string, self.Linea, columna, "Palabra Reservada No Válida")
                        self.ListaErrores.append(aux)
                        string = ""

                    elif caracter == '[':
                        estado = 2
                        aux = Error(string, self.Linea, columna, "Palabra Reservada No válida")
                        aux2 = Error("~>>", self.Linea, columna, "Se Esperaba")
                        self.ListaErrores.append(aux)
                        self.ListaErrores.append(aux2)
                        string = ""
                    else:
                        aux = Error(caracter, self.Linea, columna, "Carácter No Válido")
                        self.ListaErrores.append(aux)
                        string+= caracter
                        posicion+= 1
                        columna+= 1

            elif estado == 2:

                if caracter == '~>>':
                    estado = 3
                    posicion+= 1
                    columna+= 1

                elif caracter == '[':
                    estado = 3

                elif caracter == " ":
                    posicion+= 1
                    columna+= 1

                elif caracter.isalnum():
                    aux = Error("~>>[", self.Linea, columna, "Se Esperaba")
                    self.ListaErrores.append(aux)
                    estado = 4
                else:
                    aux2 = Error(caracter, self.Linea, columna, "Carácter Inválido, Se Esperaba ~>> [ ")
                    self.ListaErrores.append(aux2)
                    posicion+= 1
                    columna+= 1

            elif estado == 3:
                if caracter == '[':
                    estado = 4
                    posicion+= 1
                    columna+= 1

                elif caracter == " ":
                    posicion+= 1
                    caracter+= 1
                
                elif caracter.isalnum():
                    aux = Error("[", self.Linea, columna, "Se Esperaba")
                    self.ListaErrores.append(aux)
                    estado = 4
                else:
                    aux2 = Error(caracter, self.Linea, columna, "Carácter inválido, Se Esperaba [ ")
                    self.ListaErrores.append(aux2)
                    posicion+= 1
                    columna+= 1

            elif estado == 4:
                if caracter == "<":
                    aux2 = Error("[", self.Linea, columna, "Se Esperaba")
                    self.ListaErrores.append(aux2)
                    string = ""
                    posicion+= 1
                    columna+= 1
                    estado = 0

                else:
                    string+= caracter
                    posicion+= 1
                    columna+= 1

            elif estado == 5:
                if caracter == '\n':
                    aux = Error("<", self.Linea, columna, "Se Esperaba")
                    self.ListaErrores.append(aux)
                    estado = 0
                    string = ""
               
                elif caracter == ":":
                    verificar = re.search("[aA-zZ]*", string)
                    if string.lstrip().rstrip() == verificar.group():
                        if self.buscarIdentificador(string.lstrip().rstrip()):
                         aux = Error(string, self.Linea, columna, "Tipo inválido, Ya Existe")
                         self.ListaErrores.append(aux)
                         estado = 6
                         string = ""
                         posicion+=1
                         columna+=1
                        else:
                          aux = Datos(string.lstrip().rstrip(), self.Linea, columna, "Tipo")
                          self.ListaTokens.append(aux)
                          tipo1 = string.lstrip().rstrip()
                          estado = 6
                          string = ""
                          posicion+= 1
                          columna+= 1
                    else:
                        aux = Error(string, self.Linea, columna, "Tipo No Válido")
                        self.ListaErrores.append(aux)
                        estado = 6
                        string = ""
                        posicion+= 1
                        caracter+=1

                elif caracter == " ":
                    aux = Error(":", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    verificar = re.search("[Aa-Zz]*", string)
                    if string.lstrip().rstrip() == verificar.group():
                        aux = Datos(string.lstrip().rstrip(), self.Linea, columna, "Etiqueta")
                        etiqueta = string.lstrip().rstrip()
                        estado = 7
                        string = ""   
                        posicion+=1
                        columna+=1
                    else:
                        aux = Error(string, self, columna, "Etiqueta inválida")
                        self.ListaErrores.append(aux)
                        estado = 7
                        string = ""
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

                
            elif estado == 6:
                if caracter == ",":
                    estado = 7
                    posicion+=1
                    columna+=1
                elif caracter == "":
                    posicion+=1
                    columna+=1
                elif caracter in noIdentificados:
                    aux = Error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux)
                    posicion+=1
                    columna+=1
                else:
                    estado = 7
                    aux = Error(",", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)

            elif estado == 7:
                if caracter == '\n':
                    aux = Error(",", self.Linea, columna, "Se Esperaba")
                    self.ListaErrores.append(aux)
                    estado = 0
                    string = ""

                elif caracter == " ":
                    if string!= " ":
                        aux = Datos(string, self.Linea, columna, "Cadena")
                        self.ListaTokens.append(aux)
                    valor1 = string
                    posicion+=1
                    columna+=1
                    estado = 8
                    string = ""
                elif caracter == " ":
                    aux = Error(":", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2 = Datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado = 8
                    string = ""
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado == 8:
                if caracter == ":":
                    if string != " ":
                        aux2 = Error(string, self.Linea, columna, "Falta Nombre")
                        self.ListaErrores.append(aux2)
                    else:
                        aux = Datos(string, self.Linea, columna, "Cadena")
                        self.ListaTokens.append(aux)
                        nombre1 = string
                    posicion+=1
                    columna+=1
                    estado = 9
                    string = ""
                    z = dtEtiqueta(tipo1, etiqueta, valor1, nombre1)
                    self.ListaEtiquetas.append(z)
                elif caracter == ">":
                    aux = Error(",", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2 = Datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado = 10
                    string = ""
                
                elif caracter in noIdentificados:
                    aux2=Error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                elif caracter=="\n":
                    aux=Error(">", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=Datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=10
                    string=""
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==9:
                if caracter==">":
                    posicion+=1
                    columna+=1
                    estado=10
                elif caracter=="\n":
                    aux=Error(">", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    estado=10
                elif caracter in noIdentificados:
                    aux2=Error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==10:
                estado=0

    #Funciones
    def buscarPalabraReservada(self):
        encontrado = False
        for buscar in self.ListaTokens:
            if buscar.lexema == "formulario":
                encontrado = True

        if encontrado == False:
            aux = Error("formulario", "0", "0", "No existe la palabra reservada")
            self.ListaErrores.append(aux)

    def buscarIdentificador(self, id):
        encontrado = False
        for buscar in self.ListaTokens:
            if buscar.lexema == id:
                encontrado = True

        return encontrado

    def imprimirTokens(self):
        cont=1
        for tokens in self.ListaTokens:
            print(cont,tokens)
            cont+=1

    def imprimirErrores(self):
        for errores in self.ListaErrores:
            print(errores)

    def imprimirEtiquetas(self):
        for errores in self.ListaEtiquetas:
            print(errores)

    def imprimirTextos(self):
        for errores in self.ListaTextos:
            print(errores)

    def imprimirGrupoR(self):
        for errores in self.ListaGrupoR:
            print(errores)

    def imprimirGrupoO(self):
        for errores in self.ListaGrupoO:
            print(errores)

    def imprimirBotones(self):
        for errores in self.ListaBoton:
            print(errores)

    def getListaTokens(self):
        return self.ListaTokens
    
    def getListaErrores(self):
        return self.ListaErrores

    def getListaEtiquetas(self):
        return self.ListaEtiquetas

    def getListaTextos(self):
        return self.ListaTextos

    def getListaGrupoR(self):
        return self.ListaGrupoR

    def getListaGrupoO(self):
        return self.ListaGrupoO

    def getListaBotones(self):
        return self.ListaBoton

    def getNombre(self):
        return self.nombreFormulario

    def LeerArchivo(self):
        return self.leerArchivo
'''
a=AnalizarFormulario("Archivos_Prueba\entrada.txt")
a.imprimirEtiquetas()
a.imprimirTextos()
a.imprimirGrupoR()
a.imprimirGrupoO()
a.imprimirBotones()
print(a.nombreFormulario)
a.imprimirTokens()
a.imprimirErrores()
'''























                        



                
                    

                


                






