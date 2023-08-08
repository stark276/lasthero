import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
  def __init__(self, name, starting_health = 100):
    
    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    
    

  # def fight(self, opponent):
  #   winner = random.choice([self.name, opponent.name])
  #   return winner 
  
  def add_ability(self, abi):
    self.abilities.append(abi)

  def attack(self):
    total_damage = 0
    for a in self.abilities:
      total_damage += a.attack()
    return total_damage
  
  def add_armor(self, armor):
    self.armors.append(armor)
    
    
  def defend(self):
    total_block = 0
    for armor in self.armors:
      total_block += armor.block()
    return total_block
  
  def take_damage(self, damage):
    self.current_health -= damage - self.defend()
    return int(self.current_health)
  
  def is_alive(self):
    if self.current_health > 0:
      return True
    else:
      return False
    
  def fight(self, opponent):
    
    while self.is_alive() and opponent.is_alive():
      
      if not self.abilities and opponent.abilities:
        return "Draw :)"
      
      s_attack = self.attack()
      opp_attack = opponent.attack()

      self.take_damage(opp_attack)
      print(f"{self.name} 's  health : {self.current_health}")
      opponent.take_damage(s_attack)
      print(f"{opponent.name} 's  health : {opponent.current_health}")
      
      
      if opponent.is_alive() == False:
        self.winner = self.name
        print(self.winner +  " Won!")
        # self.add_kill(1)
        # opponent.add_deaths(1)
      else:
        self.winner = opponent.name
        print(self.winner +  " Won!")
        # self.add_deaths(1)
        # opponent.add_kill(1)
      
      return self.winner
    
  def add_weapon(self, weapon):
    '''Add weapon to self.abilities'''
    # This method will append the weapon object passed in as an
    # argument to self.abilities.
    # This means that self.abilities will be a list of
    # abilities and weapons.
    self.abilities.append(weapon)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())