import os
import shutil
import re
import time
import msvcrt
import icons as ic
from random import randint, choice, sample
from colorama import Fore, Style, init


#AUTOREST PARA COLORAMA
init(autoreset= True)


#VARIAVEIS
lista_npcs = []
escolhas_inimigo = []
escolhas_menu = ["Começar Novo Jogo", "Ultimos Recordes", "Créditos", "Sair"]
escolhas_raca = ["Esqueleto Flamejante", "Anjo Caído", "Sábio Feiticeiro", "Princesa Medusa", "Morte Mormurante", "Arqueiro Mágico"]
player = {}
habilidade = []
tamanho = shutil.get_terminal_size()
largura_tela = tamanho.columns
altura_tela = tamanho.lines


#COMPILA TODOS OS CARACTERES ESPECIAIS
ANSI = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')


#regex -------------------------------------------------------------------------------
_ANSI = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
def strip_ansi(s: str) -> str:
    return _ANSI.sub("", s or "")




#LIMPA TUDO QUE TEM NA TELA ANTES
def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear" )






#CENTRALIZA VERTICALMENTE APENAS
def centra_v(mensagem: str, cor_padrao: str = None) -> None:
    linhas = mensagem.strip('\n').split('\n')
    _, term_rows = shutil.get_terminal_size(fallback=(120, 30))
    padrao_ansi = re.compile(r'\x1b\[[0-9;]*m')
    def tem_ansi(s):
        return bool(padrao_ansi.search(s))
    altura = len(linhas)
    if altura > term_rows:
        linhas = linhas[:term_rows]
        altura = term_rows
    espaco_v = max((term_rows - altura) // 2, 0)
    print('\n' * espaco_v, end='')
    for linha in linhas:
        texto = linha
        if cor_padrao and not tem_ansi(linha):
            texto = f"{cor_padrao}{linha}\033[0m"
        print(texto)







#CENTRALIZA HORIZONTALMENTE APENAS
def centra_h(mensagem: str, cor_padrao: str = None) -> None:
    linhas = mensagem.strip('\n').split('\n')
    term_cols, _ = shutil.get_terminal_size(fallback=(120, 30))
    padrao_ansi = re.compile(r'\x1b\[[0-9;]*m')
    def sem_ansi(s):
        return padrao_ansi.sub('', s)
    def tem_ansi(s):
        return bool(padrao_ansi.search(s))
    largura = max(len(sem_ansi(l)) for l in linhas)
    espaco_h = max((term_cols - largura) // 2, 0)
    for linha in linhas:
        texto = linha
        if cor_padrao and not tem_ansi(linha):
            texto = f"{cor_padrao}{linha}\033[0m"
        print(' ' * espaco_h + texto)






#MOSTRA OS CRÉDITOS DO CRIADOR DO JOGO (EU)
def mostrar_creditos() -> None:
    from icons import creditos_img
    limpar_tela()
    centra_h_v(creditos_img(), Fore.RED)
    print("\n")
    centra_h("\nJOGO SINGLE DEVELOPER", Fore.MAGENTA + Style.BRIGHT)
    centra_h("Dev by Guilherme Barreto Ramos", Fore.WHITE + Style.BRIGHT)
    centra_h("email: guilhermebramos.dev@gmail.com",  Fore.WHITE + Style.BRIGHT)
    print("\n")
    centra_h(Style.DIM + "\nPressione qualquer tecla para voltar")
    msvcrt.getch()        





#MOSTRA OS ULTIMOS RECORDES FEITOS PELO PLAYER NO JOGO ANTERIOR
def ultimos_recordes() -> None:
    print("em criação!")
    input()






#CENTRALIZA VERTICALMENTE E HORIZONTALMENTE
def centra_h_v(mensagem: str, cor_padrao: str = None) -> None:
    linhas = mensagem.strip('\n').split('\n')
    term_cols, term_rows = shutil.get_terminal_size(fallback=(120, 30))
    padrao_ansi = re.compile(r'\x1b\[[0-9;]*m')
    def sem_ansi(s):
        return padrao_ansi.sub('', s)
    def tem_ansi(s):
        return bool(padrao_ansi.search(s))
    largura = max(len(sem_ansi(l)) for l in linhas)
    altura = len(linhas)
    if largura > term_cols:
        linhas = [l[:term_cols] for l in linhas]
        largura = term_cols
    if altura > term_rows:
        linhas = linhas[:term_rows]
        altura = term_rows
    espaco_h = max((term_cols - largura) // 2, 0)
    espaco_v = max((term_rows - altura - 15) // 2, 0)
    print('\n' * espaco_v, end='')
    for linha in linhas:
        texto = linha
        if cor_padrao and not tem_ansi(linha):
            texto = f"{cor_padrao}{linha}\033[0m"
        print(' ' * espaco_h + texto)






#CRIA MULTIPLOS INIMIGOS BASEADO EM ORDAS E NAS FASES
def criar_inimigos(fase: int, orda: int, player: dict) -> None:

    match fase:
        
        #FASE 1
        case 1:
            #ORDA DE MONSTROS 1
            if orda == 1:
                while True:
                    for x in range(1):
                        nivel = randint(1, 1)
                        novo_npc = criar_npc(nivel, fase)
                        lista_npcs.append(novo_npc)
                        escolhas_inimigo.append(novo_npc['nome'] + " " + novo_npc['sexo'])
                    break

            #ORDA DE MONSTROS 2
            if orda == 2:
                while True:
                    for x in range(2):
                        nivel = randint(1, 3)
                        novo_npc = criar_npc(nivel, fase)
                        lista_npcs.append(novo_npc)
                        escolhas_inimigo.append(novo_npc['nome'] + " " + novo_npc['sexo'])
                    break

            #ORDA DE MONSTROS 3
            if orda == 3:
                while True:
                    for x in range(4):
                        nivel = randint(2, 5)
                        novo_npc = criar_npc(nivel, fase)
                        lista_npcs.append(novo_npc)
                        escolhas_inimigo.append(novo_npc['nome'] + " " + novo_npc['sexo'])

                    if lista_npcs[0]['nome'] == lista_npcs[2]['nome'] or lista_npcs[1]['nome'] == lista_npcs[3]['nome']:
                        lista_npcs.clear()
                        escolhas_inimigo.clear()
                        continue
                    else:
                        break

        case 2:
            for x in range(7):
                level = randint(21, 40)
                novo_npc = criar_npc(level,fase)
                lista_npcs.append(novo_npc)
            exibir_player(player)
            print(Fore.GREEN + "CAMPOS DE BATALHA DE DRAKMOR\n")


            #ORDA DE INIMIGOS 2
            if orda == 2:
                while True:
                    for x in range(5):
                        nivel = randint(4, 10)
                        novo_npc = criar_npc(nivel, fase)
                        lista_npcs.append(novo_npc)
                        escolhas_inimigo.append(novo_npc['nome'] + " " + novo_npc['sexo'])

                    if lista_npcs[0]['nome'] == lista_npcs[1 or 2]['nome'] or lista_npcs[3]['nome'] == lista_npcs[4]['nome']:
                        lista_npcs.clear()
                        escolhas_inimigo.clear()
                        continue
                    else: 
                        break
            

            #ORDA DE INIMIGOS 3
            if orda == 3:
                while True:
                    for x in range(5):
                        nivel = randint(8, 15)
                        novo_npc = criar_npc(nivel, fase)
                        lista_npcs.append(novo_npc)
                        escolhas_inimigo.append(novo_npc['nome'] + " " + novo_npc['sexo'])

                    if lista_npcs[0]['nome'] == lista_npcs[2]['nome'] or lista_npcs[1]['nome'] == lista_npcs[3]['nome']:
                        lista_npcs.clear()
                        escolhas_inimigo.clear()
                        continue
                    else: 
                        break
    
        case 3:
            for x in range(7):
                level = randint(41, 60)
                novo_npc = criar_npc(level, fase)
                lista_npcs.append(novo_npc)
            exibir_player(player)
            print(Fore.CYAN + "FLORESTA DE NÉVOA ETERNA\n")

        case 4:
            for x in range(7):
                level = randint(61, 80)
                novo_npc = criar_npc(level, fase)
                lista_npcs.append(novo_npc)
            exibir_player(player)
            print(Fore.RED + "COVIL DO DRAGÃO ESCARLATE\n")

        case 5:
            for x in range(7):
                level = randint(81, 100)
                novo_npc = criar_npc(level, fase)
                lista_npcs.append(novo_npc)
            exibir_player(player)
            print(Fore.MAGENTA + "FORTALEZA DAS SOMBRAS ANTIGAS\n")







#GERA OS STATUS DO PLAYER (NOME, RAÇA, ETC...)
def criar_personagem(nome: str,raca: int) -> dict: 

    level = 1
    hp_normal = 90 + level * 18
    dano_normal = 6 + level * 2.1
    habilidade = None

    match raca:
        case 1:
            raca = "Esqueleto Flamejante"
            hp = hp_normal * 0.8
            dano = dano_normal * 1.3
            sorte = 0.2
            habilidade = "CHAMAS INFERNAIS"
        
        case 2:
            raca = "Anjo caído"
            hp = hp_normal
            dano = dano_normal * 1.3
            sorte = 0.1
            habilidade = "CEIFEIRO"
        
        case 3:
            raca = "Sábio Feiticeiro"
            hp = hp_normal
            dano = dano_normal * 0.75
            sorte = 0.35
            habilidade = "FEITIÇOS ELEMENTAIS"
        
        case 4: 
            raca = "Pricesa Medusa"
            hp = hp_normal * 1.4
            dano = dano_normal 
            sorte = 0.10
            habilidade = "ENCANTO DE PEDRA"
        
        case 5:
            raca = "Morte Mormurante"
            hp = hp_normal 
            dano = dano_normal * 1.3
            sorte = 0.10
            habilidade = "ILUSÃO"
        
        case 6:
            raca = "Arqueiro Mágico"
            hp = hp_normal * 0.8
            dano = dano_normal 
            sorte = 0.35
            habilidade = "FLECHA MÁGICA"

    return {
        "nome": nome,
        "raca": raca,
        "level": int(level),
        "exp": 0,
        "xp_next": xp_para_upar(int(level)),
        "hp": int(hp),
        "hp_max": int(hp),
        "dano": int(dano),
        "hp_base": int(hp),
        "dano_base": int(dano),
        "sorte": sorte,
        "habilidade": habilidade
    }   









#DECIDE O NOME DO INIMIGO BASEADO NO LEVEL, E NA FASE QUE SE ENCONTRA E NO FINAL RETORNA TODOS OS STATUS DO INIMIGO EM DICT
def criar_npc(level, fase) -> dict:

    if fase == 1:

        if level >= 1 and level <= 5:
            if level <= 2:
                nome = "dominus".upper()
            else:
                nome = "draconis".upper()

        elif level >= 6 and level <= 10:
            if level <= 8:
                nome = "carceres".upper()
            else:
                nome = "mytus".upper()

        elif level >= 11 and level <= 15:
            if level <= 13:
                nome = "wetiza".upper()
            else:
                nome = "ogroid".upper()

        elif level >= 16 and level <= 20:
            if level <= 18:
                nome = "akari".upper()
            else:
                nome = "tarik".upper()

    if fase == 2:

        if level >= 21 and level <= 25:
            if level <= 23:
                nome = "".upper()
            else:
                nome = "magma".upper()

        elif level >= 26 and level <= 30:
            if level <= 28:
                nome = "".upper()
            else:
                nome = "".upper()

        elif level >= 31 and level <= 35:
            if level <= 33:
                nome = "wertz".upper()
            else:
                nome = "quantinum".upper()

        elif level >= 36 and level <= 40:
            if level <= 38:
                nome = "fraskra".upper()
            else:
                nome = "hydra".upper()

    if fase == 3:

        if level >= 41 and level <= 45:
            if level <= 43:
                nome = Fore.GREEN + "".upper()
            else:
                nome = Fore.BLUE + "".upper()

        elif level >= 46 and level <= 50:
            if level <= 48:
                nome = Fore.YELLOW + "".upper()
            else:
                nome = Fore.RED + "".upper()

        elif level >= 51 and level <= 55:
            if level <= 53:
                nome = Fore.YELLOW + "".upper()
            else:
                nome = Fore.RED + "".upper()

        elif level >= 56 and level <= 60:
            if level <= 58:
                nome = Fore.YELLOW + "".upper()
            else:
                nome = Fore.RED + "".upper()

    if fase == 4:

        if level >= 41 and level <= 45:
            if level <= 43:
                nome = Fore.GREEN + "".upper()
            else:
                nome = Fore.BLUE + "".upper()

        elif level >= 46 and level <= 50:
            if level <= 48:
                nome = Fore.YELLOW + "".upper()
            else:
                nome = Fore.RED + "".upper()

        elif level >= 51 and level <= 55:
            if level <= 53:
                nome = Fore.YELLOW + "".upper()
            else:
                nome = Fore.RED + "".upper()

        elif level >= 56 and level <= 60:
            if level <= 58:
                nome = Fore.YELLOW + "".upper()
            else:
                nome = Fore.RED + "".upper()

    if fase == 5:

        if level >= 41 and level <= 45:
            if level <= 43:
                nome = Fore.GREEN + "toon".upper()
            else:
                nome = Fore.BLUE + "tartarus".upper()

        elif level >= 46 and level <= 50:
            if level <= 48:
                nome = Fore.YELLOW + "endless".upper()
            else:
                nome = Fore.RED + "foguinho".upper()

        elif level >= 51 and level <= 55:
            if level <= 53:
                nome = Fore.YELLOW + "endless".upper()
            else:
                nome = Fore.RED + "foguinho".upper()

        elif level >= 56 and level <= 60:
            if level <= 58:
                nome = Fore.YELLOW + "endless".upper()
            else:
                nome = Fore.RED + "foguinho".upper()

    sexo = randint(1,2)
    if sexo == 1:
        sexo = "Macho"
    else:
        sexo = "Femea"

    novo_npc = {
        "nome": nome,
        "sexo": sexo,
        "level": level,
        "dano": int(3 * level),
        "hp": int(40 * level),
        "exp": int(12 * (level ** 1.35)),
        "cor": choice([
            "\033[31m", "\033[32m", "\033[33m",
            "\033[34m", "\033[35m", "\033[36m",
            "\033[91m", "\033[92m", "\033[94m"
        ])
    }

    return novo_npc
        





#EXIBE O PERFIL ATUAL DO JOGADOR (NOME, NIVEL, VIDA, DANO, ETC...)
def exibir_player(player: dict) -> None:
    nome = player['nome']
    raca = player['raca']
    level = player['level']
    exp = player['exp']
    xp_next = player.get('xp_next', 0)
    vida = player['hp']
    dano = player['dano']
    sorte = player['sorte']
    habilidade = player['habilidade'] 

    if sorte <= 0.15 and sorte >= 0:
        sorte = "Baixa"
    elif sorte >= 0.2 and sorte <= 0.29:
        sorte = "Normal"
    elif sorte >= 0.3:
        sorte = "Acima"

    largura = 21 

    status = (
        "  ╔" + "═" * 34 + "╗\n"
        "  ║         STATUS DO JOGADOR        ║\n"
        "  ╠" + "═" * 34 + "╣\n"
        f"  ║    Nome   : {str(nome).ljust(largura)}║\n"
        f"  ║    Raça   : {str(raca).ljust(largura)}║\n"
        f"  ║    Level  : {str(level).ljust(largura)}║\n"
        f"  ║     EXP   : {str(exp).ljust(largura)}║\n"
        f"  ║  PróxLvl  : {str(xp_next).ljust(largura)}║\n"
        f"  ║ XP Barra  : {barra_xp(exp, xp_next).ljust(largura)}║\n"
        "  ╠" + "═" * 34 + "╣\n"
        f"  ║      HP   : {str(vida).ljust(largura)}║\n"
        f"  ║     Dano  : {str(dano).ljust(largura)}║\n"
        f"  ║    Sorte  : {str(sorte).ljust(largura)}║\n"
        f"  ║ Habilidade: {str(habilidade).ljust(largura)}║\n"
        "  ╚" + "═" * 34 + "╝\n"
    )


    centra_h(rgb_text(status))







#RETORNA A ESCOLHA DE RAÇA DO PLAYER 
def escolha_seta_raca() -> str:
    idx = 0
    while True:
        imagem_seta_escolhida_raca(idx)
        print("\n")
        centra_h("\nPARAÍSO MEDIEVAL", Fore.YELLOW + Style.BRIGHT)
        centra_h(Style.DIM + "use ↑/↓ para navegar e ENTER para confirmar")

        largura_interna = 56
        
        centra_h(Fore.CYAN + "╔" + "═" * largura_interna + "╗")

        for i, esc in enumerate(escolhas_raca):
            selecionado = (i == idx)
            seta = "➤" if selecionado else " "
            cor = Fore.GREEN + Style.BRIGHT if selecionado else Fore.WHITE
            conteudo = f"{seta} {esc}"
            largura_visivel = len(strip_ansi(conteudo))
            espaco = max(largura_interna - largura_visivel, 0)
            linha_final = (
                Fore.CYAN + "║ "
                + cor + conteudo + Style.RESET_ALL
                + " " * espaco
                + Fore.CYAN + " ║"
            )
            centra_h(linha_final)

        centra_h(Fore.CYAN + "╚" + "═" * largura_interna + "╝")      

        ch = msvcrt.getch()
        if ch in (b"\x00", b"\xe0"):
            ch2 = msvcrt.getch()
            if ch2 == b"H":
                idx = (idx - 1) % len(escolhas_raca)
            elif ch2 == b"P":
                idx = (idx + 1) % len(escolhas_raca)
        elif ch in (b"\r", b"\n"):
            escolha = escolhas_raca[idx]
            return escolha
        elif ch in (b"1", b"2", b"3", b"4"):
            n = int(ch.decode()) - 1
            if 0 <= n < len(escolhas_raca):
                escolha = escolhas_raca[n]
                return escolha
        else:
            time.sleep(0.00000000000000000000000000001)






#EXIBE A IMAGEM/DESCRIÇÃO DE ACORDO COM A SETA INDICADORA NA TELA DE ESCOLHA DA RAÇAS
def imagem_seta_escolhida_raca(idx) -> None:
    from icons import esqueleto_flamejante, anjo_caido, sabio_feiticeiro, pricesa_medusa, morte_mormurante, arqueiro_magico
    if idx == 0:
        esqueleto_flamejante()
    
    elif idx == 1:
        anjo_caido()

    elif idx == 2:
        sabio_feiticeiro()

    elif idx == 3:
        pricesa_medusa()

    elif idx == 4:
        morte_mormurante()

    elif idx == 5:
        arqueiro_magico()






#RETORNA A ESCOLHA FEITA PELO PLAYER DO MENU DA TELA INICIAL
def escolha_seta_menu() -> str:
    from icons import design_tela_inicio
    idx = 0
    while True:
        design_tela_inicio(idx)
        centra_h("\n\nPARAÍSO MEDIEVAL", Fore.YELLOW + Style.BRIGHT)
        centra_h(Style.DIM + "use ↑/↓ para navegar e ENTER para confirmar")

        largura_interna = 56
        centra_h(Fore.CYAN + "╔" + "═" * largura_interna + "╗")

        for i, esc in enumerate(escolhas_menu):
            selecionado = (i == idx)
            seta = "➤" if selecionado else " "
            cor = Fore.GREEN + Style.BRIGHT if selecionado else Fore.WHITE
            conteudo = f"{seta} {esc}"
            largura_visivel = len(strip_ansi(conteudo))
            espaco = max(largura_interna - largura_visivel, 0)
            linha_final = (
                Fore.CYAN + "║ "
                + cor + conteudo + Style.RESET_ALL
                + " " * espaco
                + Fore.CYAN + " ║"
            )
            centra_h(linha_final)

        centra_h(Fore.CYAN + "╚" + "═" * largura_interna + "╝")

        ch = msvcrt.getch()
        if ch in (b"\x00", b"\xe0"):
            ch2 = msvcrt.getch()
            if ch2 == b"H":
                idx = (idx - 1) % len(escolhas_menu)
            elif ch2 == b"P":
                idx = (idx + 1) % len(escolhas_menu)
        elif ch in (b"\r", b"\n"):
            escolha = escolhas_menu[idx]
            return escolha
        elif ch in (b"1", b"2", b"3", b"4"):
            n = int(ch.decode()) - 1
            if 0 <= n < len(escolhas_menu):
                escolha = escolhas_menu[n]
                return escolha
        else:
            time.sleep(0.00000000000000000000000000001)






#RETORNA A ESCOLHA DO INIMIGO SELECIONADO
def escolha_seta_inimigo_fase1(player, orda) -> int | None:
    def strip_ansi(s: str) -> str:
        return _ANSI.sub("", s or "")

    idx = 0
    sorte = player['sorte'] * 100
    mostrar_poder = (randint(1, 100) <= sorte) 

    while True:
        if not escolhas_inimigo:
            return None

        img = imagem_seta_escolhida_inimigo_fase1(idx)
        extra = exibe_status_monstro(idx)

        limpar_tela()
        descri_monstro_mais_img(img, "\n".join(extra))
        print("\n")
        centra_h("\nQUE INIMIGO DESEJA ATACAR?", Fore.RED + Style.BRIGHT)
        centra_h(Style.DIM + "use ↑/↓ para navegar e ENTER para confirmar")

        largura_interna = 35
        centra_h(Fore.CYAN + "╔" + "═" * largura_interna + "╗")

        for i, esc in enumerate(escolhas_inimigo):
            selecionado = (i == idx)
            seta = "➤" if selecionado else " "
            cor = Fore.RED + Style.BRIGHT if selecionado else Fore.WHITE

            nome = esc.split()[0]
            sexo = esc.split()[-1]
            coresc = (
                Fore.BLUE + sexo if sexo == "Macho"
                else Fore.MAGENTA + sexo
            ) + Style.RESET_ALL

            conteudo = f"{seta} {nome} {coresc}"
            largura_visivel = len(strip_ansi(conteudo))
            espaco = max(largura_interna - largura_visivel, 0)

            linha_final = (
                Fore.CYAN + "║ "
                + cor + conteudo + Style.RESET_ALL
                + " " * espaco
                + Fore.CYAN + " ║"
            )
            centra_h(linha_final)

        centra_h(Fore.CYAN + "╚" + "═" * largura_interna + "╝")

        if mostrar_poder and orda >= 2:
            centra_h(rgb_text(caixa_poder_heroi(player)))

        ch = msvcrt.getch()

        if ch in (b"\x00", b"\xe0"):
            ch2 = msvcrt.getch()
            if ch2 == b"H":
                idx = (idx - 1) % len(escolhas_inimigo)
            elif ch2 == b"P":
                idx = (idx + 1) % len(escolhas_inimigo)

        elif ch in (b"\r", b"\n"):
            return idx  

        elif mostrar_poder and ch in (b"p", b"P"):
            atacar_monstro_habilidade(player, idx)
            print("\n")
            input()
            return None

        elif ch in (b"1", b"2", b"3", b"4", b"5"):
            n = int(ch.decode()) - 1
            if 0 <= n < len(escolhas_inimigo):
                return n









#EXIBE A IMAGEM DO INIMIGO QUE ESTA SENDO SELECIONADO (FASE 1)
def imagem_seta_escolhida_inimigo_fase1(idx: int) -> str:
    from icons import dominus_img, draconis_img, carceres_img, mytus_img, wetiza_img, akari_img, ogroid_img, tarik_img
    imgs = {
        "DOMINUS": dominus_img,
        "DRACONIS": draconis_img,
        "CARCERES": carceres_img,
        "MYTUS": mytus_img,
        "WETIZA": wetiza_img,
        "AKARI": akari_img,
        "OGROID": ogroid_img,
        "TARIK": tarik_img,
    }

    if not escolhas_inimigo:
        return ""

    if idx < 0 or idx >= len(escolhas_inimigo):
        return ""

    nome = escolhas_inimigo[idx].split()[0]

    img = imgs.get(nome)
    if not img:
        return ""

    img_str = img()
    npc = lista_npcs[idx]
    img_str = aplicar_cor_monstro(img_str, npc["cor"])
    return img_str







#DESCRICAO COM STATUS DO NPC SELECIONADO
def exibe_status_monstro(idx: int) -> list[str]:
    nome = lista_npcs[idx]['nome']
    sexo = lista_npcs[idx]['sexo']
    level = lista_npcs[idx]['level']
    exp = lista_npcs[idx]['exp']
    vida = lista_npcs[idx]['hp']
    dano = lista_npcs[idx]['dano']

    largura = 21

    status = (
        "  ╔" + "═" * 34 + "╗\n"
        "  ║         STATUS DO INIMIGO        ║\n"
        "  ╠" + "═" * 34 + "╣\n"
        f"  ║    Nome   : {str(nome).ljust(largura)}║\n"
        f"  ║    Sexo   : {str(sexo).ljust(largura)}║\n"
        f"  ║    Level  : {str(level).ljust(largura)}║\n"
        f"  ║     EXP   : {str(exp).ljust(largura)}║\n"
        "  ╠" + "═" * 34 + "╣\n"
        f"  ║    Saúde  : {str(vida).ljust(largura)}║\n"
        f"  ║     Dano  : {str(dano).ljust(largura)}║\n"
        "  ╚" + "═" * 34 + "╝\n"
    )

    linhas = status.split("\n")

    linhas_rgb = [rgb_text(l) for l in linhas if l]

    return linhas_rgb







#CAIXA COM O PODER DO HEROI, DEPENDENDO DE QUAL RACA ELE ESCOLHE
def caixa_poder_heroi(player: dict) -> str:
    titulo = "PODER DO HERÓI DISPONÍVEL"
    habilidade = str(player["habilidade"])

    largura_interna = 34 

    dica = 'clique em "P" para usar'
    dica_linha = dica[:largura_interna]
    hab_linha = habilidade[:largura_interna]

    caixa = (
        "  ╔" + "═" * largura_interna + "╗\n"
        f" ║ {titulo.center(largura_interna)} ║\n"
        "  ╠" + "═" * largura_interna + "╣\n"
        f" ║ {dica_linha.center(largura_interna)} ║\n"
        f" ║ {hab_linha.center(largura_interna)} ║\n"
        "  ╚" + "═" * largura_interna + "╝\n"
    )
    return caixa







#USA A HABILIDADE DO PLAYER PARA ATACAR MONSTROS
def atacar_monstro_habilidade(player: dict, idx: int) -> None:
    import time
    from icons import (
        esqueleto_flamejante_especial,
        anjo_caido_especial,
        sabio_feiticeiro_especial,
        pricesa_medusa_especial,
        arqueiro_magico_especial,
        morte_mormurante_especial
    )

    habilidade = player['habilidade']
    hp = lista_npcs[idx]['hp']
    nome = lista_npcs[idx]['nome']

    # HABILIDADE ESQUELETO FLAMEJANTE
    if habilidade == "CHAMAS INFERNAIS" and len(lista_npcs) > 0:

        player['dano por fogo'] = int(player['dano'] * 0.8)
        for npc in lista_npcs:
            npc['hp'] -= player['dano por fogo']

        img = esqueleto_flamejante_especial()
        linhas_img = img.splitlines()

        for i, linha in enumerate(linhas_img):
            linhas_img[i] = Fore.RED + linha + Style.RESET_ALL

        linhas_texto = []
        largura_barra = 54
        linhas_texto.append(
            Fore.RED + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
        )
        linhas_texto.append(
            Fore.YELLOW + Style.BRIGHT + "          H A B I L I D A D E   A T I V A D A          " + Style.RESET_ALL
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + f"{player['nome']}" + Style.RESET_ALL
            + Fore.WHITE + Style.BRIGHT + " invocou " + Style.RESET_ALL
            + Fore.RED + Style.BRIGHT + f"{player['habilidade']}" + Style.RESET_ALL
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + "Dano em área: " + Style.RESET_ALL
            + Fore.RED + Style.BRIGHT + f"{int(player['dano por fogo'])}" + Style.RESET_ALL
            + Fore.WHITE + Style.BRIGHT + " (Fogo)" + Style.RESET_ALL
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.CYAN + Style.BRIGHT + "Alvos atingidos:" + Style.RESET_ALL
        )
        for npc in lista_npcs:
            linhas_texto.append(Fore.WHITE + Style.BRIGHT + f"• {npc['nome']}" + Style.RESET_ALL)

        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.RED + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
        )

        largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

        for i, linha in enumerate(linhas_texto, start=7):
            visivel = strip_ansi(linha)
            espaco_esq = (largura_bloco - len(visivel)) // 2
            linha_centro = " " * espaco_esq + linha
            linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

        img_final = "\n".join(linhas_img)
        centra_h_v(img_final)

        indices_mortos = []
        mortes = []

        for i, npc in enumerate(lista_npcs):
            if int(npc["hp"]) <= 0:
                npc["hp"] = 0
                indices_mortos.append(i)

        if not indices_mortos:
            centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
        else:
            centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            input(" ")

        for i in indices_mortos:
            npc = lista_npcs[i]
            xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
            player['exp'] = int(player.get('exp', 0)) + xp_ganho
            verificar_level_up(player)
            normalizar_stats(player)

            img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
            mortes.append((img_monstro, npc['nome'], xp_ganho))

        for i in reversed(indices_mortos):
            del lista_npcs[i]
            del escolhas_inimigo[i]

        for img_monstro, nome_monstro, xp_ganho in mortes:
            mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

    # HABILIDADE ANJO CAÍDO
    elif habilidade == "CEIFEIRO" and len(lista_npcs) > 0:

        lista_npcs[idx]['hp'] -= player['dano']
        player['vida ceifada'] = int(int(player['dano']) * 0.6)
        player['hp'] = int(player['hp']) + int(player['vida ceifada'])
        if 'hp_max' in player:
            player['hp'] = min(int(player['hp']), int(player['hp_max']))

        img = anjo_caido_especial()
        linhas_img = img.splitlines()

        for i, linha in enumerate(linhas_img):
            linhas_img[i] = Fore.BLACK + linha + Style.RESET_ALL

        linhas_texto = []
        largura_barra = 54
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
        )
        linhas_texto.append(
            Fore.MAGENTA + Style.BRIGHT + "              G O L P E   D A   F O I C E              " + Style.RESET_ALL
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + f"{player['nome']}" + Style.RESET_ALL
            + Fore.WHITE + Style.BRIGHT + " usou " + Style.RESET_ALL
            + Fore.MAGENTA + Style.BRIGHT + f"{player['habilidade']}" + Style.RESET_ALL
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
            + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
        )
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + "Dano causado: " + Style.RESET_ALL
            + Fore.RED + Style.BRIGHT + f"{int(player['dano'])}" + Style.RESET_ALL
        )
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + "Vida ceifada: " + Style.RESET_ALL
            + Fore.GREEN + Style.BRIGHT + f"+{int(player['vida ceifada'])}" + Style.RESET_ALL
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
        )

        largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

        for i, linha in enumerate(linhas_texto, start=17):
            visivel = strip_ansi(linha)
            espaco_esq = (largura_bloco - len(visivel)) // 2
            linha_centro = " " * espaco_esq + linha
            linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

        img_final = "\n".join(linhas_img)
        centra_h_v(img_final)

        indices_mortos = []
        mortes = []

        for i, npc in enumerate(lista_npcs):
            if int(npc["hp"]) <= 0:
                npc["hp"] = 0
                indices_mortos.append(i)

        if not indices_mortos:
            centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
        else:
            centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            input(" ")

        for i in indices_mortos:
            npc = lista_npcs[i]
            xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
            player['exp'] = int(player.get('exp', 0)) + xp_ganho
            verificar_level_up(player)
            normalizar_stats(player)

            img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
            mortes.append((img_monstro, npc['nome'], xp_ganho))

        for i in reversed(indices_mortos):
            del lista_npcs[i]
            del escolhas_inimigo[i]

        for img_monstro, nome_monstro, xp_ganho in mortes:
            mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

    # HABILIDADE SÁBIO FEITICEIRO
    elif habilidade == "FEITIÇOS ELEMENTAIS" and len(lista_npcs) > 0:
        poderes = ["Tsunami", "Terremoto", "Tornado", "Vinhas"]
        poder_escolhido = choice(poderes)

        # ---------------- TSUNAMI ----------------
        if poder_escolhido == "Tsunami":
            player['dano por tsunami'] = int(player["dano"] * 1.5)
            lista_npcs[idx]['hp'] -= player['dano por tsunami']
            lista_npcs[idx]['dano'] = int(lista_npcs[idx]['dano'] * 0.85)

            img = sabio_feiticeiro_especial()
            linhas_img = img.splitlines()

            for i, linha in enumerate(linhas_img):
                linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

            linhas_texto = []
            largura_barra = 54
            linhas_texto.append(
                Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.CYAN + Style.BRIGHT + "                 F E I T I Ç O   A T I V O              " + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + f"{player['nome']}" + Style.RESET_ALL
                + Fore.WHITE + Style.BRIGHT + " conjurou " + Style.RESET_ALL
                + Fore.CYAN + Style.BRIGHT + f"{player['habilidade']}" + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.CYAN + Style.BRIGHT + "Elemento: " + Style.RESET_ALL
                + Fore.BLUE + Style.BRIGHT + "Água (Tsunami)" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Dano causado: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{int(player['dano por tsunami'])}" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Efeito: " + Style.RESET_ALL
                + Fore.YELLOW + Style.BRIGHT + "-15% ataque do inimigo" + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )

            largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

            for i, linha in enumerate(linhas_texto, start=17):
                visivel = strip_ansi(linha)
                espaco_esq = (largura_bloco - len(visivel)) // 2
                linha_centro = " " * espaco_esq + linha
                linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

            img_final = "\n".join(linhas_img)
            centra_h_v(img_final)

            indices_mortos = []
            mortes = []

            for i, npc in enumerate(lista_npcs):
                if int(npc["hp"]) <= 0:
                    npc["hp"] = 0
                    indices_mortos.append(i)

            if not indices_mortos:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            else:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                input(" ")

            for i in indices_mortos:
                npc = lista_npcs[i]
                xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                player['exp'] = int(player.get('exp', 0)) + xp_ganho
                verificar_level_up(player)
                normalizar_stats(player)

                img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                mortes.append((img_monstro, npc['nome'], xp_ganho))

            for i in reversed(indices_mortos):
                del lista_npcs[i]
                del escolhas_inimigo[i]

            for img_monstro, nome_monstro, xp_ganho in mortes:
                mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

        # ---------------- TERREMOTO ----------------
        elif poder_escolhido == "Terremoto":
            sorte = randint(1, 3)

            if sorte == 2:
                player['dano por terremoto'] = int(lista_npcs[idx]['hp'] * 0.7)
                lista_npcs[idx]['hp'] -= player['dano por terremoto']

                img = sabio_feiticeiro_especial()
                linhas_img = img.splitlines()

                for i, linha in enumerate(linhas_img):
                    linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

                linhas_texto = []
                largura_barra = 54
                linhas_texto.append(
                    Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.YELLOW + Style.BRIGHT + "                 T E R R E M O T O   C R Í T I C O       " + Style.RESET_ALL
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "A terra se abriu sob os pés do inimigo!" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
                    + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Dano causado: " + Style.RESET_ALL
                    + Fore.RED + Style.BRIGHT + f"{int(player['dano por terremoto'])}" + Style.RESET_ALL
                    + Fore.WHITE + Style.BRIGHT + " (70% da vida)" + Style.RESET_ALL
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
                )

                largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

                for i, linha in enumerate(linhas_texto, start=17):
                    visivel = strip_ansi(linha)
                    espaco_esq = (largura_bloco - len(visivel)) // 2
                    linha_centro = " " * espaco_esq + linha
                    linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

                img_final = "\n".join(linhas_img)
                centra_h_v(img_final)

                indices_mortos = []
                mortes = []

                for i, npc in enumerate(lista_npcs):
                    if int(npc["hp"]) <= 0:
                        npc["hp"] = 0
                        indices_mortos.append(i)

                if not indices_mortos:
                    centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                else:
                    centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                    input(" ")

                for i in indices_mortos:
                    npc = lista_npcs[i]
                    xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                    player['exp'] = int(player.get('exp', 0)) + xp_ganho
                    verificar_level_up(player)
                    normalizar_stats(player)

                    img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                    mortes.append((img_monstro, npc['nome'], xp_ganho))

                for i in reversed(indices_mortos):
                    del lista_npcs[i]
                    del escolhas_inimigo[i]

                for img_monstro, nome_monstro, xp_ganho in mortes:
                    mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

            else:
                lista_npcs[idx]['hp'] -= int(player['dano'] * 0.5)

                img = sabio_feiticeiro_especial()
                linhas_img = img.splitlines()

                for i, linha in enumerate(linhas_img):
                    linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

                linhas_texto = []
                largura_barra = 54
                linhas_texto.append(
                    Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.YELLOW + Style.BRIGHT + "                   T E R R E M O T O                     " + Style.RESET_ALL
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "A criatura escapou do pior por pouco..." + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
                    + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Dano causado: " + Style.RESET_ALL
                    + Fore.RED + Style.BRIGHT + f"{int(player['dano'] * 0.5)}" + Style.RESET_ALL
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
                )

                largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

                for i, linha in enumerate(linhas_texto, start=17):
                    visivel = strip_ansi(linha)
                    espaco_esq = (largura_bloco - len(visivel)) // 2
                    linha_centro = " " * espaco_esq + linha
                    linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

                img_final = "\n".join(linhas_img)
                centra_h_v(img_final)

                indices_mortos = []
                mortes = []

                for i, npc in enumerate(lista_npcs):
                    if int(npc["hp"]) <= 0:
                        npc["hp"] = 0
                        indices_mortos.append(i)

                if not indices_mortos:
                    centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                else:
                    centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                    input(" ")

                for i in indices_mortos:
                    npc = lista_npcs[i]
                    xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                    player['exp'] = int(player.get('exp', 0)) + xp_ganho
                    verificar_level_up(player)
                    normalizar_stats(player)

                    img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                    mortes.append((img_monstro, npc['nome'], xp_ganho))

                for i in reversed(indices_mortos):
                    del lista_npcs[i]
                    del escolhas_inimigo[i]

                for img_monstro, nome_monstro, xp_ganho in mortes:
                    mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

        # ---------------- TORNADO ----------------
        elif poder_escolhido == "Tornado":

            multiplicador = randint(2, 3)
            player['dano por tornado'] = player['dano'] * multiplicador
            lista_npcs[idx]['hp'] -= player['dano por tornado']

            img = sabio_feiticeiro_especial()
            linhas_img = img.splitlines()

            for i, linha in enumerate(linhas_img):
                linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

            linhas_texto = []
            largura_barra = 54
            linhas_texto.append(
                Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.CYAN + Style.BRIGHT + "                     T O R N A D O                      " + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Ventos violentos rasgam o campo de batalha!" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Dano causado: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{int(player['dano por tornado'])}" + Style.RESET_ALL
                + Fore.WHITE + Style.BRIGHT + f" (x{multiplicador})" + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )

            largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

            for i, linha in enumerate(linhas_texto, start=17):
                visivel = strip_ansi(linha)
                espaco_esq = (largura_bloco - len(visivel)) // 2
                linha_centro = " " * espaco_esq + linha
                linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

            img_final = "\n".join(linhas_img)
            centra_h_v(img_final)

            indices_mortos = []
            mortes = []

            for i, npc in enumerate(lista_npcs):
                if int(npc["hp"]) <= 0:
                    npc["hp"] = 0
                    indices_mortos.append(i)

            if not indices_mortos:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            else:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                input(" ")

            for i in indices_mortos:
                npc = lista_npcs[i]
                xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                player['exp'] = int(player.get('exp', 0)) + xp_ganho
                verificar_level_up(player)
                normalizar_stats(player)

                img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                mortes.append((img_monstro, npc['nome'], xp_ganho))

            for i in reversed(indices_mortos):
                del lista_npcs[i]
                del escolhas_inimigo[i]

            for img_monstro, nome_monstro, xp_ganho in mortes:
                mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

        # ---------------- VINHAS ----------------
        elif poder_escolhido == "Vinhas":

            sorte = randint(1, 3)
            if sorte == 2:
                multiplicador = min(len(lista_npcs), 3)
                player['dano por vinhas'] = player['dano'] * multiplicador * 2
                lista_npcs[idx]['hp'] -= player['dano por vinhas']

                img = sabio_feiticeiro_especial()
                linhas_img = img.splitlines()

                for i, linha in enumerate(linhas_img):
                    linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

                linhas_texto = []
                largura_barra = 54
                linhas_texto.append(
                    Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.GREEN + Style.BRIGHT + "                       V I N H A S                      " + Style.RESET_ALL
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Vinhas espinhosas prendem o inimigo com força!" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
                    + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Dano causado: " + Style.RESET_ALL
                    + Fore.RED + Style.BRIGHT + f"{int(player['dano por vinhas'])}" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Bônus: " + Style.RESET_ALL
                    + Fore.YELLOW + Style.BRIGHT + "escala com inimigos na arena" + Style.RESET_ALL
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
                )

                largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

                for i, linha in enumerate(linhas_texto, start=17):
                    visivel = strip_ansi(linha)
                    espaco_esq = (largura_bloco - len(visivel)) // 2
                    linha_centro = " " * espaco_esq + linha
                    linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

                img_final = "\n".join(linhas_img)
                centra_h_v(img_final)

                indices_mortos = []
                mortes = []

                for i, npc in enumerate(lista_npcs):
                    if int(npc["hp"]) <= 0:
                        npc["hp"] = 0
                        indices_mortos.append(i)

                if not indices_mortos:
                    centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                else:
                    centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                    input(" ")

                for i in indices_mortos:
                    npc = lista_npcs[i]
                    xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                    player['exp'] = int(player.get('exp', 0)) + xp_ganho
                    verificar_level_up(player)
                    normalizar_stats(player)

                    img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                    mortes.append((img_monstro, npc['nome'], xp_ganho))

                for i in reversed(indices_mortos):
                    del lista_npcs[i]
                    del escolhas_inimigo[i]

                for img_monstro, nome_monstro, xp_ganho in mortes:
                    mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

            else:
                lista_npcs[idx]['hp'] -= player['dano']

                img = sabio_feiticeiro_especial()
                linhas_img = img.splitlines()

                for i, linha in enumerate(linhas_img):
                    linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

                linhas_texto = []
                largura_barra = 54
                linhas_texto.append(
                    Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.GREEN + Style.BRIGHT + "                       V I N H A S                      " + Style.RESET_ALL
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "A conjuração saiu torta... mas ainda atingiu!" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
                    + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
                )
                linhas_texto.append(
                    Fore.WHITE + Style.BRIGHT + "Dano causado: " + Style.RESET_ALL
                    + Fore.RED + Style.BRIGHT + f"{int(player['dano'])}" + Style.RESET_ALL
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    Fore.BLUE + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
                )

                largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

                for i, linha in enumerate(linhas_texto, start=17):
                    visivel = strip_ansi(linha)
                    espaco_esq = (largura_bloco - len(visivel)) // 2
                    linha_centro = " " * espaco_esq + linha
                    linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

                img_final = "\n".join(linhas_img)
                centra_h_v(img_final)

                indices_mortos = []
                mortes = []

                for i, npc in enumerate(lista_npcs):
                    if int(npc["hp"]) <= 0:
                        npc["hp"] = 0
                        indices_mortos.append(i)

                if not indices_mortos:
                    centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                else:
                    centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                    input(" ")

                for i in indices_mortos:
                    npc = lista_npcs[i]
                    xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                    player['exp'] = int(player.get('exp', 0)) + xp_ganho
                    verificar_level_up(player)
                    normalizar_stats(player)

                    img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                    mortes.append((img_monstro, npc['nome'], xp_ganho))

                for i in reversed(indices_mortos):
                    del lista_npcs[i]
                    del escolhas_inimigo[i]

                for img_monstro, nome_monstro, xp_ganho in mortes:
                    mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

    # HABILIDADE PRINCESA MEDUSA
    elif habilidade == "ENCANTO DE PEDRA" and len(lista_npcs) > 0:
        sorte = randint(1, 3)
        if sorte == 1:
            player['dano por medusa'] = lista_npcs[idx]['hp']
            lista_npcs[idx]['hp'] -= player["dano por medusa"]

            img = pricesa_medusa_especial()
            linhas_img = img.splitlines()

            for i, linha in enumerate(linhas_img):
                linhas_img[i] = Fore.GREEN + linha + Style.RESET_ALL

            linhas_texto = []
            largura_barra = 54
            linhas_texto.append(
                Fore.GREEN + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.YELLOW + Style.BRIGHT + "                P E T R I F I C A Ç Ã O !               " + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "O olhar da Medusa selou o destino do inimigo..." + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Resultado: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + "morte instantânea" + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.GREEN + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )

            largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

            for i, linha in enumerate(linhas_texto, start=17):
                visivel = strip_ansi(linha)
                espaco_esq = (largura_bloco - len(visivel)) // 2
                linha_centro = " " * espaco_esq + linha
                linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

            img_final = "\n".join(linhas_img)
            centra_h_v(img_final)

            indices_mortos = []
            mortes = []

            for i, npc in enumerate(lista_npcs):
                if int(npc["hp"]) <= 0:
                    npc["hp"] = 0
                    indices_mortos.append(i)

            if not indices_mortos:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            else:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                input(" ")

            for i in indices_mortos:
                npc = lista_npcs[i]
                xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                player['exp'] = int(player.get('exp', 0)) + xp_ganho
                verificar_level_up(player)
                normalizar_stats(player)

                img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                mortes.append((img_monstro, npc['nome'], xp_ganho))

            for i in reversed(indices_mortos):
                del lista_npcs[i]
                del escolhas_inimigo[i]

            for img_monstro, nome_monstro, xp_ganho in mortes:
                mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

        else:
            lista_npcs[idx]['hp'] -= player['dano']

            img = pricesa_medusa_especial()
            linhas_img = img.splitlines()

            for i, linha in enumerate(linhas_img):
                linhas_img[i] = Fore.GREEN + linha + Style.RESET_ALL

            linhas_texto = []
            largura_barra = 54
            linhas_texto.append(
                Fore.GREEN + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.YELLOW + Style.BRIGHT + "                 F Ú R I A   D A   M E D U S A           " + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "O inimigo desviou do olhar... mas não do ataque!" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Alvo: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Dano causado: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{int(player['dano'])}" + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.GREEN + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )

            largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

            for i, linha in enumerate(linhas_texto, start=17):
                visivel = strip_ansi(linha)
                espaco_esq = (largura_bloco - len(visivel)) // 2
                linha_centro = " " * espaco_esq + linha
                linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

            img_final = "\n".join(linhas_img)
            centra_h_v(img_final)

            indices_mortos = []
            mortes = []

            for i, npc in enumerate(lista_npcs):
                if int(npc["hp"]) <= 0:
                    npc["hp"] = 0
                    indices_mortos.append(i)

            if not indices_mortos:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            else:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                input(" ")

            for i in indices_mortos:
                npc = lista_npcs[i]
                xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                player['exp'] = int(player.get('exp', 0)) + xp_ganho
                verificar_level_up(player)
                normalizar_stats(player)

                img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                mortes.append((img_monstro, npc['nome'], xp_ganho))

            for i in reversed(indices_mortos):
                del lista_npcs[i]
                del escolhas_inimigo[i]

            for img_monstro, nome_monstro, xp_ganho in mortes:
                mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

    # HABILIDADE ARQUEIRO MÁGICO
    elif habilidade == "FLECHA MÁGICA" and len(lista_npcs) > 0:

        if len(lista_npcs) >= 3:
            player['dano por flecha magica'] = int(player['dano'] * 1.8)
            alvos = sample(lista_npcs, 3)
            for npc in alvos:
                npc['hp'] -= player['dano por flecha magica']

            img = arqueiro_magico_especial()
            linhas_img = img.splitlines()

            for i, linha in enumerate(linhas_img):
                linhas_img[i] = Fore.CYAN + linha + Style.RESET_ALL

            nomes = ", ".join(npc['nome'] for npc in alvos)

            linhas_texto = []
            largura_barra = 54
            linhas_texto.append(
                Fore.CYAN + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.YELLOW + Style.BRIGHT + "                   F L E C H A   M Á G I C A            " + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Disparo múltiplo atravessando os inimigos!" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Alvos: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{nomes}" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Dano em cada alvo: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{int(player['dano por flecha magica'])}" + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.CYAN + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )

            largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

            for i, linha in enumerate(linhas_texto, start=17):
                visivel = strip_ansi(linha)
                espaco_esq = (largura_bloco - len(visivel)) // 2
                linha_centro = " " * espaco_esq + linha
                linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

            img_final = "\n".join(linhas_img)
            centra_h_v(img_final)

            indices_mortos = []
            mortes = []

            for i, npc in enumerate(lista_npcs):
                if int(npc["hp"]) <= 0:
                    npc["hp"] = 0
                    indices_mortos.append(i)

            if not indices_mortos:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            else:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                input(" ")

            for i in indices_mortos:
                npc = lista_npcs[i]
                xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                player['exp'] = int(player.get('exp', 0)) + xp_ganho
                verificar_level_up(player)
                normalizar_stats(player)

                img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                mortes.append((img_monstro, npc['nome'], xp_ganho))

            for i in reversed(indices_mortos):
                del lista_npcs[i]
                del escolhas_inimigo[i]

            for img_monstro, nome_monstro, xp_ganho in mortes:
                mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

        else:
            alvos = sample(lista_npcs, len(lista_npcs))
            for npc in alvos:
                npc['hp'] -= player['dano'] * 2

            img = arqueiro_magico_especial()
            linhas_img = img.splitlines()

            for i, linha in enumerate(linhas_img):
                linhas_img[i] = Fore.CYAN + linha + Style.RESET_ALL

            nomes = ", ".join(npc['nome'] for npc in alvos)

            linhas_texto = []
            largura_barra = 54
            linhas_texto.append(
                Fore.CYAN + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.YELLOW + Style.BRIGHT + "                   F L E C H A   M Á G I C A            " + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Poucos inimigos na arena — disparo certeiro!" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Alvos: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{nomes}" + Style.RESET_ALL
            )
            linhas_texto.append(
                Fore.WHITE + Style.BRIGHT + "Dano em cada alvo: " + Style.RESET_ALL
                + Fore.RED + Style.BRIGHT + f"{int(player['dano'] * 2)}" + Style.RESET_ALL
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                Fore.CYAN + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
            )

            largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

            for i, linha in enumerate(linhas_texto, start=17):
                visivel = strip_ansi(linha)
                espaco_esq = (largura_bloco - len(visivel)) // 2
                linha_centro = " " * espaco_esq + linha
                linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

            img_final = "\n".join(linhas_img)
            centra_h_v(img_final)

            indices_mortos = []
            mortes = []

            for i, npc in enumerate(lista_npcs):
                if int(npc["hp"]) <= 0:
                    npc["hp"] = 0
                    indices_mortos.append(i)

            if not indices_mortos:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            else:
                centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
                input(" ")

            for i in indices_mortos:
                npc = lista_npcs[i]
                xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
                player['exp'] = int(player.get('exp', 0)) + xp_ganho
                verificar_level_up(player)
                normalizar_stats(player)

                img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
                mortes.append((img_monstro, npc['nome'], xp_ganho))

            for i in reversed(indices_mortos):
                del lista_npcs[i]
                del escolhas_inimigo[i]

            for img_monstro, nome_monstro, xp_ganho in mortes:
                mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)

    # HABILIDADE MORTE MURMURANTE
    elif habilidade == "ILUSÃO" and len(lista_npcs) > 0:
        for npc in lista_npcs:
            npc['hp'] = int(npc['hp']) - int(npc['dano']) * 2

        img = morte_mormurante_especial()
        linhas_img = img.splitlines()

        for i, linha in enumerate(linhas_img):
            linhas_img[i] = Fore.CYAN + linha + Style.RESET_ALL

        linhas_texto = []
        largura_barra = 54
        linhas_texto.append(
            Fore.MAGENTA + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
        )
        linhas_texto.append(
            Fore.CYAN + Style.BRIGHT + "                         I L U S Ã O                    " + Style.RESET_ALL
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + "As criaturas perderam o controle..." + Style.RESET_ALL
        )
        linhas_texto.append(
            Fore.WHITE + Style.BRIGHT + "Efeito: " + Style.RESET_ALL
            + Fore.YELLOW + Style.BRIGHT + "inimigos atacam a si mesmos (dano dobrado)" + Style.RESET_ALL
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            Fore.MAGENTA + Style.BRIGHT + "✦" + "━" * largura_barra + "✦" + Style.RESET_ALL
        )

        largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

        for i, linha in enumerate(linhas_texto, start=17):
            visivel = strip_ansi(linha)
            espaco_esq = (largura_bloco - len(visivel)) // 2
            linha_centro = " " * espaco_esq + linha
            linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

        img_final = "\n".join(linhas_img)
        centra_h_v(img_final)

        indices_mortos = []
        mortes = []

        for i, npc in enumerate(lista_npcs):
            if int(npc["hp"]) <= 0:
                npc["hp"] = 0
                indices_mortos.append(i)

        if not indices_mortos:
            centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
        else:
            centra_h(f"{Fore.WHITE}{Style.BRIGHT}Aperte ENTER para continuar...{Style.RESET_ALL}")
            input(" ")

        for i in indices_mortos:
            npc = lista_npcs[i]
            xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
            player['exp'] = int(player.get('exp', 0)) + xp_ganho
            verificar_level_up(player)
            normalizar_stats(player)

            img_monstro = imagem_seta_escolhida_inimigo_fase1(i)
            mortes.append((img_monstro, npc['nome'], xp_ganho))

        for i in reversed(indices_mortos):
            del lista_npcs[i]
            del escolhas_inimigo[i]

        for img_monstro, nome_monstro, xp_ganho in mortes:
            mostrar_monstro_derrotado(img_monstro, nome_monstro, player, xp_ganho)




                



#FUNCAO DE ATACAR OS MONSTROS APENAS (DANO) NORMAL DO JOGADOR
def atacar_monstro(idx: int, player: dict, orda: int) -> None:

    hp = lista_npcs[idx]['hp']

    img = imagem_seta_escolhida_inimigo_fase1(idx)
    inimigo = lista_npcs[idx]['nome']

    lista_npcs[idx]['hp'] = int(lista_npcs[idx]['hp']) - int(player['dano'])

    if lista_npcs[idx]['hp'] <= 0:

        lista_npcs[idx]['hp'] = 0

        npc = lista_npcs[idx]
        xp_ganho = int(calcular_xp(npc, player, len(lista_npcs)))
        player['exp'] = int(player.get('exp', 0)) + xp_ganho
        verificar_level_up(player)
        normalizar_stats(player)

        inimigo = npc['nome']

        del escolhas_inimigo[idx]
        del lista_npcs[idx]

        mostrar_monstro_derrotado(img, inimigo, player, xp_ganho)


    if len(lista_npcs) == 0:
        
        mensagem_horda_derrotada = (
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            f"{Fore.BLUE}✦━━━━━━━━━━━━━━━ ✧ HORDA DERROTADA ✧ ━━━━━━━━━━━━━━━✦{Style.RESET_ALL}\n"
            f"\n"
            f"{Style.BRIGHT}A horda inimiga foi esmagada diante de sua determinação.{Style.RESET_ALL}\n"
            f"{Style.BRIGHT}Você permanece de pé entre os corpos dos derrotados.{Style.RESET_ALL}\n"
        )

        if orda <= 2:
            mensagem_horda_derrotada += f"{Style.BRIGHT}Essa não, parece que mais uma horda está se aproximando...{Style.RESET_ALL}\n"
        else:
            mensagem_horda_derrotada += f"{Style.BRIGHT}Você derrotou todas as hordas de monstros, pronto para a proxima fase?{Style.RESET_ALL}\n"

        mensagem_horda_derrotada += f"\n{Style.BRIGHT}Pressione ENTER para continuar{Style.RESET_ALL}"

        limpar_tela()
        print("\n" * 2)
        descri_monstro_mais_img(ic.fase1_cidade_salva(), mensagem_horda_derrotada)
        input()

    else:
        mensagem_dano_oponente = (
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            f"{Fore.RED}✦━━━━━━━━━━━━━━ ✧ DANO CAUSADO ✧ ━━━━━━━━━━━━━━✦{Style.RESET_ALL}\n"
            f"\n"
            f"{Style.BRIGHT}você atacou o inimigo {Fore.RED + inimigo + Style.RESET_ALL}!"
            f"\n"
            f"{Style.BRIGHT}Dano dado: {Fore.RED + str(player['dano'])}{Style.BRIGHT}{Style.RESET_ALL}\n"
            f"{Style.BRIGHT}HP restante do inimigo: {Fore.MAGENTA + str(hp)}{Style.BRIGHT}{Style.RESET_ALL}\n"
            f"\n"
            f"{Style.BRIGHT}Aperte ENTER para continuar{Style.RESET_ALL}"
        )

        limpar_tela()
        print("\n" * 2)
        descri_monstro_mais_img(img, mensagem_dano_oponente)
        input()







#ATAQUE PROFERIDO INDIVIDUALMENTE DE UM DOS MONSTROS ALEATORIAMENTE
def ataque_dos_monstros(player: dict, lista_npcs: list) -> None:

    if not lista_npcs:
        return 
    
    idx = randint(0, len(lista_npcs) - 1)
    monstro = lista_npcs[idx]

    player['hp'] -= monstro['dano']
    if player['hp'] <= 0:
        player['hp'] = 0

    img = imagem_seta_escolhida_inimigo_fase1(idx)

    limpar_tela()

    mensagem_turno_oponente = (
        f"{Fore.RED}{Style.BRIGHT}"
        f"✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦\n"
        f"{Style.RESET_ALL}"
        f"\n"
        f"             {Fore.YELLOW}{Style.BRIGHT}T U R N O   D O   O P O N E N T E{Style.RESET_ALL}\n"
        f"\n"
        f"              {Fore.WHITE}{Style.BRIGHT}As criaturas avançam lentamente...{Style.RESET_ALL}\n"
        f"                   {Fore.WHITE}{Style.BRIGHT}O perigo se aproxima.{Style.RESET_ALL}\n"
        f"\n"
        f"{Fore.RED}{Style.BRIGHT}"
        f"✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
        f"{Style.RESET_ALL}"
    )

    print("\n" * 3)
    centra_h_v(mensagem_turno_oponente)
    print("\n")
    centra_h(f"{Fore.CYAN}{Style.BRIGHT}Aperte ENTER para continuar{Style.RESET_ALL}")
    input(" ")


    mensagem_ataque = (
        f"\n"
        f"{Fore.RED}✦━━━━━━━━━━━━━━ {Style.BRIGHT}ATAQUE INIMIGO{Style.RESET_ALL}{Fore.RED} ━━━━━━━━━━━━━━✦{Style.RESET_ALL}\n"
        f"\n"
        f"{Style.BRIGHT}{Fore.YELLOW}O monstro atacou!{Style.RESET_ALL}\n"
        f"\n"
        f"{Style.BRIGHT}Inimigo:{Style.RESET_ALL} {Fore.MAGENTA}{Style.BRIGHT}{monstro['nome']}{Style.RESET_ALL} "
        f"{Fore.CYAN}{Style.BRIGHT}(Lv. {monstro['level']}){Style.RESET_ALL}\n"
        f"\n"
        f"{Style.BRIGHT}Dano recebido:{Style.RESET_ALL} {Fore.RED}{Style.BRIGHT}{monstro['dano']}{Style.RESET_ALL}\n"
        f"{Style.BRIGHT}Sua vida agora:{Style.RESET_ALL} {Fore.GREEN}{Style.BRIGHT}{player['hp']}{Style.RESET_ALL}\n"
        f"\n"
        f"{Fore.RED}✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦{Style.RESET_ALL}\n"
        f"\n"
        f"{Style.BRIGHT}{Fore.WHITE}Aperte ENTER para continuar...{Style.RESET_ALL}"
    )

    limpar_tela()
    descri_monstro_mais_img(img, mensagem_ataque)
    input(" ")


    if player['hp'] <= 0:
        limpar_tela()
        img_morte = ic.morte_player_img() 

        extra_morte = Fore.WHITE + f"""
O silêncio toma conta do campo de batalha.
Seu corpo já não responde, e suas forças se esgotaram por completo.
Os inimigos ainda estão de pé, enquanto sua jornada chega ao fim.
Cada escolha feita ecoa como uma última lembrança do combate.
Não foi o fim que você esperava, mas foi o fim que encontrou.
A história para aqui, mas poderia ter sido diferente.

                    {Fore.RED}VOCÊ MORREU{Style.RESET_ALL}
                    
        {rgb_text("Aperte ENTER para voltar para o inicio!")}
"""

        descri_monstro_mais_img(img_morte, extra_morte)
        input(" ")




#PEGA A IMAGEM DO MONSTRO E ADICIONA A DESCRICAO QUE EU QUERO QUE O MONSTRO TENHA, JUNTANDO OS DOIS
def descri_monstro_mais_img(imagem: str, extra: str) -> None:

    linhas = imagem.splitlines()
    extras = extra.splitlines()

    for i, msg in enumerate(extras, start=(len(linhas) // 2) - (len(linhas) // 4)):
        if i < len(linhas):
            linhas[i] = linhas[i] + (" " * 13) + msg
        
    centra_h_v("\n".join(linhas))




#FAZ COM QUE AS IMAGENS DOS M0NSTROS FIQUEM COM CORES ALEATORIAS DEIXANDO MAIS INDIVIDUAL CADA MONSTRO
def aplicar_cor_monstro(imagem: str, cor: str) -> str:
    reset = "\033[0m"
    return "\n".join(cor + linha + reset for linha in imagem.splitlines())

            





#TRANSFORMA A COR DO TEXTO EM RGB
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



#SISTEMA DE LEVEL UP PLAYER / QUANTIDADE DE XP POR MONSTRO ----------------------------------

def multiplicador_qtd(qtd: int) -> float:
    if qtd == 1: return 1.0
    if qtd == 2: return 1.15
    if qtd == 3: return 1.30
    if qtd == 4: return 1.50
    return 1.75


def multiplicador_level(player_lvl: int, npc_lvl: int) -> float:
    diff = npc_lvl - player_lvl

    if diff >= 5:
        return 1.6
    elif diff >= 2:
        return 1.3
    elif diff == 1:
        return 1.15
    elif diff == 0:
        return 1.0
    elif diff == -1:
        return 0.9
    else:
        return 0.75



def xp_para_upar(level: int) -> int:

    return int(round(100 * (level ** 1.7) * 0.30))



def calcular_xp(npc: dict, player: dict, qtd_inimigos: int) -> int:

    xp_base = int(npc.get('exp', 0))

    mult_qtd = multiplicador_qtd(int(qtd_inimigos))
    mult_lvl = multiplicador_level(int(player.get('level', 1)), int(npc.get('level', 1)))

    xp_final = xp_base * mult_qtd * mult_lvl
    return int(round(xp_final))


def verificar_level_up(player: dict) -> None:
    player['level'] = int(player.get('level', 1))
    player['exp'] = int(player.get('exp', 0))
    player['xp_next'] = int(player.get('xp_next', xp_para_upar(player['level'])))

    while player['exp'] >= player['xp_next']:
        player['exp'] -= player['xp_next']
        player['level'] += 1
        player['xp_next'] = xp_para_upar(player['level'])

        atualizar_stats_por_level(player, curar_total=True)
        normalizar_stats(player) 







def barra_xp(exp, xp_next, tamanho=20):
    exp = inteiro(exp)
    xp_next = inteiro(xp_next)

    if xp_next <= 0:
        return "█" * tamanho

    proporcao = exp / xp_next
    if proporcao < 0:
        proporcao = 0
    if proporcao > 1:
        proporcao = 1

    preenchido = int(proporcao * tamanho)
    vazio = tamanho - preenchido
    return "█" * preenchido + "░" * vazio





def inteiro(n) -> int:
    try:
        return int(n)
    except Exception:
        return 0


def normalizar_stats(player: dict) -> None:

    player['level'] = inteiro(player.get('level', 1))
    player['exp'] = inteiro(player.get('exp', 0))
    player['xp_next'] = inteiro(player.get('xp_next', 0))

    player['dano'] = inteiro(player.get('dano', 0))

    player['hp'] = inteiro(player.get('hp', 0))
    player['hp_max'] = inteiro(player.get('hp_max', player['hp']))

    if player['hp'] < 0:
        player['hp'] = 0
    if player['hp'] > player['hp_max']:
        player['hp'] = player['hp_max']




def mostrar_monstro_derrotado(img: str, inimigo: str, player: dict, xp_ganho: int = 0) -> None:
    normalizar_stats(player)

    largura = 21
    exp = player['exp']
    xp_next = player.get('xp_next', 0)

    status_jogador = (
        "  ╔" + "═" * 34 + "╗\n"
        "  ║         STATUS DO JOGADOR        ║\n"
        "  ╠" + "═" * 34 + "╣\n"
        f"  ║    Nome   : {str(player['nome']).ljust(largura)}║\n"
        f"  ║    Level  : {str(player['level']).ljust(largura)}║\n"
        f"  ║     EXP   : {str(exp).ljust(largura)}║\n"
        f"  ║  PróxLvl  : {str(xp_next).ljust(largura)}║\n"
        f"  ║ XP Barra  : {barra_xp(exp, xp_next).ljust(largura)}║\n"
        "  ╠" + "═" * 34 + "╣\n"
        f"  ║      HP   : {str(player['hp']).ljust(largura)}║\n"
        f"  ║     Dano  : {str(player['dano']).ljust(largura)}║\n"
        f"  ║ Habilidade: {str(player['habilidade']).ljust(largura)}║\n"
        "  ╚" + "═" * 34 + "╝\n"
    )

    status_jogador_rgb = "\n".join([rgb_text(linha) for linha in status_jogador.splitlines()])

    linha_xp = ""
    if xp_ganho > 0:
        linha_xp = f"{Style.BRIGHT}Você ganhou {Fore.YELLOW}+{inteiro(xp_ganho)} XP{Style.RESET_ALL}\n"

    mensagem = (
        f"\n"
        f"{status_jogador_rgb}"
        f"\n\n"
        f"{Fore.RED}✦━━━━━━━━━━━━━━━ ✧ MENOS UM! ✧ ━━━━━━━━━━━━━━━✦{Style.RESET_ALL}\n"
        f"\n"
        f"{Style.BRIGHT}O inimigo {Fore.RED + inimigo + Style.RESET_ALL}{Style.BRIGHT} morreu!{Style.RESET_ALL}\n"
        f"{Style.BRIGHT}Parece que você derrotou um inimigo. Muito bem!{Style.RESET_ALL}\n"
        f"{linha_xp}"
        f"\n"
        f"{Style.BRIGHT}Pressione ENTER para continuar{Style.RESET_ALL}\n"
    )

    limpar_tela()
    print("\n" * 2)
    descri_monstro_mais_img(img, mensagem)
    input()





#CALCULO DAS STATS BASEADAS EM LEVEL 
def hp_normal_por_level(level: int) -> float:
    return 90 + level * 18

def dano_normal_por_level(level: int) -> float:
    return 6 + level * 2.1

def atualizar_stats_por_level(player: dict, curar_total: bool = True) -> None:

    player["level"] = inteiro(player.get("level", 1))

    base_level = 1 
    lvl = player["level"]

    if "hp_base" not in player or "dano_base" not in player:

        hp_max_atual = inteiro(player.get("hp_max", player.get("hp", 1)))
        dano_atual = inteiro(player.get("dano", 1))

        r_hp = hp_normal_por_level(lvl) / hp_normal_por_level(base_level)
        r_dano = dano_normal_por_level(lvl) / dano_normal_por_level(base_level)

        player["hp_base"] = max(1, int(round(hp_max_atual / r_hp))) if r_hp > 0 else hp_max_atual
        player["dano_base"] = max(1, int(round(dano_atual / r_dano))) if r_dano > 0 else dano_atual

    hp_max_antigo = inteiro(player.get("hp_max", player.get("hp", 0)))
    hp_antigo = inteiro(player.get("hp", 0))

    r_hp = hp_normal_por_level(lvl) / hp_normal_por_level(base_level)
    r_dano = dano_normal_por_level(lvl) / dano_normal_por_level(base_level)

    player["hp_max"] = max(1, int(round(player["hp_base"] * r_hp)))
    player["dano"] = max(1, int(round(player["dano_base"] * r_dano)))

    if curar_total:
        player["hp"] = player["hp_max"]
    else:
        if hp_max_antigo > 0:
            pct = hp_antigo / hp_max_antigo
            player["hp"] = int(round(player["hp_max"] * pct))
        else:
            player["hp"] = player["hp_max"]

    if player["hp"] < 0:
        player["hp"] = 0
    if player["hp"] > player["hp_max"]:
        player["hp"] = player["hp_max"]
