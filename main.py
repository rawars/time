import pytz

from datetime import datetime

# Obtener la zona horaria deseada
zona_horaria = pytz.timezone('America/Bogota')

# Obtener la hora actual en la zona horaria deseada
hora_actual = datetime.now(zona_horaria).time()

hora_usuario = input("Ingrese la hora en formato HH:MM: ")

# Crear un objeto de hora con las 18:00
hora_objetivo = datetime.strptime(hora_usuario, '%H:%M').time()

# Comparar la hora actual con la hora objetivo
if hora_actual > hora_objetivo:
    print(f"La hora actual ha pasado de las {hora_usuario} en la zona horaria America/Bogota.")
else:
    print(f"La hora actual es antes de las {hora_usuario} en la zona horaria America/Bogota.")
