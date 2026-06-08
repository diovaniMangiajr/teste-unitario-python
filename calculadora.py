
# calculadora.py

  
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números.

    Se o segundo número for zero, o Python irá gerar um erro.
    """
    return a / b

def potencia(a: float, b: float) -> float:
    """Retorna a potência de dos números."""
    return a**b

def calcular_media(lista: list) -> float:
    """Retorna a média de uma lista de números
    Se a lista vier vazia levanta um ValueError
    """

    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    
    return sum(lista) / len(lista)