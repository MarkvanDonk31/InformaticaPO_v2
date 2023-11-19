import os
from fighting import Fighting

#from battle import Battle
from chest import Chest
from item import Item, Sword, DeathSword, Shield, Bow, Axe, FireAxe, Chainmail, SteelChestplate
from monster import Monster, Skeleton, Troll
from player import Player
from visual import Visual
from movement import Movement

############################################################################

game_Status = "running"
battle_count = 0

#############################################################################

clear = lambda: os.system('clear')

#############################################################################

# Opening screen
Visual.openingScreen()

# Lore screen
Visual.loreScreen()

#P Player name
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

  # Show the current location and ask the player what he wants to d
  Movement.showLocation()
  playeraction = input("  > ")
  playeraction = playeraction.lower().split(" ", 1)

  # Makes the player walk
  if playeraction[0] == "walk":
    clear()
    Movement.walk(playeraction[1])

  # Makes the player attack an enemie
  elif playeraction[0] == "attack":
    Fighting.player_attack(player)
    Fighting.monster_attack(player)  

  # Make the player use an item
  elif playeraction[0] == "use":
    Player.use(player)

  # Shows the player a help window
  elif playeraction[0] == "help":
    Visual.commandScreen()

  # Shows the player his stays
  elif playeraction[0] == "stats":
    Player.print_Stats(player)

  # Makes the player pick up an item
  elif playeraction[0] == "pickup":
    Player.pickUp(player)

  # Opens a chest with a key
  elif playeraction[0] == "open":
    Player.openChest(player) 

  # If the command doesn't exist
  else:
    print(" > That command does not exist..")


#############################################################################

## Check if the plater is alive, if HP < 0 than the game stops.
  if player.hp < 0:
    game_Status = "player_death"

  # Check if the player won the game by killing Balam and Fenrir.
  # elif fenrir_Defeat == True and balam_Defeat == True:
  #   game_Status = "player_win"

  if Fighting.fenrir_Defeat == True and Fighting.balam_Defeat == True:
    game_Status = "player_win"

## Show visual  of deathScreen
if game_Status == "player_death":
  Visual.defeatScreen()

## Show visual of winScreen
elif game_Status == "player_win":
  Visual.winScreen()

#############################################################################
