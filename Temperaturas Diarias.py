import random


def generar_temperaturas(ciudades, dias, semanas):
    """
    Genera una matriz 3D con temperaturas aleatorias entre 25 y 36 grados Celsius.
    Cada ciudad tiene una lista de temperaturas para cada semana y cada día.

    Argumentos:
    ciudades -- Lista de nombres de las ciudades.
    dias -- Lista de días de la semana.
    semanas -- Número de semanas para las cuales se generan las temperaturas.

    Retorna:
    Una lista 3D con las temperaturas generadas aleatoriamente.
    """

    return [[[random.randint(25, 36) for _ in dias] for _ in range(semanas)] for _ in ciudades]


def calcular_promedios(temperaturas, ciudades, dias, semanas):
    """
    Calcula el promedio de temperatura para cada ciudad, sumando las temperaturas de
    todos los días de cada semana y dividiendo por el número de días.

    Argumentos:
    temperaturas -- Matriz 3D que contiene las temperaturas por ciudad, semana y día.
    ciudades -- Lista de nombres de las ciudades.
    dias -- Lista de días de la semana.
    semanas -- Número de semanas de datos disponibles.

    Retorna:
    Un diccionario con la ciudad como clave y la lista de promedios de temperatura por semana.
    """
    promedios_ciudades = {}

    for i, ciudad in enumerate(ciudades):
        promedios = []  # Lista para almacenar los promedios de cada semana
        for j in range(semanas):
            suma = sum(temperaturas[i][j])  # Suma de las temperaturas de la semana
            promedio = suma / len(dias)  # Calculando el promedio para la semana
            promedios.append(promedio)
        promedios_ciudades[ciudad] = promedios  # Guardamos los promedios de la ciudad

    return promedios_ciudades


def main():
    # Datos de entrada
    ciudades = ["Quito", "Guayaquil", "Cuenca"]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    semanas = 5  # Definimos 5 semanas de datos

    # Generar datos de temperaturas aleatorias
    temperaturas = generar_temperaturas(ciudades, dias, semanas)

    # Calcular promedios de temperaturas
    promedios = calcular_promedios(temperaturas, ciudades, dias, semanas)

    # Mostrar resultados
    for ciudad, promedios_semana in promedios.items():
        print(f"Ciudad: {ciudad}")
        for semana_num, promedio in enumerate(promedios_semana, start=1):
            print(f"  Semana {semana_num}: Promedio de temperatura = {promedio:.2f}°C")
        print("-")


if __name__ == "__main__":
    main()
