import os
import re
import platform


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
