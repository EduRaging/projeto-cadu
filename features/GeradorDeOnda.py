import random


# gerar um numero randomizado de 5 casas decimais
def NumeroOnda():
    onda = random.randrange(9999, 99999)
    return onda

print("\nOnda numero: ", NumeroOnda() )


