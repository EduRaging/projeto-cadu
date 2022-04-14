"gerador de arquivos Mgcbk"

from random import randint
import string
import random

class GeradorArquivo():
    pass

class NumeroCpf:
    def __init__(self, cpf):
        self.cpf = NumeroCpf
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

class GeradorOnda():
    pass

class GeradorXcid:

    pass





