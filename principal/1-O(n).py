# O(n) - Esta función tiene una complejidad de O(n) ya que el número de operaciones que realiza es "PROPORCIONAL"
# al número de elementos que recibe como parámetro.

def print_items(n):
    for i in range(n):
        print(i)


# Otras posibles soluciones:

def print_items2(n):
    i = 0
    while i < n:
        print(i)
        i += 1


def print_items3(n):
    for i in list(range(n)):
        print(i)


def print_items4(n):
    for i in iter(range(n)):
        print(i)


def print_items5(n):
    _ = [print(i) for i in range(n)]


def print_items6(n):
    _ = list(map(print, range(n)))


print_items6(10)
