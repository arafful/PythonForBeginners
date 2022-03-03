"""
    OPERADORES
"""
# Aritméticos
print("ARITIMÉTICOS")
print("============")
print(10 + 20)
print(30 - 10)
print(30 / 10)
print(30 // 8)  # Divisão arredondda
print(30 * 8)  #
print(30 ** 3)  # Exponencial
print(5 % 2)  # Módulo

# Comparadores
print("COMPARADORES")
print("============")
a = 10
b = 20
print(a == b)   # IGUALDADE
print(a != b)   # NEGAÇÃO
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# Lógico
print("LÓGICOS")
print("=======")
a = 8
b = 10
if a > 10 and b == 10:
    print("Verdadeiro")

if not (a > 10):
    print("a <= 10")
else:
    print("a é > 10")

a = 20
b = 25
if a >= 10 or b <= 25:
    print("Verdadeiro")
else:
    print("Falso")

# Atribuição
print("ATRIBUIÇÃO")
print("==========")
a = 10
print("a -> ", a)
a += 5
print("a += 5 ->", a)
a -= 5
print("a -= 5 ->", a)
a *= 5
print("a *= 5 ->", a)
a /= 5
print("a /= 5 ->", a)
a = 16
a %= 5
print("16 %= 5 ->", a)
a = 5
a **= 3
print("5 **= 3 ->", a)
a = 9
a //= 3
print("9 //= 3 ->", a)

# Bitwise
print("BITWISE")
print("=======")
print(bin(70))
a = 5
b = 9
print(a & b)