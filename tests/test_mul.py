"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

"""
Este test parametrizado realiza 4 vueltas
1era vuelta: comprueba que 4 * 0 devuelva 0 (Multiplicar por cero)
2da vuelta: comprueba que -2 * -2 devuelva 4 (resultado positivo)
3era vuelta: comprueba que 4 * -4 devuelva -16 (resultado negativo)
4ta vuelta: comprueba que 1.5 * 1 devuelva 1.5 (elemento neutro)
5ta vuelta: comprueba que 1.5 * 1.5 devuelva 2.25 (multiplicación de float)
"""


@pytest.mark.parametrize("a,b,expected", [(4, 0, 0),(-2, -2, 4),(4, -4, -16),(1.5, 1, 1.5), (1.5, 1.5, 2.25)])
def test_add_parametrizado(a, b, expected):
     assert mul(a, b) == expected
