from controller import *
import os


def main():
    os.system('cls')
    print('''
        RJ - Registar jogador
        EJ - Remover jogador
        LJ - Listar jogadores
        IJ - Iniciar jogo
        DJ - Detalhes do jogo
        D - Desistir
        CP - Colocar peça
        V - Visualizar resultado
        G - Gravar
        L - Ler
    ''')
    menu = input()
    # n = int(input("Numero de pecas em linha necessarias para a vitoria"))
    # x = round(n*1.5)
    # y = round(n*1.25)

main()