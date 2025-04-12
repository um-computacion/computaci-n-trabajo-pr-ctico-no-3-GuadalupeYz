class NumeroDebeSerPositivo(Exception):
    pass

def ingrese_numero():
    entrada = input("Ingrese un número: ")

    if not entrada.lstrip('-').isdigit():
        raise ValueError("La entrada debe ser un número válido")

    numero = int(entrada)

    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo")

    return numero

