from googleDrive import crearRecurso

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import re # soporte para expresiones regulares
# import os

import cv2 as cv

recursoDrive = crearRecurso()
rutaImagen = './test/img/original.jpg'

def detectarQR():
    print("Detectando el código QR...")
    img = cv.imread(rutaImagen)
    dectectorQR = cv.QRCodeDetector()

    datos, puntos, _ = dectectorQR.detectAndDecode(img)

    if(len(datos) > 0):
        """
        imagenConQRDetectado = img.copy()
        
        n = len(puntos[0])
        for i in range(n):
            punto1 = tuple(map(int, puntos[0][i]))
            # usamos wrap aroun para volver al punto inicial
            punto2 = tuple(map(int, puntos[0][(i+1)%n]))
            cv.line(imagenConQRDetectado, punto1, punto2, (0, 255, 0), 8)

        qrDetectado = os.path.basename(rutaImagen)
        cv.imwrite(qrDetectado, imagenConQRDetectado)
        """
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
        rutaImagen,
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
    print(f"El número de cliente es: {numCliente}")
    subirArchivo(numCliente)
else:
    print("No se detecto ningún código QR")