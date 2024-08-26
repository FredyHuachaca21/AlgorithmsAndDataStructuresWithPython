
# Drop Constants - Esto es una técnica de optimización que consiste en eliminar las constantes de un algoritmo.

# En el siguiente ejemplo, la función print_items tiene una complejidad de O(2n) ya que tiene dos ciclos for que
# recorren n elementos cada uno. Sin embargo, al aplicar la técnica de Drop Constants, se elimina la constante 2 y
# se simplifica a O(n).
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print(print_items(10))