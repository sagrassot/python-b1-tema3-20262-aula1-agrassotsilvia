# archivo ej3a1_operations.py


def add(num_1: float, num_2: float) -> float:
    # Funció Suma
    return num_1 + num_2
    pass


def subtract(num_1: float, num_2: float) -> float:
    # Sunció Resta
    return num_1 - num_2
    pass


def multiply(num_1: float, num_2: float) -> float:
    # Funció Umplicació
    return num_1 * num_2
    pass


def divide(num_1: float, num_2: float) -> float:
    # Control divisió per zero
    if num_2 == 0:
        return "Error: no es pot dividir per zero"
    # Funció Divisió
    return num_1 // num_2
    pass
