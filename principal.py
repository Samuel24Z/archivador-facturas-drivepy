from googleDrive import crearRecurso

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import re

import cv2 as cv

recursoDrive = crearRecurso()
nombreArchivo = "factura1.jpg"

def detectarQR():
    print("Detectando el código QR...")
    img = cv.imread(nombreArchivo)
    dectectorQR = cv.QRCodeDetector()

    datos, _, _ = dectectorQR.detectAndDecode(img)

    if(len(datos) > 0):
        return datos
    else:
        return ""

def buscarNumeroDeCliente(datos):
    print("Buscando el número de cliente...")
    resultado = re.search(r"cliente:\s*(\d+)", datos)
    numeroCliente = resultado.group(1)

    return numeroCliente

def subirArchivo(numeroCliente):
    print("Subiendo factura...")
    idCarpeta = "idDeCarpeta"

    metadatos = {
        'name': "Factura_" + str(numeroCliente) + str(".jpg"),
        'parents': [idCarpeta]
    }

    media = MediaFileUpload(
        nombreArchivo,
        mimetype = "image/jpeg",
        resumable = True
    )

    try:
        recursoDrive.files().create(
                body = metadatos, # metadatos a enviar
                media_body = media, # datos a enviar
                fields = 'id' # La API devuelve un id único del archivo
            ).execute()
    except HttpError as error:
        print(f"Ocurrio un error al subir el archivo: {error}")

datosExtraidos = detectarQR()
if datosExtraidos:
    numCliente = buscarNumeroDeCliente(datosExtraidos)
    subirArchivo(numCliente)
else:
    print("No se detecto ningún código QR")