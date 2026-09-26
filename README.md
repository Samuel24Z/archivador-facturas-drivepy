# Archivador automático de facturas PDF
Esta aplicación tiene como objetivo archivar automáticamente facturas en formato PDF en el almacenamiento de Google Drive, para ello se va utilizar Python, la biblioteca de visión por computador OpenCV y la API de Google Drive.

El diagrama de bloques del funcionamiento de esta aplicación se muestra a continuación

![Diagrama de bloques](/img/diagrama_bloques_app.JPG)

A continuación se describe con más detalle los procsesos que ejecuta esta aplicación.

* **Detección y decodificación de código QR:** En este punto el programa llama al detector de QRs de OpenCV y con ello también se decodifican los datos que están almacenados al interior del código.
* **Búsqueda de patrones en datos decodificados:** Debido a que el texto almacenado en el QR puede ser extenso, se busca un valor específico para poder extraerlo y con ello definir la carpeta de Drive a la que se va subir la factura asociada a ese QR.
* **Creación de Recurso de interacción con servicios:** En este proceso se realiza un inicio de sesión con Google para solciitar que su API le de acceso a nuestra aplicación de python, con esto se van a crear las credenciales que nos van a permitir crear un Recurso que va poder interactuar con los servicios de Google, en este caso con el servicio de Google Drive.
* **Alojamiento de facturas en Google Drive:** Ya que hemos creado un Recurso que nos permite interactuar con Google workspace entonces definimos los archivos con sus correspondientes metadatos y solicitamos a la API la subida de tales archivos por medio del Recurso que hemos creado.

## Configuración
Las bibiliotecas que necesita esta apliación son las siguientes:
* [OpenCV para Python versión 4 o superior](https://pypi.org/project/opencv-python/)
* [Biblioteca cliente de la API de Google](https://pypi.org/project/google-api-python-client/)
* [Biblioteca cliente de HTTP](https://pypi.org/project/httplib2/)
* [Biblioteca de implementación de OAuth](https://pypi.org/project/oauthlib/)

## Pruebas
En el siguiente [enlace](/test/README.md) se puede observar las condiciones bajo las que se probo esta apliacación, por ejemplo, foto de una factura con poca luz, foto con oclusión parcial, etc.

En las siguiente imagenes se muestran las detecciones en las condiciones en las que si se pudo localizar el código QR.

![Deteccion imagen original](/test/resultados_deteccion/original.jpg)

![Detección imagen con rayadura](/test/resultados_deteccion/danio1.jpg)

![Detección imagen con poca luz](/test/resultados_deteccion/poca_luz.jpg)

## Referencias
* [Clase QRCodeDetector de OpenCV](https://docs.opencv.org/5.0/main_modules/classcv_1_1QRCodeDetector.html)
* [Documentación de la API de Google Drive](https://developers.google.com/workspace/drive/api/guides/about-sdk)
