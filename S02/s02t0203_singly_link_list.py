#IMportando clase Node
from s02t0201_Likend_List import Node

#Creando la clase de una listaenlazada
class SinglyLinkdList:
    #Contructor 
    def __int__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # Medo de insercion de Nnofdo en la lista
    def append (self,data):
        # Creo el nodo
        new_node = Node(data)

        # Si hay un Tail, el nuevo nodo
        # Pasa a ser le nuevo Tail
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node

        #Si no hay tail 
        else:
            self.tail = new_node
            self.head = new_node

        #Se increnta  size en 1
        self.size += 1 

    #Isertando en posicion intermedia
    # supangamos que la lista esta:
    # [A -> B -> C]
    # [0    1    2]
    # size = 3
    def append_at_location(self, data, index):
        if index < 1 or index > self.size + 1:
            raise IndexError(f"Indice {index} fuera de rango")

        #Crear un nuevo nodo 
        new_node = Node(data)

        #Insetar al inicio
        if  index == 1:
            new_node.next = self.head
            self.head = new_node
            if self.tail == None:
                self.tail = new_node
            #Incremento el 1 el tamano
            self.size += 1

        #Creando cariables de control 
        #para las inserciones intermedias
        current = self.head
        prev = None
        position = 1


        # Traversal (Recorrido)
        while current is not None and position < index:
            prev = current 
            current = current.next
            position += 1

            #Lleganod a la posicion 
            #EStoy al final?

        if current is None:
            prev.next = new_node
            self.tail = new_node
            self.size += 1
            return

        #si llegamos a un posicion
        #intermedia 
        #🚩 TODO: Pendiente en terminar  🚩

#1 Creo funcion principall
def main():
    #Creando una istancia de una lista enlazada
    my_list = SinglyLinkdList()
    #Agregando elemento a la lista
    my_list.appped(30) 
    my_list.appped(59)
    my_list.appped(80)
    my_list.appped(100)

    #Recorrer la lista
    for value in my_list.head.iter():
        print (f"{value},", end=" ")
    print ()

#Evaluoel valor de __name__
if __name__ == "__main__":
    main()