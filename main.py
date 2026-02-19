import os 
import sys
import shutil
import funcoes as fn
import fase as fs
import icons as ic
from colorama import Fore, Style, init

init(autoreset= True)
largura_tela = os.get_terminal_size().columns
altura_tela = shutil.get_terminal_size().lines
fase = 1
orda = 1


while True:

    escolha_menu = fn.escolha_seta_menu()

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
        escolha_raca = fn.escolha_seta_raca()
        
        if escolha_raca == "Esqueleto Flamejante":
            raca = 1
        elif escolha_raca == "Anjo Caído":
            raca = 2
        elif escolha_raca == "Sábio Feiticeiro":
            raca = 3
        elif escolha_raca == "Princesa Medusa":
            raca = 4
        elif escolha_raca == "Morte Mormurante":
            raca = 5
        elif escolha_raca == "Arqueiro Mágico":
            raca = 6

        ic.fase1_caminho_portal()
        input()
        ic.fase1_castelo()
        input()
        ic.fase1_entrada_castelo()
        input()
        ic.fase1_cidade()
        input()
        ic.fase1_heroina_alertando()
        input()
        ic.fase1_heroina_alertando2()
        input()
        ic.fase1_heroina_alertando3()
        input()
        ic.fase1_ataque_cidade()
        input()

        player = fn.criar_personagem(nome, raca)
        fn.limpar_tela()
        fn.exibir_player(player)
        print("\n")
        ic.exibir_player_img()
        print("\n")
        fn.centra_h(fn.rgb_text("Aperte ENTER para continuar"))
        input()
        fs.fase_1(fase, orda, player)

        if player['hp'] >= 1:
            ic.fase1_heroina_parabenizando()
            input()
            ic.fase1_heroina_parabenizando2()
            input()
        else:
            pass



    elif escolha_menu == "Ultimos Recordes":
        fn.ultimos_recordes()

    elif escolha_menu == "Créditos":
        fn.mostrar_creditos()

    elif escolha_menu == "Sair":
        fn.limpar_tela()
        print("\n" * 5)
        fn.centra_h_v(ic.jogo_encerrado(), Fore.RED)
        print("\n" * 2)
        fn.centra_h(fn.rgb_text("Jogo encerrado, volte quando quiser se aventurar mais!"))
        fn.centra_h(fn.rgb_text("   Os aldeões clamam pela volta do herói deles"))
        sys.exit(0)

    else:
        continue