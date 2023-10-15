import os
clear = lambda: os.system('clear')

class Movement:

  location = "Galander Castle"
  galander = {
      "Galander Castle": {
          "transitions": {
              "north": "The Road"
          },
          "items": [],
          "enemies": [],
          "objects" : []
      },
      "The Road": {
          "transitions": {
              "east": "The Dark Cave",
              "south": "Galender Castle",
              "west": "Village of 'Luminairy'"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "Village of 'Luminairy'": {
          "transitions": {
              "north": "The River",
              "east": "The Road",
              "south": "The Bakery",
              "west": "The Blacksmith"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The River": {
          "transitions": {
              "north": "The Farmland",
              "south": "Village of 'Luminairy'",
              "west": "The Forest"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Forest": {
          "transitions": {
              "east": "The River"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Farmland": {
          "transitions": {
              "north": "The Graveyards",
              "east": "The Trolls Hideout",
              "south": "The River",
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Graveyards": {
          "transitions": {
              "north": "The Bloody Ruins",
              "south": "The Farmlands",
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Bloody Ruins": {
          "transitions": {
              "south": "The Graveyards",
              "west": "Fenrir's Dungeon",
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Dark Cave": {
          "transitions": {
              "north": "Old Woods",
              "east": "The Goblin Village"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Goblin Village": {
          "transitions": {
              "north": "The Goldmine",
              "west": "The Dark Cave",
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Goldmine": {
          "transitions": {
              "south": "The Goblin Village",
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "Old Woods": {
          "transitions": {
              "north": "The Grasslands",
              "south": "The Dark Cave"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Grasslands": {
          "transitions": {
              "north": "The Misty Swamps",
              "south": "Old Woods",
              "west": "The Trolls Hideout"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Trolls Hideout": {
          "transitions": {
              "east": "The Grasslands",
              "west": "The Farmlands"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Misty Swamps": {
          "transitions": {
              "north": "Balam's Dungeon",
              "east": "The Sorceres Cave",
              "south": "The Misty Swamps"
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "The Sorceres Cave": {
          "transitions": {
              "west": "The Misty Swamps",
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
      "Balam's Dungeon": {
          "transitions": {
              "south": "The Misty Swamps",
          },
        "items": [],
        "enemies": [],
        "objects" : []
      },
  }

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

    print("Possible directions:")
    for path_options in Movement.galander[Movement.location]["transitions"]:
      print(" > " + path_options)
    print()

    if len(Movement.galander[Movement.location]["items"]) > 0:
      print("Possible items:")
      for item in Movement.galander[Movement.location]["items"]:
        print(" > " + item)
      print()

    if len(Movement.galander[Movement.location]["enemies"]) > 0:
      print("Possible enemies:")
      for enemy in Movement.galander[Movement.location]["enemies"]:
        print(" > " + enemy)
      print()

    if len(Movement.galander[Movement.location]["objects"]) > 0:
      print("Possible objects:")
      for object in Movement.galander[Movement.location]["objects"]:
        print(" > " + object)
      print()



  def walk(direction=str):
    if direction in Movement.galander[Movement.location]["transitions"]:
      Movement.location = Movement.galander[Movement.location]["transitions"][direction]
      clear()
    else:
      print("You can't go that way.")