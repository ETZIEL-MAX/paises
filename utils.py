
# utils.py - Funciones auxiliares: ingreso de datos, validacion y visualizacion.



def validar_cantidad_paises(lista_paises):
    """
    valida "al menos 2 elementos" en todo el proyecto.
    Se recicla en ingresar_paises() y en main().
    Retorna True si la lista tiene 2 o mas elementos, False si no.
    """
    if len(lista_paises) < 2:
        print(f"  [X] Se necesitan al menos 2 paises. Solo hay {len(lista_paises)}.")
        return False
    return True


def ingresar_paises():
    """
    Pregunta cuantos paises comparar, pide sus nombres y retorna la lista.
    Recicla validar_cantidad_paises() 
    """
    # while externo: se repite hasta que el usuario ingrese >= 2 paises validos
    while True:
        # Preguntar la cantidad, manejar entradas no numericas
        while True:
            try: #intenta ejecutar esto
                cantidad = int(input("\nCuantos paises quieres comparar? (minimo 2): "))
                break
            except ValueError: #si fallo lo anterior significa que 
                print("  [!] Ingresa un numero valido.")

        # Pedir cada nombre, no aceptar vacios
        paises = []
        for i in range(1, cantidad + 1):
            while True:
                nombre = input(f"  Pais #{i}: ").strip()
                if nombre == "":
                    print("  [!] El nombre no puede estar vacio.")
                    continue
                paises.append(nombre.lower())
                break

        # Reciclamos validar_cantidad_paises (unica fuente de verdad para ">= 2")
        if validar_cantidad_paises(paises):
            return paises
        # Si no paso la validacion, el while externo repite todo el proceso


def formatear_numero(numero):
    """Convierte un numero a texto con separadores de miles. Ej: 5000000 -> '5,000,000'"""
    return f"{int(numero):,}"


def mostrar_resultados(lista_info):
    """Muestra nombre, poblacion y area de cada pais en consola."""
    print("\n--- RESULTADOS ---")
    for pais in lista_info:
        print(f"  {pais['nombre']}")
        print(f"    Poblacion: {formatear_numero(pais['poblacion'])} hab.")
        print(f"    Area:      {formatear_numero(pais['area'])} km2")
    print("-" * 30)
