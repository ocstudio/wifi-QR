import random
import string
import qrcode
import subprocess
import sys

def escanear_redes_wifi():
    # Comando para escanear redes WiFi en Linux y obtener las primeras 10 señales
    try:
        result = subprocess.run(['nmcli', '-f', 'SSID', 'dev', 'wifi', 'list'], capture_output=True, text=True)
        redes = result.stdout.splitlines()[1:11]  # Tomar solo las primeras 10 señales
        return [red.strip() for red in redes if red.strip()]
    except Exception as e:
        print(f"No se pudo escanear redes WiFi: {e}")
        return []

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generar_codigo_qr(nombre_wifi, contrasena):
    # Formato para generar el WiFi QR code
    wifi_config = f"WIFI:T:WPA;S:{nombre_wifi};P:{contrasena};;"

    # Crear el objeto QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Agregar los datos al QR Code
    qr.add_data(wifi_config)
    qr.make(fit=True)

    # Crear la imagen del QR Code
    qr_image = qr.make_image(fill='black', back_color='white')

    return qr_image

def seleccionar_red():
    redes = escanear_redes_wifi()
    if not redes:
        print("No se encontraron redes WiFi disponibles.")
        sys.exit(1)

    print("Selecciona la red WiFi a la cual quieres asignar la contraseña segura:")
    for i, red in enumerate(redes):
        print(f"{i + 1}. {red}")

    while True:
        try:
            opcion = int(input("Ingresa el número de la red WiFi: "))
            if 1 <= opcion <= len(redes):
                return redes[opcion - 1]
            else:
                print("Opción inválida. Ingresa un número válido.")
        except ValueError:
            print("Por favor, ingresa un número.")

if __name__ == "__main__":
    # Escanear y seleccionar la red WiFi
    nombre_wifi = seleccionar_red()

    # Solicitar longitud de la contraseña
    print("Selecciona la longitud de la contraseña (máximo 32 caracteres):")
    while True:
        try:
            longitud = int(input("Longitud deseada para la contraseña: "))
            if 1 <= longitud <= 32:
                break
            else:
                print("Longitud inválida. Ingresa un número entre 1 y 32.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Generar una contraseña segura con la longitud especificada
    contrasena_segura = generar_contrasena(longitud)
    print("Contraseña segura generada:", contrasena_segura)

    # Guardar la contraseña en un archivo de texto
    nombre_archivo_txt = "contrasena_wifi.txt"
    with open(nombre_archivo_txt, 'w') as archivo:
        archivo.write(f"Contraseña de WiFi ({nombre_wifi}): {contrasena_segura}\n")

    print(f"Contraseña guardada en {nombre_archivo_txt}")

    # Generar el código QR
    qr_image = generar_codigo_qr(nombre_wifi, contrasena_segura)

    # Guardar el código QR como imagen PNG
    nombre_archivo_qr = "codigo_qr_wifi.png"
    qr_image.save(nombre_archivo_qr)

    print(f"Código QR generado y guardado como {nombre_archivo_qr}")

    # Mensaje final
    print("¡Disfruta de tu contraseña segura! \U0001F680")
