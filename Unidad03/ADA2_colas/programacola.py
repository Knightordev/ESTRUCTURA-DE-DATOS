class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add_item(self, item):
        self.items.append(item)

    def out_item(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacía")
    def get_queue_len(self):
        return len(self.items)
class Queue_system:
    queue = Queue()
    ids = 0
    def add_client(self):
        self.ids += 1
        self.queue.add_item("C"+str(self.ids))
    def attend_client(self):
        if not self.queue.isEmpty():
            client = self.queue.out_item()
            print(f"Atendiendo al cliente {client}")
        else:
            print("No hay clientes en la cola")
    def aattend_spesial_client(self, client_id):
        if client_id in self.queue.items:
            self.queue.items.remove(client_id)
            print(f"Atendiendo al cliente especial {client_id}")
        else:
            print(f"El cliente {client_id} no está en la cola")
    def get_ids(self):
        return self.queue.items
def main():
    while True:
        print("SISTEMA DE COLAS \n C .- Agregar cliente \n E .- Atender cliente \n A .- Atender cliente con ID \n Q .- Salir")
        option = input("Seleccione una opción (C, E, A) o 'Q' para salir: ").upper()
        match(option):
            case 'C':
                system.add_client()
                print(f"Clientes en la cola: {system.get_ids()}")
            case 'E':
                system.attend_client()
                print(f"Clientes en la cola: {system.get_ids()}")
            case 'A':
                client_id = input("Ingrese el ID del cliente a atender (ejemplo: C1): ")
                system.aattend_spesial_client(client_id)
                print(f"Clientes en la cola: {system.get_ids()}")     
            case 'Q':
                print("Saliendo del sistema de colas.")
                break           
system = Queue_system()
main()