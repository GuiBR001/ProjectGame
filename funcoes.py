import os
import shutil
import re
import time
import msvcrt
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
    centra_h_v(creditos_img())
    centra_h("\nJOGO SINGLE DEVELOPER", Fore.MAGENTA + Style.BRIGHT)
    centra_h("Dev by Guilherme Barreto Ramos", Fore.WHITE + Style.BRIGHT)
    centra_h("email: guilhermebramos.dev@gmail.com",  Fore.WHITE + Style.BRIGHT)
    centra_h(Style.DIM + "\npressione qualquer tecla para voltar")
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
                    for x in range(3):
                        nivel = randint(1, 5)
                        novo_npc = criar_npc(nivel, fase)
                        lista_npcs.append(novo_npc)
                        escolhas_inimigo.append(novo_npc['nome'] + " " + novo_npc['sexo'])

                    if lista_npcs[0]['nome'] == lista_npcs[1]['nome']:
                        lista_npcs.clear()
                        escolhas_inimigo.clear()
                        continue
                    else:
                        break


                        
            #ORDA DE INIMIGOS 2
            if orda == 2:
                while True:
                    for x in range(5):
                        nivel = randint(6, 10)
                        novo_npc = criar_npc(nivel, fase)
                        lista_npcs.append(novo_npc)
                        escolhas_inimigo.append(novo_npc['nome'])

                    if lista_npcs[0]['nome'] == lista_npcs[1 or 2]['nome'] or lista_npcs[3]['nome'] == lista_npcs[4 or 5]['nome']:
                        lista_npcs.clear()
                        escolhas_inimigo.clear()
                        continue
                    else: 
                        break
            

            #ORDA DE INIMIGOS 3
            if orda == 3:
                while True:
                    for x in range(7):
                        nivel = randint(8, 15)
                        novo_npc = criar_npc(nivel, fase)
                        lista_npcs.append(novo_npc)
                        escolhas_inimigo.append(novo_npc['nome'])

                    if lista_npcs[0]['nome'] == lista_npcs[1 or 2]['nome'] or lista_npcs[3]['nome'] == lista_npcs[4 or 5]['nome'] or lista_npcs[5]['nome'] == lista_npcs[6 or 7]['nome']:
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

    hp_normal = 150
    dano_normal = 30
    sorte_normal = 2
    habilidade = None

    match raca:
        case 1:
            raca = "Esqueleto Flamejante"
            hp = hp_normal // 2
            dano = dano_normal * 2
            sorte = sorte_normal
            habilidade = "CHAMAS INFERNAIS"
        
        case 2:
            raca = "Anjo caído"
            hp = hp_normal
            dano = dano_normal * 2
            sorte = sorte_normal - 1
            habilidade = "CEIFEIRO"
        
        case 3:
            raca = "Sábio Feiticeiro"
            hp = hp_normal 
            dano = dano_normal // 2
            sorte = sorte_normal + 1
            habilidade = "FEITIÇOS ELEMENTAIS"
        
        case 4: 
            raca = "Pricesa Medusa"
            hp = hp_normal * 2
            dano = dano_normal 
            sorte = sorte_normal - 1
            habilidade = "ENCANTO DE PEDRA"
        
        case 5:
            raca = "Morte Mormurante"
            hp = hp_normal 
            dano = dano_normal * 2
            sorte = sorte_normal - 1
            habilidade = "ILUSÃO"
        
        case 6:
            raca = "Arqueiro Mágico"
            hp = hp_normal // 2
            dano = dano_normal 
            sorte = sorte_normal + 1
            habilidade = "FLECHA MÁGICA"

    return  {
        "nome": nome,
        "raca": raca,
        "level": 1,
        "exp": 0,
        "hp": hp,
        "dano": dano,
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
        "dano": 5 * level,
        "hp": 100 * level,
        "exp": 7 * level,
    }

    return novo_npc
        





