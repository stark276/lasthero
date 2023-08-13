from random import randint, choice

class Ability:
  def __init__(self, name, max_damage):
    self.name = name
    self.max_damage = max_damage

  def attack(self):
    random_value = randint(0, int(self.max_damage))
    return random_value
  
class Weapon(Ability):
  """docstring for Weapon."""
  def attack(self):
    random_value = randint(self.max_damage // 2, self.max_damage)
    return random_value
  
class Armor:

# instance attributes
 def __init__(self, name, max_block):
   self.name = name
   self.max_block = max_block

# instance method
 def block(self):
   random_value = random.randint(0, int(self.max_block))
   return random_value
 
 

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
    

class Team:
  """docstring for Team."""
  def __init__(self, name):
    self.name = name
    self.heroes = []

  def add_hero(self, hero):
    '''Add Hero object to self.heroes.'''
    self.heroes.append(hero)

  foundHero = False
  def revome_hero(self, name):
    for hero in self.heroes:
      if hero.name == name:
        self.heroes.remove(hero)
        foundHero = True
    if not foundHero:
      return 0
    
  def view_all_heroes(self):
    for hero in self.heroes:
      print(hero.name)
      # return hero.name
      
  def revive_heroes(self, health=100):
    ''' Reset all heroes health to starting_health'''
    # for each hero in self.heroes,
    # set the hero's current_health to their starting_health
    for hero in self.heroes:
      hero.current_health = health
  def attack(self, other_team):
    
    ''' Battle each team against each other.'''

    # living_heroes = list()
    # living_opponents = list()

    # for hero in self.heroes:
    #     living_heroes.append(hero)

    # for hero in other_team.heroes:
    #     living_opponents.append(hero)

    while len(self.survivors()) > 0 or len(other_team.survivors() > 0):
      # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
      hero = choice(self.survivors())
      other_hero = choice(other_team.survivors())
      # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
      return hero.fight(other_hero)
          
    
  def survivors(self):
    living = [hero for hero in self.heroes if hero.is_alive()]
    return living
  
  def stats(self):
    '''Print team statistics'''
    for hero in self.heroes:
      print("Hero: {}".format(hero.name))
      print("Kills: {}".format(hero.kills))
      print("Death: {} \n".format(hero.deaths))
      
      

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