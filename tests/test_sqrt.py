"""Tests para la función sqrt(x) -> float."""

import pytest
import math
from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0)
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)
#   - Raíz de un número negativo → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_sqrt_negativo():
#     with pytest.raises(ValueError):
#         sqrt(-4)

"""
Esta serie de testeos tiene una funcion parametrizada con 2 vueltas:
1era vuelta: comprueba la raiz de cero devuelva cero
2da vuelta: comprueba que la raiz de un numero impar devuelva decimal
"""

@pytest.mark.parametrize("a,expected", [(0,0.0 ),(5, math.sqrt(5))])
def test_add_parametrizado(a, expected):
     assert sqrt(a) == expected

def test_sqrt_negativo():
     """
     Este test comprueba que al intentar realizar la raiz de
     un numero negativo, la funcion lance una excepción de tipo
     "ValueError"
     """
     with pytest.raises(ValueError):
         sqrt(-4)
