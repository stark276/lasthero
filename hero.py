import random

class Hero:
  def __init__(self, name, starting_health = 100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    winner = random.choice([self.name, opponent.name])
    return winner 

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  my_hero = Hero("Grace Hopper", 200)
  other_hero = Hero("Manas", 200)

  print(my_hero.fight(other_hero))
  print(my_hero.current_health)