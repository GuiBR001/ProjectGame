import os
from random import randint
from colorama import Fore, Style, init


init(autoreset= True)

lista_npcs = []
player = {}


#limpa tela
def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear" )



#menu
def iniciar(fase: int, player: dict) -> None:

    match fase:

        case 1:
            for x in range(7):
                level = randint(1, 20)
                novo_npc = criar_npc(level)
                lista_npcs.append(novo_npc)

            exibir_player(player)
            print(f"""
                            {rgb_text("FASE 1")}

                {Fore.YELLOW} CIDADELA DO REI DE FERRO\n
                    """)
    
        case 2:
            for x in range(7):
                level = randint(21, 40)
                novo_npc = criar_npc(level)
                lista_npcs.append(novo_npc)
            exibir_player(player)
            print(Fore.GREEN + "CAMPOS DE BATALHA DE DRAKMOR\n")
    
        case 3:
            for x in range(7):
                level = randint(41, 60)
                novo_npc = criar_npc(level)
                lista_npcs.append(novo_npc)
            exibir_player(player)
            print(Fore.CYAN + "FLORESTA DE NÉVOA ETERNA\n")

        case 4:
            for x in range(7):
                level = randint(61, 80)
                novo_npc = criar_npc(level)
                lista_npcs.append(novo_npc)
            exibir_player(player)
            print(Fore.RED + "COVIL DO DRAGÃO ESCARLATE\n")

        case 5:
            for x in range(7):
                level = randint(81, 100)
                novo_npc = criar_npc(level)
                lista_npcs.append(novo_npc)
            exibir_player(player)
            print(Fore.MAGENTA + "FORTALEZA DAS SOMBRAS ANTIGAS\n")

            #exibir manualmente para manter a formatacao das letras coloridas corretamente
            print("\n" + "-" * (len(lista_npcs) * 12 + 10 ) + "\n")
            print(f"{'Nome':<8}", end="|")
            for npc in lista_npcs:
                print(f"{npc['nome']:<15}", end="|")
            print()

            print(Fore.CYAN + f"{'Level':<8}", end="|")
            for npc in lista_npcs:
                print(Fore.CYAN + f"{npc['level']:<10}", end="|")
            print()

            print(Fore.RED + f"{'Dano':<8}", end="|")
            for npc in lista_npcs:
                print(Fore.RED + f"{npc['dano']:<10}", end="|")
            print()

            print(Fore.MAGENTA + f"{'Saúde':<8}", end="|")
            for npc in lista_npcs:
                print(Fore.MAGENTA + f"{npc['hp']:<10}", end="|")
            print()

            print(Fore.GREEN + f"{'EXP':<8}", end="|")
            for npc in lista_npcs:
                print(Fore.GREEN + f"{npc['exp']:<10}", end="|")
            print()
            print("\n" + "-" * (len(lista_npcs) * 12 + 10))



#gera personagem
def criar_personagem() -> dict:

    nome = str(input("Escolha um nome: ")).upper()

    return  {
        "nome": nome,
        "level": 1,
        "exp": 0,
        "hp": 150,
        "dano": 10000
    }



# cria npc
def criar_npc(level) -> dict:

    if level >= 1 and level <= 10:
        if level <= 5:
            nome = "dominus"
        else:
            nome = "draconis"

    elif level >= 11 and level <= 20:
        if level <= 15:
            nome = "carceres"
        else:
            nome = "minotauro"

    elif level >= 21 and level <= 30:
        if level <= 25:
            nome = "poseidon"
        else:
            nome = "kraken"

    elif level >= 31 and level <= 40:
        if level <= 35:
            nome = "saci"
        else:
            nome = "boitatá"

    elif level >= 41 and level <= 50:
        if level <= 45:
            nome = "bobbafet"
        else:
            nome = "magma"

    elif level >= 51 and level <= 60:
        if level <= 55:
            nome = "farquad"
        else:
            nome = "ogroid"

    elif level >= 61 and level <= 70:
        if level <= 65:
            nome = "monsa"
        else:
            nome = "fenrir"

    elif level >= 71 and level <= 80:
        if level <= 75:
            nome = "mytus"
        else:
            nome = "hydra"

    elif level >= 81 and level <= 90:
        if level <= 85:
            nome = Fore.GREEN + "GUISPARK"
        else:
            nome = Fore.BLUE + "TARTARUS"

    elif level >= 91 and level <= 100:
        if level <= 95:
            nome = Fore.YELLOW + "ENDLESS"
        else:
            nome = Fore.RED + "FOGUINHO"

    novo_npc = {
        "nome": f"{nome}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "exp": 7 * level,
    }

    return novo_npc



