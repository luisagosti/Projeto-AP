from funcoes import *
import os

def main():
    lista_jogadores = []
    z = len(lista_jogadores)
    decorrer_jogo = 0
    print('''
                RJ + Nome - Registar jogador
                EJ + Nome - Remover jogador
                        LJ - Listar jogadores
            IJ + 2 Nomes - Iniciar jogo
                        DJ - Detalhes do jogo
            D + 1/2 Nomes - Desistir
                        CP - Colocar peça
                        V - Visualizar resultado
                        G - Gravar
                        L - Ler
                        X - Sair
            ''')
    op1 = input("Digite uma opção: ").split(' ', 2)   # Opção 1

        # Enquanto a "Opção 1" não igualar nenhuma das opções do array, o programa irá continuar a perguntar por uma opção.
        # Ele passa quando a "Opção 1" for equivalente a alguma das opções dentro do array
    while op1[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]:
        print("Instrução inválida.")
        print('''
                RJ + Nome - Registar jogador
                EJ + Nome - Remover jogador
                        LJ - Listar jogadores
            IJ + 2 Nomes - Iniciar jogo
                        DJ - Detalhes do jogo
            D + 1/2 Nomes - Desistir
                        CP - Colocar peça
                        V - Visualizar resultado
                        G - Gravar
                        L - Ler
                        X - Sair
            ''')
        op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1

        # Enquanto a "Opção 1" for diferente de X
    while op1[0] != "X":

            # RJ - Registar jogador
        if op1[0] == "RJ":
            r_registar = registar_jogadores(op1[1], lista_jogadores)
            print(lista_jogadores)
            if r_registar == True:
                print("Jogador adicionado com sucesso.")
    
            else: 
                print("Jogador existente")    

            print('''
                RJ + Nome - Registar jogador
                EJ + Nome - Remover jogador
                        LJ - Listar jogadores
            IJ + 2 Nomes - Iniciar jogo
                        DJ - Detalhes do jogo
            D + 1/2 Nomes - Desistir
                        CP - Colocar peça
                        V - Visualizar resultado
                        G - Gravar
                        L - Ler
                        X - Sair
            ''')
            op1 = input("Digite uma opção: ").split(' ', 2)   # Opção 1
            
            # EJ - Remover jogador
        elif op1[0] == "EJ":
            if len(lista_jogadores) == 0:
                print("Não existem jogadores registados.")
            else:
                for i in range(len(lista_jogadores)):
                    print(lista_jogadores[i])
                r_remover = remover_jogadores(lista_jogadores, op1, decorrer_jogo)
                if r_remover == True:
                    print("Jogador removido com sucesso")
                elif r_remover == False: 
                    print("Jogador participa no jogo em curso..")    
                else: 
                    print("Jogador não existente.")
                print('''
                RJ + Nome - Registar jogador
                EJ + Nome - Remover jogador
                        LJ - Listar jogadores
                IJ + 2 Nomes - Iniciar jogo
                        DJ - Detalhes do jogo
                D + 1/2 Nomes - Desistir
                        CP - Colocar peça
                        V - Visualizar resultado
                        G - Gravar
                        L - Ler
                        X - Sair
                ''')
                op1 = input("Digite uma opção: ").split(' ', 2)
main()