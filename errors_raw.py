class HttpUnprocessableEntityError(Exception):
  def __init__(self, message: str) -> None:
    super().__init__(message)
    self.message = message
    self.name = 'UnprocessableEntity'
    self.status_code = 422

try:
  print('Estou no bloco try')
  raise HttpUnprocessableEntityError('Estou lançanso uma exception')
except HttpUnprocessableEntityError as e:
  print('Estou no tratamento do erro')
  print(e.name)
  print(e.message)
  print(e.status_code)

    