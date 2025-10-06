class Pila:
    def __init__(self):
        self.elementos = []  

    def esta_vacia(self):
        return len(self.elementos) == 0

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]

    def _str_(self):
        return str(self.elementos)

def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de {nombres[origen]} a {nombres[destino]}")
    else:
        hanoi(n - 1, origen, destino, auxiliar)
        hanoi(1, origen, auxiliar, destino)
        hanoi(n - 1, auxiliar, origen, destino)

origen = Pila()
auxiliar = Pila()
destino = Pila()

nombres = {origen: "Origen", auxiliar: "Auxiliar", destino: "Destino"}

for disco in range(3, 0, -1):
    origen.apilar(disco)

print("Estado inicial:")
print("Origen:", origen)
print("Auxiliar:", auxiliar)
print("Destino:", destino)
print("\nMovimientos:")

hanoi(3, origen, auxiliar, destino)

print("\nEstado final:")
print("Origen:", origen)
print("Auxiliar:", auxiliar)
print("Destino:",destino)