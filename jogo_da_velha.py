#!/usr/bin/#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
    Um jogo da velha simples.
    Versão 1.0.0
    Desenvolvido por: Carl Edwin Antonio Nascimento
    Licenca:
    Copyright 2019 - Carl Edwin Antonio Nascimento
"""

from curses import initscr, wrapper
from random import randint

def main(stdscr):

    reiniciar_tela(stdscr)

    while True:
        entrada = stdscr.getkey()

        if entrada == 'Q' or entrada == 'q':
            break
        elif entrada == 'H' or entrada == 'h':
            ajuda(stdscr)
        else:
            boas_vindas(stdscr)


if __name__ == "__main__":
    initscr()
    wrapper(main)

def boas_vindas(stdscr):
    stdscr.addstr(1, 1, 'Bem-vindo ao Jogo da Velha!')
    stdscr.addstr(2, 1, 'Pressione \'S\' para sair ou \'H\' para obter ajuda' )
    stdscr.addstr(16, 1, 'Desenvolvido por: Carl Edwin Antonio Nascimento')
    stdscr.addstr(17, 1, 'Licença Copyright 2019 - Carl Edwin Antonio Nascimento')

def ajuda(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 1, 'Pressione \'S\' para sair ou \'H\' para exibir essa ajuda.')
    stdscr.addstr(2, 1, 'Para mudar a posição, use as teclas \'A\' para se movimentar para a esquerda, \'F\' para se movimentar para a direita, \'E\' para se movimentar para cima e \'C\' para se movimentar para baixo.')
    stdscr.addstr(3, 1, 'Para definir uma posição do jogo, digite \'L\'.')
    stdscr.addstr(4, 1, 'Para reinciar a partida, digite \'Y\'')
    stdscr.addstr(5, 1, 'Pressione \'espaço\' para sair desta tela.')
    stdscr.refresh()

def reiniciar_tela(stdscr, limpar=True):

    if limpar is True:
        stdscr.clear()

    stdscr.border()
    boas_vindas(stdscr)
    stdscr.refresh()

def tabuleiro(stdscr, posicoes, x_center):
    stdscr.clear()
    reiniciar_tela(stdscr, limpar=False)

    stdscr.addstr(10, x_center - 3, '------')
    stdscr.addstr(12, x_center - 3, '------')

    i = 9

    for posicao in posicoes:
        linha = '%s|%s|%s' % tuple(posicao)
        stdscr.addstr(i, x_center - 3, linha)
        i += 2
