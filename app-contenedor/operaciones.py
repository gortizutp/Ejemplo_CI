
#def sumar(a,b):
def sumar(a: int, b: int) -> int:
    resultado = a + b
    print("Suma 2 + 3 = {}".format(resultado))
    return resultado



def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return float(a) / float(b)  


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n < 0:
        raise ValueError("No existe factorial de un numero negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


if __name__ == "__main__":
    
    sumar(2, 3)
    
  
    print("Resta 5 - 2 = {}".format(restar(5, 2)))
    print("Multiplicacion 4 * 3 = {}".format(multiplicar(4, 3)))
    print("Division 10 / 2 = {}".format(dividir(10, 2)))
    print("Factorial de 5 = {}".format(factorial(5)))