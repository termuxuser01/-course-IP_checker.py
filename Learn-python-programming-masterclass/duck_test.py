class Wing(object):
  def __init__(self, ratio):
    self.ratio = ratio

  def fly(self):
    if self.ratio > 1:
      print("this is fun!")
    elif self.ratio == 1:
      print("this is hard but im flying")
    else:
      print("think ill walk")

class Duck(object):
  def __init__(self):
    self.wing = Wing(1.8)

  def walk(self):
    print("waddle, waddle")

  def swim(self):
    print("the water is lovley")

  def quack(self):
    print("quack, quack")

  def fly(self):
    self.wing.fly()


class Penguin(object):
  def __init__(self):
    self.wing = Wing(0.5)
 
  def walk(self):
    print("wadle, wadle, i wadle too")

  def swim(self):
    print("come on in")

  def quack(self):
    print("im a penguin!")

  def fly(self):
    self.wing.fly()

def testduck(duck):
  duck.walk()
  duck.swim()
  duck.quack()

if __name__ == "__main__":
  donald = Duck()
  testduck(donald)
  donald.fly()

  percy = Penguin()
  testduck(percy)
  percy.fly()

