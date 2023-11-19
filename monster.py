import random

##########################################################################
class Monster():
  hp = 1
  max_hp = 1
  min_damage = 1
  max_damage = 1

  monster_type = None
  monster_phrase = " "
  monster_loot = []

  xp_value = 1

  def __init__(self, level):
    self.level = level

  def attack(self):
    damage = random.randint(self.min_damage, self.max_damage)
    return damage

  def take_hit(self, damage, target):
    self.hp -= damage

    if self.hp > 0:
      print(" > ", self.monster_type, " has ",  self.hp, " HP left.")
      print()

    else:
      print(" > ", self.monster_type, " was slain.")
      print()

  # Prints the monster's stats
  def print_stats(self):
    print(self.monster_type, "- level", self.level)
    if self.hp > 0:
      print("HP: ", self.hp, "/", self.max_hp)
    else:
      print("*Dead*")

  # Prints the monster phrase of every monster
  def monstertalk(monster_type):
    print(monster_type.monster_phrase)


##Class Skeleton
class Skeleton(Monster):

  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Skeleton"
    self.monster_phrase = " *RATLLE* I'm dead but my bones are still remaining!"
    self.hp = 15
    self.max_hp = 15
    self.min_damage = 5
    self.max_damage = 10
    self.xp_value = 150
    self.monster_loot = []

##Class Troll
class Troll(Monster):

  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Troll"
    self.monster_phrase = " *OEHAA* uhh.. Troll am I uuh.."
    self.hp = 20
    self.max_hp = 20
    self.min_damage = 8
    self.max_damage = 14
    self.xp_value = 200
    self.monster_loot = []
    self.crit_chance = max(30, level * 10)


##Class Sorcerer
class Sorcerer(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Sorcerer"
    self.monster_phrase = " *PFEWWH* Fire... is POWER!"
    self.hp = 25
    self.max_hp = 25
    self.min_damage = 10
    self.max_damage = 14
    self.xp_value = 250
    self.monster_loot = []


##Class Ghost
class Ghost(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Ghost"
    self.monster_phrase = " *BOO!* Death doesn't stop me!"
    self.hp = 20
    self.max_hp = 20
    self.min_damage = 7
    self.max_damage = 12
    self.xp_value = 150
    self.monster_loot = []


##Class Goblin
class Goblin(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Goblin"
    self.monster_phrase = " *GRRRRR* Give me your gold!"
    self.hp = 20
    self.max_hp = 20
    self.min_damage = 7
    self.max_damage = 12
    self.xp_value = 175
    self.monster_loot = []


##Class Fenrir (Boss)
class Fenrir(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Fenrir"
    self.monster_phrase = "  *AWOEHH* I.. want.. your.. BLOOD!"
    self.hp = 40
    self.max_hp = 40
    self.min_damage = 9
    self.max_damage = 16
    self.xp_value = 300
    self.monster_loot = []
    self.crit_chance = max(30, level * 10)

  def attack(self):
    damage = random.randint(self.min_damage, self.max_damage)
  
    if random.randint(1, 100) <= self.crit_chance:
      print(" > ", self.monster_type, "whips is tail against you, with its special attack!")
      damage *= 2
  
    return damage


##Class Balam (Boss)
class Balam(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Balam"
    self.monster_phrase = " *HMMM* Even death fears me..."
    self.hp = 40
    self.max_hp = 40   
    self.min_damage = 10
    self.max_damage = 18
    self.xp_value = 300
    self.monster_loot = []
    self.crit_chance = max(30, level * 10)
    
  def attack(self):
    damage = random.randint(self.min_damage, self.max_damage)
  
    if random.randint(1, 100) <= self.crit_chance:
      print(" > ", self.monster_type, "calls all hell monsters upon you with its special attack!")
      damage *= 2
  
    return damage

##########################################################################






