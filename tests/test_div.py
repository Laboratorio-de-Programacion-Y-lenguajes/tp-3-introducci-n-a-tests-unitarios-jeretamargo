"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:
#

"""
Esta serie de testeos tiene una funcion parametrizada con 2 vueltas:
1era vuelta: comprueba que 5 / 2 devuelva 2.5 (resultado decimal)
2da vuelta: comprueba que 4 / -2 devuelva -2 (division con negativos)

"""

@pytest.mark.parametrize("a,b,expected", [(5, 2, 2.5),(4,-2, -2)])
def test_add_parametrizado(a, b, expected):
     assert div(a, b) == expected

def test_div_por_cero():
     """
     Este test comprueba que al dividir un numero en cero
     se lance una excepcion de tipo "ZeroDivisionError"
     """
     with pytest.raises(ZeroDivisionError):
         div(10, 0)
