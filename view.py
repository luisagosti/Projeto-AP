from controller import *
import os


def main():
    os.system('cls')
    lista = []      #não seria melhor uma lista de dicionários? ir adicionando um dicionário a cada jogador
    while True:
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
            S - Sair
        ''')
        z = len(lista)
        menu = input().upper()
        if menu == 'RJ':
            jogador = input("Insira o nome do jogador: ")
            r_adicionar_jogador = adicionar_jogador(lista, jogador)
            if r_adicionar_jogador == True:
                print('Jogador registado com sucesso.')
            else:
                print('Jogador existente.')

        elif menu == 'EJ':
            jogador = input('Insira o nome do jogador que deseja eliminar: ')
            r_eliminar_jogador = eliminar_jogador(lista, jogador)
            if r_eliminar_jogador == True:
                print('Jogador removido com sucesso.')
            else:
                print('Jogador não existente.')

        elif menu == 'LJ':
            jogador_1 = [lista[z-1]]
            jogador_2 = [lista[z]]
            print(f'''
                jogador 1 é {jogador_1}
                jogador 2 é {jogador_2}
            ''')

        elif menu == 'IJ':
            # n = int(input("Numero de pecas em linha necessarias para a vitoria"))
            # x = round(n*1.5)
            # y = round(n*1.25)
            # a = {}
            # p = 
            pass

        elif menu == 'DJ':
            pass
        elif menu == 'D':
            pass
        elif menu == 'CP': 
            pass
        elif menu == 'V':
            pass
        elif menu == 'G':
            pass
        elif menu == 'L':
            pass
        
        elif menu == 'S':
            break
        
        else:
            print('Instrução inválida.')

                  
        
   
    
main()