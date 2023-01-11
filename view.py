from controller import *
import os

def main():

    # w (comprimento_Grelha) — Comprimento da grelha, em peças, onde w ∈ N
    comprimento_grelha = 0

    # h (altura_Grelha) — Altura da grelha em peças, onde h ∈ N, [w/2] ≤ h ≤ w
    altura_grelha = 0

    # n (tamanho_Sequencia) — Número de peças em linha para determinar a vitória, onde n ∈ N, n ≤ w
    tamanho_sequencia = ''

    # S (tamanho_PecasEspeciais) — Conjunto de tamanhos de peças especiais disponível para cada jogador, onde ∀s ∈ S : S ∈ N, s < n
    tamanho_pecas_especiais = []

    # Lista jogadores
    lista_jogadores = ["Pedro", "João"]
    z = len(lista_jogadores)

    # Verificação de jogo em curso
    decorrer_jogo = 0

    # Variável com valores temporários
    temp_var = ''


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
                # LJ - Listar jogadores
        elif op1[0] == "LJ":
            os.system('cls')
            listar_jogadores(lista_jogadores,z)
        # IJ - Iniciar jogo
        elif op1[0] == "IJ":
            os.system('cls')
            if len(lista_jogadores) < 2:
                print("Jogadores insuficientes.")
            elif decorrer_jogo == 1:
                print("Existe um jogo em curso.")
            else:
                nome_jogador1 = input("Indique o nome do 1º jogador: ")
                while nome_jogador1 not in lista_jogadores:
                    print("Jogador não registado.")
                    nome_jogador1 = input("Indique o nome do 1º jogador: ")

                nome_jogador2 = input("Indique o nome do 2º jogador: ")
                while nome_jogador2 not in lista_jogadores:
                    print("Jogador não registado.")
                    nome_jogador2 = input("Indique o nome do 2º jogador: ")

                # Perguntar altura e comprimento do tabuleiro ao usuário
                comprimento_grelha = int(input("Insira o comprimento do tabuleiro: "))
                altura_grelha = int(input("Insira a altura do tabuleiro: "))

                # Perguntar número de peças para a sequência vencedora
                tamanho_sequencia = int(input("Insira o número de peças seguidas para vencer: ")) # FAZER VERIFICAÇÃO
                
                # Gerar tabuleiro com as especificações inseridas
                tabuleiro = [[' ' for _ in range(comprimento_grelha)] for _ in range(altura_grelha)]

                jogador = 'X'
                jogador_atual = nome_jogador1

                while True:
                    print_tabuleiro(comprimento_grelha, tabuleiro)
                    coluna = int(input(f"{jogador_atual} ({jogador}), escolhe uma coluna: "))
                    jogada(jogador, coluna, altura_grelha, tabuleiro)
                    if ganhar(jogador, tabuleiro, comprimento_grelha, altura_grelha, tamanho_sequencia):
                        print_tabuleiro(comprimento_grelha, tabuleiro)
                        print(f"{jogador} Venceu!")
                        break
                    jogador = 'O' if jogador == 'X' else 'X'
                    jogador_atual = nome_jogador2 if jogador_atual == nome_jogador1 else nome_jogador1          


        # DJ - Detalhes do jogo
        elif op1[0] == "DJ":
            os.system('cls')
            print(f'''Para vencer é necessario o {nome_jogador1} ou o {nome_jogador2}
        numa tabela de {comprimento_grelha}comprimento e {altura_grelha}altura         DENTRO E FORA DO IJ MAS ESTE É O DE DENTRO          
        colocar {tamanho_sequencia}peças em linha horizontal,vertical ou diagonal
        ''')

        # D - Desistir             
        elif op1[0] == "D": 
            os.system('cls')
            print(f'''Apos desistencia do {nome_jogador1}
                        O {nome_jogador2} vence
                        ''')
        # CP - Colocar peça            
        elif op1[0] == "CP":
            os.system('cls')
        
        # V - Visualizar resultado      
        elif op1[0] == "V":
            os.system('cls')

        # G - Gravar
        elif op1[0] == "G":
            gravar_jogo(lista_jogadores, decorrer_jogo, tabuleiro, temp_var)
            if gravar_jogo == True:
                os.system('cls')
                print("Jogo gravado.")
            
            else:
                os.system('cls')
                print("Ocorreu um erro na gravação.")
            

        # L - Ler                        
        elif op1[0] == "L":
            os.system('cls')

        # X - Sair
        else:
            print("Obrigado por jogar")
            pass
main()