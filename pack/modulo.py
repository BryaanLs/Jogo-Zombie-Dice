from time import sleep
import random
from os import system
from pack.cores import amarelo, azul, verde, vermelho, nocolor, nomes, negrito, fundo


def pesp(msg, car):  # FUNÇÃO PRINT ESPECIAL (CHAMADA PESP('MENSAGEM', CARACTERE ESPECIAL))
    negrito = '\033[1m'
    nocolor = '\033[m'
    tam = len(msg)+6
    sleep(0.4)
    print(f'{negrito}{car}{nocolor}' * tam)
    sleep(0.4)
    print(f'{negrito}{msg:^{tam}}{nocolor}')
    sleep(0.4)
    print(f'{negrito}{car}{nocolor}' * tam)


def titulofixo():  # TITULO COM APARIÇÃO FREQUENTE
    system("cls")
    print('-=-'*33)
    print('\033[7;32;42m=\033[m'*100)
    print(f'{vermelho} {"Z O M B I E  D I C E":>60}')
    print('\033[7;32;42m=\033[m'*100)
    print('-=-'*33)
    print('\n'*1)


def inserir_dados():  # Inserir dados no copo
    dadoVerde = 'CPCTPC'
    dadoAmarelo = 'TPCTPC'
    dadoVermelho = 'TPTCPT'
    copo = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo,
            dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]
    return copo


def quantidade_jogadores():  # Informando quantidade de jogadores
    Njogadores = 0
    JogadorA = 0
    while Njogadores < 2:
        sleep(0.2)
        Njogadores = int(
            input(f'{nomes}Informe o número de jogadores!:{negrito} '))
        if Njogadores < 2:
            sleep(0.2)
            pesp(f'{vermelho}{"      * * INSIRA NO MINÍMO 2 JOGADORES!! * *"}{nocolor}',
                 f'{amarelo}~{nocolor}')
            print('\n')
            sleep(2)
            system("cls")
            titulofixo()
    return Njogadores, JogadorA


def inserir_jogadores(NumeroJogadores):  # Inserir nome dos jogadores OK
    listaJ = []
    aux = []
    tiros = passos = cerebros = 0
    Njogadores = NumeroJogadores
    for c in range(0, Njogadores):
        nome = str(
            input(f'\n{azul}Insira o nome do(a) {c+1}° jogador(a):{nocolor}{negrito} '))
        print(f'{nocolor}')
        aux.append(nome)
        aux.append(0)
        aux.append(0)
        listaJ.append(aux[:])
        aux.clear()
    return listaJ, tiros, passos, cerebros


def inicio_jogo():  # Iniciando o jogo (Loading)
    sleep(1)
    system("cls")
    titulofixo()
    print(f'{negrito}{"INICIANDO JOGO":>57}{nocolor}')
    print()
    for c in range(0, 96):
        sleep(0.01)
        print(f'{fundo}_', end=f'{nocolor}', flush=True)
        if c == 95:
            print(f'{fundo}100%{nocolor}')
    print()
    print(f'{amarelo}{"CARREGAMENTO COMPLETO":^101}{nocolor}')
    sleep(2)
    system("cls")
    titulofixo()


def turno(jogadorA, listaJ, copo):  # Primeiro Turno de cada jogador E SORTEAR A COR DOS DADOS
    dadosSorteados = []
    print(f'{negrito}-{nocolor}'*40)
    print(
        f'{negrito}TURNO DO(A) JOGADOR(A): {verde}{listaJ[jogadorA][0]}{nocolor}')
    print(f'{negrito}-{nocolor}'*40)
    print(f'{negrito}COR E DADOS SORTEADOS{nocolor}')
    print('\n')
    for c in range(0, 3):
        numSort = random.randint(0, 12)
        dadosorteado = copo[numSort]  # copo [5]
        if dadosorteado == 'CPCTPC':
            corDado = (f'{verde}VERDE{nocolor}')
        elif dadosorteado == 'TPCTPC':
            corDado = (f'{amarelo}AMARELO{nocolor}')
        elif dadosorteado == 'TPTCPT':
            corDado = (f'{vermelho}VERMELHO{nocolor}')
        sleep(0.4)
        print(corDado, end=' ')
        dadosSorteados.append(dadosorteado)
    print()
    return jogadorA, dadosSorteados


