def fibonacci(n):
    a, b = 0, 1
    secuencia = []
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

print(fibonacci(100000))
