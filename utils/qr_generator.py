import qrcode
import os
from datetime import datetime

def generar_qr(texto: str) -> str:
    # Crear carpeta si no existe
    carpeta = "qr"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Nombre único del archivo
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"qr_{timestamp}.png"
    filepath = os.path.join(carpeta, filename)

    # Crear QR
    img = qrcode.make(texto)
    img.save(filepath)

    # Devolver SOLO la ruta para guardarla en la BD
    return filepath
