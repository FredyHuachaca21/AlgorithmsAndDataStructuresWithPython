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

    # Función para agregar un nodo al principio de la lista
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    # Función para obtener un nodo
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # Función para remover un nodo
    def remove(self, index):
        """
        Elimina y retorna el nodo en una posición específica de la lista enlazada.

        Parámetros:
        - index: La posición del nodo que se desea eliminar de la lista enlazada.

        Retorno:
        - El nodo eliminado si la operación fue exitosa.
        - None si el índice es inválido.
        """
        # Verifica si el índice es inválido (menor que 0 o mayor o igual a la longitud de la lista)
        if index < 0 or index >= self.length:
            return None  # Retorna None si el índice es inválido

        # Si el índice es 0, elimina el primer nodo usando pop_first y retorna ese nodo
        if index == 0:
            return self.pop_first()

        # Si el índice es el último nodo de la lista, elimina el último nodo usando pop y retorna ese nodo
        if index == self.length - 1:
            return self.pop()

        # Obtiene el nodo anterior al que se va a eliminar
        prev_node = self.get(index - 1)

        # El nodo a eliminar es el siguiente del nodo anterior obtenido
        temp = prev_node.next

        # El nodo anterior ahora apunta al siguiente nodo del que se va a eliminar
        prev_node.next = temp.next

        # Desconecta el nodo eliminado de la lista
        temp.next = None

        # Decrementa la longitud de la lista en 1
        self.length -= 1

        # Retorna el nodo eliminado
        return temp


print('\nAntes de remover un nodo:')
my_linked_list = LinkedList(11)
my_linked_list.append(12)
my_linked_list.append(13)
my_linked_list.append(14)
my_linked_list.print_list()

print('\nDespués de remover un nodo:')
nodeRemoved = my_linked_list.remove(1)
my_linked_list.print_list()

print('\nImprime el nodo eliminado:')
print(nodeRemoved.value)


print('\n======= Detalles de Linked List =========\n')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


