from random import randint, choice

class Armor:

# instance attributes
 def __init__(self, name, max_block):
   self.name = name
   self.max_block = max_block

# instance method
 def block(self):
   random_value = random.randint(0, int(self.max_block))
   return random_value
 
# if __name__ == "__main__":
#   armor = Armor("Debugging Shield", 10)
#   print(armor.name)
#   print(armor.block())