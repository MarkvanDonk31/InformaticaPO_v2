import random
from monster import Monster, Skeleton, Troll
from item import Item, Weapon, Armor


class Battle:

  def __init__(self, player):
    self.player = player
    self.difficulty = random.randint(1, 3)
    self.monster_list = []
    self.xp_value = 0
    monster_type = ["Skeleton", "Troll"]

    for i in range(self.difficulty):
      monster_choice = random.choice(monster_type)
      ######################################################### Level
      if monster_choice == "Skeleton":
        self.monster_list.append(Skeleton(self.player.level))  ##

      elif monster_choice == "Troll":
        self.monster_list.append(Troll(self.player.level))  ##

      self.xp_value += self.monster_list[i].xp_value

  def battle_stats(self):
    print("You are fighting:")

    for i in range(self.difficulty):
      print("Enemy", i + 1)
      self.monster_list[i].print_stats()
      print()

    print("##############")
    print()

  def generate_loot(self, item):
    loot = False

    if self.difficulty == 1:
      if random.randint(1, 100) <= 25:
        loot = True

    elif self.difficulty == 2:
      if random.randint(1, 100) <= 40:
        loot = True

    elif self.difficulty == 3:
      if random.randint(1, 100) <= 60:
        loot = True

    if loot == True:

      loot_list = ["Weapon", "Armor"]
      loot_type = random.choice(loot_list)

      if loot_type == "Weapon":
        item = Weapon(random.randint(self.player.level, self.player.level + 1), "")
        print("Yay! The monsters dropped a new weapon piece!")
      elif loot_type == "Armor":
        item = Armor(random.randint(self.player.level, self.player.level + 1), "")
        print("Yay! The monsters dropped a new armor piece!")

      item.print_stats()

      print()
      print("Your current stats are!")
      self.player.print_stats()
      print()

      choice = input("Do you want to equip the new item (Y/N)?")
      choice = choice.lower()

      if choice == "n":
        print("You left the item on the ground...")

      else:
        self.player.equip.item(item)
        print("You equiped the new item!")

    else:
      print("The monsters dropped nothing...")

  def monster_attack(self):
    for monster in self.monster_list:
      if monster.hp > 0:
        monster_damage = monster.attack()
        self.player.take_hit(monster_damage)

  def player_attack(self):
    if len(self.monster_list) > 1:
      max_target = len(self.monster_list)
      target = -1

      while target < 1 or target > max_target:
        target = int(
            input("Which monster would you like to attack? ( 1 -" +
                  str(max_target)))
      target -= 1

    else:
      target = 0

    player_damage = self.player.attack()

    if self.monster_list[target].hp > 0:
      self.monster_list[target].take_hit(player_damage)
    else:
      print("You hit the dead monster. It is still dead...")

  def player_heal(self):
    if random.randint(1, 100) <= 40:
      heal_amount = (random.randint(self.player.max_hp // 4,
                                    self.player.max_hp // 3))
      self.player.heal(heal_amount)

    else:
      print("You tried to heal yourself but failed...")

  def player_run(self):
    if random.randint(1, 100) <= 25:
      print("You rand away! You lost the monsters!")
      return True

    else:
      print("You tried to run away but failed")
      return False

  def player_quit(self):
    print("You gave up...")
    self.player.hp = 0

  def fight_battle(self):
    print()
    print("You are under attack")

    while True:
      print("#### Battle Round ####")
      self.battle_stats()

      player_action = ""
      while player_action not in ["S", "F", "H", "R", "Q"]:
        player_action = input(
            "What will you do? (S)tats, (F)ight, (H)eal, (R)un, (Q)uit").upper(
            )

      if player_action == "S":
        self.player.print_Stats()
        input("Press enter to continue the fight")

      elif player_action == "F":
        self.player_attack()

        monster_alive = 0
        for monster in self.monster_list:
          if monster.hp > 0:
            monster_alive += 1

        if monster_alive > 0:
          self.monster_attack()

        else:
          print("############################")
          print("You won the battle!")
          print("############################")

          self.player.xp_gain(self.xp_value)

          self.generate_loot("")
          break

      elif player_action == "H":
        self.player_heal()
        print()
        self.monster_attack()

      elif player_action == "R":
        if self.player_run() == True:
          break

        else:
          self.monster_attack()

      elif player_action == "Q":
        self.player.quit()
        break

      if self.player.hp <= 0:
        print("################")
        print("!!! You died !!!")
        print("################")

        break
