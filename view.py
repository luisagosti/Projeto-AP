from controller import *
import os

def main():

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
        op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1

    # Enquanto a "Opção 1" for diferente de X
    while op1[0] != "X":

        # RJ - Registar jogador
        if op1[0] == "RJ":
            os.system('cls')

            verificar_Registo = registar_jogadores(op1[1], lista_jogadores)
            print(lista_jogadores)
            if verificar_Registo == True:
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

            while op1[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]:
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
                op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1
            
        # EJ - Remover jogador
        elif op1[0] == "EJ":
            if len(lista_jogadores) == 0:
                os.system('cls')

                print("Não existem jogadores registados.")
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

                while op1[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]:
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
                    op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1

            else:
                os.system('cls')

                if op1[1] not in lista_jogadores:
                    print("Jogador inexistente.")

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

                    while op1[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]:
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
                        op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1
                    
                else:
                    remover_Jogador = remover_jogadores(lista_jogadores, op1, decorrer_jogo)

                    if remover_Jogador == True:
                        print("Jogador removido com sucesso")

                    elif remover_Jogador == False: 
                        print("Jogador participa no jogo em curso..")    

                        os.system('cls') 

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

                        while op1[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]:
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
                            op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1
                    
                    else:
                        continue

        # LJ - Listar jogadores
        elif op1[0] == "LJ":
            os.system('cls')

            for i in len(lista_jogadores):
                print(str(i + 1) + " - " + lista_jogadores[i])
            
            print('''\n
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
                op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1          


        # IJ - Iniciar jogo
        elif op1[0] == "IJ":
            os.system('cls')

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

            if decorrer_jogo == 0:
                print("Comece um jogo para obter detalhes.")
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
                    op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1

            else:
                print(f'''
                        Tamanho grelha - {width}
                        1º Jogador - {nome_jogador1}
                        2º Jogador - {nome_jogador2} 

                        Quantidade de peças especiais disponiveis de {nome_jogador1} - {len(player_X_special_pieces)}
                        Quantidade de peças especiais disponiveis de {nome_jogador2} - {len(player_O_special_pieces)}
                        ''')
                
                print('''\n
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
                    op1 = input("Digite uma opcão: ").split(' ', 2)   # Opção 1 
            

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