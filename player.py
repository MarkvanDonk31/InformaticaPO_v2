import random

from item import Armor, Weapon


class Player:
  level = 10
  xp = 0
  next_level_xp = 500
  hp = 1
  max_hp = 50
  name = ""
  inventory = []

  def __init__(self, name):
    self.name = name

    self.weapon = Weapon(1, "")
    self.armor = Armor(1, "")

  def attack(self):
    damage = self.level + random.randint(self.weapon.min_damage,
                                         self.weapon.max_damage)
    print(self.name, "attacks with a ", self.weapon.weapon_type, "for", damage,
          "damage")
    return damage

  def take_hit(self, damage):

    final_damage = damage - self.armor.defence

    if final_damage > 0:

      self.hp -= final_damage

      if self.hp <= 0:
        ## Dood
        print("AAAAAAAARRRGHHH! You died!")
      else:
        print("Ouch! You took ", final_damage, " damage!")
        print("You have ", self.hp, "HP left!")

    else:
      print("Your shiny armor protected you! You took no damage!")

  def heal(self, heal_amount):
    self.hp += heal_amount

    if self.hp > self.max_hp:
      self.hp = self.max_hp

    print("You heald for", heal_amount, "hp.")
    print("You currently have", self.hp, "/", self.max_hp, "hp.")

  def xp_gain(self, xp_amount):
    self.xp += xp_amount
    print("You have gained", xp_amount, "xp!")

    if self.xp >= self.next_level_xp:
      self.level += 1
      self.xp -= self.next_level_xp

      self.next_level_xp *= int(self.next_level_xp * 1.25)
      self.max_hp = int(self.max_hp * 1.2)
      self.hp = self.max_hp

      print("YAY! You reached level", self.level, "!")
      self.print_Stats()

  def equip_item(self, item):
    if item.item_type == "weapon":
      self.weapon = item
    elif item.item_type == "armor":
      self.armor = item

  def print_Stats(self):
    print()
    print("##########################")
    print("####   Player Stats:   ###")
    print("##########################")
    print("Name: ", self.name)
    print("Level: ", self.level)
    print("HP: ", self.hp, "/", self.max_hp)
    print("XP: ", self.xp, "/", self.next_level_xp)
    print("--------------------------")
    self.weapon.print_stats()
    self.armor.print_stats()
    print("##########################")
