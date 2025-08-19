from typing import Dict

def add(num1:int, num2:int) -> Dict:
  response = num1 + num2
  return {"sum": response}

print(add(90, 9))