"""
Autor: Luis Fernando do Rosario Cintra
Componente Curricular: MI - Algoritmos
Concluido em: 25/04/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

from random import choice # Importação da função choice , que escolhe um valor aleatorio em uma lista, da biblioteca random

'''
Função que cria a matriz que representa o mapa/tela do jogo
'''
def criar_mapa():
    x_coluna = 65 
    y_linha = 32
    mapa = [] # Lista que recebererá outras listas/linhas se tornando uma matriz
    for cont1 in range(0, y_linha): 
        linha = [] # Lista temporaria que armazena os espaços/colunas
        if cont1 == 0 or cont1 == y_linha - 1: # Condicional que possibilita a criação da divisão superior e inferior do mapa
            for cont2 in range(0, x_coluna):
                linha.append('█')
        else:
            for cont2 in range(0, x_coluna):
                if cont2 == 0 or cont2 == x_coluna - 1: # Condicional que possibilita a criação da divisão esqeuda e direita do mapa
                    linha.append('█')
                else:
                    linha.append(' ')
        mapa.append(linha)
    return mapa # Retorna a matriz mapa já concluida

'''
Função que cria a nave na matriz mapa substituindo os caracteres nos respectivos índices
'''
def criar_nave(mapa): # A matriz mapa é passada por referência, logo não precisa ser retornada (obs. isso também ocorre nas outras funções que fazem uso da matriz mapa)
    mapa[29][32] = '*'
    mapa[30][31] = '*'
    mapa[30][32] = '*'
    mapa[30][33] = '*'
    return [29, 32] # Retorna as posições/índices do caractere referencia da nave na matriz mapa, em uma lista

'''
Função que cria o meteoro na matriz mapa substituindo os caracteres nos respectivos índices (obs. semelhante a criação da nave)
'''
def criar_meteoro(mapa):
    x_coluna = choice([4, 11, 18, 25, 32, 39, 46, 53, 60]) # x_coluna recebe um valor aleatorio dentre os da lista que será usado como referencia para criação do meteoro
    mapa[1][x_coluna-1] = '*'
    mapa[1][x_coluna] = '*'
    mapa[1][x_coluna+1] = '*'
    return [1, x_coluna] # Retorna as posições/índices do caractere referencia do meteoro na matriz mapa, em uma lista

'''
Função que cria o tiro na matriz mapa substituindo os caracteres nos respectivos índices (obs. semelhante a criação da nave)
'''
def criar_tiro(mapa, nave): # A lista nave também é passada por referência, logo não precisa ser retornada (obs. isso também ocorre nas outras funções que fazem uso da lista nave)
    linha = nave[0] - 1 # linha recebe o indice correspondente a linha da nave - 1
    coluna = nave[1]
    mapa[linha][coluna] = 'o'
    return [linha, coluna] # Retorna as posições/índices do caractere do tiro na matriz mapa, em uma lista

'''
Função responsável por mover a nave na matriz mapa substituindo os caracteres nos respectivos índices gerados pela tecla recebida
'''
def mover_nave(tecla, mapa, nave):
    meteoro_pas = '' # Variavel que guarda a condição da nave em relação ao asteroide

    linha = nave[0]
    coluna = nave[1]
    mapa[linha][coluna] = ' '
    mapa[linha + 1][coluna + 1] = ' '
    mapa[linha + 1][coluna] = ' '
    mapa[linha + 1][coluna - 1] = ' '

    """
    Aspos verificar se a nave não está saindo dos limites da matriz mapa
    verifica se a futura posição da nave não possui um meteoro
    se for o caso, a condição da nave/meteoro_pas recebe 'atingiu'
    """
    if coluna+7 <= 62 and coluna-7 >= 2:
        if tecla == 'right' and mapa[linha+1][coluna+7] == '*':
            meteoro_pas = 'atingiu'
        elif tecla == 'left' and mapa[linha][coluna-7] == '*':
            meteoro_pas = 'atingiu'

    """
    Verifica-se qual tecla foi recebida pela função e
    de acordo com a mesma é alterado na matriz mapa de
    acordo com os novos indices/posições o lugar da nave
    E caso a futura posição da nave seja fora dos limites
    da matriz mapa a nave se mantem no mesmo local
    """
    if tecla == 'right' and coluna+7 <= 62:
        nave[1] += 7 
        linha = nave[0]
        coluna = nave[1]
        mapa[linha][coluna] = '*'
        mapa[linha + 1][coluna + 1] = '*'
        mapa[linha + 1][coluna] = '*'
        mapa[linha + 1][coluna - 1] = '*'
    elif tecla == 'left' and coluna-7 >= 2:
        nave[1] -= 7 
        linha = nave[0]
        coluna = nave[1]
        mapa[linha][coluna] = '*'
        mapa[linha + 1][coluna + 1] = '*'
        mapa[linha + 1][coluna] = '*'
        mapa[linha + 1][coluna - 1] = '*'
    else:
        mapa[linha][coluna] = '*'
        mapa[linha + 1][coluna + 1] = '*'
        mapa[linha + 1][coluna] = '*'
        mapa[linha + 1][coluna - 1] = '*'

    return meteoro_pas # Retorna a condição da nave

'''
Função responsável por mover os meteoros na matriz mapa substituindo os caracteres nos respectivos índices gerados pelo movimento dos mesmo
'''
def mover_meteoros(mapa, meteoros): # A matriz meteoros também é passada por referência, logo não precisa ser retornada (obs. isso também ocorre nas outras funções que fazem uso da matriz meteoros)
    meteoro_pas = ''
    c = 0 # Variavel contadora
    """
    Para cada lista contendo as os índices/posições do seu respectivo meteoro na matriz meteoros
    tem-se o índice referente as linhas amentado em 1 (que siginifica que o meteoro desceu)
    """
    while c < len(meteoros):
        meteoros[c][0] += 1
        linha = meteoros[c][0]
        coluna = meteoros[c][1]
        
        """
        Essa condicional verifica se na futura posição do meteoro 
        se encontra a nave, caso ocorra a condição da nave
        passa a ser 'atingiu'
        """
        if linha < 31:
            if mapa[linha][coluna] == '*':
                meteoro_pas = 'atingiu'

        """
        A sequência de condicionais abaixo é responsável pela
        movimentação do asteroide na matriz mapa, assim substituindo
        os caracteres nas respectivas
        """
        if linha < 31:
            mapa[linha][coluna-1] = '*'
            mapa[linha][coluna] = '*'
            mapa[linha][coluna+1] = '*'

        if linha < 32:
            mapa[linha-1][coluna-2] = '*'
            mapa[linha-1][coluna+2] = '*'

        if 3 <= linha < 33:
            mapa[linha-2][coluna-3] = '*'
            mapa[linha-2][coluna+3] = '*'
        if 4 <= linha < 34:
            mapa[linha-3][coluna-3] = ' '
            mapa[linha-3][coluna+3] = ' '
        if 5 <= linha < 35:
            mapa[linha-4][coluna-2] = ' '
            mapa[linha-4][coluna+2] = ' '
        if 6 <= linha < 36:
            mapa[linha-5][coluna-1] = ' '
            mapa[linha-5][coluna] = ' '
            mapa[linha-5][coluna+1] = ' '
        if linha == 36:
            meteoros.pop(c)
            meteoro_pas = 'passou'
            
        c += 1    
    return meteoro_pas

'''
Função responsável por mover os tiros na matriz mapa substituindo os caracteres nos respectivos índices gerados pelo movimento dos mesmo
'''
def mover_tiros(mapa, tiros, meteoros):  # A matriz tiros também é passada por referência, logo não precisa ser retornada
    score = 0 # conta quantos meteoros foram acertados pelos tiros
    c = 0
    """
    Para cada lista contendo as os índices/posições do seu respectivo tiro na matriz tiros
    tem-se o índice referente as linhas diminuido em 1 (que siginifica que o tiro está subindo)
    """
    while c < len(tiros):
        tiros[c][0] = tiros[c][0] - 1
        linha = tiros[c][0]
        coluna = tiros[c][1]

        """
        Caso a posição futura do tiro for fora da matriz mapa ou entre
        em colisão com um meteoro o tiro é eliminado, tanto da matriz mapa
        quanto da matriz tiros
        """
        if linha > 0 and mapa[linha][coluna] != '*':
            mapa[linha][coluna] = 'o'
        else:
            score += eliminar_meteoro(mapa, tiros[c], meteoros) # a função eliminar_meteoro é chamada
            tiros.pop(c)
        mapa[linha+1][coluna] = ' '
        c += 1
    return score # É retornada o score/pontuação fruto do movimento dos tiros

'''
Função responsável por, em caso de colisão, eliminar o meteoro tanto da matriz mapa quato da matriz meteoros
'''
def eliminar_meteoro(mapa, tiro, meteoros):
    score = 0
    c = 0
    while c < len(meteoros):
        """
        Caso tanto a coluna/índice 1 do meteoro sejá a mesma do tiro em questão assim como
        a linha/índice 0 for igual ou maior, ocorre a eliminação do meteoro
        """
        if tiro[1] == meteoros[c][1]:
            if tiro[0] <= meteoros[c][0]:
                linha = meteoros[c][0]
                coluna = meteoros[c][1]
                """
                Susbtituição dos caracteres do meteoro na matriz mapa
                """
                for y_linha in range(0, 5):
                    for x_coluna in range(1, 4):
                        if mapa[linha-y_linha][coluna-x_coluna] == '*':
                            mapa[linha-y_linha][coluna-x_coluna] = ' '
                        if mapa[linha-y_linha][coluna] == '*':
                            mapa[linha-y_linha][coluna] = ' '
                        if mapa[linha-y_linha][coluna+x_coluna] == '*':
                            mapa[linha-y_linha][coluna+x_coluna] = ' '
                meteoros.pop(c) # Eliminação da matriz meteoros
            score = 1
            
        c += 1
    return score

'''
Função responsável por mostrar no terminal matriz mapa juntamente com a vida e a pontuação
'''
def mostrar_mapa(mapa, vidas, score):
    print(f'Vida: {vidas}\t\tPontuação: {score}')
    """
    Percorre a matriz mapa, pritando linha a linha a mesma
    """
    for linha in mapa:
        linha_temp = ''
        for coluna in linha:
            linha_temp += coluna
        print(linha_temp)
    print('Aperte [Esc] para voltar')
        