# SORTEAR FACE DOS DADOS
def sortear_dados(jogadorA, tiros, passos, cerebros, dadosSorteados, listaJ):
    for dadosorteado in dadosSorteados:
        FaceDoDado = random.randint(0, 5)
        if dadosorteado[FaceDoDado] == 'C':
            sleep(0.8)
            print('\nVocê comeu um  cérebro!')
            cerebros += 1
            listaJ[jogadorA][1] += 1
        elif dadosorteado[FaceDoDado] == 'T':
            sleep(0.8)
            print('\nVocê levou um tiro!')
            tiros += 1
            listaJ[jogadorA][2] += 1
        elif dadosorteado[FaceDoDado] == 'P':
            sleep(0.8)
            print('\nUm sobrevivente fugiu!')
            passos += 1
    return tiros, passos, cerebros


def placar(jogadorA, listaJ):  # Mostrando placar do jogador atual
    sleep(0.5)
    print('\n')
    print(f'{nomes}-{nocolor}'*40)
    sleep(0.5)
    print(f'{azul} {"-- SCORE ATUAL --":^38} {nocolor}')
    print(f'{nomes}.{nocolor}'*40)
    print()
    sleep(0.5)
    print(
        f'{f"{verde}CÉREBROS: {listaJ[jogadorA][1]}{nocolor}":>23}', end=' ', flush=True)
    sleep(0.5)
    print(f'{f"{vermelho}TIROS: {listaJ[jogadorA][2]}{nocolor}":>34}')
    sleep(0.5)
    print()
    print(f'{nomes}-{nocolor}'*40)
    sleep(0.5)
    print()


# VERIFICAR SE O JOGADOR ATUAL LEVOU 3 TIROS
def verificar_tiros(Njogadores, jogadorA, tiros, passos, cerebros, listaJ):
    listaJ[jogadorA][2] = 0
    listaJ[jogadorA][1] -= cerebros
    print(
        f'{vermelho}HEADSHOT!{nocolor} {negrito}{listaJ[jogadorA][0]}{nocolor} você levou {vermelho} - {tiros} tiros - {nocolor} e perdeu os {verde} - {cerebros} cerebros - {nocolor} dessa rodada')
    print(f'{negrito}{"Passando para o(a) próximo(a) jogador(a)...":^60}{nocolor}')
    sleep(4)
    jogadorA += 1
    tiros = 0
    cerebros = 0
    passos = 0
    if jogadorA+1 > Njogadores:
        jogadorA = 0
    return jogadorA, tiros, passos, cerebros


def verificar_cerebros(jogadorA, listaJ):  # VERIFICAR CEREBROS
    titulofixo()
    print(
        f'{negrito}{verde} = = | PARABÉNS <@ {listaJ[jogadorA][0]} @> !Você atingiu o limite de pontos e venceu a partida! | = = {nocolor}')
    sleep(5)


# PROXIMO JOGADOR CASO O JOGADOR ATUAL DECIDA NÃO CONTINUAR A RODADA
def proximo_jogador(numjogadores, jogadorA, tiros, passos, cerebros, listaJ):
    Njogadores = numjogadores
    system("cls")
    titulofixo()
    listaJ[jogadorA][2] = 0
    jogadorA += 1
    tiros = 0
    cerebros = 0
    passos = 0
    if jogadorA+1 > Njogadores:
        jogadorA = 0
    return jogadorA, tiros, cerebros, passos


# MISTURAR OS DADOS CASO O JOGADOR QUEIRA CONTINUAR A RODADA
def misturar_dados():
    sleep(0.2)
    system("cls")
    titulofixo()
    pesp('* * * MISTURANDO OS DADOS * * *', '-')
    sleep(1.3)
    system("cls")
    titulofixo()
