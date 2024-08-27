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
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # Función para cambiar el valor de un nodo
    def set(self, index, value):
        """
        Actualiza el valor de un nodo existente en una posición específica de la lista enlazada.

        Parámetros:
        - index: La posición en la lista enlazada donde se quiere actualizar el valor del nodo.
        - value: El nuevo valor que se asignará al nodo en la posición especificada.

        Retorno:
        - True si la actualización fue exitosa.
        - False si no se pudo realizar la actualización (por ejemplo, si el índice es inválido).
        """
        # Obtiene el nodo en la posición especificada usando el método get
        temp = self.get(index)

        # Verifica si el nodo existe (temp no es None)
        if temp:
            # Si el nodo existe, actualiza su valor con el valor proporcionado
            temp.value = value
            return True  # Retorna True indicando que la actualización fue exitosa

        # Si el nodo no existe (temp es None), retorna False indicando que la actualización falló
        return False


print('\nLista antes de cambiar el valor del nodo:')
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print(my_linked_list.print_list())

print('\nLista después de cambiar el valor del nodo:')
my_linked_list.set(1, 4)
print(my_linked_list.print_list())


print('\n======= Detalles de Linked List =========\n')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


