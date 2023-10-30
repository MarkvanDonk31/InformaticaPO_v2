from movement import Movement
from player import Player


class Fighting():
    @staticmethod
    def monster_attack(player):
      for monster in Movement.monster_list:
        if monster.hp > 0:
          monster_damage = monster.attack()
          player.take_hit(monster_damage)
        else:   
          Movement.monster_list.remove(monster)
                
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

