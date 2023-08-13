from random import randint, choice
from ability import Ability

class Weapon(Ability):
  """docstring for Weapon."""
  def attack(self):
    random_value = randint(self.max_damage // 2, self.max_damage)
    return random_value