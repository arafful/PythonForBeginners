"""
    WORD SCRAMBLE PUZZLER
"""
import random

# Prepara um dicionário ramdomico de palavras

def select():
    dicionario = ["janela", "burro", "carpete", "martelo", "bateria", "cortina", "pintura", "celular",
                  "cavalo", "flor", "macaco", "dragão", "python", "trator", "chifre", "notebook"]

    # seleciona aleatoriamente uma palavra
    escolha = random.choice(dicionario)

    return escolha

def scramble(word):
    picked = random.sample(word, len(word))

    scrambled = ".join(picked)"

    return scrambled

def final(ply1, ply2, pl1, pl2):
    print(ply1, "Total score:", pl1)
    print(ply2, "Total score:", pl2)

    who_won(ply1, ply2,pl1,pl2)

    print("Hope you enjoyed the game.")

    return True

def who_won(ply1, ply2, pl1, pl2):
    if pl1 > pl2:
        print(ply1, "won this game")
    elif pl2 > pl1:
        print(ply2, "won this game")
    else:
        print("the game was a tie!")




def game_play():
    g1_name = input("Enter your name Gamer 1: ")
    g2_name = input("Enter your name Gamer 2: ")

    gp1 = 0
    gp2 = 0

    plays = 0

    while True:
        word_select = select()
        xx = scramble(word_select)
        print("Word to unscramble:", xx)

        if plays % 2 == 0:

            print("This turn is for", g1_name)
            entry = input("Enter your choise: ")

            if entry == word_select:
                gp1 += 1
                print("Score is now:", gp1)
                plays += 1
            else:
                print("Sorry, that is incorrect")
                print(g2_name, "you are up next!")

                entry = input("Enter your choice: ")

                if entry == word_select:
                    gp2 += 1
                    print("Score now is:", gp2)

                else:
                    print("Sorry, that is incorrect! The correct word is", word_select)
                    again = int(input("Select 1 to play again or 0 to end the game: "))

                    if again == 0:
                        final(g1_name, g2_name, gp1, gp2)
                        break
        else:
            print("This turn is for:", g2_name)
            entry = input("Enter your choice: ")

            if entry == word_select:
                gp2 += 1
                print("Your score is:", gp2)
                plays += 1
            else:
                print("Sorry, that is incorrect!")
                print(g1_name, "You are up next!")
                entry = input("Enter your choice: ")

                if entry == word_select:
                    gp1 += 1
                    print("Score now:", gp1)
                else:
                    print("Sorry, that is incorrect! The correct word is:", word_select)
                    again = int(input("Press 1 to continue and 0 to quit: "))

                    if again == 0:
                        final(g1_name, g2_name, gp1, gp2)
                        break

                again = int(input("Press 1 to continue and 0 to quit: "))

                if again == 0:
                    final(g1_name, g2_name, gp1, gp2)
                    break

if __name__ == "__main__":
    game_play()






