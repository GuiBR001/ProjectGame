import os 
os.system("cls")

import funcoes as fn
import fases as fs
import icons as ic


fase = 1

nome = str(input("""
                                                Escolha um nome: """)).upper()
raca = int(input("""
                    1- Esqueleto Flamejante    2- Anjo Da Morte    3- Mago Ancião
                                                            
                                                        Escolha sua raça:
                    """))
new_raca = ""

fn.descri_raca(raca)
player = fn.criar_personagem(nome, new_raca)
cont = str(input("Aperte ENTER para continuar"))

while cont != "":
    print("Digite ENTER!")
else:
    fn.limpar_tela()
    fn.iniciar(fase, player)
    fs.fase_1(fase, player)