# api.py - Conexión con la API REST Countries (https://restcountries.com/)
# obtiene: nombre, población y área de cada país.


import requests

# URL base de la API v3.1 para buscar países por nombre
URL_BASE = "https://restcountries.com/v3.1/name/"


def obtener_datos_pais(nombre_pais):
    """
    Consulta la API y retorna un diccionario con nombre, poblacion y area.
    Si hay cualquier error (conexión, país no encontrado, etc.), retorna None.
    """
    url = URL_BASE + nombre_pais # el mas es para la concatenacion y se busque la ruta directa por ejemplo si queremos mexico quedaria https://restcountries.com/v3.1/name/mexico

    try: #intentamos si no hay error
        respuesta = requests.get(url, timeout=10) #

        if respuesta.status_code == 200: #significa que si respondio la api correctamente 
            datos = respuesta.json()
            pais = datos[0]

            # Solo extraemos los 3 campos que necesitamos
            info = {
                "nombre": pais.get("name", {}).get("common", "Desconocido"),
                "poblacion": pais.get("population", 0),
                "area": pais.get("area", 0)  # área en km²
            }
            return info

        elif respuesta.status_code == 404: #error de no encontro la ruta (pais mal escrito , no base de datos etc)
            print(f"  [!] País no encontrado: '{nombre_pais}'")
            return None
        else: #cualquier otro numero de respuesta 
            print(f"  [!] Error de la API (código {respuesta.status_code})")
            return None

    except requests.exceptions.ConnectionError: #tipos de errores que puede tirar el try
        print("  [!] Error de conexión a internet.")
        return None
    except requests.exceptions.Timeout: #tipos de errores que puede tirar el try
        print("  [!] La petición tardó demasiado.")
        return None
    except requests.exceptions.RequestException as e: #tipos de errores que puede tirar el try
        print(f"  [!] Error: {e}")
        return None
