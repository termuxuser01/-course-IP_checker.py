# This function returns its nested function
def decorator(f):
  def newfunc():
    print("new functionality")
    f()
  return newfunc


# this is the decorator that adds the function
@decorator
# this is our main function that we wil decorate
def initialfunc():
  print("initial funcionality")

# notice how both functions are executed even if only the later was called
initialfunc()

# now lets see the @property decorator
class House:
  def __init__(self, price):
    self._price = price

  # here we define the getter function
  @property
  # the method is named like the attribute we want to access but without the underscore to keep it protected
  def price(self):
    return self._price

  # this is a setter property
  @price.setter
  def price(self, new_price):
    # an intermediary (the setter) to validate the argument before assigning it.
    if new_price > 0 and isinstance(new_price, float):
      self._price = new_price
    else:
      print("value is invalid")

  @price.deleter
  def price(self):
    del self._price


if __name__ == "__main__":
  house = House(30000)
  print(house.price)
  house.price = 1000.00
  print(house.price)
  print(house._price)
