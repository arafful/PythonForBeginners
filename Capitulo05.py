"""
    DATA TYPES - LISTAS E TUPLAS
"""
# LISTAS

minha_lista = [1, 2, "laranjas", "bananas"]
print(minha_lista)

minha_lista = ["Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"]
print(minha_lista[2])
print(minha_lista[2:4])
print(minha_lista[2:])
minha_lista[4] = "Lobo"
print(minha_lista[4])

print(type(minha_lista))

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
print(minha_lista)

if "Passaro" in minha_lista:
    print("Passaro é um dos meus animais")

minha_lista[2:5] = ["Leão", "Rinoceronte", "Lobo"]
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
print(minha_lista)
minha_lista[1:6] = ["Leão", "Rinoceronte"]
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista.insert(2, "Leão")
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista.append("Leão")
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista_2 = ["Águia", "Leão", "Lobo", "Ovelha"]
minha_lista.extend(minha_lista_2)
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista.remove("Passaro")
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista.pop(4)
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
del minha_lista[4]
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
del minha_lista
# print(minha_lista)    COMENTADA PORQUE DÁ ERRO NA EXECUÇÃO POR NÃO EXISTIR A VARIÁVEL

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista.clear()
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista.sort()
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista.sort(reverse=True)
print(minha_lista)

minha_lista = list(("Elefante", "Tigre", "Macaco", "Urso", "Passaro", "Coelho"))
minha_lista.reverse()
print(minha_lista)

# LISTAS 2D
minha_lista = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [0]
]
print(minha_lista)
print(minha_lista[0][2])

# TUPLAS
tup1 = (9, 10, "Dove", "Crab", 8)
print(tup1)
print(tup1[2])
