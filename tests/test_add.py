"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected


def test_add_suma_negativos():
    """Ejemplo: -4 + -4 deberia darme -8"""
    assert add(-4, -4) == -8

def test_add_suma_positivo_y_negativo():
    """Ejemplo: -4 + 4 deberia darme 0"""
    assert add(-4, 4) == 0

def test_add_suma_con_cero():
    """Ejemplo: -4 + 0 deberia darme 4"""
    assert add(4, 0) == 4

def test_add_suma_decimal():
    """Ejemplo: 1.5 + 1.5 deberia darme 3"""
    assert add(1.5, 1.5) == 3

