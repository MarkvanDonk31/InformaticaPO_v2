import random
import os

from battle import Battle
from item import Armor, Item, Weapon
from monster import Monster, Skeleton, Troll
from player import Player

############################################################################

fenrir_Defeat = False
balam_Defeat = False
game_Status = "running"

#############################################################################

clear = lambda: os.system('clear')

#############################################################################

print(''''

################################################
#                  Welcome to!                 #
#                GALANDERS QUEST               #
################################################

               [][][] /""\ [][][]
                |::| /____\ |::|
                |[]|_|::::|_|[]|
                |::::::__::::::|
                |:::::/||\:::::|
                |:#:::||||::#::|
               #%*###&*##&*&#*&##
              ##%%*####*%%%###*%*#

################################################
#            Made by Mark en Thijmen           # 
#            Press ENTER to Continue!          #
################################################
''')
input()
clear()
#############################################################################

print("")
print('################################################')
print("#                 Welcome Sir!                 #")
print('################################################')
print("#You are a knight from the kingdom of Galender!#")
print("#It is your task to slay the legendary monsters#")
print("# called Fenrir and Balam! These beasts form a #")
print("# threat to the kingdom! On your path you can  #")
print("# find chest, keys, weapons, armor pieces and  #")
print("#  enchantments. Combine the keys and chests   #")
print("# collect the loot! Good luck on your mission! #")
print("#      What is your name, noble knight?        #")
print('################################################')
print()

player_name = input("Your name: ")
player = Player(player_name)

print("Good luck " + player_name + "! Your journey will be legendary!")
print()
print("Press ENTER to Start your journey!")
input()

#############################################################################


battle_count = 0
while player.hp > 0:
  print()
  print("----")
  print()
  battle_count += 1
  print("Battle", battle_count)

  battle = Battle(player)
  battle.fight_battle()

print()
print("You have fought", battle_count, "battles")
player.print_Stats()
print()
print("Thanks for playing!")
