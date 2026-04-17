"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

"""
Este test parametrizado realiza 4 vueltas:
1era vuelta: comprueba que 5^0 devuelva 1 (numero elevado a la 0 = 1)
2da vuelta: comprueba que 5^1 devuelva 5 (numero elevado a la 1 = mismo número)
3era vuelta: comprueba que -4^2 devuelva  16 (resultado positivo)
4ta vuelta: comprueba que  devuelva 9^1.5 devuelva 3 (raíz cuadrada)
"""

@pytest.mark.parametrize("a,b,expected", [(5, 0, 1),(5, 1, 5),(-4, 2, 16),(9 , 0.5 , 3)])
def test_add_parametrizado(a, b, expected):
     assert pow_(a, b) == expected
