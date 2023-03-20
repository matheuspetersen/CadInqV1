import tkinter as tk
from tkinter import ttk


# Variáveis globais para armazenar as páginas de tela
pagina_de_boas_vindas = None
pagina_gerar_intimacao = None
pagina_adicionar_inqueritos = None


def cria_tela_boas_vindas():
    # Cria a tela de boas vindas
    global pagina_de_boas_vindas

    pagina_de_boas_vindas = tk.Frame()
    pagina_de_boas_vindas.pack(fill="both", expand=True)

    tk.Label(pagina_de_boas_vindas, text='Sistema de Controle Cartorário',
             font=("Times New Roman", 24)).pack(expand=True, fill="both", padx=10, pady=10, anchor="center")

    tk.Label(pagina_de_boas_vindas, text='Andrelândia - MG \nCriado por Matheus dos Santos Petersen Barreto - V1.0',
             font=("Times New Roman", 10)).pack(side="bottom")


def destroi_tela_boas_vindas():
    # Destroi a tela de boas vindas
    global pagina_de_boas_vindas
    if pagina_de_boas_vindas is not None:
        pagina_de_boas_vindas.destroy()
        pagina_de_boas_vindas = None


def cria_tela_gerar_intimacao():
    """Cria a tela de gerar intimações"""
    global pagina_gerar_intimacao

    # Cria um frame dentro da janela principal
    pagina_gerar_intimacao = tk.Frame()
    pagina_gerar_intimacao.pack(fill="both", expand=True)

    # Definindo estilos
    estilo = ttk.Style()
    estilo.configure('TEntry', background='#FFFFFF', foreground='#ffffff')

    # Título

    tk.Label(pagina_gerar_intimacao, text='Gerar Intimação',
             font=("Times New Roman", 18)).grid(column=1, row=0, padx=10, pady=10, columnspan=1)

    # Criando campos do formulário na coluna esquerda
    ttk.Label(pagina_gerar_intimacao, text="Número do PCnet").grid(column=0, row=1)
    pcnet_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    pcnet_entry.grid(column=1, row=1, padx=10, pady=10)

    ttk.Label(pagina_gerar_intimacao, text="Número do REDS").grid(column=0, row=2)
    reds_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    reds_entry.grid(column=1, row=2, padx=10, pady=10)

    ttk.Label(pagina_gerar_intimacao, text="Nome do Intimado").grid(column=0, row=3)
    nome_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    nome_entry.grid(column=1, row=3, padx=10, pady=10)

    ttk.Label(pagina_gerar_intimacao, text="Endereço do Intimado").grid(column=0, row=4)
    endereco_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    endereco_entry.grid(column=1, row=4, padx=10, pady=10)

    ttk.Label(pagina_gerar_intimacao, text="Telefone do Intimado").grid(column=0, row=5)
    telefone_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    telefone_entry.grid(column=1, row=5, padx=10, pady=10)

    # Criando campos do formulário na coluna direita
    ttk.Label(pagina_gerar_intimacao, text="Condição").grid(column=2, row=1)
    condicao_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    condicao_entry.grid(column=3, row=1, padx=10, pady=10)

    ttk.Label(pagina_gerar_intimacao, text="Nome da Vítima").grid(column=2, row=2)
    vitima_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    vitima_entry.grid(column=3, row=2, padx=10, pady=10)

    ttk.Label(pagina_gerar_intimacao, text="Delito Investigado").grid(column=2, row=3)
    delito_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    delito_entry.grid(column=3, row=3, padx=10, pady=10)

    ttk.Label(pagina_gerar_intimacao, text="Data da Oitiva").grid(column=2, row=4)
    data_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    data_entry.grid(column=3, row=4, padx=10, pady=10)

    ttk.Label(pagina_gerar_intimacao, text="Horário da Oitiva").grid(column=2, row=5)
    horario_entry = ttk.Entry(pagina_gerar_intimacao, style='TEntry',  width=30)
    horario_entry.grid(column=3, row=5, padx=10, pady=10)

    # Criando o botão
    gerar_intimacao_btn = ttk.Button(pagina_gerar_intimacao, text="Gerar Intimação")
    gerar_intimacao_btn.grid(column=0, row=6, padx=10, pady=10, columnspan=2)


def destroi_tela_gerar_intimacao():
    """Destroi a tela de gerar intimações"""
    global pagina_gerar_intimacao
    if pagina_gerar_intimacao is not None:
        pagina_gerar_intimacao.destroy()
        pagina_gerar_intimacao = None


def cria_tela_adicionar_inqueritos():
    """Cria a tela de adicionar inquéritos"""
    global pagina_adicionar_inqueritos

    # Cria um frame dentro da janela principal
    pagina_adicionar_inqueritos = tk.Frame()
    pagina_adicionar_inqueritos.pack(fill="both", expand=True)

    # Definindo estilos
    estilo = ttk.Style()
    estilo.configure('TEntry', background='#FFFFFF', foreground='#ffffff')

    # Título
    tk.Label(pagina_adicionar_inqueritos, text='Adicionar Inquéritos',
             font=("Times New Roman", 18)).pack(side="top", padx=10, pady=10)

    # Criando campos do formulário
    ttk.Label(pagina_adicionar_inqueritos, text="Número do inquérito").pack(padx=10, pady=10)
    inquerito_entry = ttk.Entry(pagina_adicionar_inqueritos, style='TEntry')
    inquerito_entry.pack()

    ttk.Label(pagina_adicionar_inqueritos, text="Nome do investigado").pack(padx=10, pady=10)
    investigado_entry = ttk.Entry(pagina_adicionar_inqueritos, style='TEntry')
    investigado_entry.pack()

    ttk.Label(pagina_adicionar_inqueritos, text="Descrição do delito").pack(padx=10, pady=10)
    delito_entry = ttk.Entry(pagina_adicionar_inqueritos, style='TEntry')
    delito_entry.pack()

    ttk.Label(pagina_adicionar_inqueritos, text="Data de abertura").pack(padx=10, pady=10)
    data_entry = ttk.Entry(pagina_adicionar_inqueritos, style='TEntry')
    data_entry.pack()

    ttk.Label(pagina_adicionar_inqueritos, text="Situação atual").pack(padx=10, pady=10)
    situacao_entry = ttk.Entry(pagina_adicionar_inqueritos, style='TEntry')
    situacao_entry.pack()

    # Criando o botão
    adicionar_inquerito_btn = ttk.Button(pagina_adicionar_inqueritos, text="Adicionar Inquérito")
    adicionar_inquerito_btn.pack(side='bottom', padx=10, pady=10)


def destroi_tela_adicionar_inqueritos():
    """Destroi a tela de adicionar inquéritos"""
    global pagina_adicionar_inqueritos
    if pagina_adicionar_inqueritos is not None:
        pagina_adicionar_inqueritos.destroy()
        pagina_adicionar_inqueritos = None
