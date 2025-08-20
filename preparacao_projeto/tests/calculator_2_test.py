import sys
sys.path.append('../')

from src.calculators.calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_iterface import DriverHandlerInterface

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler(): # driverHandlerInterface removido para não precisar declarar todas as funçoes abstratas
  def standard_derivation(self, numbers: List[float]) -> float:
    return 3

# Esse é um teste de integração entre NumpyHandler e Calculator2
def test_calculate_integration():
  mock_request = MockRequest(body={'numbers': [1, 2.32, 7.39]})

  driver = NumpyHandler()

  calculator2 = Calculator2(driver)

  formated_response = calculator2.calculate(mock_request)
  
  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'calculator': 2, 'result': 0.04}}


def test_calculate():
  mock_request = MockRequest(body={'numbers': [1, 2.32, 7.39]})

  driver = MockDriverHandler()

  calculator2 = Calculator2(driver)

  formated_response = calculator2.calculate(mock_request)
  
  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'calculator': 2, 'result': 0.33}}

