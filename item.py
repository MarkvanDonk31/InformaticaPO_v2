import random

class Item:
  item_type = None
  item_enchantments = []
  

  def __init__(self, item_level, item_enchantments):
    self.item_level = item_level
    self.item_enchantments = item_enchantments
    

  def print_stats(self):
    print(self.item_type, "- level:", self.item_level)


class Weapon(Item):

  def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)

    self.item_type = "weapon"
    weapon_list = ["Sword", "Axe"]
    enchantment_list = [
    "Fire I",
    "Fire II",
    "Ice I",
    "Ice II",
    "Dark Mater I",
    "Dark Mater II",
    "Blood I",
    "Blood II"
    ]
    self.weapon_type = random.choice(weapon_list)
    

    if self.weapon_type == "Sword":
      self.min_damage = self.item_level * 2
      self.max_damage = self.item_level * 3

    elif self.weapon_type == "Axe":
      self.min_damage = 1
      self.max_damage = self.item_level * 4

    def print_stats(self):
      Item.print_stats(self)
      print(self.weapon_type, "damage: ", self.min_damage, "-",
            self.max_damage)


class Armor(Item):

  def __init__(self, item_level, item_enchantments):
    Item.__init__(self, item_level, item_enchantments)
    self.item_type = "armor"
    self.defence = self.item_level * 2
