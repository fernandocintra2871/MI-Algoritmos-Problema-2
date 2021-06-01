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

from keyboard import is_pressed, press # Importação das funções is_pressed e press, da biblioteca keyboard, responsáveis respectivamente por detectar quando uma tecla é pressionada e simular o pressionamento de uma
from os import system, name # Importação das funções system e name, da biblioteca os, responsáveis em conunto por limpar o teminal
from time import sleep # Importação da função sleep, da biblioteca time, responsável por parar a execução do codigo por uma quantidade de tempo

# Abaixo estão todas funções importadas da biblioteca jogar_funções, criada pelo autor do codigo e explicdas em outro arquivo
from jogar_funcoes import criar_mapa, criar_nave, criar_meteoro, criar_tiro, mover_nave, mover_meteoros, mover_tiros, mostrar_mapa


dic_pont = {} # Definição do dicionário que guardará o nome e a pontuação dos jogadores
lista_menu =  ['Jogar', 'Recordes', 'Sobre', 'Sair'] # Definição das opções selecionaveis do menu principal em uma lista

press('f11') # É simulado o pressionamento da tecla f11 para a tela do terminal fica cheia

'''
Abaixo tem-se o sistema do menu principal que é dividido em dois
O primeiro responsável por printar as opções do menu principal com a respectiva opção selecionada
O segundo é reponsável por detectar a tecla pressionada para realiazar a alteração da seleção
'''
sair_menu = False # Variavel chave para a permanencia da repetição do while
cont_opcao = 0 # Contem a opção selecionada no momento
while sair_menu == False:
    print('═══════════════'*2)
    print('\t╔═════════════╗')
    print('\t║  Asteroids  ║')
    print('\t╚═════════════╝')
    print('═══════════════'*2)

    """
    Primeiro sistema
    """
    cont_menu = 0 # Variavel contadora utilizada para percorrer a lista_menu
    while cont_menu < len(lista_menu):
        if cont_menu == cont_opcao:
            print(f'> {lista_menu[cont_menu]}')
        else:
            print(f'  {lista_menu[cont_menu]}')
        cont_menu += 1

    print('═══════════════'*2)

    '''
    Segundo sistema
    '''
    tecla_press = False
    sair_opcao = False
    while tecla_press == False:
        if is_pressed('up'): # Assim como as proximas, detecta quando a telca especificada é pressionada
            cont_opcao -= 1
            if cont_opcao == -1:
                cont_opcao = 3
            tecla_press = True
        elif is_pressed('down'):
            cont_opcao += 1
            if cont_opcao == 4:
                cont_opcao = 0
            tecla_press = True
        elif is_pressed('enter'): # Quando o enter é pressionado será excutada a opção referente ao cont_opçao

            '''
            A primeira condicional se refere a primeira opção do menu e ela iniciará a jogatina
            A segunda a exibição dos recordes dos jogadores
            A terceira a exibição das informações do jogo
            E a quarta a saida do jogo
            '''
            if cont_opcao == 0:
                meteoros = [] # Futura matriz que guardará as posições dos meteoros
                tiros = [] # Futura matriz que guardará as posições dos tiros
                mapa = criar_mapa()
                nave = criar_nave(mapa)
                vidas = 10
                score = 0 # Pontuação por meteoro destruido
                cont_quadros = 0 # Variavel que guarda a quantidade de vezes que o loop se repetiu
                cont_meteoros = 0 # Variavel que guarda a ultima vez que um meteoro foi criado
                meteoro_pas = '' # Variavel que guarda a condição da nave em relação aos meteoros
                jogador = '' # Variavel que guardara o nome do jogador
                """
                O while continuara em loop até que o nome do jogador seja preenchido, o que só ocorro quando a jogatina é encerrada
                Enquanto isso não acontece a jogatina continua e a cada repetição é printado um frame diferente do jogo e
                """
                while jogador == '':
                    """
                    Caso aconteça a colisão da nave com o meteoro, a vida chegue a zero ou a tecla esc venha a ser
                    presisonada a jogatina é encerrada e a execução ficara em loop até que o jogador digite o seu nome
                    Assim então ocorrera o salvamento do recorde dele
                    """
                    if meteoro_pas == 'atingiu' or vidas <= 0:
                        system('cls' if name == 'nt' else 'clear')
                        while jogador == '' and len(jogador) < 3:
                            jogador = ''
                            system('cls' if name == 'nt' else 'clear')
                            print('FIM DE JOGO!!')
                            jogador = input('\nSeu nome: ')
                            jogador = jogador.strip()
                            if jogador != '':
                                dic_pont[jogador] = score
                    else:
                        system('cls' if name == 'nt' else 'clear')
                        mostrar_mapa(mapa, vidas, score)
                        if meteoro_pas == 'passou': # se a condição da nave em relação ao meteoro for que um meteoro passou
                            vidas -= 1

                        """
                        As condicionais a seguir detectam se as suas respectivas teclas são apertadas
                        """
                        if is_pressed('right'):
                            meteoro_pas = mover_nave('right', mapa, nave)
                        elif is_pressed('left'):
                            meteoro_pas = mover_nave('left', mapa, nave)
                        elif is_pressed('space'):
                            tiros.append(criar_tiro(mapa, nave))
                        elif is_pressed('esc'):
                            meteoro_pas = 'atingiu'

                        if meteoro_pas != 'atingiu':
                            meteoro_pas = mover_meteoros(mapa, meteoros)

                        score += mover_tiros(mapa, tiros, meteoros)

                        if cont_quadros > cont_meteoros + 7: # Faz com que seja criado um meteoro a cada 7 repetições
                            meteoros.append(criar_meteoro(mapa))
                            cont_meteoros = cont_quadros

                        cont_quadros += 1
                        sleep(0.07)

            elif cont_opcao == 1:
                system('cls' if name == 'nt' else 'clear')
                while sair_opcao == False:
                    dic_pont_temp = dict(dic_pont) # Salva uma copia do dicionário de pontos no dicionario temporario
                    dic_pont_ord = {} # Dicionário que será utilizada para armazenar os jogadores na ordem de maior pontuação
                    """
                    Percorre todos itens do dicionário dic_pont_temp salvando a cada repetição o jogador com maior pontuação
                    no dic_pont_od e excluindo o mesmo do dic_pont_temp
                    """
                    while len(dic_pont_temp) != 0:
                        pont_temp = -1
                        for jogador, pontuacao in dic_pont_temp.items():
                            if pontuacao > pont_temp:
                                jogador_temp = jogador
                                pont_temp = pontuacao
                        dic_pont_temp.pop(jogador_temp)
                        dic_pont_ord[jogador_temp] = pont_temp

                    print('══════════════'*2)
                    print('\t╔════════════╗')
                    print('\t║  Recordes  ║')
                    print('\t╚════════════╝')
                    print('══════════════'*2)

                    print('Jogador\t\tPontuação')
                    for jogador, pontuacao in dic_pont_ord.items(): # Percorre o dicionário dic_pont_ord printando suas respectivas chaves e valores
                        print(f'{jogador}\t\t{pontuacao}')
                    
                    print('══════════════'*2)
                    print('Aperte [Esc] para voltar')

                    """
                    Detecta quando a  tecla esc é pressionada
                    Mundando a variavel sair_opcao para True
                    Assim voltando para o menu principal
                    """
                    tecla_press == False
                    while tecla_press == False:
                        if is_pressed('esc'):
                            sair_opcao = True
                            tecla_press = True
         
            elif cont_opcao == 2:
                system('cls' if name == 'nt' else 'clear')
                while sair_opcao == False:
                    print('═════════════'*2)
                    print('\t╔═════════╗')
                    print('\t║  Sobre  ║')
                    print('\t╚═════════╝')
                    print('═════════════'*2)
                    print('Criado por Fernando Cintra')
                    print('Este jogo foi baseado no jogo Asteroids dá Atari')
                    print('═════════════'*2)
                    print('Aperte [Esc] para voltar')

                    tecla_press == False
                    while tecla_press == False:
                        if is_pressed('esc'):
                            sair_opcao = True
                            tecla_press = True
                                                       
            else:
                sair_menu = True
            tecla_press = True

    sleep(0.1)
    system('cls' if name == 'nt' else 'clear')