"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

"""
Este test parametrizado realiza 4 vueltas
1era vuelta: comprueba que 5 - 4 devuelva 1
2da vuelta: comprueba que 0 - 4 devuelva -4
3era vuelta: comprueba que -4 - (-4) devuelva 0
4ta vuelta: comprueba que -1.5 - (-1.5) devuelva 0
"""

@pytest.mark.parametrize("a,b,expected", [(5, 4, 1),(0, 4, -4),(-4,-4,0),(-1.5,-1.5,0)])
def test_add_parametrizado(a, b, expected):
     assert sub(a, b) == expected

