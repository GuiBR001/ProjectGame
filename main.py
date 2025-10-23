import os 
os.system("cls")

import funcoes as fn
import fases as fs
import icons as ic


fase = 1
nome = input("""
                                ╔══════════════════════════════════════════════════════════════════════╗
                                ║                                                                      ║
                                ║                🏰  Bem-vindo à Terra dos Heróis  🏰                 ║
                                ║                                                                      ║
                            ║     Escolha um nome digno para seu aventureiro:                       ║
                                ║                                                                       ║ 
                                ╚══════════════════════════════════════════════════════════════════════╝

                                > """).upper()
raca = int(input("""
                                ╔══════════════════════════════════════════════════════════════════════╗
                                ║                                                                      ║
                                ║                     ⚔️  Escolha sua Raça  ⚔️                         ║ 
                               ║                                                                       ║
                                ║     1 - Esqueleto Flamejante                                         ║
                                ║     2 - Anjo da Morte                                                ║
                                ║     3 - Mago Ancião                                                 ║
                                 ║                                                                     ║
                                ║    Digite o número da raça:                                          ║
                                ╚══════════════════════════════════════════════════════════════════════╝
                 
                                >  """))


fn.descri_raca(raca)
player = fn.criar_personagem(nome, raca)
cont = str(input("Aperte ENTER para continuar"))
fn.limpar_tela()
fn.iniciar(fase, player)
fs.fase_1(fase, player)