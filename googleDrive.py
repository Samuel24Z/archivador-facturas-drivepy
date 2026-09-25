import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive"]

def crearRecurso():
    # La variable creds almacenará el token de acceso del usuario. Si no se encuentra un token válido, crearemos uno.
    creds = None

    # El archivo token.json almacena los tokens de acceso y actualización del usuario.
    # Se crea automáticamente cuando el flujo de autorización se completa por primera vez.

    # Se verifica si existe el archivo token.json
    if os.path.exists('token.json'):
        # Lee el token del archivo y lo guarda en la variable creds
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Si no hay credenciales válidas disponibles, solicita al usuario que inicie sesión
    if not creds or not creds.valid:
        # Si el token ha caducado, se actualizará; de lo contrario, solicitaremos uno nuevo.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            misCredenciales = "credentials.json"
            flow = InstalledAppFlow.from_client_secrets_file(misCredenciales, SCOPES)
            creds = flow.run_local_server(port=0)

        # Se guarda el token de acceso en el archivo token.json para su uso futuro
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    """
    Se realiza una conexión al servicio API
    build() devuelve un objeto Resource con métodos para interactuar con 
    el servicio específicado, drive en este caso
    """
    recurso = build('drive', 'v3', credentials=creds)

    # Devuelve el servicio para ser usado por diferentes programas
    return recurso



