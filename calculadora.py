#!/usr/bin/env python3
"""Calculadora básica en consola."""


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def calcular(a: float, operador: str, b: float) -> float:
    operaciones = {
        "+": sumar,
        "-": restar,
        "*": multiplicar,
        "/": dividir,
    }

    if operador not in operaciones:
        raise ValueError(f"Operador no soportado: {operador}")

    return operaciones[operador](a, b)


def main() -> None:
    print("=== Calculadora ===")
    try:
        a = float(input("Primer número: "))
        operador = input("Operador (+, -, *, /): ").strip()
        b = float(input("Segundo número: "))
        resultado = calcular(a, operador, b)
        print(f"Resultado: {resultado}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
