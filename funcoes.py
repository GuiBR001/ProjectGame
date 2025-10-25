import os
import shutil
import re
from random import randint
from colorama import Fore, Style, init


init(autoreset= True)

lista_npcs = []
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
                novo_npc = criar_npc(level)
                lista_npcs.append(novo_npc)

            exibir_player(player)
            arte = f"""
FASE 1

CIDADELA DO REI DE FERRO\n
                    """
            for linha in arte.splitlines():
                print(Fore.YELLOW + linha.center(largura_tela))
    
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



#descricao da raca + imagem
def descri_raca(raca) -> None:
    from icons import esqueleto, anjo, mago

    try:
        match raca:

            case 1:
                esqueleto()
            
            case 2:
                anjo()
            
            case 3:
                mago()

    except ValueError:
        print("Escolha com um número de 1 a 3!")



#gera personagem
def criar_personagem(nome: str,raca: int) -> dict: 

    match raca:
        case 1:
            raca = "Esqueleto Flamejante"
        
        case 2:
            raca = "Anjo Da Morte"
        
        case 3:
            raca = "Mago Ancião"

    return  {
        "nome": nome,
        "raca": raca,
        "level": 1,
        "exp": 0,
        "hp": 150,
        "dano": 100000000
    }



# cria npc
def criar_npc(level) -> dict:

    if level >= 1 and level <= 10:
        if level <= 5:
            nome = "dominus".upper()
        else:
            nome = "draconis".upper()

    elif level >= 11 and level <= 20:
        if level <= 15:
            nome = "carceres".upper()
        else:
            nome = "faskra".upper()

    elif level >= 21 and level <= 30:
        if level <= 25:
            nome = "wetiza".upper()
        else:
            nome = "hommer".upper()

    elif level >= 31 and level <= 40:
        if level <= 35:
            nome = "vyper".upper()
        else:
            nome = "fryth".upper()

    elif level >= 41 and level <= 50:
        if level <= 45:
            nome = "akari".upper()
        else:
            nome = "magma".upper()

    elif level >= 51 and level <= 60:
        if level <= 55:
            nome = "tarik".upper()
        else:
            nome = "ogroid".upper()

    elif level >= 61 and level <= 70:
        if level <= 65:
            nome = "wertz".upper()
        else:
            nome = "fenrir".upper()

    elif level >= 71 and level <= 80:
        if level <= 75:
            nome = "mytus".upper()
        else:
            nome = "hydra".upper()

    elif level >= 81 and level <= 90:
        if level <= 85:
            nome = Fore.GREEN + "toon".upper()
        else:
            nome = Fore.BLUE + "tartarus".upper()

    elif level >= 91 and level <= 100:
        if level <= 95:
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




