from movement import Movement
from player import Player

##########################################################################

class Fighting():
    # Variable to check if fenir and balam are defeated
    fenrir_Defeat = False
    balam_Defeat = False

    # check if enemy is alive (and if they are balam and fenrir for game win) 
    @staticmethod
    def monster_attack(player):
      for monster in Movement.monster_list:
        if monster.hp > 0:
          monster_damage = monster.attack()
          player.take_hit(monster_damage)
        elif monster.hp <= 0:
          Player.xp_gain(monster.xp_value, monster.xp_value)
          print("You gained: " + str(monster.xp_value) + "xp!")
          Movement.monster_list.remove(monster)
          if monster.monster_type == "Balam":
            Fighting.balam_Defeat = True
            print(Fighting.fenrir_Defeat)
            print(Fighting.balam_Defeat)
          elif monster.monster_type == "Fenrir":
            Fighting.fenrir_Defeat = True
            print(Fighting.fenrir_Defeat)
            print(Fighting.balam_Defeat)

    # Attack an enemy
    @staticmethod
    def player_attack(player):
      if len(Movement.monster_list) > 1:
        max_target = len(Movement.monster_list)
        target = -1

        while target < 1 or target > max_target:
          target = int(
              input(" > Which monster would you like to attack? ( 1 - " +
                    str(max_target) + " ) "))
        target -= 1
        print("  > You are attacking " + Movement.monster_list[target].monster_type)

      else:
        target = 0
        print("  > You are attacking " + Movement.monster_list[target].monster_type)

      player_damage = player.attack()
    
      if Movement.monster_list[target].hp > 0:
        Movement.monster_list[target].take_hit(player_damage, target)
        
      else:
        print("You hit the dead monster. It is still dead...")

##########################################################################