import random

from battle import Battle
from item import Armor, Item, Weapon
from monster import Monster, Skeleton, Troll
from player import Player

player_name = input("What is your name, sir?")

player = Player(player_name)
print("Good luck! ", player_name)
print("Tof maat")
print("Helloooo")

input("Press enter to play!")

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
