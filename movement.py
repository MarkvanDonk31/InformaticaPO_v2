import os
from chest import Chest, normalChest, goldChest, mythicalChest
from item import ArmorPotion, Item, Axe, Sword, DeathSword, Axe, FireAxe, Bow, Shield, Chainmail, SteelChestplate, Apple, GoldenKey, NormalKey, MythicalKey
from monster import Fenrir, Monster, Skeleton, Goblin, Troll, Balam, Sorcerer, Ghost

##########################################################################

clear = lambda: os.system('clear')

##########################################################################

class Movement:
  monster_list = []
  item_list = []

  # Worldmap / locations
  location = "Galander Castle"
  galander = {
      "Galander Castle": {
          "transitions": {
              "north": "The Road"
          },
          "items": [Apple(1, ""), NormalKey(1, "")],
          "enemies": [],
          "objects": [normalChest(Axe(1, "sharpness"))]
      },
      "The Road": {
          "transitions": {
              "east": "The Dark Cave",
              "south": "Galander Castle",
              "west": "Village of 'Luminairy'"
          },
          "items": [],
          "enemies": [Skeleton(1), Ghost(2)],
          "objects": []
      },
      "Village of 'Luminairy'": {
          "transitions": {
              "north": "The River",
              "east": "The Road",
              "south": "The Bakery",
              "west": "The Blacksmith"
          },
          "items": [MythicalKey(1, "")],
          "enemies": [],
          "objects": []
      },
      "The Blacksmith": {
          "transitions": {
              "east": "Village of 'Luminairy'"
          },
          "items": [ArmorPotion(1, "")],
          "enemies": [Ghost(1)],
          "objects": [normalChest(Axe(1, "sharpness"))]
      },
      "The River": {
          "transitions": {
              "north": "The Farmland",
              "south": "Village of 'Luminairy'",
              "west": "The Forest"
          },
          "items": [Apple(1, "")],
          "enemies": [Skeleton(1)],
          "objects": []
      },
      "The Forest": {
          "transitions": {
              "east": "The River"
          },
          "items": [Shield(1, "")],
          "enemies": [],
          "objects": []
      },
      "The Farmland": {
          "transitions": {
              "north": "The Graveyards",
              "east": "The Trolls Hideout",
              "south": "The River",
          },
          "items": [Apple(1, "")],
          "enemies": [],
          "objects": []
      },
      "The Graveyards": {
          "transitions": {
              "north": "The Bloody Ruins",
              "south": "The Farmlands",
          },
          "items": [],
          "enemies": [Skeleton(1), Skeleton(2), Skeleton(1)],
          "objects": []
      },
      "The Bloody Ruins": {
          "transitions": {
              "south": "The Graveyards",
              "west": "Fenrir's Dungeon",
          },
          "items": [],
          "enemies": [Sorcerer(1), Ghost(3)],
          "objects": []
      },
      "The Dark Cave": {
          "transitions": {
              "north": "Old Woods",
              "east": "The Goblin Village"
          },
          "items": [Shield(1, "")],
          "enemies": [],
          "objects": []
      },
      "The Goblin Village": {
          "transitions": {
              "north": "The Goldmine",
              "west": "The Dark Cave",
          },
          "items": [],
          "enemies": [Goblin(1), Goblin(2), Skeleton(4)],
          "objects": []
      },
      "The Goldmine": {
          "transitions": {
              "south": "The Goblin Village",
          },
          "items": [],
          "enemies": [Ghost(2)],
          "objects": [mythicalChest(DeathSword(1, ""))]
      },
      "Old Woods": {
          "transitions": {
              "north": "The Grasslands",
              "south": "The Dark Cave"
          },
          "items": [ArmorPotion(1, "")],
          "enemies": [Skeleton(1)],
          "objects": []
      },
      "The Grasslands": {
          "transitions": {
              "north": "The Misty Swamps",
              "south": "Old Woods",
              "west": "The Trolls Hideout"
          },
          "items": [Apple(1, "")],
          "enemies": [],
          "objects": []
      },
      "The Trolls Hideout": {
          "transitions": {
              "east": "The Grasslands",
              "west": "The Farmlands"
          },
          "items": [GoldenKey(1, "")],
          "enemies": [Troll(1), Troll(1), Troll(2)],
          "objects": []
      },
      "The Misty Swamps": {
          "transitions": {
              "north": "Balam's Dungeon",
              "east": "The Sorceres Cave",
              "south": "The Misty Swamps"
          },
          "items": [Apple(1, "")],
          "enemies": [Ghost(1), Ghost(3)],
          "objects": []
      },
      "The Sorceres Cave": {
          "transitions": {
              "west": "The Misty Swamps",
          },
          "items": [],
          "enemies": [Sorcerer(1), Sorcerer(1)],
          "objects": [goldChest(SteelChestplate(1, ""))]
      },
      "Balam's Dungeon": {
          "transitions": {
              "south": "The Misty Swamps",
          },
          "items": [],
          "enemies": [Balam(1), Skeleton(1)],
          "objects": []
      },
      "Fenrir's Dungeon": {
          "transitions": {
              "east": "The Bloody Ruins",
          },
          "items": [],
          "enemies": [Fenrir(1), Troll(1)],
          "objects": []
      },
    
  }
  
