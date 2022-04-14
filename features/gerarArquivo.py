from random import randint
from uuid import uuid4
import random

def numeroCpf():
    while True:
        cpf = [randint(0,9) for i in range(9)]
        if cpf != cpf[::-1]:
            break
    for i in range(9,11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digitoVerificador = ((value * 10) % 11) %10
        cpf.append(digitoVerificador)

    result = ''.join(map(str, cpf))
    return result




def NumeroOnda():
    onda = random.randrange(9999, 99999)
    return onda


def geradorXcid():
    Xcid = geradorXcid()
    return uuid4()




onda = str(NumeroOnda())
cpf = str(numeroCpf())
xCid = str(uuid4())



arquivo = open('E:\projeto-cadu\Arquivos\ArquivoBase\ArquivotesteDataDeHoje', 'w+')
arquivo.seek(0)
arquivo.write(cpf)
arquivo.seek(20)
arquivo.write(onda)
arquivo.seek(40)
arquivo.write(xCid)
arquivo.write(' \n')
arquivo.close()





a