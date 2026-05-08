
# graficas.py - Genera UNA SOLA figura con la comparación visual de población
#               y área de los países consultados (gráfico de barras doble).


import matplotlib.pyplot as plt
from utils import formatear_numero  # reciclamos la función de utils


# Colores base para las barras (se usan los necesarios según cantidad de países)
COLORES = ["#2196F3", "#4CAF50", "#FF9800", "#9C27B0",
           "#F44336", "#00BCD4", "#FFEB3B", "#795548"]


def _extraer_datos(lista_info):
    """
    Función interna que extrae nombres, poblaciones y áreas de la lista
    de diccionarios.
    Retorna tres listas: nombres, poblaciones, areas.
    """
    nombres = []
    poblaciones = []
    areas = []
    for pais in lista_info:
        nombres.append(pais["nombre"])
        poblaciones.append(pais["poblacion"])
        areas.append(pais["area"])
    return nombres, poblaciones, areas


def _poner_etiquetas(barras):
    """
    Coloca el valor numérico formateado encima de cada barra.
    Se reutiliza para la gráfica de población y la de área.
    """
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2,
                 altura,
                 formatear_numero(int(altura)),
                 ha="center", va="bottom", fontsize=8, fontweight="bold")


def generar_grafica_comparativa(lista_info):
    """
    Crea UNA SOLA figura (ventana) con dos gráficos de barras:
      - Izquierda: comparación de población
      - Derecha:   comparación de área
    """
    nombres, poblaciones, areas = _extraer_datos(lista_info)
    colores_usados = COLORES[:len(nombres)]

    # Figura con 2 subplots lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # --- Subplot 1: Población ---
    barras1 = ax1.bar(nombres, poblaciones, color=colores_usados, # PRIMERA GRAFICA SOLO PARA POBLACION definimos el color las lineas etc
                      edgecolor="black", linewidth=0.5) 
    ax1.set_title("Población", fontsize=13, fontweight="bold") #agreamos el titulo
    ax1.set_ylabel("Habitantes") #ponemos de lado izq de la grafica que hablamos de habitantes
    ax1.ticklabel_format(axis="y", style="plain")
    ax1.tick_params(axis="x", rotation=20) # rotamos las etiquetas pa que se vea perron 
    ax1.grid(axis="y", alpha=0.3, linestyle="--")
    # Reutilizamos la función de etiquetas
    plt.sca(ax1)
    _poner_etiquetas(barras1) # es solo poner el numerito mero arriba

    # --- Subplot 2: Área ---
    barras2 = ax2.bar(nombres, areas, color=colores_usados, #aqui emepezamos con la 2da grafica 
                      edgecolor="black", linewidth=0.5)
    ax2.set_title("Área", fontsize=13, fontweight="bold") # agergamos el titulo
    ax2.set_ylabel("km²") #ponemos de lado izq que hablamos de km ²
    ax2.ticklabel_format(axis="y", style="plain")
    ax2.tick_params(axis="x", rotation=20) # rotamos las etiquetas pa que se vea perron 
    ax2.grid(axis="y", alpha=0.3, linestyle="--")
    plt.sca(ax2)
    _poner_etiquetas(barras2) # ponermos el numerito mero arriba

    # Título general de la figura
    fig.suptitle("Comparación de Países", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()
