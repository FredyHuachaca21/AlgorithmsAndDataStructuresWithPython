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

    # Función para eliminar el primer nodo de la lista
    def pop_first(self):
        """
        Elimina y retorna el primer nodo de la lista enlazada.

        Retorno:
        - El nodo eliminado si la lista no está vacía.
        - None si la lista está vacía.
        """
        # Verifica si la lista está vacía (longitud igual a 0)
        if self.length == 0:
            return None  # Retorna None si la lista está vacía

        # Guarda temporalmente el nodo cabeza (el primer nodo)
        temp = self.head

        # Mueve la cabeza al siguiente nodo en la lista
        self.head = self.head.next

        # Desconecta el nodo eliminado de la lista
        temp.next = None

        # Decrementa la longitud de la lista en 1
        self.length -= 1

        # Si la lista quedó vacía después de eliminar el primer nodo, ajusta la cola (tail) a None
        if self.length == 0:
            self.tail = None

        # Retorna el nodo eliminado
        return temp


my_linked_list = LinkedList(2)
my_linked_list.append(1)


# (2) Items -> Return 2 Node
print(my_linked_list.pop_first().value)
# (1) Item -> Return 1 Node
print(my_linked_list.pop_first().value)
# None -> Return None
print(my_linked_list.pop_first())

print('\n================\n')
print('Head:', my_linked_list.head)
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)


