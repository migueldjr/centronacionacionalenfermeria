#!/usr/bin/env python3
"""Calculadora básica con interfaz gráfica y modo consola."""

from __future__ import annotations

import argparse
import tkinter as tk
from tkinter import messagebox


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


class CalculadoraApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculadora")
        self.root.resizable(False, False)

        tk.Label(root, text="Primer número").grid(row=0, column=0, padx=8, pady=6, sticky="w")
        self.entrada_a = tk.Entry(root)
        self.entrada_a.grid(row=0, column=1, padx=8, pady=6)

        tk.Label(root, text="Operación").grid(row=1, column=0, padx=8, pady=6, sticky="w")
        self.operador = tk.StringVar(value="+")
        tk.OptionMenu(root, self.operador, "+", "-", "*", "/").grid(row=1, column=1, padx=8, pady=6, sticky="ew")

        tk.Label(root, text="Segundo número").grid(row=2, column=0, padx=8, pady=6, sticky="w")
        self.entrada_b = tk.Entry(root)
        self.entrada_b.grid(row=2, column=1, padx=8, pady=6)

        tk.Button(root, text="Calcular", command=self.resolver).grid(row=3, column=0, columnspan=2, padx=8, pady=8, sticky="ew")

        self.resultado = tk.StringVar(value="Resultado: --")
        tk.Label(root, textvariable=self.resultado, font=("Arial", 12, "bold")).grid(
            row=4, column=0, columnspan=2, padx=8, pady=(2, 10)
        )

    def resolver(self) -> None:
        try:
            a = float(self.entrada_a.get())
            b = float(self.entrada_b.get())
            operador = self.operador.get()
            valor = calcular(a, operador, b)
            self.resultado.set(f"Resultado: {valor}")
        except ValueError as error:
            messagebox.showerror("Error", str(error))


def ejecutar_consola() -> None:
    print("=== Calculadora ===")
    try:
        a = float(input("Primer número: "))
        operador = input("Operador (+, -, *, /): ").strip()
        b = float(input("Segundo número: "))
        resultado = calcular(a, operador, b)
        print(f"Resultado: {resultado}")
    except ValueError as error:
        print(f"Error: {error}")


def ejecutar_gui() -> None:
    root = tk.Tk()
    CalculadoraApp(root)
    root.mainloop()


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadora básica")
    parser.add_argument(
        "--modo",
        choices=["gui", "consola"],
        default="gui",
        help="Modo de ejecución: gui (ventana) o consola",
    )
    args = parser.parse_args()

    if args.modo == "consola":
        ejecutar_consola()
    else:
        ejecutar_gui()


if __name__ == "__main__":
    main()
