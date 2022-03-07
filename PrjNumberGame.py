"""
Number Game
"""
import random
from random import randint
import math

menor = int(input("Entre com o menor número da faixa: "))
maior = int(input("Entre com o maior número da faixa: "))

rn = random.randint(menor, maior)

count = 0
max = round(math.log(maior - menor + 1, 2))

while count < max:

    print("\n\tVocê tem", max - count, "oportunidades restantes!\n")

    count +=1

    pick = int(input("O número é: "))

    if rn == pick:
        print("\nParabéns, você acertou o número.")
        break
    elif rn > pick:
        print("\nLamento, o número é maior que isso.")
    elif rn < pick:
        print("\nLamento, o número é menor que isso.")

    if count >= max:
        print("\nInfelizmente você esgotou suas chances.")
        print("O computador escolheu o número:", rn)
