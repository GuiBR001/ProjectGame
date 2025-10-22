import funcoes as fn
from colorama import Fore, Style, init



#fase 1
def fase_1(fase: int, player: dict) -> None:
    npc_atacado = ""
    
    while fase == 1:

        input("\nAperte ENTER para continuar")
        fn.limpar_tela()
        fn.exibir_player(player)
        print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
        fn.exibir_npcs()
        try:
            if len(fn.lista_npcs) <= 0:
                fn.limpar_tela()
                fn.fase_1()
                sair = input("\nAperte ENTER para voltar")
                if sair == "":
                    fn.limpar_tela()
                    print(fn.rgb_text("\nPARABÉNS GUERREIRO, SEUS STATUS ATUAIS SÃO:\n"))
                    fn.exibir_player(player)
                    return fase == 2
            else:
                escolha = int(input("\nEscolha qual monstro deseja atacar: "))

        except ValueError:
            fn.limpar_tela()
            print(fn.rgb_text("\nNúmero invalido! digite um numero de 1 a 7"))
            continue

        match escolha:

            case 1:
                   fn.limpar_tela()
                   npc_atacado = fn.lista_npcs[0]['nome']
                   fn.lista_npcs[0]['hp'] -= player['dano']
                   fn.limpar_tela()
                   fn.exibir_player(player)
                   print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                   fn.exibir_npcs()
                   if fn.lista_npcs[0]['hp'] <= 0:
                       print(f"""
                                   {fn.lista_npcs[0]['nome']} derrotado!
                       """.upper())
                       del fn.lista_npcs[0]

                   else:
                        print(f"""
                                {Fore.RED}{npc_atacado} recebeu {player["dano"]} de dano!

                            """)
                        continue
                    


            case 2:
                if len(fn.lista_npcs) <= 1:
                    fn.limpar_tela()
                    print(fn.rgb_text(f"\nNúmero invalido! Digite um número de 1 a {len(fn.lista_npcs)}"))
                    sair = input("\nAperte ENTER para voltar")
                    if sair == "":
                        fn.limpar_tela()
                        fn.exibir_player(player)
                        print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                        fn.exibir_npcs()
                        continue
                else:
                    fn.limpar_tela()
                    npc_atacado = fn.lista_npcs[1]['nome']
                    fn.lista_npcs[1]['hp'] -= player['dano']
                    fn.limpar_tela()
                    fn.exibir_player(player)
                    print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                    fn.exibir_npcs()
                    if fn.lista_npcs[1]['hp'] <= 0:
                        print(f"""
                                    {fn.lista_npcs[1]['nome']} derrotado!
                        """.upper())
                        del fn.lista_npcs[1]

                    else:
                        print(f"""
                                {Fore.RED}{npc_atacado} recebeu {player["dano"]} de dano!

                            """)
                        continue


            case 3:
                if len(fn.lista_npcs) <= 2:
                    fn.limpar_tela()
                    print(fn.rgb_text(f"\nNúmero invalido! Digite um número de 1 a {len(fn.lista_npcs)}"))
                    sair = input("\nAperte ENTER para voltar")
                    if sair == "":
                        fn.limpar_tela()
                        fn.exibir_player(player)
                        print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                        fn.exibir_npcs()
                        continue
                else:
                    fn.limpar_tela()
                    npc_atacado = fn.lista_npcs[2]['nome']
                    fn.lista_npcs[2]['hp'] -= player['dano']
                    fn.limpar_tela()
                    fn.exibir_player(player)
                    print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                    fn.exibir_npcs()
                    if fn.lista_npcs[2]['hp'] <= 0:
                        print(f"""
                                    {fn.lista_npcs[2]['nome']} derrotado!
                        """.upper())
                        del fn.lista_npcs[2]

                    else:
                        print(f"""
                                {Fore.RED}{npc_atacado} recebeu {player["dano"]} de dano!

                            """)
                        continue


            case 4:
                if len(fn.lista_npcs) <= 3:
                    fn.limpar_tela()
                    print(fn.rgb_text(f"\nNúmero invalido! Digite um número de 1 a {len(fn.lista_npcs)}"))
                    sair = input("\nAperte ENTER para voltar")
                    if sair == "":
                        fn.limpar_tela()
                        fn.exibir_player(player)
                        print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                        fn.exibir_npcs()
                        continue
                else:
                    fn.limpar_tela()
                    npc_atacado = fn.lista_npcs[3]['nome']
                    fn.lista_npcs[3]['hp'] -= player['dano']
                    fn.limpar_tela()
                    fn.exibir_player(player)
                    print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                    fn.exibir_npcs()
                    if fn.lista_npcs[3]['hp'] <= 0:
                        print(f"""
                                    {fn.lista_npcs[3]['nome']} derrotado!
                        """.upper())
                        del fn.lista_npcs[3]

                    else:
                        print(f"""
                                {Fore.RED}{npc_atacado} recebeu {player["dano"]} de dano!

                            """)
                        continue


            case 5:
                if len(fn.lista_npcs) <= 4:
                    fn.limpar_tela()
                    print(fn.rgb_text(f"\nNúmero invalido! Digite um número de 1 a {len(fn.lista_npcs)}"))
                    sair = input("\nAperte ENTER para voltar")
                    if sair == "":
                        fn.limpar_tela()
                        fn.exibir_player(player)
                        print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                        fn.exibir_npcs()
                        continue
                else:
                    fn.limpar_tela()
                    npc_atacado = fn.lista_npcs[4]['nome']
                    fn.lista_npcs[4]['hp'] -= player['dano']
                    fn.exibir_player(player)
                    fn.limpar_tela()
                    print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                    fn.exibir_npcs()
                    if fn.lista_npcs[4]['hp'] <= 0:
                        print(f"""
                                    {fn.lista_npcs[4]['nome']} derrotado!
                        """.upper())
                        del fn.lista_npcs[4]

                    else:
                        print(f"""
                                {Fore.RED}{npc_atacado} recebeu {player["dano"]} de dano!

                            """)
                        continue


            case 6:
                if len(fn.lista_npcs) <= 5:
                    fn.limpar_tela()
                    print(fn.rgb_text(f"\nNúmero invalido! Digite um número de 1 a {len(fn.lista_npcs)}"))
                    sair = input("\nAperte ENTER para voltar")
                    if sair == "":
                        fn.limpar_tela()
                        fn.exibir_player(player)
                        print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                        fn.exibir_npcs()
                        continue
                else:
                    fn.limpar_tela()
                    npc_atacado = fn.lista_npcs[5]['nome']
                    fn.lista_npcs[5]['hp'] -= player['dano']
                    fn.limpar_tela()
                    fn.exibir_player(player)
                    print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                    fn.exibir_npcs()
                    if fn.lista_npcs[5]['hp'] <= 0:
                        print(f"""
                                    {fn.lista_npcs[5]['nome']} derrotado!
                        """.upper())
                        del fn.lista_npcs[5]
                
                    else:
                        print(f"""
                                 {Fore.RED}{npc_atacado} recebeu {player["dano"]} de dano!

                             """)
                        continue


            case 7:
                if len(fn.lista_npcs) <= 6:
                    fn.limpar_tela()
                    print(fn.rgb_text(f"\nNúmero invalido! Digite um número de 1 a {len(fn.lista_npcs)}"))
                    sair = input("\nAperte ENTER para voltar")
                    if sair == "":
                        fn.limpar_tela()
                        fn.exibir_player(player)
                        print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                        fn.exibir_npcs()
                        continue
                else:
                    fn.limpar_tela()
                    npc_atacado = fn.lista_npcs[6]['nome']
                    fn.lista_npcs[6]['hp'] -= player['dano']
                    fn.limpar_tela()
                    fn.exibir_player(player)
                    print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                    fn.exibir_npcs()
                    if fn.lista_npcs[6]['hp'] <= 0:
                        print(f"""
                                    {fn.lista_npcs[6]['nome']} derrotado!
                        """.upper())
                        del fn.lista_npcs[6]
                    else:
                        print(f"""
                                 {Fore.RED}{npc_atacado} recebeu {player["dano"]} de dano!

                             """)
                        continue


            case _:
                fn.limpar_tela()
                print(fn.rgb_text(f"\nNúmero invalido! Digite um número de 1 a {len(fn.lista_npcs)}"))
                sair = input("\nAperte ENTER para voltar")
                if sair == "":
                    fn.limpar_tela()
                    fn.exibir_player(player)
                    print(Fore.YELLOW + "CIDADELA DO REI DE FERRO\n")
                    fn.exibir_npcs()
                    continue