import funcoes as fn
import icons as ic
import shutil
from colorama import Fore, Style, init

largura_tela = shutil.get_terminal_size().columns
altura_tela = shutil.get_terminal_size().lines

#INICIALIZA A FASE 1 CRIANDO TUDO QUE A DE FUNÇÕES DENTRO DELA
def fase_1(fase: int, orda: int, player: dict) -> None:

    while fase == 1:

        fn.limpar_tela()
        escolha = fn.escolha_seta_inimigo_fase1()
        fn.atacar_monstro(escolha, player)
