import ttkbootstrap as bootstrap
from tkinter import *

import logoff
import questoes
import task
import enviar_questionario
import admin_view

def route(root, username):
    root.geometry("500x550")

    def select_logoff():
        grid.destroy()
        logoff.initiation(root)

    def select_checkList():
        grid.destroy()
        enviar_questionario.init(root, username)

    def select_chamados():
        grid.destroy()
        task.chamado_init(root, username, 'usuario')

    grid = bootstrap.Frame(root)
    router = Label(grid, text='Escolha o Sistema')
    router.pack(side='top', pady=30)
    selecter = Label(grid)
    selecter.pack(pady=50, side='top')
    buton_select = bootstrap.Button(selecter, text='CheckList', command=select_checkList)
    buton_select.pack()
    buton_select = bootstrap.Button(selecter, text='Chamados', command=select_chamados)
    buton_select.pack(pady=10)
    buton_logoss = bootstrap.Button(selecter, text='Sair', command=select_logoff)
    buton_logoss.pack(pady=10)
    grid.pack()


def admin(root, username):
    root.geometry("500x550")

    def select_logoff():
        grid.destroy()
        logoff.initiation(root)

    def select_questoes():
        grid.destroy()
        questoes.quest_edit(root,username)

    def select_chamados():
        grid.destroy()
        task.chamado_init(root, username, 'admin')

    def select_checkList():
        grid.destroy()
        admin_view.init_adm(root, username)

    grid = bootstrap.Frame(root)
    router = Label(grid, text='Fiscal do Sistema')
    router.pack(side='top', pady=30)
    selecter = Label(grid)
    selecter.pack(pady=50, side='top')
    buton_select = bootstrap.Button(selecter, text='Check List ADM', command=select_checkList)
    buton_select.pack()
    buton_select_chamados = bootstrap.Button(selecter, text='Chamados', command=select_chamados)
    buton_select_chamados.pack(pady=10)
    buton_select_chamados = bootstrap.Button(selecter, text='Questões Peso', command=select_questoes)
    buton_select_chamados.pack(pady=10)
    buton_logoss = bootstrap.Button(selecter, text='Sair', command=select_logoff)
    buton_logoss.pack(pady=10)
    grid.pack()
