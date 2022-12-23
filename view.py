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
    lista = []
    z = len(lista)
    menu = input()
    if menu == 'Rj':
        print("Insira o nome do jogardor")
        x = input()
        adicionar(lista,x)
    elif menu == 'EJ':
        if len(lista) == 0:
            print("Opcao invalida")  
        else:
            print('Insira o nome do jogador que deseja eliminar')
            y = input()
            remover(lista,y)
    elif menu == 'LJ':
        jogador_1 = [lista[z-1]]
        jogador_2 = [lista[z]]
        print(f'''~
            jogador 1 é {x}
            jogador 2 é {y}
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


                  
        
   
    
main()