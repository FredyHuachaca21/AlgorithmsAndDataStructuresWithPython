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

    # Función para agregar un nodo
    def pop(self):
        """
        Elimina y retorna el último nodo de la lista enlazada.

        Retorno:
        - El nodo eliminado si la lista no está vacía.
        - None si la lista está vacía.
        """
        # Verifica si la lista está vacía (longitud igual a 0)
        if self.length == 0:
            return None  # Retorna None si la lista está vacía

        # Inicializa dos punteros: temp para recorrer la lista y pre para mantener el nodo anterior a temp
        temp = self.head
        pre = self.head

        # Recorre la lista hasta llegar al último nodo (donde temp.next es None)
        while temp.next is not None:
            pre = temp  # pre sigue a temp
            temp = temp.next  # temp avanza al siguiente nodo

        # Actualiza tail para que apunte al nodo pre, que será el nuevo último nodo
        self.tail = pre
        self.tail.next = None  # Desconecta el último nodo (temp) de la lista

        # Decrementa la longitud de la lista en 1
        self.length -= 1

        # Si la lista queda vacía después de la eliminación, ajusta head y tail a None
        if self.length == 0:
            self.head = None
            self.tail = None

        # Retorna el nodo eliminado
        return temp


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Return 2 Nodes
print(my_linked_list.pop().value)
# (1) Item - Return 1 Node
print(my_linked_list.pop().value)
# None - Return None
print(my_linked_list.pop())

print('\n================\n')
print('Head:', my_linked_list.head)
print('Tail:', my_linked_list.tail)
print('Length:', my_linked_list.length)


