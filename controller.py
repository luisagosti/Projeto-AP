def registar_jogadores(op1, lista_jogadores, dicionario_Jogos, decorrer_jogo):
    if op1.split(" ")[1] not in lista_jogadores:
        lista_jogadores.append(op1.split(" ")[1])

        # Organiza a 'lista_jogadores' alfabéticamente sempre que é adicionado um jogador novo
        lista_jogadores.sort()

        # Adiciona a 'dicionario_Jogos' as situações necessárias
        dicionario_Jogos.update({op1.split(" ")[1]: {'Jogos': 0, 'Vitorias': 0, 'em_Jogo': decorrer_jogo}})

        # Variavel 'chaves_organizadas' é as chaves de 'dicionario_Jogos' ordenadas alfabéticamente
        chaves_organizadas = sorted(dicionario_Jogos.keys())
        dicionario_organizado = {k: dicionario_Jogos[k] for k in chaves_organizadas}

        # Limpa o dicionário antigo e coloca o novo dicionário com as chaves ordenadas 
        dicionario_Jogos.clear()
        dicionario_Jogos.update(dicionario_organizado)

        return True

    else:
        return False

def remover_jogadores(lista_jogadores, op1, dicionario_Jogos):
    
    if op1.split(" ")[1] in lista_jogadores:
        lista_jogadores.remove(op1.split(" ")[1])

        dicionario_Jogos.pop(op1.split(" ")[1])

        chaves_organizadas = sorted(dicionario_Jogos.keys())
        dicionario_organizado = {k: dicionario_Jogos[k] for k in chaves_organizadas}

        dicionario_Jogos.clear()
        dicionario_Jogos.update(dicionario_organizado)
    
        return 1

    elif dicionario_Jogos[op1.split(" ")[1]]["em_Jogo"] == 1 and op1.split(" ")[1] in lista_jogadores:
        return 2
        
    else:
        return 3

def listar_jogadores(lista,z):
    for i in range(0,z):
        return lista

def gravar_jogo(lista_jogadores, decorrer_jogo, board, temp_var):
    with open('resultados.txt', 'w') as f:

        f.write("Lista Jogadores: \n")
        for i in len(lista_jogadores):
            f.write(str(i + 1) + "º Jogador - " + lista_jogadores[i])
            f.write('\n')

        if decorrer_jogo == 1:
            f.write("Jogo a decorrer atualmente: \n")
            f.write(temp_var)
            f.write('\n')
            for row in board:
                f.write('|'.join(row))
                f.write('\n')
        else:
            f.write("Não se encontra nenhum jogo a decorrer.")
            f.write('\n')

        return True

def desistir_Jogo():
    return

################ JOGO ###################

def make_move_right(jogador, coluna, dicionario_pecas_especiais, altura, largura, tabela, usar_peca_especial, index_pecas_especiais):
    coluna -= 1
    if usar_peca_especial:
        # Adicionar peca especial
        special_piece_size = dicionario_pecas_especiais[jogador][index_pecas_especiais]
        for i in range(coluna, coluna+special_piece_size):
            for j in range(altura-1, -1, -1):
                if i < largura and tabela[j][i] == ' ':
                    tabela[j][i] = jogador
                    break
        else:
            return True
    else:
        for i in range(altura-1, -1, -1):
            if tabela[i][coluna] == ' ':
                tabela[i][coluna] = jogador
                return
        return True



def make_move_left(jogador, dicionario_pecas_especiais, altura, tabela, coluna, usar_peca_especial, index_pecas_especiais):
    coluna -= 1
    if usar_peca_especial:
        # Adicionar peca especial
        special_piece_size = dicionario_pecas_especiais[jogador][index_pecas_especiais]
        for i in range(coluna, coluna-special_piece_size, -1):
            for j in range(altura-1, -1, -1):
                if i >= 0 and tabela[j][i] == ' ':
                    tabela[j][i] = jogador
                    break
        else:
            return True
    else:
        for i in range(altura-1, -1, -1):
            if tabela[i][coluna] == ' ':
                tabela[i][coluna] = jogador
                return
        return True

def has_won(jogador, altura, largura, tabela, peca_sequenciais):
    # Verifica vitoria usando pecas especiais
    for row in range(altura):
        for col in range(largura):
            # Verifica se a posicao atual e uma peca especial
            if tabela[row][col] == jogador:
                # Verifica se a peca especial e longa o sufeciente para vencer
                special_piece_size = 0
                while col+special_piece_size < largura and tabela[row][col+special_piece_size] == jogador:
                    special_piece_size += 1
                if special_piece_size >= peca_sequenciais:
                    return True
                
                # Verifica se a peca especial e alta o sufeciente para vencer
                special_piece_size = 0
                while row+special_piece_size < altura and tabela[row+special_piece_size][col] == jogador:
                    special_piece_size += 1
                if special_piece_size >= peca_sequenciais:
                    return True
    
    # Verifica vitoria na horizontal
    for row in tabela:
        for i in range(largura - peca_sequenciais + 1):
            if all(row[i+j] == jogador for j in range(peca_sequenciais)):
                return True
    
    # Verifica vitoria na vertical
    for col in range(largura):
        if all(tabela[row][col] == jogador for row in range(altura)):
            return True
    
    # Verifica vitoria na diagonal(cimo-esquerda para baixo-direita)
    for row in range(altura - peca_sequenciais + 1):
        for col in range(largura - peca_sequenciais + 1):
            if all(tabela[row+i][col+i] == jogador for i in range(peca_sequenciais)):
                return True
    
    # Verifica vitoria na diagonal(baixo direita para cimo-esquerda)
    for row in range(altura - peca_sequenciais + 1):
        for col in range(largura - 1, peca_sequenciais - 2, -1):
            if all(tabela[row+i][col-i] == jogador for i in range(peca_sequenciais)):
                return True
    
    # Verifica vitoria em todas as outras direcoes
    for row in range(altura - peca_sequenciais + 1):
        for col in range(largura):
            # Verifica vitoria cima-baixo
            if all(tabela[row+i][col] == jogador for i in range(peca_sequenciais)):
                return True
            # Verifica vitoria esquerda-direita
            if all(tabela[row][col+i] == jogador for i in range(peca_sequenciais)):
                return True
    
    return False


