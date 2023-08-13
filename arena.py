from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
from random import randint, choice

class Arena:
  """docstring for Arena."""
  def __init__(self):
    self.team_one = None
    self.team_two = None
  
  def create_ability(self):
    name = input('What is the ability name? ')
    max_damage = int(input("What is the max damage of the ability? "))
    
    return Ability(name, max_damage)
  
  def create_weapon(self):
    name = input('What is the weapon name? ')
    max_damage = int(input("What is the max damage of the weapon? "))
    
    return Weapon(name, max_damage)
  
  def create_armor(self):
    name = input('What is the armor name? ')
    max_block = int(input("What is the max block of the armor? "))
    
    return Weapon(name, max_block)
  
  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        ability = self.create_ability()
        hero.add_ability(ability)
        
      elif add_item == "2":
        weapon = self.create_weapon()
        hero.add_ability(weapon)
      elif add_item == "3":
        armor = self.create_armor()
        hero.add_armor(armor)
    return hero
  
  def build_team_one(self):
    '''Prompt the user to build team_one '''
    name = input("What\'s your team name? ")
    self.team_one = Team(name)
    
    build_time = True
    while build_time:
      hero_count = input("How many heroes do you want on your team? ")
      if hero_count.isdigit() == False:
        print("Unrecognixed input, please try again")
      elif hero_count == '0':
        print("You need at lest one or more hero on your team")
      else:
        count = 0
        while int(hero_count)> count:
          hero = self.create_hero()
          self.team_one.add_hero(hero)
          count += 1
        build_time = False
    self.team_one.view_all_heroes()
    return self.team_one
  
  def build_team_two(self):
    '''Prompt the user to build team_two '''
    name = input("What\'s your team name? ")
    self.team_two = Team(name)
    
    build_time = True
    while build_time:
      hero_count = input("How many heroes do you want on your team? ")
      if hero_count.isdigit() == False:
        print("Unrecognized input, please try again")
      elif hero_count == '0':
        print("You need at lest one or more hero on your team")
      else:
        count = 0
        while int(hero_count)> count:
          hero = self.create_hero()
          self.team_two.add_hero(hero)
          count += 1
        build_time = False
    self.team_two.view_all_heroes()
    return self.team_two  
          
  def team_battle(self):
    
    '''Battle team_one and team_two together.'''
    self.team_one.attack(self.team_two)
    if len(self.team_one.survivors()) > 0 and len(self.team_two.survivors()) == 0:
      self.winner = self.team_one.name
      return self.winner
    else:
      self.winner = self.team_two.name
      return self.winner

  def show_stats(self):
    
    '''Prints team statistics to terminal.'''
    print(self.team_battle() + " wins!" )

    self.team_one.stats()
    self.team_two.stats()

    if self.winner == self.team_one.name:
      for hero in self.team_one.survivors():
        print("Survivor: {}".format(hero.name))
    elif self.winner == self.team_two.name:
      for hero in self.team_two.survivors():
        print("Survivor: {}".format(hero.name))
    else:
      print("No survivors")
      
      
if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  game_is_running = True

  # Instantiate Game Arena
  arena = Arena()

  #Build Teams
  arena.build_team_one()
  arena.build_team_two()

  while game_is_running:
    arena.team_battle()
    arena.show_stats()
    play_again = input("Play Again? Y or N: ")

    #Check for Player Input
    if play_again.lower() == "n":
      game_is_running = False

    else:
      #Revive heroes to play 
      arena.team_one.revive_heroes()
      arena.team_two.revive_heroes()