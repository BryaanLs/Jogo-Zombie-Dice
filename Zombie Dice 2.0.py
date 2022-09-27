#  -=-=-=@ INFORMAÇÕES DO ALUNO (EU)   @=-=-=-
# NOME: Bryan Luccas De Paula Soares
# CURSO: Analise e desenvolvimento de sistemas
# TURMA: 01

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# BIBLIOTECAS E CORES UTILIZADAS NO DECORRER DO PROGRAMA
import pack.modulo
from pack.cores import azul, nocolor


pack.modulo.titulofixo()  # TITULO FIXO DO GAME

# INICIO DO GAME
input(f'\n\n{azul}{" | PRESSIONE ENTER PARA INICAR O JOGO |":^100}{nocolor}')


pack.modulo.titulofixo()  # TITULO FIXO DO GAME


# SOLICITANDO QUANTIDADE DE JOGADORES E NOMES
numJogadores, jogadorA = pack.modulo.quantidade_jogadores()

listaJ, tiros, passos, cerebros = pack.modulo.inserir_jogadores(numJogadores)


pack.modulo.titulofixo()  # TITULO FIXO DO GAME

copo = pack.modulo.inserir_dados()  # DADOS

pack.modulo.inicio_jogo()  # Iniciando o jogo

while True:
    # INICIANDO TURNO E SORTEANDO COR DOS DADOS
    jogadorA, dadosSorteados = pack.modulo.turno(jogadorA, listaJ, copo)

    # SORTEANDO AS FACES DOS DADOS:
    tiros, passos, cerebros = pack.modulo.sortear_dados(
        jogadorA, tiros, passos, cerebros, dadosSorteados, listaJ)

    pack.modulo.placar(jogadorA, listaJ)  # SCORE ATUAL DO JOGADOR

    # SE TOMOU 3 TIROS (Seguindo a regra do jogo, caso o jogador tome >=3 tiros ele perde os pontos feitos na rodada)
    if listaJ[jogadorA][2] >= 3:
        jogadorA, tiros, passos, cerebros = pack.modulo.verificar_tiros(
            numJogadores, jogadorA, tiros, passos, cerebros, listaJ)
        pack.modulo.titulofixo()

    elif listaJ[jogadorA][1] >= 13:
        pack.modulo.verificar_cerebros(jogadorA, listaJ)
        break
    else:
        continuarTurno = input(
            'Você deseja jogar os dados outra vez? [S/N]: ').strip().upper()
        if continuarTurno == 'N':
            jogadorA, tiros, passos, cerebros = pack.modulo.proximo_jogador(
                numJogadores, jogadorA, tiros, passos, cerebros, listaJ)
        else:
            pack.modulo.misturar_dados()
