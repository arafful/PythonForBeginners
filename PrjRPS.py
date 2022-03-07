"""
    Rock, Paper & Scissors game
"""
import random
from random import randint

print("Rock - Paper - Scissos Rules\n" +
      "Paper covers Rock - Paper wins\n" +
      "Rock smashes Scissors - Rock wins\n" +
      "Scissors cuts Paper - Scissors wins\n")

while True:
    print("Chose your gane play: \n 1.Rock\n 2.Paper\n 3.Scissors\n")
    player1 = int(input("Player 1, it's your turn: "))
    while player1 > 3 or player1 < 1:
        player1 = int(input("enter a valid number: "))

    if player1 == 1:
        player1_choise = "Rock"
    elif player1 == 2:
        player1_choise = "Paper"
    else:
        player1_choise = "Scissors"

    print("Player 1. You chose", player1_choise)
    print("\nPlease, allow your computer to make its choice...")

    while True:
        player2 = random.randint(1, 3) # escolhe um numero aleatorio entre 1 e 3
        if player2 != player1:
            break

    if player2 == 1:
        player2_choise = "Rock"
    elif player2 == 2:
        player2_choise = "Paper"
    else:
        player2_choise = "Scissors"

    print("The computer has chosen:", player2_choise)
    print(player1_choise, "vs", player2_choise)

    if ((player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 1)):
        print("Paper wins this round =>", end="")
        result = "Paper"
    elif ((player1 == 1 and player2 == 3) or (player1 == 3 and player2 == 1)):
        print("Rock wins this round =>", end="")
        result = "Rock"
    else:
        print("Scissors wins this round =>", end="")
        result = "Scissors"

    if result == player1_choise:
        print("Player 1 wins.")
    else:
        print("Computer wins. Better luck next time.")

    print("Would you like to play again? (S/N)")
    ans = input().upper()

    if ans != "S":
        break

print("\nThanks for playing RPS.")


