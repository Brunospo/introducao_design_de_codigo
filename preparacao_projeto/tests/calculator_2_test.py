import sys
sys.path.append('../')

from src.calculators.calculator_2 import Calculator2
from typing import Dict
# from pytest import raises

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={'numbers': [1, 2.32, 7.39]})

  calculator2 = Calculator2()

  formated_response = calculator2.calculate(mock_request)
  
  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'calculator': 2, 'result': 0.04}}

# def test_calculate_with_body_error():
#   mock_request = MockRequest(body={'something': 1})

#   calculator1 = Calculator1()

#   with raises(Exception) as excinfo:
#     calculator1.calculate(mock_request)

#   assert str(excinfo.value) == "body mal formatado!"
  
  