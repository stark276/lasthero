from hero import Hero
import random


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

    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
        living_heroes.append(hero)

    for hero in other_team.heroes:
        living_opponents.append(hero)

    while len(self.survivors()) > 0 or len(other_team.survivors() > 0):
      # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
      hero = random.choice(self.survivors())
      other_hero = random.choice(other_team.survivors())
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
      
team = Team("Avengers")
team2 = Team("XXX")
hero1 = Hero("Mustang", 500)
other_heros = Hero("Toyota", 500)
team.add_hero(hero1)
team2.add_hero(other_heros)
team.view_all_heroes()
team2.view_all_heroes()
team.attack(team2)
team2.stats()
