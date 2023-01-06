from controller import *
import os

def main():

    # w (comprimento_Grelha) — Comprimento da grelha, em peças, onde w ∈ N
    comprimento_Grelha = 0

    # h (altura_Grelha) — Altura da grelha em peças, onde h ∈ N, [w/2] ≤ h ≤ w
    altura_Grelha = 0

    # n (tamanho_Sequencia) — Número de peças em linha para determinar a vitória, onde n ∈ N, n ≤ w
    tamanho_Sequencia = ''

    # S (tamanho_PecasEspeciais) — Conjunto de tamanhos de peças especiais disponível para cada jogador, onde ∀s ∈ S : S ∈ N, s < n
    tamanho_PecasEspeciais = []

    # Lista jogadores
    lista_Jogadores = ["Pedro", "João"]

    # Verificação de jogo em curso
    decorrer_Jogo = 0

    # Variável com valores temporários
    temp_var = ''


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
        X - Sair
        ''')
    op1 = input("Digite uma opção: ")   # Opção 1
    
    # Enquanto a "Opção 1" não igualar nenhuma das opções do array, o programa irá continuar a perguntar por uma opção.
    # Ele passa quando a "Opção 1" for equivalente a alguma das opções dentro do array
    while op1 not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]:
        os.system('cls')
        print("Instrução inválida.")
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
        op1 = input("Digite uma opção: ")   # Opção 1

    # Enquanto a "Opção 1" for diferente de X
    while op1 != "X":

        # RJ - Registar jogador
        if op1 == "RJ":
            os.system('cls')
            num_Jogadores = eval(input("Quantos jogadores pretende registar: "))
            for i in range(num_Jogadores):
                nome_Jogador = input("Digite o nome do " + str(i + 1) + "º jogador: ")
                os.system('cls')
                print(registar_Jogadores(nome_Jogador, lista_Jogadores))

            print('''
                RJ - Registar jogador
                EJ - Remover jogador
                LJ - Listar jogadores
                IJ - Iniciar  jogo
                DJ - Detalhes do jogo
                D - Desistir
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
            if len(lista_Jogadores) == 0:
                print("Não existem jogadores registados.")
            else:
                for i in range(len(lista_Jogadores)):
                    print(lista_Jogadores[i])
                nome_apagarJogador = input("Digite o nome do utilizador que pretende apagar")
                print(remover_Jogadores(lista_Jogadores, nome_apagarJogador, decorrer_Jogo))


        # LJ - Listar jogadores
        elif op1 == "LJ":
            os.system('cls')
            LJ(lista_Jogadores,z)
        # IJ - Iniciar jogo
        elif op1 == "IJ":
            os.system('cls')
            if len(lista_Jogadores) < 2:
                print("Jogadores insuficientes.")
            elif decorrer_Jogo == 1:
                print("Existe um jogo em curso.")
            else:
                nome_Jogador1 = input("Indique o nome do 1º jogador: ")
                while nome_Jogador1 not in lista_Jogadores:
                    print("Jogador não registado.")
                    nome_Jogador1 = input("Indique o nome do 1º jogador: ")

                nome_Jogador2 = input("Indique o nome do 2º jogador: ")
                while nome_Jogador2 not in lista_Jogadores:
                    print("Jogador não registado.")
                    nome_Jogador2 = input("Indique o nome do 1º jogador: ")

                comprimento_Grelha = eval(input("Indique o comprimento da grelha: "))
                altura_Grelha = eval(input("Indique a altura da grelha: "))

                while altura_Grelha < comprimento_Grelha/2 and altura_Grelha > comprimento_Grelha:
                    os.system('cls')
                    print("Dimensões de grelha invalidas.")
                    comprimento_Grelha = input("Indique o comprimento da grelha: ")
                    altura_Grelha = input("Indique a altura da grelha: ")

                # Exibir o tabuleiro
                for i in range(comprimento_Grelha):
                    temp_var = temp_var + str(str(i + 1) + ' ')

                jogada = 'X'
                jogador_Atual = nome_Jogador1

                while True:

                    print(temp_var)

                    # Tabuleiro
                    tabuleiro = [[' ' for _ in range(comprimento_Grelha)] for _ in range(altura_Grelha)]

                    for row in tabuleiro:
                        print('|'.join(row))

                    coluna = int(input(f"{jogador_Atual}, escolhe uma coluna: "))
                    movimento_Jogada(jogada, coluna, tabuleiro, altura_Grelha)
                    if verificar_Vitoria(jogada, tabuleiro, coluna, comprimento_Grelha):

                        print(temp_var)
                        for row in tabuleiro:
                            print('|'.join(row))

                        print(f"{jogador_Atual} Venceu!")
                        break

                    jogada = 'O' if jogada == 'X' else 'X'
                    jogador_Atual = nome_Jogador2 if jogador_Atual == nome_Jogador1 else nome_Jogador1
            


        # DJ - Detalhes do jogo
        elif op1 == "DJ":
            os.system('cls')
            detalhes_jogo(nome_Jogador1,nome_Jogador2,comprimento_Grelha,altura_Grelha,tamanho_Sequencia)
        # D - Desistir             Adicionar no Ij
        elif op1 == "D": 
            os.system('cls')
            print(f'''Apos desistencia do {nome_Jogador1}
                        O {nome_Jogador2} vence                             #Apenas exemplo do que será feito, o objetivo será o programa verificar de quem era a vez de jogar e atribuir a vitoria ao outro
                        ''')
        # CP - Colocar peça             Adicionar no Ij
        elif op1 == "CP":
            os.system('cls')
        
        # V - Visualizar resultado      Adicionar no Ij
        elif op1 == "V":
            os.system('cls')

        # G - Gravar
        elif op1 == "G":
            os.system('cls')

        # L - Ler                        Ler ficheiro
        elif op1 == "L":
            os.system('cls')

        # X - Sair
        else:
            #print("Obrigado por jogar")
            pass


main()
