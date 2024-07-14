import json

# Cargar el JSON original
with open('comunas-regiones.json', 'r', encoding='utf-8') as f:
    comunas_regiones = json.load(f)

# Listas para las regiones y comunas
regiones = []
comunas = []

# Contadores para las claves primarias
pk_region = 1
pk_comuna = 1

# Iterar sobre las regiones y comunas en el JSON original
for region_entry in comunas_regiones['regiones']:
    # Crear un diccionario para la región
    region = {
        "model": "inmuebles.Region",
        "pk": pk_region,
        "fields": {
            "nombre": region_entry["region"]
        }
    }
    regiones.append(region)  # Añadir la región a la lista de regiones

    # Iterar sobre las comunas de la región actual
    for comuna_name in region_entry["comunas"]:
        # Crear un diccionario para la comuna
        comuna = {
            "model": "inmuebles.Comuna",
            "pk": pk_comuna,
            "fields": {
                "nombre": comuna_name,
                "region": pk_region  # Clave foránea a la región
            }
        }
        comunas.append(comuna)  # Añadir la comuna a la lista de comunas
        pk_comuna += 1  # Incrementar el contador de claves primarias para comunas

    pk_region += 1  # Incrementar el contador de claves primarias para regiones

# Guardar los datos formateados en archivos JSON
with open('regiones.json', 'w', encoding='utf-8') as f:
    json.dump(regiones, f, ensure_ascii=False, indent=4)

with open('comunas.json', 'w', encoding='utf-8') as f:
    json.dump(comunas, f, ensure_ascii=False, indent=4)

print("Archivos regiones.json y comunas.json creados exitosamente.")
