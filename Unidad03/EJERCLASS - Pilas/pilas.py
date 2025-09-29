class pilas():
    def __init__(self):
        self.pila = []

    def isEmpty(self):
        return len(self.pila) == 0
    
    def push(self, value):
        self.pila.append(value)

    def pop_pila(self):
        if not self.isEmpty():
            return self.pila.pop()
        else:
            return "pila is empty"
    
    def peek(self):
        if not self.isEmpty():
            return self.pila[-1]
        else:
            return "pila is empty"
        
pilaUno  = pilas()
pilaUno.push(1)
pilaUno.push(2)
pilaUno.push(3)
pilaUno.pop_pila()
pilaUno.peek()
print(pilaUno.pila)