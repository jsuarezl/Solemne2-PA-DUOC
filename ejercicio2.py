# -*- coding: utf-8 -*-

import os
import sys
import time
import re
import platform
from enum import Enum


class Course(Enum):
    PYTHON = "Python Avanzado"
    BIG_DATA = "Big Data"
    ANDROID = "Desarrollo en Android"


python = 0
big_data = 0
android = 0


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


def print_main_options():
    print("""
    1) Comprar cursos
    2) Mostrar cursos comprados
    3) Estadísticas de cursos comprados
    4) Salir
    """)


def print_curses():
    print("""
    |-------------------------------------------|
    | Nombre curso             | Fecha          |
    |-------------------------------------------|
    | 1) {}       | 01-08 al 01-09 |
    | 2) {}              | 05-08 al 22-08 |
    | 3) {} | 12-08 al 04-09 |
    |-------------------------------------------|
    """.format(Course.PYTHON.value, Course.BIG_DATA.value, Course.ANDROID.value))


def get_inscribed(course: Course):
    return python if course == Course.PYTHON else big_data if course == Course.BIG_DATA else android


def bought_course(course: Course, date: str):
    print("""
     Curso: {} | Fecha: {}
     Total de cursos: {}
     Total a pagar: ${}
    """.format(course.value, date, get_inscribed(course), get_inscribed(course) * 65000))
    paid_amount = int_in_range(input("Ingrese una cantidad de dinero para pagar los cursos: "),
                               get_inscribed(course) * 65000, sys.maxsize,
                               "No ha ingresado una cantidad que cubra el valor total, reintente: ")
    print("""
     Dinero Ingresado: ${}
     Vuelto: ${}
    """.format(paid_amount, paid_amount - get_inscribed(course) * 65000))


def print_bought_courses():
    print("""Cursos comprados hasta ahora:
    
    Python Avanzado: {}
    Big Data: {}
    Desarrollo en Android: {}
    """.format(python, big_data, android))


def get_inscribed_total():
    total = 0
    for x in Course:
        total += get_inscribed(x)
    return total


def print_bought_stats():
    print("""
    Python Avanzado: {}
    Total: ${}
    
    Big Data: {}
    Total: ${}
    
    Desarrollo en Android: {}
    Total: ${}
    
    
    Total en compras: ${}
    """.format(get_inscribed(Course.PYTHON), get_inscribed(Course.PYTHON) * 65000, get_inscribed(Course.BIG_DATA),
               get_inscribed(Course.BIG_DATA) * 65000, get_inscribed(Course.ANDROID),
               get_inscribed(Course.ANDROID) * 65000, get_inscribed_total() * 65000))


while True:
    clear()
    print_main_options()
    option = int_in_range(input("Ingrese una opción: "), 1, 4)
    if option == 1:
        clear()
        print_curses()
        option_curses = int_in_range(input("Ingrese una opción: "), 1, 3)
        if option_curses == 1:
            python += 1
            bought_course(Course.PYTHON, "01-08 al 01-09")
        elif option_curses == 2:
            big_data += 1
            bought_course(Course.BIG_DATA, "05-08 al 22-08")
        else:
            android += 1
            bought_course(Course.ANDROID, "12-08 al 04-09")
    elif option == 2:
        clear()
        print_bought_courses()
    elif option == 3:
        clear()
        print_bought_stats()
    elif option == 4:
        input("Saliendo del programa...")
        time.sleep(3)
        exit(0)
    input("Presione enter para continuar.")
