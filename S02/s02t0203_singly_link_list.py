#IMportando clase Node
from s02t0201_Likend_List import Node

#Creando la clase de una listaenlazada
class SinglyLinkdList:
    #Contructor 
    def __int__(self):
        self.head = None
    # Medo de insercion de Nnofdo en la lista
    def append (self,data):
        # Creo el nodo
        new_node = Node(data)
        # Si la lista esta vacia
        # Apuntamos el head al nuevo mucndo
        # Que se creo
        if not self.head:
            self.hand = new_node
            return
        #Si la lista no esta vacia, hay
        #que recorrer el nodo hasta llegar
        #al final de la lista

        #Estableciendo el nodo actual
        #como el primero en la lista
        current_node = self.head
        while current_node.next:
            current_node = current_node.text
        #Que hacemos ahora ?
        current_node.next = new_node


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