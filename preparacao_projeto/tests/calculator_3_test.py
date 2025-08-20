import sys
sys.path.append('../')

from typing import Dict, List
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator3

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandlerError(): # driverHandlerInterface removido para não precisar declarar todas as funçoes abstratas
  def variance(self, numbers: List[float]) -> float:
    return 3
  
class MockDriverHandler(): # driverHandlerInterface removido para não precisar declarar todas as funçoes abstratas
  def variance(self, numbers: List[float]) -> float:
    return 10000

# TESTANDO A INTEGRAÇÃO, NÃO É TESTE UNITARIO
def test_calculate_with_variance_error():
  mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
  calculator_3 = Calculator3(NumpyHandler())

  with raises (Exception) as excinfo:
    calculator_3.calculate(mock_request)

  assert str(excinfo. value) == 'Falha no processo: Variância menor que a multiplicação'

def test_calculate():
  mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 100] })
  calculator_3 = Calculator3(NumpyHandler () )

  response = calculator_3.calculate(mock_request)

  assert response == {'data': {'calculator': 3, 'value': 1568.16, 'sucsess': True}}

# TESTE UNITARIO
def test_calculate_with_variance_error():
  mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
  calculator_3 = Calculator3(MockDriverHandlerError())

  with raises (Exception) as excinfo:
    calculator_3.calculate(mock_request)

  assert str(excinfo. value) == 'Falha no processo: Variância menor que a multiplicação'

def test_calculate():
  mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 100] })
  calculator_3 = Calculator3(MockDriverHandler())

  response = calculator_3.calculate(mock_request)

  assert response == {'data': {'calculator': 3, 'value': 10000, 'sucsess': True}}
