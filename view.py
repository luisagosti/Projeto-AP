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
            X - Sair
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
            #os.system('cls')
                        # def LJ(lista):
                        # jogador_1 = [lista[z-1]]
                        # jogador_2 = [lista[z]]                    DENTRO DO IJ
                        # x = (f'''                                                         
                        #     jogador 1 é {jogador_1}
                        #     jogador 2 é {jogador_2}
                        # ''')
                        # return x
            #LJ(lista)
            pass
        elif menu == 'IJ':
            print()
            pass

        elif menu == 'DJ':
            #os.system('cls')
                            # def detalhes_jogo(jogador_1,jogador_2,comprimento_Grelha,altura_Grelha,n):
                            #     x  =(f'''Para vencer é necessario o {jogador_1} ou o {jogador_2} 
                            #         numa tabela de {comprimento_Grelha}comprimento e {altura_Grelha}altura         DENTRO E FORA DO IJ MAS ESTE É O DE DENTRO          
                            #         colocar {n}peças em linha horizontal,vertical ou obliqua
                            #         ''')
                          #     return x
            #detalhes_jogo(jogador_1,jogador_2,comprimento_Grelha,altura_Grelha,n)     
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
        
        elif menu == 'X':
            break
        
        else:
            print('Instrução inválida.')

                  
        
   
    
main()