import sqlite3

db = sqlite3.connect("account.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
#deposits will be positive, widrawls negative.
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY ( time, amount))")


class Account(object):

  def __init__(self, name: str, openning_balance: float = 0.0) -> None:
    cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
    row = cursor.fetchone()

    if row:
      self.name, self._balance = row
      print("retrieved record for {}".format(self.name))
    else:
      self.name = name
      self._balance = openning_balance
      cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, openning_balance))
      cursor.connection.commit()
      print("account created succesfully for {}!".format(self.name))
    self.show_blanace()

  def deposit(self, amount: float) -> float:
    if amount > 0.0:
      new_balance = self._balance + amount
      deposit_time = 
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

  Veronica = Account("VIanney")
