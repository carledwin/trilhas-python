#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
Jogo de Dados
Programa sob licença GNU V.1
Desenvolvido por: Carl Edwin Antonio Nascimento
Versão 1.0.0
"""

from random import randint

print('Jogo de Dados')
print('Test sua sorte')

while True:
    numero = int(input('\nEscolha um numero entre 1 e 6: '))
    dado = randint(1, 6)
    if dado == numero:
        print('\n\nParabéns, saiu o seu número no dado!')
        print('O número sorteado foi: ', str(dado),' e o número que você escolheu foi: ', str(numero))
    else:
        print('\n\nNão foi dessa vez :')
        print('O número sorteado foi: ', str(dado),' e o número que você escolheu foi: ', str(numero) )

    print('\n\nDeseja tentar a sorte novamente?')
    continuar = input('\nDigite C para Continuar ou N para Sair:')

    if continuar == 'S' or continuar == 'n':
        break