##########################################################################

  # For each location print a message
  def showLocation():

    if Movement.location == "Galander Castle":
      print('''You are at Galander Castle!''')

    elif Movement.location == "The Road":
      print("You are at The Road..")

    elif Movement.location == "Village of 'Luminairy'":
      print("You are at Village of 'Luminairy'..  ")

    elif Movement.location == "The River":
      print("You are at The River..")

    elif Movement.location == "The Forest":
      print("You are at The Fores..")

    elif Movement.location == "The Farmland":
      print("You are at The Farmland..")

    elif Movement.location == "The Graveyards":
      print("You are at The Graveyards..")

    elif Movement.location == "The Bloody Ruins":
      print("You are at The Bloody Ruins..")

    elif Movement.location == "The Goblin Village":
      print("You are at The Golbin Village..")

    elif Movement.location == "The Goldmine":
      print("You are at The Goldmine..")

    elif Movement.location == "The Sorceres Cave":
      print("You are at The Sorceres Cave..")

    elif Movement.location == "Balam's Dungeon":
      print("You are at Balam's Dungeon..")

    elif Movement.location == "The Blacksmith":
      print("You are at The Blacksmith..")

    elif Movement.location == "The Bakery":
      print("You are at The Bakery..")

    elif Movement.location == "Old Woods":
      print("You are at Old Woods..")

    elif Movement.location == "The Grasslands":
      print("You are at The Grasslands..")

    elif Movement.location == "The Trolls Hideout":
      print("You are at The Trolls Hideout..")

    elif Movement.location == "The Misty Swamps":
      print("You are at The Misty Swamps..")

    elif Movement.location == "Fenrir's Dungeon":
      print("You are at Fenrir's Dungeon..")

    elif Movement.location == "The Dark Cave":
      print("You are at The Dark Cave.. ")

##########################################################################

    Movement.monster_list = Movement.galander[Movement.location]["enemies"]
    Movement.item_list = Movement.galander[Movement.location]["items"]

    # Print the directions, objects items and enemies
    print("Directions:")
    for path_options in Movement.galander[Movement.location]["transitions"]:
      print(" > " + path_options)
    print()

    if len(Movement.galander[Movement.location]["items"]) > 0:
      print("Items:")
      for item in Movement.galander[Movement.location]["items"]:
        print(" > " + item.item_name +  " | " + item.item_lore)
        if len(item.item_enchantments) > 0:
          print("  > Enchantments : " + str(item.item_enchantments))
      print()

    if len(Movement.galander[Movement.location]["enemies"]) > 0:
      print("Enemies:")
      for enemy in Movement.monster_list:
        print(" > " + enemy.monster_type  + "  HP: " + str(enemy.hp) + "/" +  str(enemy.max_hp) + " " + str(enemy.monster_phrase))        
      print()

    if len(Movement.galander[Movement.location]["objects"]) > 0:
      print("Possible objects:")
      for object in Movement.galander[Movement.location]["objects"]:
        print(" > " + str(object.object_name))
      print()

##########################################################################

  # Makes the player able to move to another location
  def walk(direction=str):
    if direction in Movement.galander[Movement.location]["transitions"]:
      Movement.location = Movement.galander[
          Movement.location]["transitions"][direction]
      clear()
    else:
      print("You can't go that way.")


##########################################################################

