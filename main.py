import os 
os.system("cls")

import funcoes as fn
import fases as fs
import icons as ic
from colorama import Fore, Style, init

init(autoreset= True)
largura_tela = os.get_terminal_size().columns

fase = 1
ic.menu_tela_incicio()
nome = input(Fore.YELLOW + """
                                               ╔══════════════════════════════════════════════════════════════════════╗
                                                ║                                                                     ║
                                               ║                  Bem-vindo à forja dos Heróis                       ║
                                               ║                                                                      ║
                                              ║              Escolha um nome digno para seu aventureiro:              ║
                                               ║                                                                       ║ 
                                               ╚══════════════════════════════════════════════════════════════════════╝

                                > """ + Style.RESET_ALL).upper()
ic.menu_tela_incicio()
raca = int(input(Fore.YELLOW + """
                                               ╔══════════════════════════════════════════════════════════════════════╗
                                               ║                                                                      ║
                                               ║                        Escolha sua Raça                             ║ 
                                              ║                                                                        ║
                                               ║                   1 - Esqueleto Flamejante                           ║
                                               ║                   2 - Anjo da Morte                                  ║
                                              ║                    3 - Mago Ancião                                    ║
                                               ║                                                                     ║
                                               ║    Digite o número da raça:                                          ║
                                               ╚══════════════════════════════════════════════════════════════════════╝
                                
                                >  """ + Style.RESET_ALL))


fn.descri_raca(raca)
player = fn.criar_personagem(nome, raca)
cont = str(input("Aperte ENTER para continuar"))
fn.limpar_tela()
fn.iniciar(fase, player)
fs.fase_1(fase, player)