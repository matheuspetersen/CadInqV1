import tkinter as tk
import paginas as pg
from tkinter import *

# Cria a janela principal
janela = Tk()
janela.title("Sistema Cartorário")

# Tema instalado
janela.tk.call("source", "azure.tcl")
janela.tk.call("set_theme", "dark")

# Largura da tela do usuário
width = int(janela.winfo_screenwidth() * 0.7)
height = int(janela.winfo_screenheight() * 0.7)

# Encontrar o centro da tela
posx = janela.winfo_screenwidth()/2 - width/2
posy = janela.winfo_screenheight()/2 - height/2


# Define o tamanho da janela
janela.geometry("%dx%d+%d+%d" % (width,height, posx, posy-20) )
janela.minsize(width=width, height=height)

pg.cria_tela_boas_vindas()


def destruir_todas_paginas():
    pg.destroi_tela_gerar_intimacao()
    pg.destroi_tela_boas_vindas()
    pg.destroi_tela_adicionar_inqueritos()


# Funções para alternar entre as guias
def mostrar_pagina_de_boas_vindas():
    destruir_todas_paginas()
    pg.cria_tela_boas_vindas()


def mostrar_pagina_gerar_intimacoes():
    destruir_todas_paginas()
    pg.cria_tela_gerar_intimacao()


def mostrar_pagina_adicionar_inquerito():
    destruir_todas_paginas()
    pg.cria_tela_adicionar_inqueritos()


# ----------------------------------------------------------------------------------------------
# -------------------------------------------MENU-----------------------------------------------
# ----------------------------------------------------------------------------------------------
menubar = tk.Menu(janela)
janela.config(menu=menubar)


# Comandos do menu Arquivo
def fechar():
    janela.quit()


def mostrar_inicio():
    mostrar_pagina_de_boas_vindas()


# Comandos do menu Procedimentos
def adicionar_procedimento():
    mostrar_pagina_adicionar_inquerito()


def excluir_procedimento():
    return


def consultar_procedimento():
    return


# Comandos do menu Intimação
def gerar_intimacoes():
    mostrar_pagina_gerar_intimacoes()


# Comandos do menu Modelos
def abrir_termo_entrega():
    return


def abrir_termo_representacao():
    return


def abrir_certidao_generica():
    return


# Criação dos menus
arquivo = tk.Menu(menubar, tearoff=0)
procedimentos = tk.Menu(menubar, tearoff=0)
intimacao = tk.Menu(menubar, tearoff=0)
modelos = tk.Menu(menubar, tearoff=0)

# Adiciona os comandos aos menus
arquivo.add_command(label="Início", command=mostrar_inicio)
arquivo.add_command(label="Fechar", command=fechar)
procedimentos.add_command(label="Adicionar", command=adicionar_procedimento)
procedimentos.add_command(label="Excluir", command=excluir_procedimento)
procedimentos.add_command(label="Consultar", command=consultar_procedimento)
intimacao.add_command(label="Gerar", command=gerar_intimacoes)
modelos.add_command(label="Termo de Entrega", command=abrir_termo_entrega)
modelos.add_command(label="Termo de Representação", command=abrir_termo_representacao)
modelos.add_command(label="Certidão Genérica", command=abrir_certidao_generica)

# Adiciona os menus à barra de menus
menubar.add_cascade(label="Arquivo", menu=arquivo)
menubar.add_cascade(label="Procedimentos", menu=procedimentos)
menubar.add_cascade(label="Intimação", menu=intimacao)
menubar.add_cascade(label="Modelos", menu=modelos)

# Finaliza
janela.mainloop()
