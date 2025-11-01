import os
import shutil
import re
import time
import msvcrt
from random import randint
from colorama import Fore, Style, init


#AUTOREST PARA COLORAMA
init(autoreset= True)


#VARIAVEIS
lista_npcs = []
escolhas_inimigo = []
escolhas_menu = ["Começar Novo Jogo", "Ultimos Recordes", "Créditos", "Sair"]
escolhas_raca = ["Esqueleto Flamejante", "Anjo Caído", "Sábio Feiticeiro", "Princesa Medusa", "Morte Mormurante", "Arqueiro Mágico"]
player = {}
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






#CRIA MULTIPLOS INIMIGOS BASEADO EM ORDAS, E NA FASE, 
def criar_npcs_em_massa(fase: int, player: dict) -> None:

    orda = 1

    match fase:
        
        #FASE 1
        case 1:

            while True:
                       
                    #ORDA DE MONSTROS 1
                    if orda == 1:
                        for x in range(3):
                            nivel = randint(1, 5)
                            novo_npc = criar_npc(nivel, fase)
                            lista_npcs.append(novo_npc)
                            escolhas_inimigo.append(novo_npc['nome'])
                        
                        escolha_seta_inimigo()

                    elif lista_npcs[0]['nome'] == lista_npcs[1]['nome']:
                        for x in range(3):
                            nivel = randint(1, 5)
                            novo_npc = criar_npc(nivel, fase)
                            lista_npcs.append(novo_npc)
                            escolhas_inimigo.append(novo_npc['nome'])

                    elif len(lista_npcs) == 0 and player["level"] <= 4:
                        orda == 1

                    else:
                        orda == 2

                    #ORDA DE INIMIGOS 2
                    if orda == 2:
                        for x in range(5):
                            nivel = randint(6, 10)
                            novo_npc = criar_npc(nivel, fase)
                            lista_npcs.append(novo_npc)
                            escolhas_inimigo.append(novo_npc['nome'])
                        
                        escolha_seta_inimigo()

                    elif lista_npcs[randint(0,2)]['nome'] == lista_npcs[randint(3,5)]:
                        for x in range(5):
                            nivel = randint(6, 10)
                            novo_npc = criar_npc(nivel, fase)
                            lista_npcs.append(novo_npc)
                            escolhas_inimigo.append(novo_npc['nome'])

                    elif len(lista_npcs) == 0 and player["level"] <= 9:
                        orda == 2

                    else:
                        orda == 3
                    

                    #ORDA DE INIMIGOS 3
                    if orda == 3:
                        for x in range(8):
                            nivel = randint(11, 15)
                            novo_npc = criar_npc(nivel, fase)
                            lista_npcs.append(novo_npc)
                            escolhas_inimigo.append(novo_npc['nome'])
                        
                        escolha_seta_inimigo()

                    elif lista_npcs[randint(0,5)]['nome'] == lista_npcs[randint(6,8)]:
                        for x in range(8):
                            nivel = randint(11, 15)
                            novo_npc = criar_npc(nivel, fase)
                            lista_npcs.append(novo_npc)
                            escolhas_inimigo.append(novo_npc['nome'])

                    elif len(lista_npcs) == 0 and player["level"] <= 15:
                        orda == 3

                    else:
                        continue
    
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





