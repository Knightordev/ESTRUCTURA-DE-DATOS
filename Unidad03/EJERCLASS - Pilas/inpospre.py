class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]


def precedencia(operador):
    if operador in ('+', '-'):
        return 1
    if operador in ('*', '/'):
        return 2
    return 0


def infijo_a_posfijo(expresion):
    pila = Pila()
    salida = []

    for token in expresion.split():
        if token.isdigit():
            salida.append(token)
        elif token == '(':
            pila.apilar(token)
        elif token == ')':
            while not pila.esta_vacia() and pila.ver_tope() != '(':
                salida.append(pila.desapilar())
            pila.desapilar()
        else:
            while (not pila.esta_vacia() and precedencia(pila.ver_tope()) >= precedencia(token)):
                salida.append(pila.desapilar())
            pila.apilar(token)
    
    while not pila.esta_vacia():
        salida.append(pila.desapilar())

    return " ".join(salida)


def infijo_a_prefijo(expresion):
    pila = Pila()
    salida = []
    expresion = expresion[::-1].split()

    for i in range(len(expresion)):
        if expresion[i] == '(':
            expresion[i] = ')'
        elif expresion[i] == ')':
            expresion[i] = '('
    
    for token in expresion:
        if token.isdigit():
            salida.append(token)
        elif token == '(':
            pila.apilar(token)
        elif token == ')':
            while pila.ver_tope() != '(':
                salida.append(pila.desapilar())
            pila.desapilar()
        else:
            while (not pila.esta_vacia() and precedencia(pila.ver_tope()) >= precedencia(token)):
                salida.append(pila.desapilar())
            pila.apilar(token)

    while not pila.esta_vacia():
        salida.append(pila.desapilar())

    return " ".join(salida[::-1])

expresion_infija = "3 + 4 * 2 / ( 1 - 5 )"


expresion_posfija = infijo_a_posfijo(expresion_infija)
expresion_prefija = infijo_a_prefijo(expresion_infija)

print(f"Expresión infija: {expresion_infija}")
print(f"Expresión posfija: {expresion_posfija}")
print(f"Expresión prefija: {expresion_prefija}")
