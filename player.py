import random
from item import Item, Sword, DeathSword, Shield, Bow, Axe, FireAxe, Chainmail, SteelChestplate
from movement import Movement

##########################################################################

class Player:
  level = 1
  xp = 1
  next_level_xp = 500
  hp = 80
  max_hp = 80
  name = ""
  inventory = [Sword(1, " "), Shield(2, " ")]
  armor = 2

  
  def __init__(self, name):
    self.name = name

  # Attack
  def attack(self):
    weapon_choice = " "
    while weapon_choice not in self.inventory: 
      weapon_choice = input(" > Which weapon do you want to use? ")
      weapon_choice = weapon_choice.lower()
      for item in self.inventory:
        if item.item_type == weapon_choice:
          damage = random.randint(item.min_damage, item.max_damage)
          return damage
        else:
          print("  > You don't have that weapon")
          print()

  # Use
  def use(self):
    item_choice = input(" > Which item do you want to use? ")
    for item in Player.inventory:
      if item.item_type == item_choice:
        if item.item_type == "shield":
          Player.armor = Player.armor + 2
          print(" > You gained 2 armor points! Total armor: " + str(Player.armor))

        elif item.item_type == "chainmail":
          Player.armor = Player.armor + 4
          print(" > You gained 2 armor points! Total armor: " + str(Player.armor))

        elif item.item_type == "steel chestplate":
          Player.armor = Player.armor + 5
          print(" > You gained 2 armor points! Total armor: " + str(Player.armor))

        elif item.item_type == "apple":
          Player.hp = Player.hp + 5
          print(" > You gained 5 health points! Total health: " + str(Player.hp))    

        elif item.item_type == "armor potion":
          Player.armor = Player.armor + 5
          print(" > You gained 5 armor points! Total armor: " + str(Player.armor))
        
        else:
            print("> You do not have that item.")
  
  # Pickup
  def pickUp(self):
    item_pickup = input(" > Which item do you want to pick up? ")
    item_pickup = item_pickup.lower()

    for x in  Movement.galander[Movement.location]["items"]:
      if item_pickup == x.item_type:
        print(" > You picked up a " + x.item_type)
        Player.inventory.append(x)
        Movement.galander[Movement.location]["items"].remove(x)

    else:
        print(" > That item isn't here.")
        
  # Open an chest
  def openChest(self):
    chest_choice = input(" > Which chest do you want to open? ")
    chest_choice = chest_choice.lower()
    for x in Movement.galander[Movement.location]["objects"]:
      if chest_choice == x.chest_type:
        for item in Player.inventory:
          if item.item_type == x.key_type:
            print(" > You opened the chest! You found " + str(x.item_list.item_type) + "!")
            Player.inventory.append(x.item_list)
            Movement.galander[Movement.location]["objects"].remove(x)
            Player.inventory.remove(x.key_type)

      else:
          print(" > You don't have the key to open this chest!")

    
  # Take an hit
  def take_hit(self, damage):

    final_damage = damage - self.armor

    if final_damage > 0:

      self.hp -= final_damage

      if self.hp <= 0:
        print("AAAAAAAARRRGHHH! You died!")
        print()

      else:
        print(" > Ouch! You took ", final_damage, " damage! You have ", self.hp, "HP left!")
        print()

    else:
      print("Your shiny armor protected you! You took no damage!")
      print()


  def heal(self, heal_amount):
    self.hp += heal_amount

    if self.hp > self.max_hp:
      self.hp = self.max_hp

    print("You heald for", heal_amount, "hp, you currently have", self.hp, "/", self.max_hp, "hp.")

  # Gain Exp
  def xp_gain(self, xp_amount):
    Player.xp += xp_amount

    if Player.xp >= Player.next_level_xp:
      Player.level += 1
      Player.xp -= Player.next_level_xp

      Player.next_level_xp *= int(Player.next_level_xp * 1.25)
      Player.max_hp = int(Player.max_hp * 1.2)
      Player.hp = Player.max_hp
      print(" > Wow " + Player.name + "! You leveled up! You are now level " + str(Player.level) + ".")


  # Print player stats
  def print_Stats(self):
    print()
    print("\033[1;30m\033[1m################################################")
    print("\033[1;30m\033[1m#                 Player Stats:                #")
    print("\033[1;30m\033[1m################################################")
    print("\033[1;30m\033[1m#                                              #")
    print("\033[1;30m\033[1m# Name: \033[1;33m", self.name)
    print("\033[1;30m\033[1m# Level: \033[1;33m", self.level)
    print("\033[1;30m\033[1m# HP: \033[1;33m", self.hp, "/", self.max_hp)
    print("\033[1;30m\033[1m# XP: \033[1;33m", self.xp, "/", self.next_level_xp)
    print("\033[1;30m\033[1m#                                              #")
    print("\033[1;30m\033[1m################################################")
    print("\033[1;30m\033[1m#                 Inventory:  (global)         #")
    print("\033[1;30m\033[1m################################################")
    print("\033[1;30m\033[1m#                                              #")
    for items in self.inventory:
      print("\033[1;30m\033[1m# \033[1;33m- " + str(items.item_name) +  " " +  "\""+  items.item_lore +  "\"")
    print("\033[1;30m\033[1m#                                              #")
    print("\033[1;30m\033[1m################################################")
    print()


##########################################################################