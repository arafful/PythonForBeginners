"""
    FUNÇÕES
"""
def names(fname, lname):
    print(fname, lname)

print("Vamos chamar a função names")
names("André", "Rafful")
names("Monica", "Rafful")
names("Felipe", "Rafful")
names("Luiza", "Rafful")

# Argumento default
def func1(hlang = "Inglês"):
    print("Minha linguagem nativa é", hlang)

func1()
func1("Alemão")

# Usando uma LISTA como parâmetro
def func2(animais):
    for z in animais:
        print(z)

animais = ["Elefante", "Tigre", "Urso"]
func2(animais)

def funcscope():
    animais = "bird"
    print("animal definido dentro da função:", animais)


animais = "Cachorro"
print("animal definido fora da função:", animais)
funcscope()

