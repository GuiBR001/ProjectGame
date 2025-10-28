import os
import shutil
import re
import time
import msvcrt
from random import randint
from colorama import Fore, Style, init


init(autoreset= True)

lista_npcs = []
escolhas_inimigo = [npc['nome'] for npc in lista_npcs[0], npc['nome'] for npc in lista_npcs[:4], npc['nome'] for npc in lista_npcs[:4], npc['nome'] for npc in lista_npcs[:4]]
player = {}
tamanho = shutil.get_terminal_size()
largura_tela = tamanho.columns
altura_tela = tamanho.lines
ANSI = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')


#limpa tela
def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear" )



#centraliza no meio vertical
def centra_v(mensagem: str, cor_padrao: str = None):
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



#centraliza no meio horizontal
def centra_h(mensagem: str, cor_padrao: str = None):
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



#centraliza no meio tanto na horizontal quanto na vertical
def centra_h_v(mensagem: str, cor_padrao: str = None):
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



#menu
def iniciar(fase: int, player: dict) -> None:

    match fase:

        case 1:
            for x in range(7):
                level = randint(1, 20)
                novo_npc = criar_npc(level, fase)
                lista_npcs.append(novo_npc)

            exibir_player(player)
            arte = f"""
FASE 1

REINO DO REI DE FERRO\n
                    """
            for linha in arte.splitlines():
                print(Fore.YELLOW + linha.center(largura_tela))
    
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



#puxa a imagem baseado na escolha da seta do jogador
def imagem_seta_escolhida_raca(idx):
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



#descricao da raca + imagem
def descri_raca(raca) -> None:
    from icons import esqueleto_flamejante, anjo_caido, sabio_feiticeiro, pricesa_medusa, morte_mormurante, arqueiro_magico
    limpar_tela()
    match raca:

        case 1:
            esqueleto_flamejante()
        
        case 2:
            anjo_caido()
        
        case 3:
            sabio_feiticeiro()

        case 4: 
            pricesa_medusa()
        
        case 5:
            morte_mormurante()
        
        case 6:
            arqueiro_magico()





#gera personagem
def criar_personagem(nome: str,raca: int) -> dict: 

    match raca:
        case 1:
            raca = "Esqueleto Flamejante"
        
        case 2:
            raca = "Anjo caído"
        
        case 3:
            raca = "Sábio Feiticeiro"
        
        case 4: 
            raca = "Pricesa Medusa"
        
        case 5:
            raca = "Morte Mormurante"
        
        case 6:
            raca = "Arqueiro Mágico"

    return  {
        "nome": nome,
        "raca": raca,
        "level": 1,
        "exp": 0,
        "hp": 150,
        "dano": 100000000
    }



# cria npc
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
ANSI = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def exibir_player(player: dict) -> None:

    cabecalho = rgb_text("--------------------- Jogador ---------------------")
    corpo = f"""
{rgb_text(player['nome'])}

{Fore.YELLOW}Raça: {player['raca']}
{Fore.BLUE}Level: {player['level']}
{Fore.RED}Dano: {player['dano']}
{Fore.MAGENTA}Saúde: {player['hp']}
{Fore.GREEN}EXP: {player['exp']}
"""
    rodape = rgb_text("---------------------------------------------------")

    texto_final = f"\n{cabecalho}\n{corpo}\n{rodape}\n"
    for linha in texto_final.splitlines():
        texto_puro = ANSI.sub('', linha)
        espacos_h = max((largura_tela - len(texto_puro)) // 2, 0)
        print(' ' * espacos_h + linha)





def escolha_seta_inimigo() -> str:
    _ANSI = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
    def strip_ansi(s: str) -> str:
        return _ANSI.sub("", s or "")
    
    idx = 0
    while True:
        imagem_seta_escolhida_inimigo(idx)
        print("\n")
        centra_h("\nPARAÍSO MEDIEVAL", Fore.YELLOW + Style.BRIGHT)
        centra_h(Style.DIM + "use ↑/↓ para navegar e ENTER para confirmar")

        largura_interna = 56
        centra_h(Fore.CYAN + "╔" + "═" * largura_interna + "╗")

        for i, esc in enumerate(escolhas_inimigo):
            selecionado = (i == idx)
            seta = "➤" if selecionado else " "
            cor = Fore.GREEN + Style.BRIGHT if selecionado else Fore.WHITE
            conteudo = f"{seta} {esc}"
            largura_visivel = len(strip_ansi(conteudo))
            padding = max(largura_interna - largura_visivel, 0)
            linha_final = (
                Fore.CYAN + "║ "
                + cor + conteudo + Style.RESET_ALL
                + " " * padding
                + Fore.CYAN + " ║"
            )
            centra_h(linha_final)

        centra_h(Fore.CYAN + "╚" + "═" * largura_interna + "╝")        
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
        elif ch in (b"1", b"2", b"3", b"4"):
            n = int(ch.decode()) - 1
            if 0 <= n < len(escolhas_inimigo):
                escolha = escolhas_inimigo[n]
                return escolha
        else:
            time.sleep(0.00000000000000000000000000001)





def imagem_seta_escolhida_inimigo(idx: int):

    from icons import dominus_img, draconis_img, carceres_img, mytus_img, wetiza_img, akari_img, ogroid_img, tarik_img
    if idx == 0:
        dominus_img()
    
    elif idx == 1:
        draconis_img()

    elif idx == 2:
        carceres_img()

    elif idx == 3:
        mytus_img()

    elif idx == 4:
        wetiza_img()

    elif idx == 5:
        akari_img()
    
    elif idx == 6:
        ogroid_img()

    elif idx == 7:
        tarik_img()





#exibe npcs
def exibir_npcs() -> None:
    limpar_tela()
    escolha_seta_inimigo()
    imagem_seta_escolhida_inimigo()






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




