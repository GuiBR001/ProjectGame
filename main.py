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
fase = 1


while True:

    escolha_menu = ic.escolha_seta_menu()

    if escolha_menu == "Começar Novo Jogo":

        ic.fase1_guerra_morte_inicial()
        input()
        ic.fase1_morte_inicial()
        input()
        ic.fase1_mensagem()
        input()
        ic.fase1_morto_alem_fantasma()
        input()
        ic.fase1_deusa_reincarnacao()
        input()
        ic.fase1_deusa_reincarnacao2()
        input()
        ic.fase1_bencao_deusa()
        input()
        nome = ic.esc_nome()

        fn.limpar_tela()
        escolha_raca = ic.escolha_seta_raca()
        
        if escolha_raca == "Esqueleto Flamejante":
            raca = 1
            fn.descri_raca(raca)
        elif escolha_raca == "Anjo Caído":
            raca = 2
            fn.descri_raca(raca) 
        elif escolha_raca == "Sábio Feticeiro":
            raca = 3
            fn.descri_raca(raca)
        elif escolha_raca == "Princesa Medusa":
            raca = 4
            fn.descri_raca(raca)
        elif escolha_raca == "Morte Mormurante":
            raca = 5
            fn.descri_raca(raca)
        elif escolha_raca == "Arqueiro Mágico":
            raca = 6
            fn.descri_raca(raca)

        player = fn.criar_personagem(nome, raca)
        fs.fase_1(fase, player)


    elif escolha_menu == "Ultimos Recordes":
        ic.ultimos_recordes()

    elif escolha_menu == "Créditos":
        ic.mostrar_creditos()

    elif escolha_menu == "Sair":
        fn.limpar_tela()
        print("\n" * 14)
        fn.centra_h_v(Fore.BLACK + ic.jogo_encerrado())
        print("\n" * 2)
        fn.centra_h(fn.rgb_text("Jogo encerrado, volte quando quiser se aventurar mais!"))
        fn.centra_h(fn.rgb_text("   Os aldeões clamam pela volta do herói deles"))
        sys.exit(0)

    else:
        continue