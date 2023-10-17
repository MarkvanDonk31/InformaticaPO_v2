import random


class Monster():
  hp = 1
  max_hp = 1
  min_damage = 1
  max_damage = 1

  monster_type = None
  monster_phrase = "."

  xp_value = 1

  def __init__(self, level):
    self.level = level

  def attack(self):
    damage = random.randint(self.min_damage, self.max_damage)
    print(self.monster_type, "attacks for", damage, "damage")
    return damage

  def take_hit(self, damage):
    self.hp -= damage

    if self.hp > 0:
      print(self.monster_type, "has", self.hp, "HP left.")

    else:
      print(self.monster_type, "was slain.")

  def print_stats(self):
    print(self.monster_type, "- level", self.level)
    if self.hp > 0:
      print("HP: ", self.hp, "/", self.max_hp)
    else:
      print("*Dead*")



  def monstertalk(monster_type):
    print(monster_type.monster_phrase)



class Skeleton(Monster):

  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Skeleton"
    self.monster_phrase = " *RATLLE* I'm dead but my bones are still remaining!"

    self.hp = 10
    self.max_hp = 10
    self.min_damage = self.level + 1
    self.max_damage = self.level * 3

    self.xp_value = 100 + self.level * 20


class Troll(Monster):

  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Troll"
    self.monster_phrase = " *OEHAA* uhh.. Troll am I uuh.."

    self.hp = 20
    self.max_hp = 20
    self.min_damage = 5
    self.max_damage = 10

    self.xp_value = 100 + self.level * 20

    self.crit_chance = max(30, level * 10)

  def attack(self):
    damage = random.randint(self.min_damage, self.max_damage)

    if random.randint(1, 100) <= self.crit_chance:
      print(self.monster_type, "makes a critical hit!")
      damage *= 2

    print(self.monster_type, "attacks for", damage, "damage")
    return damage



class Sorcerer(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Sorcerer"
    self.monster_phrase = " *PFEWWH* Fire... is POWER!"

    self.hp = 20
    self.max_hp = 20
    


class Ghost(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Ghost"
    self.monster_phrase = " *BOO!* Death doesn't stop me!"

    self.hp = 20
    self.max_hp = 20



class Goblin(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Goblin"
    self.monster_phrase = " *GRRRRR* Give me your gold!"

    self.hp = 20
    self.max_hp = 20



class Fenrir(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Fenrir"
    self.monster_phrase = "  *AWOEHH* I.. want.. your.. BLOOD!"

    self.hp = 20
    self.max_hp = 20



class Balam(Monster):
  def __init__(self, level):
    Monster.__init__(self, level)

    self.monster_type = "Balam"
    self.monster_phrase = " *HMMM* Even death fears me..."

    self.hp = 20
    self.max_hp = 20




