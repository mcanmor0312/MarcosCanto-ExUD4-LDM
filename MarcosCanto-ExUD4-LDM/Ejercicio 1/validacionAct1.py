import json
from datetime import datetime

def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print(f"JSON inválido: {error}")
        return False

def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# Datos JSON a validar como una cadena
json_data = """
{
    "nombre": "Juan",
    "fecha_nacimiento": "15-02-2000"
}
"""

if json_validator(json_data):
    data = json.loads(json_data)

    if "fecha_nacimiento" in data:
        if validate_date_format(data["fecha_nacimiento"]):
            print("Fecha de nacimiento válida")
        else:
            print("Fecha de nacimiento inválida")
    else:
        print("No se encontró la clave 'fecha_nacimiento' en el JSON")
else:
    print("El JSON proporcionado no es válido.")
