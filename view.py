from controller import *
import os


def main():

    # Lista jogadores
    lista_jogadores = []

    # Verificação de jogo em curso
    decorrer_jogo = 0

    # Variável com valores temporários
    temp_var = ""

    # Dicionário jogos jogados e vitórias
    dicionario_Jogos = {}

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
    X - Sair ''')
    op1 = input("Digite uma opção: ")  # Opção 1

    # Enquanto a "Opção 1" não igualar nenhuma das opções do array, o programa irá continuar a perguntar por uma opção.
    # Ele passa quando a "Opção 1" for equivalente a alguma das opções dentro do array
    while (op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
        or len(op1.split(" ")) > 3
        or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
        or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
        or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
        or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2):
        # os.system("cls")

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
        X - Sair ''')
        op1 = input("Digite uma opção: ")  # Opção 1

    # Enquanto a "Opção 1" for diferente de X
    while op1.split(" ")[0].upper() != "X":

        # RJ - Registar jogador
        if op1.split(" ")[0].upper() == "RJ":
            # os.system("cls")

            verificar_Registo = registar_jogadores(op1, lista_jogadores, dicionario_Jogos, decorrer_jogo)

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
            X - Sair ''')
            op1 = input("Digite uma opção: ")  # Opção 1

            while (
                op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                or len(op1.split(" ")) > 3
                or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
            ):
                # os.system("cls")

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
                X - Sair ''')
                op1 = input("Digite uma opção: ")  # Opção 1

        # EJ - Remover jogador
        elif op1.split(" ")[0].upper() == "EJ":
            if len(lista_jogadores) == 0:
                # os.system("cls")

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
                X - Sair ''')
                op1 = input("Digite uma opção: ")  # Opção 1

                while (
                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                    or len(op1.split(" ")) > 3
                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                ):
                    # os.system("cls")

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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")  # Opção 1

            else:
                # os.system("cls")

                if op1.split(" ")[1] not in lista_jogadores:
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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")  # Opção 1

                    while (
                        op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                        or len(op1.split(" ")) > 3
                        or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                        or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                        or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                        or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                    ):
                        # os.system("cls")

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
                        X - Sair ''')
                        op1 = input("Digite uma opção: ")  # Opção 1

                else:
                    remover_Jogador = remover_jogadores(lista_jogadores, op1, dicionario_Jogos)

                    if remover_Jogador == 1:
                        print("Jogador removido com sucesso.")
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
                        X - Sair ''')
                        op1 = input("Digite uma opção: ")

                        while (
                            op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                            or len(op1.split(" ")) > 3
                            or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                            or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                            or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                            or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                        ):
                            # os.system("cls")

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
                            X - Sair ''')
                            op1 = input("Digite uma opção: ")  # Opção 1

                    elif remover_Jogador == 2:
                        print("Jogador participa no jogo em curso.")
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
                        X - Sair ''')
                        op1 = input("Digite uma opção: ")

                        while (
                            op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                            or len(op1.split(" ")) > 3
                            or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                            or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                            or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                            or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                        ):
                            # os.system("cls")

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
                            X - Sair ''')
                            op1 = input("Digite uma opção: ")  # Opção 1

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
                        X - Sair ''')
                        op1 = input("Digite uma opção: ")

                        while (
                            op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                            or len(op1.split(" ")) > 3
                            or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                            or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                            or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                            or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                        ):
                            # os.system("cls")

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
                            X - Sair ''')
                            op1 = input("Digite uma opção: ")  # Opção 1
                        

        # LJ - Listar jogadores
        elif op1.split(" ")[0].upper() == "LJ":
            # os.system("cls")

            print(dicionario_Jogos)
            print(lista_jogadores)

            for jogador, jogos in dicionario_Jogos.items():
                print(str(jogador) + " - " + str(jogos["Jogos"]) + " jogos,", str(jogos["Vitorias"]) + " vitórias.")

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
            X - Sair ''')
            op1 = input("Digite uma opção: ")

            while (
                op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                or len(op1.split(" ")) > 3
                or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
            ):
                # os.system("cls")

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
                X - Sair ''')
                op1 = input("Digite uma opção: ")  # Opção 1

        # IJ - Iniciar jogo
        elif op1.split(" ")[0].upper() == "IJ":
            # os.system("cls")

            if op1.split(" ")[1] not in lista_jogadores or op1.split(" ")[2] not in lista_jogadores:
                print("Jogador não registado.")
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
                X - Sair ''')
                op1 = input("Digite uma opção: ")

                while (
                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                    or len(op1.split(" ")) > 3
                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                ):
                    # os.system("cls")

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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")  # Opção 1

            elif len(lista_jogadores) < 2:
                print("Jogadores insuficientes.")
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
                X - Sair ''')
                op1 = input("Digite uma opção: ")

                while (
                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                    or len(op1.split(" ")) > 3
                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                ):
                    # os.system("cls")

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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")  # Opção 1

            elif decorrer_jogo == 1:
                print("Existe um jogo em curso.")
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
                X - Sair ''')
                op1 = input("Digite uma opção: ")

                while (
                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                    or len(op1.split(" ")) > 3
                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                ):
                    # os.system("cls")

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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")  # Opção 1

            else:
                nome_jogador1 = op1.split(" ")[1]
                nome_jogador2 = op1.split(" ")[2]

                # Get board width and height from user
                while True:
                    try:
                        width = int(input("Indica o comprimento do tabuleiro: "))
                        if width <= 0:
                            raise ValueError
                        try:
                            height = int(input("Indica a altura do tabuleiro: "))
                            if height <= 0:
                                raise ValueError
                            if width/2 > height or height > width:
                                raise ValueError
                            break
                        except ValueError:
                            print("Dimensões de grelha invalidas.")
                    except ValueError:
                        print("Dimensões de grelha invalidas.")

                # Get the number of sequenced pieces needed to win
                while True:
                    try:
                        sequenced_pieces = int(input("Indica o número de peças em sequência necessárias para ganhar: "))
                        if sequenced_pieces <= 0:
                            print("Tamanho de sequência invalido.")
                        elif sequenced_pieces > width:
                            print("Tamanho de sequência invalido.")
                        else:
                            break
                    except ValueError:
                        print("Input inválido.")


                # Create a list to store the special pieces
                special_pieces = []

                # Create a dictionary to save the number of special pieces within the player name
                player_SpecialPiecesDictionary = {}

                # Get the number and size of special pieces from the user
                while True:
                    num_special_pieces = input("Indica o numero de peças especiais: ")
                    if num_special_pieces.isnumeric():
                        num_special_pieces = int(num_special_pieces)
                        break
                    elif num_special_pieces == "":
                        print("Input inválido.")
                    else:
                        print("Input inválido.")

                    

                for i in range(num_special_pieces):
                    try:
                        special_piece_size = int(input("Indica o tamanho da {} peça especial: ".format(i + 1)))
                        while special_piece_size > sequenced_pieces or special_piece_size <= 0 or special_piece_size == '':
                            print("Dimensões de peças especiais invalidas.")
                            special_piece_size = int(input("Indica o tamanho da {} peça especial: ".format(i + 1)))

                        special_pieces.append(special_piece_size)
                    except ValueError:
                        print("Dimensões de peças especiais invalidas.")



                # Generate board with the specified width and height
                board = [[" " for _ in range(width)] for _ in range(height)]

                # Initialize separate lists for each player's special pieces
                player_X_special_pieces = special_pieces.copy()
                player_O_special_pieces = special_pieces.copy()

                # Update player_SpecialPiecesDictionary with the separate lists
                player_SpecialPiecesDictionary.update(
                    {"X": player_X_special_pieces, "O": player_O_special_pieces}
                )

                player = "X"
                jogador_atual = nome_jogador1

                decorrer_jogo = 1

                print(f"Jogo iniciado entre {nome_jogador1} e {nome_jogador2}.")
                print(dicionario_Jogos)

                dicionario_Jogos[nome_jogador1]['em_Jogo'] = decorrer_jogo
                dicionario_Jogos[nome_jogador2]['em_Jogo'] = decorrer_jogo

                while True:

                    # Print the board
                    print(" ".join([str(i + 1) for i in range(width)]))
                    for row in board:
                        print("|".join(row))

                    column = int(
                        input(
                            f"{jogador_atual} ({player}), escolhe uma coluna ou '0' para jogar uma peça especial: "
                        )
                    )
                    use_special_piece = False
                    special_piece_index = None

                    if column == 0:
                        if len(player_SpecialPiecesDictionary[player]) > 0:
                            print("Escolhe qual peça especial queres usar:")
                            for i, special_piece in enumerate(
                                player_SpecialPiecesDictionary[player]
                            ):
                                print("{}: {} sequencias".format(i + 1, special_piece))
                            special_piece_index = int(input("Peça especial: ")) - 1
                            use_special_piece = True
                            while True:
                                orientation = input("Em que sentido queres jogar a peça especial (E ou D): ")
                                if orientation.upper() in ['E','D']:
                                    break
                                else:
                                    print("Input inválido. Por favor insira 'E' ou 'D'.")

                            while True:
                                column = input("Em que coluna queres jogar a peça especial: ")
                                if column.isnumeric():
                                    column = int(column)
                                    break
                                elif column == "":
                                    print("Input não pode ser vazio.")
                                else:
                                    print("Input inválido. Por favor insira um número.")


                        else:
                            print("Não existem peças especiais.")
                            continue
                    elif column < 0 or column > width:
                        print("Coluna inválida, escolhe outra coluna.")
                        continue

                    if use_special_piece == True:
                        if orientation == "E":
                            make_move_left(
                                player,
                                player_SpecialPiecesDictionary,
                                height,
                                board,
                                column,
                                use_special_piece=use_special_piece,
                                special_piece_index=special_piece_index,
                            )
                            if make_move_left == True:
                                print(
                                    "A coluna encontra-se completa, escolhe outra coluna."
                                )
                            else:
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
                                X - Sair ''')
                                op1 = input("Digite uma opção: ")

                                while (
                                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                                    or len(op1.split(" ")) > 3
                                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                                ):
                                    # os.system("cls")

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
                                    X - Sair ''')
                                    op1 = input("Digite uma opção: ")  # Opção 1
                                break

                        elif orientation == "D":
                            make_move_right(
                                player,
                                column,
                                player_SpecialPiecesDictionary,
                                height,
                                width,
                                board,
                                use_special_piece=use_special_piece,
                                special_piece_index=special_piece_index,
                            )
                            if make_move_right == True:
                                print(
                                    "A coluna encontra-se completa, escolhe outra coluna."
                                )
                            
                            else:
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
                                X - Sair ''')
                                op1 = input("Digite uma opção: ")

                                while (
                                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                                    or len(op1.split(" ")) > 3
                                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                                ):
                                    # os.system("cls")

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
                                    X - Sair ''')
                                    op1 = input("Digite uma opção: ")  # Opção 1
                                break

                        else:
                            print("Orientação inválida, escolhe outra coluna.")
                            continue
                    else:
                        make_move_right(
                            player,
                            column,
                            player_SpecialPiecesDictionary,
                            height,
                            width,
                            board,
                            use_special_piece=use_special_piece,
                            special_piece_index=special_piece_index,
                        )

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
                        X - Sair ''')
                        op1 = input("Digite uma opção: ")

                        while (
                            op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                            or len(op1.split(" ")) > 3
                            or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                            or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                            or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                            or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                        ):
                            # os.system("cls")

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
                            X - Sair ''')
                            op1 = input("Digite uma opção: ")  # Opção 1
                        break

                    if use_special_piece:
                        special_piece = player_SpecialPiecesDictionary[player][
                            special_piece_index
                        ]
                        player_SpecialPiecesDictionary[player].remove(special_piece)
                    if has_won(player, height, width, board, sequenced_pieces):

                        # Print the board
                        print(" ".join([str(i + 1) for i in range(width)]))
                        for row in board:
                            print("|".join(row))

                        print(f"{jogador_atual} ({player}) Venceu!")

                        decorrer_jogo = 0

                        dicionario_Jogos[nome_jogador1]['em_Jogo'] = decorrer_jogo
                        dicionario_Jogos[nome_jogador2]['em_Jogo'] = decorrer_jogo

                        dicionario_Jogos[nome_jogador1]['Jogos'] += 1
                        dicionario_Jogos[nome_jogador2]['Jogos'] += 1

                        if jogador_atual == nome_jogador1:
                            dicionario_Jogos[nome_jogador1]['Vitorias'] += 1
                        
                        else:
                            dicionario_Jogos[nome_jogador2]['Vitorias'] += 1

                        print(dicionario_Jogos)
                        break

                    player = "O" if player == "X" else "X"
                    jogador_atual = (
                        nome_jogador2
                        if jogador_atual == nome_jogador1
                        else nome_jogador1
                    )

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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")

                    while (
                        op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                        or len(op1.split(" ")) > 3
                        or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                        or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                        or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                        or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                    ):
                        # os.system("cls")

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
                        X - Sair ''')
                        op1 = input("Digite uma opção: ")  # Opção 1

        # DJ - Detalhes do jogo
        elif op1.split(" ")[0].upper() == "DJ":
            # os.system("cls")

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
                X - Sair ''')
                op1 = input("Digite uma opção: ")

                while (
                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                    or len(op1.split(" ")) > 3
                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                ):
                    # os.system("cls")

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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")  # Opção 1

            else:
                temp_var1 = ''
                for i in range(len(player_X_special_pieces)):
                    temp_var1 += str(i + 1) + "º peça - Tamanho " + str(player_X_special_pieces[i]) + "\n"
                
                temp_var2 = ''
                for i in range(len(player_O_special_pieces)):
                    temp_var2 += str(i + 1) + "º peça - Tamanho " + str(player_X_special_pieces[i]) + "\n"

                temp_var3 = [nome_jogador1, nome_jogador2]
                temp_var3.sort()

                print(f"Comprimento grelha - {width}\n"  
                        f"Altura grelha - {height}\n\n"  
                        f"1º Jogador - {temp_var3[0]}\n"
                        f"Quantidade de peças especiais disponiveis de {temp_var3[0]} - {len(player_X_special_pieces)}\n"
                        f"{temp_var1}\n"
                        f"2º Jogador - {temp_var3[1]}\n"
                        f"Quantidade de peças especiais disponiveis de {temp_var3[1]} - {len(player_O_special_pieces)}\n"
                        f"{temp_var2}" 
                )

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
                X - Sair ''')
                op1 = input("Digite uma opção: ")

                while (
                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                    or len(op1.split(" ")) > 3
                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                ):
                    # os.system("cls")

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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")  # Opção 1

        # D - Desistir
        elif op1.split(" ")[0].upper() == "D":
            # os.system("cls")

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
                X - Sair ''')
                op1 = input("Digite uma opção: ")

                while (
                    op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
                    or len(op1.split(" ")) > 3
                    or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
                    or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP", "V", "G", "L", "X"] and len(op1.split(" ")) > 1
                    or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
                    or op1.split(" ")[0].upper() in ["D"] and len(op1.split(" ")) > 3 and len(op1.split(" ")) < 2
                ):
                    # os.system("cls")

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
                    X - Sair ''')
                    op1 = input("Digite uma opção: ")  # Opção 1

            else:
                desistencia = int(
                    input(
                        f"""
                                Quem pretende desistir:
                                1 - {nome_jogador1}
                                2 - {nome_jogador2}
                                3 - Ambos

                                Opção: 
                            """
                    )
                )
                desistir_Jogo()

        # CP - Colocar peça
        elif op1.split(" ")[0].upper() == "CP":
            os.system("cls")

        # V - Visualizar resultado
        elif op1.split(" ")[0].upper() == "V":
            os.system("cls")

        # G - Gravar
        elif op1.split(" ")[0].upper() == "G":
            gravar_jogo(lista_jogadores, decorrer_jogo, board, temp_var)
            if gravar_jogo == True:
                # os.system("cls")
                print("Jogo gravado.")

            else:
                # os.system("cls")
                print("Ocorreu um erro na gravação.")

        # L - Ler
        elif op1.split(" ")[0].upper() == "L":
            os.system("cls")

        # X - Sair
        else:
            print("Obrigado por jogar")
            pass


main()
