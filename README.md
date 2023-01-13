### Situações em falta:

- [x] Split nos inputs
- [x] Peças especiais
- [ ] Prints no controller
- [ ] Readicionar limpezas da consola
- [x] Adicionar `tamanho_Sequencia` ás variáveis de jogo
- [x] Adicionar `tamanho_PecasEspeciais` ás variaveis de jogo
- [x] Criar dicionário com nome jogadores, jogos jogados e vitórias
    - [x] Ordenar alfabéticamente

- [x] Verificações de `Opção 1`

- [x] `RJ - Registar jogador`
    - [x] Verificações de inputs
        - [x] Verificar se `op1` leva mais do que o requisitado
    - [x] Nome unico

- [x] `EJ - Remover jogador`
    - [x] Verificações de inputs
        - [x] Verificar se `op1` leva mais do que o requisitado

- [x] `LJ - Listar jogadores`
    - [x] Verificações de inputs
        - [x] Verificar se `op1` leva mais do que o requisitado
    - [x] Indicar número de jogos jogados e vitórias

- [x] `IJ - Iniciar jogo`
    - [x] Jogo funcional
    - [x] Verificações de inputs
        - [x] Verificar se `op1` leva mais do que o requisitado
        - [x] `heigth` - Altura da grelha (`width/2` ≤ `heigth` ≤ `width`)
        - [x] `sequenced_pieces` - Número de peças em linha para determinar a vitória (`sequenced_pieces` ≤ `width`)
        - [x] `special_pieces` - Conjunto de tamanhos de peças especiais disponível para cada jogador (`special_pieces` < `sequenced_pieces`)
    - [x] Verificar se já se encontra jogo em curso
    - [x] Verificar se jogador indicado se encontra registado
    - [x] Adicionar menu depois de o jogador fazer a jogada
    - [x] Dar update a `dicionario_Jogos` para mudar `decorrer_jogo`

- [x] `DJ - Detalhes do jogo`
    - [x] Verificações de inputs
        - [x] Verificar se `op1` leva mais do que o requisitado
    - [x] Informações do jogo em curso
        - [x] Tamanho da grelha
        - [x] Nomes jogadores
            - [x] Alfabéticamente
        - [x] Quantidade de peças especiais disponíveis para cada jogador

- [ ] `D - Desistir`
    - [x] Verificações de inputs
        - [x] Verificar se `op1` leva mais do que o requisitado
    - [+-] Criar função desistir_Jogo
        - [ ] Editar dicionário jogos jogados e vitórias

- [ ] `CP - Colocar peça`
    - [ ] Verificações de inputs
        - [ ] Verificar se `op1` leva mais do que o requisitado

- [ ] `V - Visualizar resultado`
    - [ ] Verificações de inputs
        - [ ] Verificar se `op1` leva mais do que o requisitado

- [ ] `G - Gravar`
    - [ ] Verificações de inputs
        - [ ] Verificar se `op1` leva mais do que o requisitado

- [ ] `L - Ler`
    - [ ] Verificações de inputs
        - [ ] Verificar se `op1` leva mais do que o requisitado



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