import os 
os.system("cls")

import funcoes as fn
import fases as fs

fase = 1
player = fn.criar_personagem()
fn.limpar_tela()
fn.iniciar(fase, player)
fs.fase_1(fase, player)