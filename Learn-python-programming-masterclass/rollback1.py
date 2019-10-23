class Account(object):

  def __init__(self, name: str, openning_balance: float = 0.0):
    self.name = name
    self._balance = openning_balance
    print("account created succesfully for {}!".format(self.name))

  def deposit(self, amount: float) -> float:
    if amount > 0.0:
      self._balance += amount
      print(f"deposited: ${amount}")
    else:
      print("cannot deposit negative quantity")
    return  self._balance

  def withdrawal(self, amount: float) -> float:
    if amount < self._balance:
      self._balance -= abs(amount)
      print(f"${amount} withdrawn!")
    else:
      print("Can't withdraw more than your balance!")
    return self._balance

  def show_blanace(self) -> None:
    print(f'Account for {self.name} has ${self._balance}')

if __name__ == "__main__":
  Vianney = Account("Veronica")
  Vianney.deposit(420.69)
  Vianney.deposit(1337.50)
  Vianney.withdrawal(500)
  Vianney.show_blanace()
