
# n*n = n^2 -> O(n^2) - Esta función tiene una complejidad de O(n^2) ya que el número de operaciones que realiza es
# "PROPORCIONAL" al cuadrado del número de elementos que recibe como parámetro.

# En el siguiente ejemplo, la función print_items tiene una complejidad de O(n^2) ya que tiene dos ciclos for que
# recorren n elementos cada uno. Esto significa que el número total de operaciones que realiza es n * n = n^2.
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print(print_items(10))
