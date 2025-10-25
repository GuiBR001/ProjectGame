import os 
import shutil
import funcoes as fn
import fases as fs
import icons as ic
from colorama import Fore, Style, init

init(autoreset= True)
largura_tela = os.get_terminal_size().columns
altura_tela = shutil.get_terminal_size().lines

fase = 1
escolha = ic.tela_inicio()
ic.escolha_personagem()
fn.descri_raca(raca)
player = fn.criar_personagem(nome, raca)
input(Fore.GREEN + ("Aperte ENTER para continuar".center(largura_tela)))
fs.fase_1(fase, player)