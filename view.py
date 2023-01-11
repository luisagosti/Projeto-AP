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
    

    # Verificação de jogo em curso
    decorrer_jogo = 0

    # Variável com valores temporários
    temp_var = ''

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
            listar_jogadores(lista_jogadores,len(lista_jogadores))

        # IJ - Iniciar jogo
        elif op1[0] == "IJ":
            # os.system('cls')
            if len(lista_jogadores) < 2:
                print("Jogadores insuficientes.")
            elif decorrer_jogo == 1:
                print("Existe um jogo em curso.")
            else:
                nome_jogador1 = op1[1]
                nome_jogador2 = op1[2]
                
                # Get board width and height from user
                width = int(input("Indica o comprimento do tabuleiro: "))
                height = int(input("Indica a altura do tabuleiro: "))

                # Get the number of sequenced pieces needed to win
                sequenced_pieces = int(input("Indica o numero de peças em sequência necessárias para ganhar: "))

                # Create a list to store the special pieces
                special_pieces = []

                # Create a dictionary to save the number of special pieces within the player name
                player_SpecialPiecesDictionary = {}

                # Get the number and size of special pieces from the user
                num_special_pieces = int(input("Indica o numero de peças especiais: "))
                for i in range(num_special_pieces):
                    special_piece_size = int(input("Indica o tamanho da {} peça especial: ".format(i+1)))
                    special_pieces.append(special_piece_size)

                # Generate board with the specified width and height
                board = [[' ' for _ in range(width)] for _ in range(height)]

                # Initialize separate lists for each player's special pieces
                player_X_special_pieces = special_pieces.copy()
                player_O_special_pieces = special_pieces.copy()

                # Update player_SpecialPiecesDictionary with the separate lists
                player_SpecialPiecesDictionary.update({"X": player_X_special_pieces, "O": player_O_special_pieces})


                player = 'X'
                jogador_atual = nome_jogador1

                while True:
                    print("player_SpecialPiecesDictionary: " + str(player_SpecialPiecesDictionary))
                    
                    # Print the board
                    print(' '.join([str(i+1) for i in range(width)]))
                    for row in board:
                        print('|'.join(row))

                    column = int(input(f"{jogador_atual} ({player}), escolhe uma coluna ou '0' para jogar uma peça especial: "))
                    use_special_piece = False
                    special_piece_index = None

                    if column == 0:
                        if len(player_SpecialPiecesDictionary[player]) > 0:
                            print("Escolhe qual peça especial queres usar:")
                            for i, special_piece in enumerate(player_SpecialPiecesDictionary[player]):
                                print("{}: {} sequencias".format(i+1, special_piece))
                            special_piece_index = int(input("Peça especial: ")) - 1
                            use_special_piece = True
                            orientation = input("Em que sentido queres jogar a peça especial (E ou D): ")
                            column = int(input("Em que coluna queres jogar a peça especial: "))
                                
                        else:
                            print("Não existem peças especiais.")
                            continue
                    elif column < 0 or column > width:
                        print("Coluna inválida, escolhe outra coluna.")
                        continue

                    if use_special_piece == True:
                        if orientation == "E":
                            make_move_left(player, player_SpecialPiecesDictionary, height, board, column, use_special_piece=use_special_piece, special_piece_index=special_piece_index)
                            
                        elif orientation == "D":
                            make_move_right(player, column, player_SpecialPiecesDictionary, height, width, board, use_special_piece=use_special_piece, special_piece_index=special_piece_index)
                        
                        else:
                            print("Orientação inválida, escolhe outra coluna.")
                            continue
                    else:
                        make_move_right(player, column, player_SpecialPiecesDictionary, height, width, board, use_special_piece=use_special_piece, special_piece_index=special_piece_index)

                    if use_special_piece:
                        special_piece = player_SpecialPiecesDictionary[player][special_piece_index]
                        player_SpecialPiecesDictionary[player].remove(special_piece)
                    if has_won(player, height, width, board, sequenced_pieces):

                        # Print the board
                        print(' '.join([str(i+1) for i in range(width)]))
                        for row in board:
                            print('|'.join(row))

                        print(f"{jogador_atual} ({player}) Venceu!")
                        break
                    player = 'O' if player == 'X' else 'X'
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
            gravar_jogo(lista_jogadores, decorrer_jogo, board, temp_var)
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