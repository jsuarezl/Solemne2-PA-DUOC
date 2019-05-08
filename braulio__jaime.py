# -*- coding: utf-8 -*-
import os
import re
import platform
import sys


def clear() -> None:
    """Clear console, should work on Windows and *nix"""
    name = re.sub(r"[^\w]+", "", platform.system()).lower()
    if "windows" in name:
        os.system("cls")
    else:
        os.system("clear")


def isint(x: str) -> bool:
    """Return True if the provided string is an int or False otherwise"""
    try:
        int(x)
        return True
    except ValueError:
        return False


def int_in_range(x: str, min_n: int, max_n: int, err_msg="No ha ingresado una opción válida, reintente: ") -> int:
    """Transform x to int if is in the requested range or force the user to input until provide a valid number"""
    while not isint(x) or (int(x) < min_n or int(x) > max_n):
        x = input(err_msg)
        if isint(x):
            x = int(x)
            if x < min_n or x > max_n:
                x = ""
    return int(x)


peoplesecure = .55
lifeplus = .80
ss = .2
seguro = ""
op = 0.0
while True:
    clear()
    print("-----------------------------")
    print("        Bonos Duoc UC")
    print("-----------------------------")
    print("\n")
    montototal = int_in_range(input("Ingrese monto total del BONO : "), 1, sys.maxsize, "Ingrese un monto válido: ")

    print("Seguros")
    print("[1] Seguro LifePlus")
    print("[2] Seguro People Secure")
    print("[3] Sin Seguro")

    op = int_in_range(input("Ingrese Opcion Valida: "), 1, 3)
    if op == 1:
        print("\n")
        print("Monto Bono: $" + str(montototal) + "\n" +
              "Descuento: $" + str(int(montototal * lifeplus)) + "\n" +
              "Monto a pagar: $" + str((int(montototal - montototal * lifeplus))))

    elif op == 2:
        print("\n")
        print("Monto Bono: $" + str(montototal) + "\n" +
              "Descuento: $" + str(int(montototal * peoplesecure)) + "\n" +
              "Monto a pagar: $" + str((int(montototal - montototal * peoplesecure))))
    elif op == 3:
        print("\n")
        edad = int_in_range(input("Ingrese Edad del cliente: "), 0, 125, "Ingrese una edad válida: ")
        if edad >= 60:
            print("Monto bono: $" + str(montototal) + "\n" +
                  "Descuento: $" + str(int(montototal * ss)) + "\n" +
                  "Monto a Pagar: $" + str((int(montototal - montototal * ss))))
        else:
            print("\n")
            print("Monto Bono: $" + str(montototal) + "\n" +
                  "No aplica Descuento" + "\n" +
                  "Monto a Pagar: $" + str(montototal))
    input("Presione enter para continuar.")
