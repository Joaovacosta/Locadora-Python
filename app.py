import os

from funcoes import *
from classes import *

while True:
    try:
        os.system("cls")
        print("BEM VINDO AO SISTEMA DE LOCADORA")
        print("SELECIONE A OPÇÃO QUE DESEJA")
        print("1 - LISTAR")
        print("2 - ALUGAR")
        print("3 - DEVOLVER")
        print("4 - ADICIONAR ITEM")
        print("0 - SAIR")
        escolha = int(input("--> "))
        
        match escolha:
            case 1:
                listar()
            case 2:
                alugar()
            case 3:
                devolucao()
            case 4:
                additem()
            case 0:
                print("SAINDO...")
                os.system("pause")
                break
            case _:
                print("ESCOLHA INVALIDA")
                os.system("pause")

    except ValueError:
        print("Insira apenas números.")
        os.system("pause")