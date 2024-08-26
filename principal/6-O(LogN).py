# O(log n) - Logarithmic Time - Esta función tiene una complejidad de O(log n) ya que el número de operaciones que
# realiza es "LOGARÍTMICO" respecto al número de elementos que recibe como parámetro.

def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Complejidad temporal: O(log n)
    La búsqueda binaria tiene una complejidad logarítmica porque en cada
    iteración se reduce a la mitad el espacio de búsqueda. Esto resulta
    en un máximo de log2(n) pasos para encontrar el elemento o determinar
    que no está presente, donde n es el número de elementos en la lista.
    """
    izquierda = 0
    derecha = len(lista) - 1
    pasos = 0

    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1, pasos


# Ejemplo de uso
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8]
elemento_buscado = 1

resultado, pasos_tomados = busqueda_binaria(lista_ordenada, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el índice {resultado}")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista")

print(f"La búsqueda tomó {pasos_tomados} pasos")



