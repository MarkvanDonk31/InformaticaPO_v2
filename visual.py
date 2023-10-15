import os
from player import Player
from battle import Battle

clear = lambda: os.system('clear')

class Visual:

  def openingScreen():
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

  def loreScreen():
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

  def commandScreen():
    pass

  def defeatScreen():
    clear()
    print('''
    ################################################
    #               OHNOO!!  You LOST!             #
    #                GALANDERS QUEST               #
    ################################################

                   [][][]
                    |::| /___
                    |[]|_|::::|_
                      ::::__::::::
                      ::::/||\::::
                    |:#:::||  ::#::|
                   #%*###&*##&*&#*&#
                  ##%%*####*%%%###*%*###

    ################################################
    #              Thanks for playing!             # 
    #             Beter luck next time!            #
    ################################################
    ''')
  print()

  def winScreen():
    clear()
    print('''
    ################################################
    #               Good job! You won!             #
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
    #              Thanks for playing!             # 
    #     Now Galander will be peaceful again!     #
    ################################################
    ''')
    print()