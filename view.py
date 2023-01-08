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


    os.system('cls')
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
    op1 = input("Digite uma opção: ")   # Opção 1

    # Enquanto a "Opção 1" não igualar nenhuma das opções do array, o programa irá continuar a perguntar por uma opção.
    # Ele passa quando a "Opção 1" for equivalente a alguma das opções dentro do array
    while op1[:2].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"] and op1[2] != ' ':
        os.system('cls')
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
        op1 = input("Digite uma opcão: ")   # Opção 1

    # Enquanto a "Opção 1" for diferente de X
    while op1 != "X":

        # RJ - Registar jogador
        if op1 == "RJ":
            os.system('cls')
            num_jogadores = eval(input("Quantos jogadores pretende registar: "))
            for i in range(num_jogadores):
                nome_jogador = input("Digite o nome do " + str(i + 1) + "º jogador: ")
                os.system('cls')
                registar_jogadores(nome_jogador, lista_jogadores)
                if registar_jogadores == True:
                    print("Jogador adicionado com sucesso")
                else: 
                    print("Jogador existente.")    

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
            op1 = input("Digite uma opção: ")   # Opção 1
        
        # EJ - Remover jogador
        elif op1 == "EJ":
            os.system('cls')
            if len(lista_jogadores) == 0:
                print("Não existem jogadores registados.")
            else:
                for i in range(len(lista_jogadores)):
                    print(lista_jogadores[i])
                nome_apagar_jogador = input("Digite o nome do utilizador que pretende apagar")
                remover_jogadores(lista_jogadores, nome_apagar_jogador, decorrer_jogo)
                if registar_jogadores == True:
                    print("Jogador removido com sucesso")
                elif remover_jogadores == False: 
                    print("Jogador participa no jogo em curso..")    
                else: 
                    print("Jogador não existente.")

        # LJ - Listar jogadores
        elif op1 == "LJ":
            os.system('cls')
            listar_jogadores(lista_jogadores,z)
        # IJ - Iniciar jogo
        elif op1 == "IJ":
            os.system('cls')
            if len(lista_jogadores) < 2:
                print("Jogadores insuficientes.")
            elif decorrer_jogo == 1:
                print("Existe um jogo em curso.")
            else:
                nome_jogador1 = input("Indique o nome do 1º jogador: ")
                while nome_jogador1.upper() not in lista_jogadores:
                    print("Jogador não registado.")
                    nome_jogador1 = input("Indique o nome do 1º jogador: ")

                nome_jogador2 = input("Indique o nome do 2º jogador: ")
                while nome_jogador2.upper() not in lista_jogadores:
                    print("Jogador não registado.")
                    nome_jogador2 = input("Indique o nome do 2º jogador: ")

                comprimento_grelha = eval(input("Indique o comprimento da grelha: "))
                altura_grelha = eval(input("Indique a altura da grelha: "))

                while altura_grelha < comprimento_grelha/2 and altura_grelha > comprimento_grelha:
                    os.system('cls')
                    print("Dimensões de grelha inválidas.")
                    comprimento_grelha = input("Indique o comprimento da grelha: ")
                    altura_grelha = input("Indique a altura da grelha: ")

                # Exibir o tabuleiro
                for i in range(comprimento_grelha):
                    temp_var = temp_var + str(str(i + 1) + ' ')

                jogada = 'X'
                jogador_atual = nome_jogador1

                while True:

                    print(temp_var)

                    # Tabuleiro
                    tabuleiro = [[' ' for _ in range(comprimento_grelha)] for _ in range(altura_grelha)]

                    for row in tabuleiro:
                        print('|'.join(row))

                    coluna = int(input(f"{jogador_atual}, escolha uma coluna: "))
                    movimento_jogada(jogada, coluna, tabuleiro, altura_grelha)
                    if movimento_jogada == True:
                        print("A coluna encontra-se completa, escolha outra coluna.")
                    if verificar_vitoria(jogada, tabuleiro, coluna, comprimento_grelha):

                        print(temp_var)
                        for row in tabuleiro:
                            print('|'.join(row))

                        print(f"{jogador_atual} Venceu!")
                        break

                    jogada = 'O' if jogada == 'X' else 'X'
                    jogador_atual = nome_jogador2 if jogador_atual == nome_jogador1 else nome_jogador1
            


        # DJ - Detalhes do jogo
        elif op1 == "DJ":
            os.system('cls')
            print(f'''Para vencer é necessario o {nome_jogador1} ou o {nome_jogador2},
        numa tabela de {comprimento_grelha} comprimento e {altura_grelha} altura         DENTRO E FORA DO IJ MAS ESTE É O DE DENTRO          
        colocar {tamanho_sequencia} peças em linha horizontal,vertical ou diagonal.
        ''')

        # D - Desistir             
        elif op1 == "D": 
            os.system('cls')
            print(f'''Após desistencia do {nome_jogador1}
                        o {nome_jogador2} vence.
                        ''')
        # CP - Colocar peça            
        elif op1 == "CP":
            os.system('cls')
        
        # V - Visualizar resultado      
        elif op1 == "V":
            os.system('cls')

        # G - Gravar
        elif op1 == "G":
            gravar_jogo(lista_jogadores, decorrer_jogo, tabuleiro, temp_var)
            if gravar_jogo == True:
                os.system('cls')
                print("Jogo gravado.")
            
            else:
                os.system('cls')
                print("Ocorreu um erro na gravação.")
            

        # L - Ler                        
        elif op1 == "L":
            os.system('cls')

        # X - Sair
        else:
            #print("Obrigado por jogar")
            pass


main()
