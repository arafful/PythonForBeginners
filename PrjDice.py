"""
    SIMULADOR DE ROLAGEM DE DADOS
"""
import random

menor = 1
maior = 6
rolar = "sim"

while rolar == "sim":
    print("Dados rolando >>>")
    print("Dados parados em >>>")
    print(random.randint(menor, maior))
    print(random.randint(menor, maior))

    rolar = input("Rolar os dados novamente?").upper()

    if rolar != "S":
        break
    else:
        rolar = "sim"
