
# main.py - Sistema de Consulta y Comparacion de Paises
# Flujo: bienvenida -> ingresar paises -> consultar API -> validar -> mostrar -> grafica


from api import obtener_datos_pais
from utils import validar_cantidad_paises, ingresar_paises, mostrar_resultados
from graficas import generar_grafica_comparativa


def consultar_paises(lista_nombres):
    """
    Recibe lista de nombres, consulta la API para cada uno.
    Retorna lista de diccionarios con los paises encontrados.
    """
    info = [] #crea la lista 
    print("\nConsultando API...") #print estetico 
    for nombre in lista_nombres:	#recorre cada pais de la lista 
        resultado = obtener_datos_pais(nombre)
        if resultado is not None: # si el resultado NO esta vacio 
            info.append(resultado) #Lo agrega a la lista de info
            print(f"  [OK] {resultado['nombre']}")
    return info


def main():
    """Orquesta el flujo completo del programa."""

    # 1. Pedir paises al usuario (la funcion ya valida minimo 2 internamente)
    paises = ingresar_paises()

    # 2. Consultar la API
    info = consultar_paises(paises)

    # 3. Validar que se encontraron al menos 2 paises
    if not validar_cantidad_paises(info):
        return

    # 4. Mostrar resultados en consola
    mostrar_resultados(info)

    # 5. Generar grafica comparativa de poblacion y area
    print("Generando grafica...")
    generar_grafica_comparativa(info)
    print("Fin del programa.")


# --- Punto de entrada ---
if __name__ == "__main__":
    print("=== SISTEMA DE CONSULTA Y COMPARACION DE PAISES ===")
    main()
