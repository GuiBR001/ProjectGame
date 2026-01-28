import funcoes as fn
import icons as ic
import shutil
from colorama import Fore, Style, init

largura_tela = shutil.get_terminal_size().columns
altura_tela = shutil.get_terminal_size().lines

#INICIALIZA A FASE 1 CRIANDO TUDO QUE A DE FUNÇÕES DENTRO DELA
def fase_1(fase: int, orda: int, player: dict) -> None:

    fn.criar_inimigos(fase, orda, player)

    while fase == 1 and orda == 1:
        fn.limpar_tela()
        if len(fn.lista_npcs) == 0:
            orda += 1
            break
        else:
            pass

        escolha = fn.escolha_seta_inimigo_fase1(player)
        if escolha is not None:
            fn.atacar_monstro(escolha, player)

    fn.criar_inimigos(fase, orda, player)

    while fase == 1 and orda == 2:
        fn.limpar_tela()
        if len(fn.lista_npcs) == 0:
            orda += 1
            break
        else:
            pass

        escolha = fn.escolha_seta_inimigo_fase1(player)
        if escolha is not None:
            fn.atacar_monstro(escolha, player)

    fn.criar_inimigos(fase, orda, player)

    while fase == 1 and orda == 3:
        fn.limpar_tela()
        if len(fn.lista_npcs) == 0:
            fase += 1
            break
        else:
            pass

        escolha = fn.escolha_seta_inimigo_fase1(player)
        if escolha is not None:
            fn.atacar_monstro(escolha, player)


        
