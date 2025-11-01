import funcoes as fn
import icons as ic
import shutil
from colorama import Fore, Style, init

largura_tela = shutil.get_terminal_size().columns
altura_tela = shutil.get_terminal_size().lines

#INICIALIZA A FASE 1 CRIANDO TUDO QUE A DE FUNÇÕES DENTRO DELA
def fase_1(fase: int, player: dict) -> None:

    fn.limpar_tela()

    fn.criar_npcs_em_massa(fase, player)

    while fase == 1:

        input(Fore.GREEN + ("Aperte ENTER para continuar".center(largura_tela).center(altura_tela)))
        fn.limpar_tela()
        fn.escolha_seta_inimigo()