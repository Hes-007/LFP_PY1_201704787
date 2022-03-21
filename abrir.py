import tkinter as tk
from tkinter import Place, scrolledtext
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from Clases.Datos import Datos
from Clases.DatosFormulario import dtEtiqueta
from Funciones.GenerarFormulario import generarForm
from Funciones.ReporteErrores import generarR
from Funciones.ReporteTokens import generarT
from Analizador import AnalizarFormulario
#tk().withdraw()

#Variables globales
rutaForm=""

class aperturaArchivo(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.lbl_titulo = tk.Label(self, text = 'Analizador Léxico', font=('Helvetica', 14))
        self.lbl_titulo.pack()

        self.txa_contenido_archivo = scrolledtext.ScrolledText(self, width=73, height=15, wrap=tk.WORD, font=
        ('Arial', 13))
        self.txa_contenido_archivo.place(x=10, y=40)
        self.txa_contenido_archivo.pack()

        btn_cargar = tk.Button(self.master, text='Cargar Archivo', width=15)
        btn_cargar.place(x=19, y=330)
        btn_cargar['command'] = self.seleccionar_archivo

        btn_generar = tk.Button(self.master, text='Analizar', width=15)
        btn_generar.place(x=150, y=330)
        btn_generar['command'] = self.generar_archivo

        btn_generarRT = tk.Button(self.master, text='Reporte Tokens', width=15)
        btn_generarRT.place(x=280, y=330)
        btn_generarRT['command'] = self.generar_token

        btn_generarRE = tk.Button(self.master, text='Reporte Errores', width=15)
        btn_generarRE.place(x=412, y=330)
        btn_generarRE['command'] = self.generar_error


    def seleccionar_archivo(self):
        global rutaForm
        try:
          rutaForm = askopenfile(mode='r', filetypes=[('Archivos de texto', '*.form'), ("Todos los Archivos", "*.*")])

          if rutaForm is not None:
            contenido = rutaForm.read()
            self.txa_contenido_archivo.insert(tk.INSERT, contenido)
            messagebox.showinfo('Mensaje del Sistema', "Archivo Cargado Éxitosamente")
          else:
            messagebox.showerror('Mensaje del Sistema', "No se ha cargado ningún archivo")
        except:
            print("Error de Seleccion")

    def generar_archivo(self):
        if rutaForm!="":
                a = AnalizarFormulario(rutaForm)
                tokens = a.getListaTokens()
                errores = a.getListaErrores()
                if len(errores) == 0:
                  messagebox.showinfo('Mensaje del Sistema', "Archivo Analizado Correctamente")
                else:
                  messagebox.showinfo('Mensaje del Sistema', "Archivo Analizado Correctamente")         
        else:
            messagebox.showinfo('Mensaje del Sistema', "No se ha cargado ningún archivo")

    def generar_token(self):
        if rutaForm!="":
                a = AnalizarFormulario(rutaForm)
                tokens = a.getListaTokens()
                errores = a.getListaErrores()
                if len(errores) == 0:
                    generarT(tokens)
                else:
                    generarT(tokens)            
        else:
            print("No se ha cargado ningun archivo")

    def generar_error(self):
        if rutaForm!="":
                a = AnalizarFormulario(rutaForm)
                tokens = a.getListaTokens()
                errores = a.getListaErrores()
                if len(errores) == 0:
                    generarR(errores)
                else:
                    generarR(errores)            
        else:
            print("No se ha cargado ningun archivo")
 
        
        
def main():
    app = tk.Tk()
    app.title('Lenguajes Formales y De Programación')
    app.geometry('715x440')

    ventana = aperturaArchivo(app)

    ventana.mainloop()

if __name__=="__main__":
    main()