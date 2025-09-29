class pilas():
    def __init__(self):
        self.pila = []

    def isImpty(self):
        return len(self.pila) == 0
    
    def push(self, value):
        self.pila.append(value)

    def pop_pila(self):
        if not self.isImpty():
            return self.pila.pop()
        else:
            return "pila is empty"
    
    def peek(self):
        if not self.isImpty():
            return self.pila[-1]
        else:
            return "pila is empty"
        
pila  = pilas()
pila.push(1)
pila.push(2)
pila.push(3)
pila.pop_pila()
pila.peek()
print(pila.pila)