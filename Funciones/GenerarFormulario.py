import os
texto = ""

def cabecera(titulo, datos):
    global texto
    texto = ""
    c='''
    <!DOCTYPE html>
    <html lang="es">
    <title>Formulario</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Asap+Condensed:wght@400;700&family=Courgette&family=Lobster&family=Rokkitt:wght@300;800&display=swap"
        rel="stylesheet">
    <style>
        .w3-lobster {
            font-family: "Lobster", Sans-serif;
        }

        .Asap-Condensed {
            font-family: 'Asap Condensed', sans-serif;
        }

        .Courgette {
            font-family: 'Courgette', cursive;
        }

        .Rokkitt {
            font-family: 'Rokkitt', serif;
            font-weight: 800;
        }
    </style>

    <body>
        <div class="w3-display-container" style="height: 780px;" >
            <dir class="w3-display-middle" style="width: 550px;">
                <div class="w3-card-4 w3-margin-bottom">
                    <header class="w3-container w3-black  w3-round-small">
                        <p class="w3-lobster w3-center" style="font-size: 30px;">'''+str(titulo)+'''</p>
                    </header>
                    <div class="w3-container w3-middle Asap-Condensed">
                        <p>Formulario: <br><br> <b>Tipo:</b> '''+str(datos.etiqueta)+''' <br> <b>Valor: </b>'''+str(datos.nombre1)+'''<br><br> Descripción:</p>
                        <table class="w3-table w3-margin-top">
                            <tr>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Cantidad</th>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Concepto</th>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Precio</th>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Total</th>
                            </tr>
                    </div>
                    <footer class="w3-container w3-black  w3-round-small">
                        <br>
                    </footer>
                </div>
            </dir>
            <br>
        </div>
    </body>
</html>
'''
    texto+=c

def crearArchivo():
    global texto
    arhcivo=open('Formulario.html','w', encoding='utf8')
    arhcivo.write(texto)
    arhcivo.close()
    os.startfile("Formulario.html")

def generarForm(titulo, datos):
    cabecera(titulo, datos)
    crearArchivo()