#GERA OS STATUS DO PLAYER (NOME, RAÇA, ETC...)
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

    novo_npc = {
        "nome": f"{nome}",
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

    largura = 26

    status = f"""
  ________________________________
 /                                \\
/        Status Do Jogador         \\
|----------------------------------|
| Nome : {str(nome).ljust(largura)}|
| Raça : {str(raca).ljust(largura)}|
| Level: {str(level).ljust(largura)}|
| EXP  : {str(exp).ljust(largura)}|
| HP   : {str(vida).ljust(largura)}|
| Dano : {str(dano).ljust(largura)}|
|__________________________________|
 \\                                /
  \\______________________________/
"""
    centra_h_v(rgb_text(status))







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
def escolha_seta_inimigo() -> str:
    _ANSI = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
    def strip_ansi(s: str) -> str:
        return _ANSI.sub("", s or "")
    
    idx = 0
    while True:
        limpar_tela()
        imagem_seta_escolhida_inimigo_fase1(idx)
        print("\n")
        centra_h("\nQUE INIMIGO DESEJA ATACAR?", Fore.RED + Style.BRIGHT)
        centra_h(Style.DIM + "use ↑/↓ para navegar e ENTER para confirmar")

        largura_interna = 35
        centra_h(Fore.CYAN + "╔" + "═" * largura_interna + "╗")

        for i, esc in enumerate(escolhas_inimigo):
            selecionado = (i == idx)
            seta = "➤" if selecionado else " "
            cor = Fore.RED + Style.BRIGHT if selecionado else Fore.WHITE
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






#EXIBE A IMAGEM DO INIMIGO QUE ESTA PRÉ-SELECIONADO (FASE 1)
def imagem_seta_escolhida_inimigo_fase1(idx: int) -> None:

    from icons import dominus_img, draconis_img, carceres_img, mytus_img, wetiza_img, akari_img, ogroid_img, tarik_img
    if idx == 0:
        if lista_npcs[0]['nome'] == "DOMINUS":
            dominus_img()
        elif lista_npcs[0]['nome'] == "DRACONIS":
            draconis_img()
        elif lista_npcs[0]['nome'] == "CARCERES":
            carceres_img()
        elif lista_npcs[0]['nome'] == "MYTUS":
            mytus_img()
        elif lista_npcs[0]['nome'] == "WETIZA":
            wetiza_img()
        elif lista_npcs[0]['nome'] == "AKARI":
            akari_img()
        elif lista_npcs[0]['nome'] == "OGROID":
            ogroid_img()
        elif lista_npcs[0]['nome'] == "TARIK":
            tarik_img()
        
    
    elif idx == 1:
        if lista_npcs[1]['nome'] == "DOMINUS":
            dominus_img()
        elif lista_npcs[1]['nome'] == "DRACONIS":
            draconis_img()
        elif lista_npcs[1]['nome'] == "CARCERES":
            carceres_img()
        elif lista_npcs[1]['nome'] == "MYTUS":
            mytus_img()
        elif lista_npcs[1]['nome'] == "WETIZA":
            wetiza_img()
        elif lista_npcs[1]['nome'] == "AKARI":
            akari_img()
        elif lista_npcs[1]['nome'] == "OGROID":
            ogroid_img()
        elif lista_npcs[1]['nome'] == "TARIK":
            tarik_img()

    elif idx == 2:
        if lista_npcs[2]['nome'] == "DOMINUS":
            dominus_img()
        elif lista_npcs[2]['nome'] == "DRACONIS":
            draconis_img()
        elif lista_npcs[2]['nome'] == "CARCERES":
            carceres_img()
        elif lista_npcs[2]['nome'] == "MYTUS":
            mytus_img()
        elif lista_npcs[2]['nome'] == "WETIZA":
            wetiza_img()
        elif lista_npcs[2]['nome'] == "AKARI":
            akari_img()
        elif lista_npcs[2]['nome'] == "OGROID":
            ogroid_img()
        elif lista_npcs[2]['nome'] == "TARIK":
            tarik_img()

    elif idx == 3:
        if lista_npcs[3]['nome'] == "DOMINUS":
            dominus_img()
        elif lista_npcs[3]['nome'] == "DRACONIS":
            draconis_img()
        elif lista_npcs[3]['nome'] == "CARCERES":
            carceres_img()
        elif lista_npcs[3]['nome'] == "MYTUS":
            mytus_img()
        elif lista_npcs[3]['nome'] == "WETIZA":
            wetiza_img()
        elif lista_npcs[3]['nome'] == "AKARI":
            akari_img()
        elif lista_npcs[3]['nome'] == "OGROID":
            ogroid_img()
        elif lista_npcs[3]['nome'] == "TARIK":
            tarik_img()

    elif idx == 4:
        if lista_npcs[0]['nome'] == "DOMINUS":
            dominus_img()
        elif lista_npcs[0]['nome'] == "DRACONIS":
            draconis_img()
        elif lista_npcs[0]['nome'] == "CARCERES":
            carceres_img()
        elif lista_npcs[0]['nome'] == "MYTUS":
            mytus_img()
        elif lista_npcs[0]['nome'] == "WETIZA":
            wetiza_img()
        elif lista_npcs[0]['nome'] == "AKARI":
            akari_img()
        elif lista_npcs[0]['nome'] == "OGROID":
            ogroid_img()
        elif lista_npcs[0]['nome'] == "TARIK":
            tarik_img()

    elif idx == 5:
        if lista_npcs[0]['nome'] == "DOMINUS":
            dominus_img()
        elif lista_npcs[0]['nome'] == "DRACONIS":
            draconis_img()
        elif lista_npcs[0]['nome'] == "CARCERES":
            carceres_img()
        elif lista_npcs[0]['nome'] == "MYTUS":
            mytus_img()
        elif lista_npcs[0]['nome'] == "WETIZA":
            wetiza_img()
        elif lista_npcs[0]['nome'] == "AKARI":
            akari_img()
        elif lista_npcs[0]['nome'] == "OGROID":
            ogroid_img()
        elif lista_npcs[0]['nome'] == "TARIK":
            tarik_img()
    
    elif idx == 6:
        if lista_npcs[0]['nome'] == "DOMINUS":
            dominus_img()
        elif lista_npcs[0]['nome'] == "DRACONIS":
            draconis_img()
        elif lista_npcs[0]['nome'] == "CARCERES":
            carceres_img()
        elif lista_npcs[0]['nome'] == "MYTUS":
            mytus_img()
        elif lista_npcs[0]['nome'] == "WETIZA":
            wetiza_img()
        elif lista_npcs[0]['nome'] == "AKARI":
            akari_img()
        elif lista_npcs[0]['nome'] == "OGROID":
            ogroid_img()
        elif lista_npcs[0]['nome'] == "TARIK":
            tarik_img()

    elif idx == 7:
        if lista_npcs[0]['nome'] == "DOMINUS":
            dominus_img()
        elif lista_npcs[0]['nome'] == "DRACONIS":
            draconis_img()
        elif lista_npcs[0]['nome'] == "CARCERES":
            carceres_img()
        elif lista_npcs[0]['nome'] == "MYTUS":
            mytus_img()
        elif lista_npcs[0]['nome'] == "WETIZA":
            wetiza_img()
        elif lista_npcs[0]['nome'] == "AKARI":
            akari_img()
        elif lista_npcs[0]['nome'] == "OGROID":
            ogroid_img()
        elif lista_npcs[0]['nome'] == "TARIK":
            tarik_img()






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




