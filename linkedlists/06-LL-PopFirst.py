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
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
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