#cria varios npcs
def criar_npc_em_massa(n) -> None:

    for x in range(n):
       level = randint(1, 100)
       novo_npc = criar_npc(level)
       lista_npcs.append(novo_npc)
        


#exibe jogador
def exibir_player(player: dict) -> None:

    print(rgb_text("""
                                \n--------------------- Jogador ---------------------
                   """))
    print(f'''
                        {rgb_text(player['nome'])}

                {Fore.BLUE}      Level:  {player['level']}
                {Fore.RED}      Dano:  {player['dano']}
                {Fore.MAGENTA}      Saúde:  {player['hp']}
                {Fore.GREEN}      EXP:  {player['exp']}
                ''')
    print(rgb_text("""
        ---------------------------------------------------\n
                   """))



#exibe npcs
def exibir_npcs() -> None:

    print("\n" + "-" * (len(lista_npcs) * 12 + 10 ) + "\n")
    print(f"{'Nome':<8}", end="|")
    for npc in lista_npcs:
        print(f"{npc['nome']:<10}", end="|")
    print()

    print(Fore.CYAN + f"{'Level':<8}", end="|")
    for npc in lista_npcs:
        print(Fore.CYAN + f"{npc['level']:<10}", end="|")
    print()

    print(Fore.RED + f"{'Dano':<8}", end="|")
    for npc in lista_npcs:
        print(Fore.RED + f"{npc['dano']:<10}", end="|")
    print()

    print(Fore.MAGENTA + f"{'Saúde':<8}", end="|")
    for npc in lista_npcs:
        print(Fore.MAGENTA + f"{npc['hp']:<10}", end="|")
    print()

    print(Fore.GREEN + f"{'EXP':<8}", end="|")
    for npc in lista_npcs:
        print(Fore.GREEN + f"{npc['exp']:<10}", end="|")
    print()
    print("\n" + "-" * (len(lista_npcs) * 12 + 10))



#cores em rgb pro texto especial
def rgb_text(texto: str) -> str:
    resultado = ""
    comprimento = len(texto)

    for i, char in enumerate(texto):
        r = int(127 * (1 + __import__('math').sin(i * 0.3)))
        g = int(127 * (1 + __import__('math').sin(i * 0.3 + 2)))
        b = int(127 * (1 + __import__('math').sin(i * 0.3 + 4)))

        resultado += f"\033[38;2;{r};{g};{b}m{char}"
    
    resultado += "\033[0m" 
    return resultado



#fase 1 completa
def fase_1() -> None:
    print(rgb_text("""
                    |>>>                    |>>>
                    |                        |
                _  _|_  _                _  _|_  _
                | |_| |_| |              | |_| |_| |
                \  .      /              \ .    .  /
                \    ,  /                \    .  /
                    | .   |_   _   _   _   _| ,   |
                    |    .| |_| |_| |_| |_| |  .  |
                    | .   |    _______     |    . |
                    |   . |  .'       '.   |  ,   |
                    | ,   | |  PARABÉNS |  |    . |
                ___|_____| |___________|  |______|___
                /    o    o    o    o    o    o    o   \
            /_______________________________________\
            |_________________________________________|
    """))

    print(rgb_text("""
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║                PARABÉNS, GUERREIRO!                ║
    ║                                                    ║
    ║    Você conquistou a CIDADELA DO REI DE FERRO!     ║
    ║                                                    ║
    ║    Suas cinzas agora marcam sua vitória eterna.    ║
    ║                                                    ║
    ║         Prepare-se... a próxima fase é:            ║
    ║                                                    ║
    ║        ✦ CAMPOS DE BATALHA DE DRAKMOR ✦           ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """))
