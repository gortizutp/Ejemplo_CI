def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n < 0:
        raise ValueError("No existe factorial de un número negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


if __name__ == "__main__":
    print("Suma 2 + 3 =", sumar(2, 3))
    print("Resta 5 - 2 =", restar(5, 2))
    print("Multiplicación 4 * 3 =", multiplicar(4, 3))
    print("División 10 / 2 =", dividir(10, 2))
    print("¿Es 7 primo?", es_primo(7))
    print("Factorial de 5 =", factorial(5))
