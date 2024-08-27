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

    # Función para obtener un nodo
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, value, index):
        """
        Inserta un nuevo nodo con un valor específico en una posición determinada de la lista enlazada.

        Parámetros:
        - value: El valor que se desea insertar en la lista enlazada.
        - index: La posición en la lista enlazada donde se quiere insertar el nuevo nodo.

        Retorno:
        - True si la inserción fue exitosa.
        - False si la inserción falló debido a un índice inválido.
        """
        # Verifica si el índice proporcionado es inválido (menor que 0 o mayor o igual a la longitud de la lista)
        if index < 0 or index >= self.length:
            return False

        # Si el índice es 0, inserta el valor al inicio de la lista usando el método prepend
        if index == 0:
            return self.prepend(value)

        # Si el índice es igual a la longitud de la lista, inserta el valor al final usando el método append
        if index == self.length:
            return self.append(value)

        # Crea un nuevo nodo con el valor proporcionado
        new_node = Node(value)

        # Obtiene el nodo que está en la posición anterior a donde se insertará el nuevo nodo
        temp = self.get(index - 1)

        # El nuevo nodo apunta su referencia next al nodo que originalmente estaba después de temp
        new_node.next = temp.next

        # El nodo temp ahora apunta su referencia next al nuevo nodo, insertándolo en la lista
        temp.next = new_node

        # Incrementa la longitud de la lista para reflejar la adición del nuevo nodo
        self.length += 1

        # Retorna True para indicar que la inserción se realizó con éxito
        return True


print('\nLista antes de insertar un nodo:')
my_linked_list = LinkedList(0)
my_linked_list.append(2)
my_linked_list.print_list()

print('\nLista después de insertar un nodo:')
my_linked_list.insert(1, 1)
my_linked_list.print_list()


print('\n======= Detalles de Linked List =========\n')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


