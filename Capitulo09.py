"""
    LOOPS - for E while
"""
# for
animais = ["cavalo", "gato", "cachorro", "galinha"]

for b in animais:
    print(b)

for b in "ornitorrinco":
    print(b)

# while
print_counter = 0

while(print_counter < 5):
    print_counter += 1
    print("Whlie loop number:", print_counter)

# break - Saída forçada do loop
turns = 0
while True:
    print(turns)
    turns +=1
    if turns == 5:
        break   # quando a variavel turns atingir o valor 5 sairemos do loop

print("\n")
# continue - Volta ao controle do loop sem passar pelas instruções posteriores

for b in range(1, 10):
    if b % 2 == 0:
        continue
    print(b)

print("\n")

for b in range(1, 5):   # Repare que na saída o 2 será ignogado pelo continue e o 5 está fora do range pela declaração
    if b == 2:
        continue
    print(b)
"""
A função range inclui o primeiro parametro e exclui o último parametro da série
"""
# if, else e elif dentro de lopps
print("if, else e elif dentro de lopps")
counter = 0
while counter < 10:
    counter += 1
    if counter == 8:
        continue

    print(counter)

print("if, else e elif dentro de lopps - usando break")
for a in range(1,10):
    if a == 8:
        break

    print(a)