#EXIBE O PERFIL ATUAL DO JOGADOR (NOME, NIVEL, VIDA, DANO, ETC...)
def exibir_player(player: dict) -> None:
    nome = player['nome']
    raca = player['raca']
    level = player['level']
    exp = player['exp']
    vida = player['hp']
    dano = player['dano']
    sorte = player['sorte']
    habilidade = player['habilidade'] 

    if sorte == 1:
        sorte = "Baixa"
    elif sorte == 2:
        sorte = "Normal"
    else:
        sorte = "Alta"

    largura = 21 

    status = (
        "  ╔" + "═" * 34 + "╗\n"
        "  ║         STATUS DO JOGADOR        ║\n"
        "  ╠" + "═" * 34 + "╣\n"
        f"  ║    Nome   : {str(nome).ljust(largura)}║\n"
        f"  ║    Raça   : {str(raca).ljust(largura)}║\n"
        f"  ║    Level  : {str(level).ljust(largura)}║\n"
        f"  ║     EXP   : {str(exp).ljust(largura)}║\n"
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
def escolha_seta_inimigo_fase1(player) -> str:
    def strip_ansi(s: str) -> str:
        return _ANSI.sub("", s or "")
    
    idx = 0
    while True:
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
            if sexo == "Macho": 
                coresc = Fore.BLUE + sexo + Style.RESET_ALL
            else:
                coresc = Fore.MAGENTA + sexo + Style.RESET_ALL
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
        caixa_cor = rgb_text(caixa_poder_heroi(player))
        centra_h(caixa_cor)

        ch = msvcrt.getch()

        if ch in (b"\x00", b"\xe0"):
            ch2 = msvcrt.getch()

            if ch2 == b"H":
                idx = (idx - 1) % len(escolhas_inimigo)
                
            elif ch2 == b"P":
                idx = (idx + 1) % len(escolhas_inimigo)

        elif ch in (b"\r", b"\n"):
            escolha = escolhas_inimigo[idx]
            return escolha
        
        elif ch in (b"p", b"P"):
            atacar_monstro_habilidade(player, idx)
            print("\n" * 3)
            centra_h(rgb_text("Aperte ENTER para continuar"))
            input()

        if not escolhas_inimigo:
            return ""

        if idx >= len(escolhas_inimigo):
            idx = len(escolhas_inimigo) - 1


        elif ch in (b"1", b"2", b"3", b"4"):
            n = int(ch.decode()) - 1
            if 0 <= n < len(escolhas_inimigo):
                escolha = escolhas_inimigo[n]
                return escolha
        else:
            time.sleep(0.00000000000000000000000000001)






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
    from icons import esqueleto_flamejante_especial, anjo_caido_especial, sabio_feiticeiro_especial

    habilidade = player['habilidade']


    #HABILIDADE ESQUELETO FLAMEJANTE ---------------------------------------------------
    if habilidade == "CHAMAS INFERNAIS" and len(lista_npcs) > 0:

        player['dano por fogo'] = player['dano'] // len(lista_npcs)
        for npc in lista_npcs:
            npc['hp'] -= player['dano por fogo']

        img = esqueleto_flamejante_especial()
        linhas_img = img.splitlines()

        for i, linha in enumerate(linhas_img):
            linhas_img[i] = Fore.RED + linha + Style.RESET_ALL

        linhas_texto = []
        linhas_texto.append(
            rgb_text(f"{player['nome']} ATIVOU A HABILIDADE {player['habilidade']}")
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            f"Causando {Fore.RED}{player['dano por fogo']}{Style.RESET_ALL} de dano por fogo em {Fore.RED + 'AREA' + Style.RESET_ALL}"
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            rgb_text("Monstros afetados em área:")
        )
        linhas_texto.append(" ")

        largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

        for i, linha in enumerate(linhas_texto, start= 7):

            visivel = strip_ansi(linha)
            espaco_esq = (largura_bloco - len(visivel)) // 2
            linha_centro = " " * espaco_esq + linha

            linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

        img_final = "\n".join(linhas_img)
        centra_h_v(img_final)

        indices_mortos = []

        for i, npc in enumerate(lista_npcs):
            if npc['hp'] <= 0:
                npc['hp'] = 0
                linhas_texto.append(
                    Fore.RED + npc['nome'] + Style.RESET_ALL
                    + " " + Fore.BLACK + "vida atual: " + f"{npc['hp']}" + Style.RESET_ALL
                )
                indices_mortos.append(i)  
            else:
                linhas_texto.append(
                    Fore.RED + npc['nome'] + Style.RESET_ALL
                    + " " + Fore.BLACK + "vida atual: " + f"{npc['hp']}" + Style.RESET_ALL
                )

        for i in reversed(indices_mortos):
            del lista_npcs[i]
            del escolhas_inimigo[i]


    #HABILIDADE ANJO CAÍDO --------------------------------------------------------------------
    elif habilidade == "CEIFEIRO" and len(lista_npcs) > 0:

        lista_npcs[idx]['hp'] -= player['dano']
        player['vida ceifada'] = player['dano']
        player['hp'] += player['vida ceifada']        

        img = anjo_caido_especial()
        linhas_img = img.splitlines()

        for i, linha in enumerate(linhas_img):
            linhas_img[i] = Fore.BLACK + linha + Style.RESET_ALL

        linhas_texto = []
        linhas_texto.append(
            rgb_text(f"{player['nome']} ATIVOU A HABILIDADE {player['habilidade']}")
        )
        linhas_texto.append(" ")
        linhas_texto.append(
            f"Ceifando {Fore.RED}{player['vida ceifada']}{Style.RESET_ALL} de vida do monstro {Fore.RED + f"{lista_npcs[idx]['nome']}" + Style.RESET_ALL}"
        )
        linhas_texto.append(
            f"Dando {Fore.RED}{player['vida ceifada']}{Style.RESET_ALL} de dano pela foice"
        )

        largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

        for i, linha in enumerate(linhas_texto, start= 17):

            visivel = strip_ansi(linha)
            espaco_esq = (largura_bloco - len(visivel)) // 2
            linha_centro = " " * espaco_esq + linha

            linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

        img_final = "\n".join(linhas_img)
        centra_h_v(img_final)

        indices_mortos = []

        for i, npc in enumerate(lista_npcs):
            if npc['hp'] <= 0:      
                indices_mortos.append(i)

        for i in reversed(indices_mortos):
            del lista_npcs[i]
            del escolhas_inimigo[i] 

    #HABILIDADE SABIO FEITICEIRO------------------------------------------------------------------
    elif habilidade == "FEITIÇOS ELEMENTAIS" and len(lista_npcs) > 0:
        poderes = [
            "Tsunami",
            "Terremoto",
            "Tornado",
            "Vinhas"
        ]

        poder_escolhido = choice(poderes)

        if poder_escolhido == "Tsunami":
            player['dano por tsunami'] = player["dano"] * 2
            lista_npcs[idx]['hp'] -= player['dano por tsunami']
            lista_npcs[idx]['dano'] = (lista_npcs[idx]['dano'] // 2) + (lista_npcs[idx]['dano'] // 4)

            img = sabio_feiticeiro_especial()
            linhas_img = img.splitlines()

            for i, linha in enumerate(linhas_img):
                linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

            linhas_texto = []
            linhas_texto.append(
                rgb_text(f"{player['nome']} ATIVOU A HABILIDADE {player['habilidade']}")
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                f"Uma onda imensa foi invocada causando {player['dano por tsunami']} de dano na criatura {lista_npcs[idx]['nome']}"
            )
            linhas_texto.append(
                f"Fazendo com que a criatura tenha seu ataque reduzido em 25%..."
            )

            largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

            for i, linha in enumerate(linhas_texto, start= 17):

                visivel = strip_ansi(linha)
                espaco_esq = (largura_bloco - len(visivel)) // 2
                linha_centro = " " * espaco_esq + linha

                linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

            img_final = "\n".join(linhas_img)
            centra_h_v(img_final)

            indices_mortos = []

            for i, npc in enumerate(lista_npcs):
                if npc['hp'] <= 0:      
                    indices_mortos.append(i)

            for i in reversed(indices_mortos):
                del lista_npcs[i]
                del escolhas_inimigo[i] 

        elif poder_escolhido == "Terremoto":
            sorte = randint(1,3)
            if sorte == 2:
                player['dano por terremoto'] = lista_npcs[idx]['hp']
                lista_npcs[idx]['hp'] -= player['dano por terremoto']

                img = sabio_feiticeiro_especial()
                linhas_img = img.splitlines()

                for i, linha in enumerate(linhas_img):
                    linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

                linhas_texto = []
                linhas_texto.append(
                    rgb_text(f"{player['nome']} ATIVOU A HABILIDADE {player['habilidade']}")
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    f"Um Terremoto avassalador foi invocado jogando a criatura {lista_npcs[idx]['nome']} no abismo e á eliminando"
                )
                linhas_texto.append(
                    f"Parece que a criatura não conseguiu escapar do destino..."
                )

                largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

                for i, linha in enumerate(linhas_texto, start= 17):

                    visivel = strip_ansi(linha)
                    espaco_esq = (largura_bloco - len(visivel)) // 2
                    linha_centro = " " * espaco_esq + linha

                    linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

                img_final = "\n".join(linhas_img)
                centra_h_v(img_final)

                indices_mortos = []

                for i, npc in enumerate(lista_npcs):
                    if npc['hp'] <= 0:      
                        indices_mortos.append(i)

                for i in reversed(indices_mortos):
                    del lista_npcs[i]
                    del escolhas_inimigo[i]

            else:
                lista_npcs[idx]['hp'] -= 0

                img = sabio_feiticeiro_especial()
                linhas_img = img.splitlines()

                for i, linha in enumerate(linhas_img):
                    linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

                linhas_texto = []
                linhas_texto.append(
                    rgb_text(f"{player['nome']} ATIVOU A HABILIDADE {player['habilidade']}")
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    f"Um Terremoto foi invocado causando 0 de dano na criatura {lista_npcs[idx]['nome']}"
                )
                linhas_texto.append(
                    f"Parece que a criatura conseguiu se esquivar do buraco..."
                )

                largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

                for i, linha in enumerate(linhas_texto, start= 17):

                    visivel = strip_ansi(linha)
                    espaco_esq = (largura_bloco - len(visivel)) // 2
                    linha_centro = " " * espaco_esq + linha

                    linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

                img_final = "\n".join(linhas_img)
                centra_h_v(img_final)

                indices_mortos = []

                for i, npc in enumerate(lista_npcs):
                    if npc['hp'] <= 0:      
                        indices_mortos.append(i)

                for i in reversed(indices_mortos):
                    del lista_npcs[i]
                    del escolhas_inimigo[i] 

        elif poder_escolhido == "Tornado":
            player['dano por tornado'] = player['dano'] * 4
            lista_npcs[idx]['hp'] -= player['dano por tornado']
            img = sabio_feiticeiro_especial()
            linhas_img = img.splitlines()

            for i, linha in enumerate(linhas_img):
                linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

            linhas_texto = []
            linhas_texto.append(
                rgb_text(f"{player['nome']} ATIVOU A HABILIDADE {player['habilidade']}")
            )
            linhas_texto.append(" ")
            linhas_texto.append(
                f"Um Tornado enorme foi invocado causando {player['dano por tornado']} de dano na criatura {lista_npcs[idx]['nome']}"
            )
            linhas_texto.append(
                f"A criatura acabou sendo arremessada e tomando um dano absurdamente grande..."
            )

            largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

            for i, linha in enumerate(linhas_texto, start= 17):

                visivel = strip_ansi(linha)
                espaco_esq = (largura_bloco - len(visivel)) // 2
                linha_centro = " " * espaco_esq + linha

                linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

            img_final = "\n".join(linhas_img)
            centra_h_v(img_final)

            indices_mortos = []

            for i, npc in enumerate(lista_npcs):
                if npc['hp'] <= 0:      
                    indices_mortos.append(i)

            for i in reversed(indices_mortos):
                del lista_npcs[i]
                del escolhas_inimigo[i] 

        elif poder_escolhido == "Vinhas":
            sorte = randint(1,3)
            if sorte == 2:
                player['dano por vinhas'] = (player['dano'] * len(lista_npcs)) * 3
                lista_npcs[idx]['hp'] -= player['dano por vinhas']

                img = sabio_feiticeiro_especial()
                linhas_img = img.splitlines()

                for i, linha in enumerate(linhas_img):
                    linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

                linhas_texto = []
                linhas_texto.append(
                    rgb_text(f"{player['nome']} ATIVOU A HABILIDADE {player['habilidade']}")
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    f"Parece que vinhas enormes foram invocadas causando {player['dano por vinhas']} de dano na criatura {lista_npcs[idx]['nome']}"
                )
                linhas_texto.append(
                    f"As vinhas ficam cada vez mais espinhosas dependendo da quantidade de inimigos na arena..."
                )

                largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

                for i, linha in enumerate(linhas_texto, start= 17):

                    visivel = strip_ansi(linha)
                    espaco_esq = (largura_bloco - len(visivel)) // 2
                    linha_centro = " " * espaco_esq + linha

                    linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

                img_final = "\n".join(linhas_img)
                centra_h_v(img_final)

                indices_mortos = []

                for i, npc in enumerate(lista_npcs):
                    if npc['hp'] <= 0:      
                        indices_mortos.append(i)

                for i in reversed(indices_mortos):
                    del lista_npcs[i]
                    del escolhas_inimigo[i] 
            else:
                lista_npcs[idx]['hp'] -= player['dano']

                img = sabio_feiticeiro_especial()
                linhas_img = img.splitlines()

                for i, linha in enumerate(linhas_img):
                    linhas_img[i] = Fore.BLUE + linha + Style.RESET_ALL

                linhas_texto = []
                linhas_texto.append(
                    rgb_text(f"{player['nome']} ATIVOU A HABILIDADE {player['habilidade']}")
                )
                linhas_texto.append(" ")
                linhas_texto.append(
                    f"Parece que vinhas enormes foram invocadas causando {player['dano']} de dano na criatura {lista_npcs[idx]['nome']}"
                )
                linhas_texto.append(
                    f"Parece que por algum motivo você errou a conjuração do feitiço, causando menos dano..."
                )

                largura_bloco = max(len(strip_ansi(l)) for l in linhas_texto)

                for i, linha in enumerate(linhas_texto, start= 17):

                    visivel = strip_ansi(linha)
                    espaco_esq = (largura_bloco - len(visivel)) // 2
                    linha_centro = " " * espaco_esq + linha

                    linhas_img[i] = linhas_img[i] + " " * 8 + linha_centro

                img_final = "\n".join(linhas_img)
                centra_h_v(img_final)

                indices_mortos = []

                for i, npc in enumerate(lista_npcs):
                    if npc['hp'] <= 0:      
                        indices_mortos.append(i)

                for i in reversed(indices_mortos):
                    del lista_npcs[i]
                    del escolhas_inimigo[i] 

        
                


        







            








#FUNCAO DE ATACAR OS MONSTROS APENAS (DANO) NORMAL DO JOGADOR
def atacar_monstro(escolha: str, player: dict) -> None:  

    idx = None
    for i, npc in enumerate(lista_npcs):
        if npc["nome"] == escolha.split()[0]:
            idx = i
            break
    
    limpar_tela()
    img = imagem_seta_escolhida_inimigo_fase1(idx)
    centra_h_v(img)

    lista_npcs[idx]['hp'] -= player['dano']

    if lista_npcs[idx]['hp'] <= 0:

        del escolhas_inimigo[idx]
        del lista_npcs[idx]
        print("\n" * 2)
        centra_h(f"\n{rgb_text(escolha)} Derrotado! {len(lista_npcs)} Restantes...\n")
        centra_h(rgb_text("\nAperte ENTER para continuar"))
        input()

    else:
        centra_h(f"Dano dado: {player['dano']}")
        centra_h(f"HP restante: {lista_npcs[idx]['hp']}")
        input("Aperte ENTER para continuar")







#PEGA A IMAGEM DO MONSTRO E ADICIONA A DESCRICAO QUE EU QUERO QUE O MONSTRO TENHA, JUNTANDO OS DOIS
def descri_monstro_mais_img(imagem: str, extra: str) -> None:

    linhas = imagem.splitlines()
    extras = extra.splitlines()

    for i, msg in enumerate(extras, start=(len(linhas) // 2) - (len(linhas) // 4)):
        if i < len(linhas):
            linhas[i] = linhas[i] + (" " * 13) + msg
        
    centra_h_v("\n".join(linhas))




#FAZ COM QUE AS IMAGENS DOS M0NSTROS FIQUEM COM CORES ALEATORIAS DEIXANDO MAIS INDIVIDUAL CADA MONSTRO
def cor_aleatoria_monstro(imagem):

    cores = [
        "\033[31m", "\033[32m", "\033[33m",
        "\033[34m", "\033[35m", "\033[36m",
        "\033[91m", "\033[92m", "\033[94m"
    ]

    cor = choice(cores)
    reset = "\033[0m"

    linhas = imagem.splitlines()
    linhas_coloridas = [cor + l + reset for l in linhas]

    return "\n".join(linhas_coloridas)

            





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



