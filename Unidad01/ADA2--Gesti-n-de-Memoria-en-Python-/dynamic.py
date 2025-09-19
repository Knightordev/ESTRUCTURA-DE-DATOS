class MemoriaDinamica:
    def __init__(self, fruits=[]):
        self.fruits = fruits
    def add_fruit(self, fruit):
        self.fruits.append(fruit)
    def remove_fruit(self, index):
        self.fruits.pop(index)
    def show_fruits(self):
        for fruta in self.fruits:
            print(fruta)
canasta = MemoriaDinamica([])
canasta.add_fruit("Mango")
canasta.add_fruit("Manzana")
canasta.add_fruit("Banana")
canasta.add_fruit("Uvas")
canasta.remove_fruit(0)
canasta.show_fruits()

