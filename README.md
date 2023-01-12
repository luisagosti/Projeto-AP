### Situações em falta:

- [x] Split nos inputs
- [x] Peças especiais
- [ ] Prints no controller
- [x] Adicionar `tamanho_Sequencia` ás variáveis de jogo
- [x] Adicionar `tamanho_PecasEspeciais` ás variaveis de jogo
- [ ] Criar dicionário com nome jogadores, jogos jogados e vitórias
    - [ ] Ordenar alfabéticamente

- [x] Verificações de `Opção 1`

- [x] `RJ - Registar jogador`
    - [x] Verificações de inputs
    - [x] Nome unico

- [x] `EJ - Remover jogador`
    - [x] Verificações de inputs

- [ ] `LJ - Listar jogadores`
    - [x] Verificações de inputs
    - [ ] Indicar número de jogos jogados e vitórias

- [ ] `LJ - Listar jogadores`
    - [x] Jogo funcional
    - [ ] Verificações de inputs
        - [ ] `heigth` - Altura da grelha (`width/2` ≤ `heigth` ≤ `width`)
        - [ ] `sequenced_pieces` - Número de peças em linha para determinar a vitória (`sequenced_pieces` ≤ `width`)
        - [ ] `special_pieces` - Conjunto de tamanhos de peças especiais disponível para cada jogador (`special_pieces` < `sequenced_pieces`)
    - [ ] Verificar se já se encontra jogo em curso
    - [ ] Verificar se jogador indicado se encontra registado

- [ ] `DJ - Detalhes do jogo`
    - [x] Verificações de inputs
    - [ ] Informações do jogo em curso
        - [x] Tamanho da grelha
        - [x] Nomes jogadores
            - [ ] Alfabéticamente
        - [x] Quantidade de peças especiais disponíveis para cada jogador

- [ ] `D - Desistir`
    - [x] Verificações de inputs
    - [+-] Criar função desistir_Jogo
        - [ ] Editar dicionário jogos jogados e vitórias

- [ ] `CP - Colocar peça`
    - [ ] Verificações de inputs

- [ ] `V - Visualizar resultado`
    - [ ] Verificações de inputs

- [ ] `G - Gravar`
    - [ ] Verificações de inputs

- [ ] `L - Ler`
    - [ ] Verificações de inputs



### 1: Data relevantes

- 05/12/2022              — Disponibilização do enunciado.
- 13/01/2023 23:59:59 GMT —  Entrega final do trabalho.
- 16/01/2023              — 27/01/2023 Apresentação dos trabalhos.

### 2: Parâmetros de jogo

- w    —   Comprimento da grelha, em peças, ondew∈N;
- h    —   Altura da grelha em peças, ondeh∈N,⌈w 2 ⌉≤h≤w;
- n    —   Número de peças em linha para determinar a vitória (i.e.,TamanhoSequência), onde
           n∈N, n≤w;
- S    —   Conjunto de tamanhos de peças especiais disponível para cada jogador, onde ∀s∈S:S∈
           N, s < n. E.g.,n= 5, S= [3, 3 ,4], implica que cada jogador dispõe de duas peças especiais de 3
           peças, e uma peça especial de 4 peças, além do número ilimitado de peças unitárias.

### 3: Avaliação

- RJ    —   1 valor
- EJ    —   1 valor
- LJ    —   2 valor
- IJ    —   2 valor
- DJ    —   3 valores
- D     —   2 valores
- CP    —   4 valores
- V     —   3 valores
- G     —   1 valor
- L     —   1 valor



Notas joao:
    No Desistir Jogo não faz sentido estar assim, tipo como tá, o jogador 1 pode fazer o jogador 2 desistir invuluntáriamnete
    Nem pode ser como está😭, vou mexer no meu ficheiro para ver se consigo meter como é suposto
    
    
Falta "dar função" aos parametros no desistir, inputs e outputs feitos no ficheiro desistit.py no meu folder