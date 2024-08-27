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

    def reverse(self):
        """
        Invierte el orden de los nodos en la lista enlazada.

        Este método transforma la lista enlazada de modo que el primer nodo se convierta en el último,
        el segundo nodo en el penúltimo, y así sucesivamente. Al final del proceso, la cabeza (head) y
        la cola (tail) se intercambian.

        Este proceso se realiza recorriendo la lista una sola vez y ajustando las referencias 'next' de cada nodo
        para que apunten al nodo anterior en lugar del siguiente.
        """
        # Inicializa temp con el nodo que actualmente es la cabeza de la lista
        temp = self.head

        # Intercambia la cabeza con la cola para reflejar la inversión de la lista
        self.head = self.tail
        self.tail = temp

        # Inicializa after como el nodo que sigue a temp, y before como None (no hay nodo anterior al primero)
        after = temp.next
        before = None

        # Recorre la lista invirtiendo las referencias 'next' de cada nodo
        for _ in range(self.length):
            # Guarda la referencia al siguiente nodo para continuar el recorrido después de invertir
            after = temp.next

            # Invierte la referencia 'next' del nodo actual para que apunte al nodo anterior
            temp.next = before

            # Mueve el puntero 'before' al nodo actual (temp) antes de avanzar
            before = temp

            # Avanza el puntero 'temp' al siguiente nodo (after) para continuar el proceso
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print('\nImprimiendo la lista original:')
my_linked_list.print_list()

print('\nImprimiendo la lista invertida:')
my_linked_list.reverse()
my_linked_list.print_list()


print('\n======= Detalles de Linked List =========\n')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


