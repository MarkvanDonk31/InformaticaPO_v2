import os
from player import Player

clear = lambda: os.system('clear')

##########################################################################
class Visual:

  def openingScreen():
    print(''''\033[1;30m\033[1m

    ################################################
    #                  Welcome to!                 #
    #                GALANDERS QUEST               #
    ################################################
\033[0;37m\033[1m
                   [][][] /""\ [][][]
                    |::| /____\ |::|
                    |[]|_|::::|_|[]|
                    |::::::__::::::|
                    |:::::/||\:::::|
                    |:#:::||||::#::|
                   #%*###&*##&*&#*&##
                  ##%%*####*%%%###*%*#
\033[1;30m\033[1m
    ################################################
    #            Made by Mark en Thijmen           # 
    #            Press ENTER to Continue!          #
    ################################################
    ''')
    input()
    clear()

  def loreScreen():
    print("")
    print('\033[1;30m\033[1m################################################')
    print("\033[1;30m\033[1m#                 Welcome Sir!                 #")
    print('\033[1;30m\033[1m################################################')
    print("\033[1;30m\033[1m#You are a knight from the kingdom of Galender!#")
    print("\033[1;30m\033[1m#It is your task to slay the legendary monsters#")
    print("\033[1;30m\033[1m# called Fenrir and Balam! These beasts form a #")
    print("\033[1;30m\033[1m# threat to the kingdom! On your path you can  #")
    print("\033[1;30m\033[1m# find chest, keys, weapons, armor pieces and  #")
    print("\033[1;30m\033[1m#  enchantments. Combine the keys and chests   #")
    print("\033[1;30m\033[1m# collect the loot! Good luck on your mission! #")
    print("\033[1;30m\033[1m#      What is your name, noble knight?        #")
    print('\033[1;30m\033[1m################################################')
    print()

  def commandScreen():
    print()
    print("\033[1;30m\033[1m#####################################################")
    print("\033[1;30m\033[1m#                   COMMANDS LIST                   #")
    print("\033[1;30m\033[1m#####################################################")
    print("\033[1;30m\033[1m# walk [direction] - Walk in the direction!         #")
    print("\033[1;30m\033[1m# use - Asks you which item you want to use         #")
    print("\033[1;30m\033[1m# help - Shows this menu                            #")
    print("\033[1;30m\033[1m# stats - Shows your player stats                   #")
    print("\033[1;30m\033[1m# pickup - Asks you which item you want to pick up  #")
    print("\033[1;30m\033[1m# open - Asks you which chest you want to open      #")
    print("\033[1;30m\033[1m# attack - Asks you which monster you want to attack#")
    print("\033[1;30m\033[1m#####################################################")
    print()

  def defeatScreen():
    clear()
    print('''\033[1;30m\033[1m
    ################################################
    #               OHNOO!!  You LOST!             #
    #                GALANDERS QUEST               #
    ################################################
\033[0;37m\033[1m

                   [][][]
                    |::| /___
                    |[]|_|::::|_
                      ::::__::::::
                      ::::/||\::::
                    |:#:::||  ::#::|
                   #%*###&*##&*&#*&#
                  ##%%*####*%%%###*%*###
\033[1;30m\033[1m
    ################################################
    #              Thanks for playing!             # 
    #             Beter luck next time!            #
    ################################################
    ''')
  print()

  def winScreen():
    clear()
    print('''\033[1;30m\033[1m

    ################################################
    #               Good job! You won!             #
    #                GALANDERS QUEST               #
    ################################################
\033[0;37m\033[1m
                   [][][] /""\ [][][]
                    |::| /____\ |::|
                    |[]|_|::::|_|[]|
                    |::::::__::::::|
                    |:::::/||\:::::|
                    |:#:::||||::#::|
                   #%*###&*##&*&#*&##
                  ##%%*####*%%%###*%*#
\033[1;30m\033[1m
    ################################################
    #              Thanks for playing!             # 
    #     Now Galander will be peaceful again!     #
    ################################################
    ''')
    print()



##########################################################################
