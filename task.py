import ttkbootstrap as bootstrap
import tkinter as tk

from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification

import controle
import route_controler
from new_task import new_task


def chamado_init(root, username, tipo):
    toast = ToastNotification(
        title="Aviso",
        message="Pendencia Alterado",
        duration=3000,
        icon=''
    )

    def voltar(grid):
        if tipo == 'usuario':
            grid.destroy()
            route_controler.route(root, username)
        else:
            grid.destroy()
            route_controler.admin(root, username)

    def handle_excluir(idx, ret, label2):
        controle.exec_delete_task(ret[idx]['id'])
        toast.message = 'Chamado Deletado'
        toast.show_toast()
        label2.destroy()
        chamado_init(root, username, tipo)

    def handle_salvar(idx, ret, label2, loja, resumo, detalhes, numero, status, obs):
        controle.exec_update_task(ret[idx]['id'], loja, resumo, detalhes, numero, status, obs)
        toast.message = 'Chamado Alterado'
        toast.show_toast()
        label2.destroy()
        chamado_init(root, username, tipo)

    def limitar_input():
        value = entry.get()
        value = ''.join(filter(str.isdigit, value))  # Filtrar apenas os dígitos
        entry.set(value[:3])

    def validar_numeros(char):
        return char.isdigit()

    validar_numeros_cmd = root.register(validar_numeros)
    entry = tk.StringVar()
    entry.trace('w', limitar_input)

    def novo_chamado(grinder):
        new_task(root, username, grinder)

    def list_chamados():

        root.geometry("1200x550")
        grid = bootstrap.Frame(root)
        grid.pack()
        label = bootstrap.Label(grid)
        label.pack(side='bottom', padx=30)
        butom_new = bootstrap.Button(label, text='Novo Chamado', command=lambda: novo_chamado(grid))
        butom_new.grid(row=1, column=1, pady=30, sticky='w')
        volta = bootstrap.Button(label, text='Voltar', command=lambda: voltar(grid))
        volta.grid(row=1, column=2, padx=40, pady=30, sticky='w')
        # variaveis
        label2 = ScrolledFrame(grid, borderwidth=1, relief="solid", width=1250, height=950, autohide=True)
        labelT = bootstrap.Label(label2, text='Chamados')
        labelT.grid(row=1, column=5, padx=40, pady=10, sticky='w')
        label2.pack()
        loja = []
        usuario = []
        resumo = []
        detalhes = []
        numero = []
        status = []
        obs = []
        bt_save = []
        bt_del = []

        bootstrap.Label(label2, text='Loja').grid(row=3, column=1, padx=10, pady=10),
        bootstrap.Label(label2, text='Usuario').grid(row=3, column=2, padx=10, pady=10),
        bootstrap.Label(label2, text='Resumo').grid(row=3, column=3, padx=10, pady=10),
        bootstrap.Label(label2, text='Detalhes').grid(row=3, column=4, padx=10, pady=10),
        bootstrap.Label(label2, text='Numero').grid(row=3, column=5, padx=10, pady=10),
        bootstrap.Label(label2, text='Status').grid(row=3, column=6, padx=10, pady=10),
        bootstrap.Label(label2, text='Obs').grid(row=3, column=7, padx=10, pady=10)

        ret = controle.exec_retrive_task()
        for i in range(len(ret)):
            loja.append(bootstrap.Entry(label2, validate="key", validatecommand=(validar_numeros_cmd, '%S'), width=5))
            loja[i].insert(0, ret[i]['loja'])
            loja[i].grid(row=4 + i, column=1, padx=10, pady=10)
            usuario.append(bootstrap.Entry(label2))
            usuario[i].insert(0, ret[i]['usuario'])
            usuario[i].grid(row=4 + i, column=2, padx=10, pady=10)
            resumo.append(bootstrap.Entry(label2))
            resumo[i].insert(0, ret[i]['resumo'])
            resumo[i].grid(row=4 + i, column=3, padx=10, pady=10)
            detalhes.append(bootstrap.Entry(label2))
            detalhes[i].insert(0, ret[i]['detalhes'])
            detalhes[i].grid(row=4 + i, column=4, padx=10, pady=10)
            numero.append(bootstrap.Entry(label2, width=10))
            numero[i].insert(0, ret[i]['numero'])
            numero[i].grid(row=4 + i, column=5, padx=10, pady=10)
            status.append(bootstrap.Combobox(label2, values=['Solicitação aberta', 'Aberto', 'Resolvido']))
            status[i].config(state="readonly")
            if ret[i]['status'] == 'Solicitação aberta':
                status[i].current(0)
            if ret[i]['status'] == 'Aberto':
                status[i].current(1)
            if ret[i]['status'] == 'Resolvido':
                status[i].current(2)
            status[i].grid(row=4 + i, column=6, padx=10, pady=10)
            obs.append(bootstrap.Entry(label2))
            obs[i].insert(0, ret[i]['obs'])
            obs[i].grid(row=4 + i, column=7, padx=10, pady=10)
            bt_save.append(bootstrap.Button(label2, width=10, text='Salvar',
                                            command=lambda idx=i: handle_salvar(idx, ret, grid, loja[idx].get(),
                                                                                resumo[idx].get(), detalhes[idx].get(),
                                                                                numero[idx].get(), status[idx].get(), obs[idx].get())))
            bt_save[i].grid(row=4 + i, column=8, padx=10, pady=10)
            bt_del.append(bootstrap.Button(label2, width=10, text='Deletar',
                                           command=lambda idx=i: handle_excluir(idx, ret, grid)))
            bt_del[i].grid(row=4 + i, column=9, pady=10)

    list_chamados()


def reup(root, username, tipo):
    chamado_init(root, username, tipo)
