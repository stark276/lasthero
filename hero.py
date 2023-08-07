import random
from ability import Ability
from armor import Armor


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


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.

  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")
  ability1 = Ability("Super Speed", 300)
  ability2 = Ability("Super Eyes", 130)
  ability3 = Ability("Wizard Wand", 80)
  ability4 = Ability("Wizard Beard", 20)
  hero1.add_ability(ability1)
  hero1.add_ability(ability2)
  hero2.add_ability(ability3)
  hero2.add_ability(ability4)
  hero1.fight(hero2)