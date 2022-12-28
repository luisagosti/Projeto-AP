
def colocar_peca(n,x,y):
    for n in range(1,x):
        for n in range(1,y):
            pass
# def colocar_peca(n,x,y,a,p):
#     for n in range(1,x):
#         for n in range(1,y):
#            if  
#              a.append()
def adicionar_jogador(lista, jogador):
    if jogador not in lista:
        lista.append(jogador)
        return True

def eliminar_jogador(lista, jogador):
    if jogador in lista:
        lista.remove(jogador)
        return True

