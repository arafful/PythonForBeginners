"""
    HANGMAN GAME
"""
import random
from PrjHangManWords import hm_words

def pick_word():
    pick = random.choice(hm_words)
    return pick.upper()

def game(pick):
    comp_word = "_" * len(pick)
    picked = False
    picked_letras = []
    picked_word = []
    chances = 6
    print("Comece a jogar Hangman")
    print(hangman_forca(chances))
    print(comp_word)
    print("\n")

    while not picked and chances > 0:
        palpite = input("Digite a palavra ou letra para começar: ").upper()

        if len(palpite) == 1 and palpite.isalpha():
            if palpite in picked_letras:
                print("Você já usou esse caracter", palpite)
            elif palpite not in pick:
                print(palpite, "é incorreto.")
                chances -= 1
                picked_letras.append(palpite)
            else:
                print("Parabéns,", palpite, "é correto")
                picked_letras.append(palpite)
                index_words = list(comp_word)
                indexing = [i for i, letter in enumerate(pick) if letter == palpite]
                for index in indexing:
                    index_words[index] = palpite
                    comp_word = "".join(index_words)
                    if "_" not in comp_word:
                        picked = True
        elif len(palpite) == len(pick) and palpite.isalpha():
            if palpite in picked_word:
                print(palpite, "já foi usada.")
            elif palpite != pick:
                print(palpite, "não é a palavra.")
                chances -= 1
                picked_word.append(palpite)
            else:
                picked = True
                comp_word = pick
        else:
            print("Sua seleção não é válida.")
        print(hangman_forca(chances))
        print(comp_word)
        print("\n")
    if picked:
        print("Parabéns, você acertor a palavra.")
    else:
        print("OPA... Parece que suas chances terminaram, A palavra era:", pick)

def hangman_forca(chances):
    forca = ["O-<<-<<", "O-<<-<", "O-<<-", "O-<-", "O--", "O", ""]
    return forca[chances]

def main():
    pick = pick_word()
    game(pick)
    while input("Quer ter outra chance?(S/N)").upper() == "S":
        pick = pick_word()
        game(pick)

if __name__ == "__main__":
    main()
