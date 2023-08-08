from hero import Hero
import random


class Team:
  """docstring for Team."""
  def __init__(self, name):
    self.name = name
    self.heroes = list()

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
      
team = Team("Avengers")
hero1 = Hero("Mustang", 100)
team.add_hero(hero1)
team.view_all_heroes()
