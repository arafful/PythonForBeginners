def somar(a, b):
    return a + b

def dividir(a, b):
    return a / b

def multiplicar(a, b):
    return a * b

def subtrair(a, b):
    return a - b

print("Selecione a operação desejada:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("F - Finalizar")

while True:
    operacao = input("Digite 1, 2, 3, 4 ou F")

    if operacao == 'F':
        break

    numero1 = float(input("Primeiro número: "))
    numero2 = float(input("Segundo  número: "))
    if operacao == '1':
        print(numero1, " + ", numero2, " = ", somar(numero1, numero2))

    elif operacao == '2':
        print(numero1, " - ", numero2, " = ", subtrair(numero1, numero2))

    elif operacao == '3':
        print(numero1, " x ", numero2, " = ", multiplicar(numero1, numero2))

    elif operacao == '4':
        print(numero1, " / ", numero2, " = ", dividir(numero1, numero2))

    else:
        print("FFaça uma opção válida.")


