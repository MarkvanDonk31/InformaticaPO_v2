import random
import os
from fighting import Fighting

#from battle import Battle
from item import Item, Sword, DeathSword, Shield, Bow, Axe, FireAxe, Chainmail, SteelChestplate
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

  Movement.showLocation()
  playeraction = input("  > ")
  playeraction = playeraction.lower().split(" ", 1)
  
  if playeraction[0] == "walk":
    Movement.walk(playeraction[1])

  if playeraction[0] == "attack":
    Fighting.player_attack(player)
    Fighting.monster_attack(player)                                   

    pass
  if playeraction[0] == "use":
    pass

  if playeraction[0] == "help":
    Visual.commandScreen()

  if playeraction[0] == "stats":
    Player.print_Stats(player)

  if playeraction[0] == "":
    pass
  else:
    print(" > Is that an valid commands? Try 'help'")

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
