import funcoes as fn
import icons as ic
import shutil
from colorama import Fore, Style, init

largura_tela = shutil.get_terminal_size().columns
altura_tela = shutil.get_terminal_size().lines

itens = []


#INICIALIZA A FASE 1 CRIANDO TUDO QUE A DE FUNÇÕES DENTRO DELA
def fase_1(fase: int, orda: int, player: dict) -> None:

    fn.lista_npcs.clear()
    fn.escolhas_inimigo.clear()
    fn.criar_inimigos(fase, orda, player)

    while fase == 1 and orda == 1:
        fn.limpar_tela()
        if len(fn.lista_npcs) == 0:
            orda += 1
            break
        else:
            pass
        escolha = fn.escolha_seta_inimigo_fase1(player, orda)
        if escolha is not None:
            fn.atacar_monstro(escolha, player, orda)
            fn.ataque_dos_monstros(player, fn.lista_npcs)
            if player['hp'] <= 0:
                break
            else: 
                continue

    fn.criar_inimigos(fase, orda, player)
    fn.comprar_itens(player)

    while fase == 1 and orda == 2:
        fn.limpar_tela()
        if len(fn.lista_npcs) == 0:
            orda += 1
            break
        else:
            pass

        escolha = fn.escolha_seta_inimigo_fase1(player, orda)
        if escolha is not None:
            fn.atacar_monstro(escolha, player, orda)
            fn.ataque_dos_monstros(player, fn.lista_npcs)
            if player['hp'] <= 0:
                break
            else: 
                continue

    fn.criar_inimigos(fase, orda, player)

    while fase == 1 and orda == 3:
        fn.limpar_tela()
        if len(fn.lista_npcs) == 0:
            fase += 1
            break
        else:
            pass

        escolha = fn.escolha_seta_inimigo_fase1(player, orda)
        if escolha is not None:
            fn.atacar_monstro(escolha, player, orda)
            fn.ataque_dos_monstros(player, fn.lista_npcs)
            if player['hp'] <= 0:
                break
            else: 
                continue

    fn.escolhas_boss.append(fn.ogro_boss)
    while fn.ogro_boss['boss'] == True and player['hp'] >= 1:
        escolha = fn.escolha_seta_inimigo_bossfight(player)
        if fn.ogro_boss['hp'] <= 0:
            fn.ogro_boss['boss'] = False
        else: 
            pass

        if fn.ogro_boss['boss'] == False:
            break
        else:
            pass

        if escolha is not None:
            fn.atacar_boss(escolha, player)
            fn.ataque_dos_boss(player, fn.escolhas_boss)
            if player['hp'] <= 0:
                break
            else: 
                continue