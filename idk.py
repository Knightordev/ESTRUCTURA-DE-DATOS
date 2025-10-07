import time
import string

def simular_abecedario_signal():
    print("Iniciando la secuencia del ABECEDARIO con SIGNAL...\n")
    
    letras = string.ascii_lowercase
    i = 0
    SIGNAL = True  # CONTROL: solo avanza mientras SIGNAL = True

    while i < len(letras):
        while SIGNAL:  # Mientras SIGNAL es True, la secuencia avanza
            letra = letras[i]
            print(f"Abecedario: {letra}", flush=True)
            time.sleep(1)

            # Letras donde hacemos WAIT
            if letra == 'e':
                print("⏸ WAIT inicial de Emma\n")
                SIGNAL = False  # Detenemos la secuencia
            elif letra == 'g':
                print("⏸ WAIT inicial de Gadiel\n")
                SIGNAL = False
            elif letra == 'm':
                print("⏸ WAIT inicial de Maximo\n")
                SIGNAL = False
            elif letra == 's':
                print("⏸ WAIT inicial de Sofia\n")
                SIGNAL = False

            i += 1  # Avanzamos a la siguiente letra

        # Cuando SIGNAL = False, hacemos WAIT
        if not SIGNAL:
            print("⏸ SIGNAL detenido, esperando para continuar...")
            time.sleep(2)  # simulamos espera
            SIGNAL = True  # reactivamos la secuencia

    print("\n>> Abecedario completado.")

# Ejecución principal
if __name__ == "__main__":
    simular_abecedario_signal()
    print("\nSimulación finalizada.")
    print("\n" + "="*50 + "\n")
    print("""
    L         IIIII   SSSS   TTTTT    OOO
    L           I    S         T     O   O
    L           I     SSS      T     O   O
    L           I        S     T     O   O
    LLLLL     IIIII   SSSS     T      OOO
    """)
    print("\n" + "="*50)
