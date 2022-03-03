"""
    DATA TYPES - STRINGS E NÚMEROS EM PYTHON
"""
#==============
# STRINGS
#==============
print('sentença em aspas simples')
print("sentença em aspas duplas")

fname = "Harry"
lname = "Greenwood"
print("My name is", fname, lname)

# CONCATENAÇÃO
str1 = "Sally Brown"
str2 = "tem olhos azuis"
print(str1, str2)
print(str1 + " " + str2)

# REPETIÇÃO
str3 = "laa dee dah "
print(str3 * 3)

# REPLACE
print(str3.replace("d", "t"))
print(str3.replace("dah", "row"))

# SUBSTRING
str4 = "Tone"
print(str4[1])
print(str4[1:4])
print(str4[1:3])

str5 = "sublime"
print(str5)
print(str5[-4])
print(str5[-4:-1])
print(str5[-4:])

#==============
# NUMEROS
#==============
print(50)
print(5 + 9.03)
print(-10 + 5)
print(10 * 3 + 7)
print(10 * (3 + 7))

numv1 = 9
print(numv1)
numv2 = (9 + 1)
print(numv1 * numv2)

print("Tommy turned " + str(numv1))

# FUNÇÕES MATEMÁTICAS
print(abs(-9))
numv = -9
print(abs(numv))
print(max(3, 6, 9))
numvar1 = 3
numvar2 = 6
numvar3 = 9
print(max(numvar1, numvar2, numvar3))

print(min(3, 6, 9))
numvar1 = 3
numvar2 = 6
numvar3 = 9
print(min(numvar1, numvar2, numvar3))

print(pow(3, 3))
print(pow(numvar1, numvar2))

print(round(9.4))
print(round(9.5))
numvar4 = 9.6
print(round(numvar4))

a = 2
b = 9.5
c = 45J
print(type(a))
print(type(b))
print(type(c))

