import random
import os

from battle import Battle
from item import Armor, Item, Weapon
from monster import Monster, Skeleton, Troll
from player import Player
from visual import Visual
from movement import Movement

############################################################################

fenrir_Defeat = False
balam_Defeat = False
game_Status = "running"
battle_count = 0


#############################################################################

clear = lambda: os.system('clear')

#############################################################################

Visual.openingScreen()

Visual.loreScreen()
player_name = input("Your name: ")
player = Player(player_name)

print("Good luck " + player_name + "! Your journey will be legendary!")
print()
print("Press ENTER to Start your journey!")
input()
clear()

#############################################################################


## While the game_Status == running the game is during.
while game_Status == "running":
  # print("----")
  # print()

  
  # battle = Battle(player)
  # battle.fight_battle()

  Movement.showLocation()
  playeraction = input("  > ")
  playeraction = playeraction.lower().split(" ", 1)

  if playeraction[0] == "walk":
    Movement.walk(playeraction[1])


#############################################################################
  
## Check if the plater is alive, if HP < 0 than the game stops.
  if player.hp < 0:
    game_Status = "player_death"

  # Check if the player won the game by killing Balam and Fenrir.
  elif fenrir_Defeat == True and balam_Defeat == True:
    game_Status = "player_win"

## Show visual  of deathScreen
if game_Status == "player_death":
      Visual.defeatScreen()

## Show visual of winScreen
if game_Status == "player_win":
      Visual.winScreen()
  
#############################################################################
