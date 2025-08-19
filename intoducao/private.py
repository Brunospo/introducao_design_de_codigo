class MyClass:
  def registry(self) -> None:
    print('start process...')
    self.__verify()
    self.__verify_registry()
    self.__insert_data()

  def __verify(self) -> None:
    print('verify data')

  def __verify_registry(self) -> None:
    print('verify registry')

  def __insert_data(self) -> None:
    print('insert in DB')


class1 = MyClass()

# da erro, pois o metodo é privado

# class1.__verify()

class1.registry()