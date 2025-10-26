import os 
import sys
import shutil
import funcoes as fn
import fases as fs
import icons as ic
from colorama import Fore, Style, init

init(autoreset= True)
largura_tela = os.get_terminal_size().columns
altura_tela = shutil.get_terminal_size().lines
ic.guerreira_elfica_espadalendaria()
input()
fase = 1
while True:

    escolha_menu = ic.escolha_seta_menu()

    if escolha_menu == "Começar Novo Jogo":

        fn.limpar_tela()
        escolha_raca = ic.escolha_seta_raca()
        
        if escolha_raca == "Esqueleto Flamejante":
            raca = 1
            fn.descri_raca(raca)
        elif escolha_raca == "Anjo Da Morte":
            raca = 2
            fn.descri_raca(raca) 
        elif escolha_raca == "Mago Ancião":
            raca = 3
            fn.descri_raca(raca)


        player = fn.criar_personagem(nome, raca)
        input(Fore.GREEN + ("Aperte ENTER para continuar".center(largura_tela)))
        fs.fase_1(fase, player)


    elif escolha_menu == "Ultimos Recordes":
        ic.ultimos_recordes()

    elif escolha_menu == "Créditos":
        ic.mostrar_creditos()

    elif escolha_menu == "Sair":
        fn.centra_h_v(fn.rgb_text("Volte sempre, os cidadões precisam de você!"))
        fn.centra_h(fn.rgb_text("Encerrando Jogo..."))
        sys.exit(0)

    else:
        continue