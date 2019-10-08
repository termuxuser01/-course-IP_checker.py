import random

class Enemy:
  def __init__(self, name="enemy", hit_points=0, lives=1):
    self.name = name
    self.hit_points = hit_points
    self.lives = lives
    self.vitality = True

  def take_damage(self, damage):
    if self.hit_points > 0:
      self.hit_points -= damage
      print("I took {} damage and have {} hit points left!".format(damage, self.hit_points))

    else:
      print("Ugggg!")
      self.lives -= 1
      if self.lives > 0:
        print("{0.name} lost a live!".format(self))
      else:
        print("{0.name} died".format(self))
        self.vitality = False

  def __str__(self):
    return "Name: {0.name}\nhit poitns: {0.hit_points}\nlives: {0.lives}".format(self)



class Troll(Enemy):
  def __init__(self, name):
    #call the Enemy.__init__ method from superclass
    #can alsp be  Enemy.__init__(name, hit_points=23, lives=1)

    super(Troll, self).__init__(name, hit_points=23, lives=1)

  def grunt(self):
    print("{} stomp you".format(self.name))

class Vampyre(Enemy):
  def __init__(self, name, hit_points=12, lives=3):
    super().__init__(name=name, hit_points=hit_points, lives=lives)

  #give a vampyre a 1 in 3 chance of dodging an attack
  def dodges(self):
    if random.randint(1, 3) == 3:
      print("***{0.name} dodges***".format(self))
      return True
    else:
      return False

  #give vampyres a special overwritten take damage method
  def take_damage(self, damage):
    if not self.dodges():
      #call superior method
      super().take_damage(damage)

class VampyreKing(Vampyre):
  def __init__(self, name):
    super().__init__(name=name, hit_points=120, lives=5)

  def take_damage(self, damage):
    damage /= 4
    super().take_damage(damage)


vampy = VampyreKing("troy")
troll = Troll("Ugg")
print("a troll - {}".format(troll))

troll.grunt()

troll.take_damage(5)


while vampy.vitality:
  vampy.take_damage(random.randint(1, 20))











e = Enemy()

print(e)
