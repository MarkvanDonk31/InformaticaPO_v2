
##########################################################################

class Item:
  item_type = None
  item_lore = ""
  
  def __init__(self, item_level, item_enchantments):
    self.item_level = item_level
    self.item_enchantments = item_enchantments
    
  def print_stats(self):
    print(self.item_type, "- level:", self.item_level)
    print("Enchantments: ", self.item_enchantments)

## Class Sword
class Sword(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
     
    self.item_type = "sword"
    self.item_name = "Sword"
    self.min_damage = 20
    self.max_damage = 20

    #Enchantments
    if "sharpness" in item_enchantments:
      self.item_lore = "WOW.. Extra sharp!"
      self.min_damage = 12
      self.max_damage = 14

    if "fire" in self.item_enchantments:
      self.item_lore = "WOW.. Fire proof!"
      self.min_damage = 13
      self.max_damage = 15

    else:
      self.item_lore = "Old.. but sharp!"

## Class DeathSword
class DeathSword(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "death sword"
    self.item_name = "Death Sword"
    self.item_lore = "A sword made by death it self.."
    self.min_damage = 6
    self.max_damage = 9

## Class Axe
class Axe(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
     
    self.item_type = "axe"
    self.item_name = "Axe"
    self.min_damage = 3
    self.max_damage = 6
    item_enchantments = []

    #Enchantments
    if "sharpness" in self.item_enchantments:
      self.item_lore = "WOW.. Extra sharp!"
      self.min_damage = 6
      self.max_damage = 8
      
    if "fire" in self.item_enchantments:
      self.item_lore = "WOW.. Fire proof!"
      self.min_damage = 5
      self.max_damage = 9

    else:
      self.item_lore = "SWWWFFF.. that does the job!"

## Class FireAxe
class FireAxe(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "fire axe"
    self.item_name = "Fire Axe"
    self.item_lore = "WOW Thats realy hot!"
    self.min_damage = 2
    self.max_damage = 5

## Class Bow
class Bow(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
     
    self.item_type = "bow"
    self.item_name = "Bow"
    self.item_lore = "Old thing... but it works.."
    self.min_damage = 2
    self.max_damage = 5

## Class Shield
class Shield(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "shield"
    self.item_name = "Shield"
    self.item_lore = "Use me.. and I'll be of service"

## Class Chainmail
class Chainmail(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "chainmail"
    self.item_name = "Chainmail"
    self.item_lore = "Use me.. and I'll be of service"


## Class SteelChestplate
class SteelChestplate(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "steel chestplate"
    self.item_name = "Steel Chestplate"
    #Adds 5 armor points
    self.item_lore = "Use me.. and I'll be of service"

## Class NormalKey
class NormalKey(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
    self.item_type = "normal key"
    self.item_name = "Normal Key"
    self.item_lore = "Use me on a normale chest and it will open!"

## Class GoldenKey
class GoldenKey(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
    self.item_type = "golden key"
    self.item_name = "Golden Key"
    self.item_lore = "Use me on a golden chest and it will open!"

## Class MythicalKey
class MythicalKey(Item):
   def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
    self.item_type = "mythical key"
    self.item_name = "Mythical Key"
    self.item_lore = "Use me on a mythical chest and it will open!"

## Class ArmorPotion
class ArmorPotion(Item):
  def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
    self.item_type = "armor potion"
    self.item_name = "Armor Potion"
    self.item_lore = "Use me for som extra armor!"

## Class Apple
class Apple(Item):
  def __init__(self, item_level, item_enchantments):
   Item.__init__(self, item_level, item_enchantments)

   self.item_type = "apple"
   self.item_name = "Apple"
   self.item_lore = "Use me.. and I'll be of service"
   #Adds 5 health points
   self.heal_value = 5

##########################################################################

  
