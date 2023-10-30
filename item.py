import random

class Item:
  item_type = None
  item_lore = ""
  

  def __init__(self, item_level, item_enchantments):
    self.item_level = item_level
    self.item_enchantments = item_enchantments
    

  def print_stats(self):
    print(self.item_type, "- level:", self.item_level)
    print(self.item_enchantments )


class Sword(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
     
    self.item_type = "sword"
    self.item_name = "Sword"
    self.min_damage = 10
    self.max_damage = 10

    if "sharpness" in item_enchantments:
      self.item_lore = "WOW.. Extra sharp!"

    if "fire" in self.item_enchantments:
      self.item_lore = "WOW.. Fire proof!"

    else:
      self.item_lore = "Old.. but sharp!"

class DeathSword(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

     

    self.item_type = "death sword"
    self.item_name = "Death Sword"

    self.item_lore = "A sword made by death it self.."
    self.min_damage = 2
    self.max_damage = 5

class Axe(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
     
    self.item_type = "axe"
    self.item_name = "Axe"
    self.min_damage = 2
    self.max_damage = 5
    item_enchantments = []
     
    if "sharpness" in self.item_enchantments:
      self.item_lore = "WOW.. Extra sharp!"
      
    if "fire" in self.item_enchantments:
      self.item_lore = "WOW.. Fire proof!"

    else:
      self.item_lore = "SWWWFFF.. that does the job!"


class FireAxe(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "fire axe"
    self.item_name = "Fire Axe"

    self.item_lore = "WOW Thats realy hot!"
    
    self.min_damage = 2
    self.max_damage = 5

class Bow(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
     
    self.item_type = "bow"
    self.item_name = "Bow"
    self.item_lore = "Old thing... but it works.."
    self.min_damage = 2
    self.max_damage = 5


class Shield(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "shield"
    self.item_name = "Shield"



class Chainmail(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "chainmail"
    self.item_name = "Chainmail"


class SteelChestplate(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "steel chestplate"
  


# class Armor(Item):

#   def __init__(self, item_level, item_enchantments):
#     Item.__init__(self, item_level, item_enchantments)
#     self.item_type = "armor"
#     self.defence = self.item_level * 2
