# O(n^2 + n) - Drop Non-Dominants - Esta función tiene una complejidad de O(n^2 + n) ya que tiene dos ciclos for que
# recorren n elementos cada uno y un ciclo for adicional que recorre n elementos. Sin embargo, al aplicar la técnica de
# Drop Non-Dominants, se eliminan los términos no dominantes y se simplifica a O(n^2).

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


print(print_items(10))
