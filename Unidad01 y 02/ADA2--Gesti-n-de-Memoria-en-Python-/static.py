class MemoriaEstatica:
    calificaciones = [0] * 5
    @staticmethod
    def main():
        for i in range(5):
            calificacion = int(input(f"Ingresa la calificación {i + 1}: "))
            MemoriaEstatica.calificaciones[i] = calificacion

MemoriaEstatica.main()