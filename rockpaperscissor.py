#-------------------------------------------------------------------------------
#   File: rockpaperscissor.py       Author: Anthony Hein
#
#   Description: A Python program to serve as a reference for an ArnoldC
#   program which implements Rock, Paper, Scissors.
#-------------------------------------------------------------------------------

from sys import exit, stdout
from random import randint

def playAFriend():
    print("-------------------------------------------------------------------")
    print("Beginning two player local rock, paper, scissors game.")
    print()

    prompt = "y"
    while prompt == "y":
        print("*******************************************************************")
        print("Player 1 enter your option (r/p/s): ", end="")
        p1 = input()
        print("\x1B[F\x1B[2K", end="")
        print("Player 1 enter your option (r/p/s): (hidden)")
        print()

        print("Player 2 enter your option (r/p/s): ", end="")
        p2 = input()
        print("\x1B[F\x1B[2K", end="")
        print("Player 2 enter your option (r/p/s): (hidden)")
        print()

        print("Player 1: " + p1)
        print("Player 2: " + p2)
        print()

        if p1 == p2:
            print("Tie, you both threw " + p1 + "!")
        elif p1 == "r":
            if p2 == "s":
                print("Rock crushes scissors. Player 1 wins!")
            elif p2 == "p":
                print("Paper covers rock. Player 2 wins!")
        elif p1 == "s":
            if p2 == "r":
                print("Rock crushes scissors. Player 2 wins!")
            elif p2 == "p":
                print("Scissors cuts paper. Player 1 wins!")
        elif p1 =="p":
            if p2 == "r":
                print("Paper covers rock. Player 1 wins!")
            elif p2 == "s":
                print("Scissors cuts paper. Player 2 wins!")

        print()
        print("Continue? (y/n): ", end="")
        prompt = input()

    return

def playAComputer():
    print("-------------------------------------------------------------------")
    print("Beginning a game against a computer.")
    print()

    options = ["r", "p", "s"]

    prompt = "y"
    while prompt == "y":
        print("*******************************************************************")
        print("Player, enter your option (r/p/s): ", end="")
        p1 = input()
        print("\x1B[F\x1B[2K", end="")
        print("Player, enter your option (r/p/s): (hidden)")
        print()

        print("Computer is selecting....")
        print()

        p2 = options[randint(0,2)]

        print("Player 1: " + p1)
        print("Computer: " + p2)
        print()

        if p1 == p2:
            print("Tie, you both threw " + p1 + "!")
        elif p1 == "r":
            if p2 == "s":
                print("Rock crushes scissors. Player wins!")
            elif p2 == "p":
                print("Paper covers rock. Computer wins!")
        elif p1 == "s":
            if p2 == "r":
                print("Rock crushes scissors. Computer wins!")
            elif p2 == "p":
                print("Scissors cuts paper. Player wins!")
        elif p1 =="p":
            if p2 == "r":
                print("Paper covers rock. Player wins!")
            elif p2 == "s":
                print("Scissors cuts paper. Computer wins!")

        print()
        print("Continue? (y/n): ", end="")
        prompt = input()

    return

if __name__ == "__main__":

    while True:
        print("===================================================================")
        print("Play a friend, play a computer, or quit? (f/c/q): ", end="")
        option = input()

        if option == "f":
            playAFriend()
        elif option == "c":
            playAComputer()
        elif option == "q":
            break

    exit(1)
