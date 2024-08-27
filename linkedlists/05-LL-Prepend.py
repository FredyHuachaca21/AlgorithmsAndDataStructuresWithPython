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
        """
        Inserta un nuevo nodo al principio de la lista enlazada.

        Parámetros:
        - value: El valor que se desea asignar al nuevo nodo.

        Retorno:
        - True para indicar que la operación de inserción fue exitosa.
        """
        # Crea un nuevo nodo con el valor proporcionado
        new_node = Node(value)

        # Si la lista está vacía (head es None), establece tanto head como tail al nuevo nodo
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Si la lista no está vacía, enlaza el nuevo nodo al inicio de la lista
            new_node.next = self.head
            # Actualiza head para que apunte al nuevo nodo
            self.head = new_node

        # Incrementa la longitud de la lista en 1
        self.length += 1

        # Retorna True para indicar que la operación fue exitosa
        return True


my_linked_list = LinkedList(2)
my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()

print('\n================\n')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


