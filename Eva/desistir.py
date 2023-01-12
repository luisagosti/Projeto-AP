from funcoes import *
import os

def main():

    # Lista jogadores
    lista_jogadores = ["Pedro", "João"]
    
    # Verificação de jogo em curso
    decorrer_jogo = 0

    # Variável com valores temporários
    temp_var = ''

    # Dicionário jogos jogados e vitórias
    x = {}
    def desistir_jogo(op1, lista_jogadores, nome_jogador1, nome_jogador2):
        if op1[1] not in lista_jogadores:
            return 1                                                                            #Jogador um não registado
        if op1[2] not in lista_jogadores:
            return 2                                                                            #Jogador dois não registado
        elif op1[1] != nome_jogador1 or op1[1] != nome_jogador2 and op1[1] in lista_jogadores :
            return 3                                                                            #Jogador não participa do jogo em curso
        elif op1[2] != nome_jogador1 or op1[2] != nome_jogador2 and op1[2] in lista_jogadores :
            return 3                                                                            #Jogador não participa do jogo em curso
        elif op1[1] == nome_jogador1 and op1[2] == nome_jogador2:
            return 4                                                                            #fim de jogo, ninguem vence
        elif op1[1] == nome_jogador2 and op1[2] == nome_jogador1:
            return 4                                                                            #fim de jogo, ninguem vence
        elif op1[1] == nome_jogador1:
            return 5                                                                            #fim de jogo, jogador 2 vence
        elif op1[1] == nome_jogador2:
            return 6                                                                            #fim de jogo, jogador 1 vence         
    
    if op1[0] == "D": 
    
        if decorrer_jogo == 0:
                print("Comece um jogo para poder desistir.")
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

        else:
                desistencia = desistir_jogo(op1, lista_jogadores, nome_jogador1, nome_jogador2)
                if desistencia == 1:
                    print("Jogador 1 não registado.") 
                if desistencia == 2:
                    print("Jogador 2 não registado.")
                elif desistencia == 3:
                    print("Jogador não participa do jogo em curso.")
                elif desistencia == 4:
                    print("Fim de jogo, ninguém vence.")
                elif desistencia == 5:
                    print("Fim de jogo, jogador 2 vence.")
                elif desistencia == 6:
                    print("Fim de jogo, jogador 1 vence.")