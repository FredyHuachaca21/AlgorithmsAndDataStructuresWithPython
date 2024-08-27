class Node:
    # Constructor
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # Constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Función para imprimir la lista
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Función para agregar un nodo
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Función para obtener un nodo
    def get(self, index):
        """
        Retorna el nodo en una posición específica de la lista enlazada.

        Parámetros:
        - index: La posición del nodo que se desea obtener en la lista enlazada.

        Retorno:
        - El nodo en la posición especificada si el índice es válido.
        - None si el índice es inválido (menor que 0 o mayor o igual que la longitud de la lista).
        """
        # Verifica si el índice es inválido (menor que 0 o mayor o igual a la longitud de la lista)
        if index < 0 or index >= self.length:
            return None  # Retorna None si el índice es inválido

        # Comienza desde el nodo cabeza (head) de la lista
        temp = self.head

        # Recorre la lista desde la cabeza hasta el índice especificado
        for _ in range(index):
            temp = temp.next  # Avanza al siguiente nodo

        # Retorna el nodo en la posición especificada
        return temp


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2).value)


print('\n================\n')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


