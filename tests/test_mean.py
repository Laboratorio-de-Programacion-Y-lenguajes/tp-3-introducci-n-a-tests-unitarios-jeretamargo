"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])

"""
Esta serie de testeos tiene una funcion parametrizada con 2 vueltas:
1era vuelta: comprueba que una lista con un unico elemento debe retornar el mismo elemento (1)
2da vuelta: comprueba que funcione una lista con numeros negativos
3ra vuelta: comprueba que funcione una lista con numeros decimales 
"""

@pytest.mark.parametrize("a,expected", [([1], 1), ([-3,-4,-5,-6], -4.5 ), ([5.5, 4.3, 9.7, 8.6],7.0249999999999995 )])
def test_add_parametrizado(a, expected):
     assert mean(a) == expected

def test_mean_lista_vacia():
     """
     Este test comprueba que al intentar realizar mean con
     una lista vacía, la funcion lance una excepción de tipo
     "ValueError"
     """
with pytest.raises(ValueError):
        mean([])
