from random import randint, choice
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
    self.deaths = 0
    self.kills = 0
    
    

  # def fight(self, opponent):
  #   winner = random.choice([self.name, opponent.name])
  #   return winner 
  
  def add_ability(self, abi):
    self.abilities.append(abi)

  def attack(self):
    '''Calculate the total damage from all ability attacks.
      return: total:Int
    '''
    total_attack = 0

    for ability in self.abilities:
      attack = ability.attack()
      total_attack = total_attack + attack
    
    return total_attack
  
  def add_armor(self, armor):
    self.armors.append(armor)
    
    
  def defend(self, damage_amount=0):
    '''Runs `block` method on each armor.
        Returns sum of all blocks
    '''
    total_armor = 0

    for armor in self.armors:
      total_armor = total_armor + armor.block()

    result = total_armor - damage_amount
    
    return result
  
  def take_damage(self, damage):
    '''Updates self.current_health to reflect the damage minus the defense. '''

    self.current_health = int(self.current_health) - int(damage)
  
  def is_alive(self):
    if self.current_health <= 0:
      return False
    else:
      return True
    
  def add_kill(self, num_kills):
    self.kills += num_kills
  
  def add_death(self,  num_deaths):
    self.deaths += num_deaths
    
  def fight(self, opponent):
    
    while self.is_alive() and opponent.is_alive():
      
      if not self.abilities and opponent.abilities:
        return "Draw"
      
      s_attack = self.attack()
      opp_attack = opponent.attack()

      self.take_damage(opp_attack)
      print(f"{self.name} 's  health : {self.current_health}")
      
      opponent.take_damage(s_attack)
      print(f"{opponent.name} 's  health : {opponent.current_health}")
      
      
      if opponent.is_alive() == False:
        self.winner = self.name
        print(self.winner +  " Won!")
        self.add_kill(1)
        opponent.add_death(1)
      else:
        self.winner = opponent.name
        print(self.winner +  " Won!")
        self.add_death(1)
        opponent.add_kill(1)
      
      return self.winner 
    
  def add_weapon(self, weapon):
    '''Add weapon to self.abilities'''
    self.abilities.append(weapon)
    
  


# if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # hero = Hero("Wonder Woman")
    # weapon = Weapon("Lasso of Truth", 90)
    # hero.add_weapon(weapon)
    # print(hero.attack())