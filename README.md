# Generador de Contraseña Segura para WiFi

Este proyecto es un script en Python que permite generar contraseñas seguras para redes WiFi, escanear las redes disponibles, seleccionar una de ellas, generar un código QR y guardar la contraseña en un archivo de texto.

## Características

- Escanea las primeras 10 redes WiFi disponibles.
- Permite seleccionar una red WiFi de la lista.
- Genera una contraseña segura con una longitud definida por el usuario (hasta 32 caracteres).
- Crea un código QR con la configuración de la red WiFi y la nueva contraseña.
- Guarda la contraseña generada en un archivo de texto (`contrasena_wifi.txt`).
- Guarda el código QR en una imagen PNG (`codigo_qr_wifi.png`).

## Requisitos

- Python 3.x
- `qrcode` y `Pillow` para generar el código QR
- `nmcli` para escanear redes WiFi en Linux
  
pip install pyqrcode pip install pillow

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/GeneradorContrasenaWiFi.git
   cd GeneradorContrasenaWiFi
