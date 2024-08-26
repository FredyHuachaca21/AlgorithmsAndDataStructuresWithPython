# Diferentes términos para los inputs - En la complejidad de un algoritmo, se pueden presentar diferentes términos para
# los inputs. Por ejemplo, si una función recibe dos parámetros a y b, y realiza una operación que depende de ambos
# parámetros, la complejidad de la función se puede expresar como O(a + b) o O(a * b), dependiendo de la operación que


"""
O(a + b) - Suma de Términos - Esta función tiene una complejidad de O(a + b), ya que el número de operaciones que
realiza es "LINEAL" respecto a la suma de los elementos que recibe como parámetro.
"""


def print_items(a, b):
    for i in range(a):
        print(i)

    for i in range(b):
        print(i)


# Ejemplo de uso
print(print_items(10, 5))

"""
O(a * b) - Producto de Términos - Esta función tiene una complejidad de O(a * b), ya que el número de operaciones que
realiza es "CUADRÁTICA" respecto al producto de los elementos que recibe como parámetro.
"""


def print_items2(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


# Ejemplo de uso
print(print_items2(10, 5))
