class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar_al_final(self, data):
        nuevo_nodo = Node(data)
        if not self.head:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            nuevo_nodo.prev = self.tail
            self.tail = nuevo_nodo

    def eliminar_nodo(self, data):
        nodo_actual = self.head
        while nodo_actual:
            if nodo_actual.data == data:
                if nodo_actual.prev:
                    nodo_actual.prev.next = nodo_actual.next
                else:
                    self.head = nodo_actual.next

                if nodo_actual.next:
                    nodo_actual.next.prev = nodo_actual.prev
                else:
                    self.tail = nodo_actual.prev

                return True
            nodo_actual = nodo_actual.next
        return False

    def insertar_nodo(self, data, pos):
        nuevo_nodo = Node(data)
        if pos == 0:
            nuevo_nodo.next = self.head
            self.head.prev = nuevo_nodo
            self.head = nuevo_nodo
        else:
            nodo_actual = self.head
            index = 0
            while nodo_actual and index < pos - 1:
                nodo_actual = nodo_actual.next
                index += 1
            if nodo_actual:
                nuevo_nodo.prev = nodo_actual
                nuevo_nodo.next = nodo_actual.next
                nodo_actual.next = nuevo_nodo
                if nuevo_nodo.next:
                    nuevo_nodo.next.prev = nuevo_nodo
                else:
                    self.tail = nuevo_nodo
            else:
                self.agregar_al_final(data)

    def imprimir_lista(self):
        nodo_actual = self.head
        while nodo_actual:
            print(nodo_actual.data, end=" -> ")
            nodo_actual = nodo_actual.next
        print("None")
        
lista = ListaDoblementeEnlazada()
lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
lista.imprimir_lista()

lista.eliminar_nodo(2)
lista.imprimir_lista()

lista.insertar_nodo(4, 1)
lista.imprimir_lista()