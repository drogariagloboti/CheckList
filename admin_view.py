from datetime import date as data
from tkinter import *
import ttkbootstrap as bootstrap

import route_controler
from pend_adm_window import pd_view

import controle
import feedback_window
import jsoncreate

def init_adm(root, username):
    def voltar():
        grid.destroy()
        route_controler.admin(root, username)

    def list_pend():
        pd_view(username, root)

    def new_feed():
        feedback_window.gen(username, questionario_id, date, root)

    def retriv_users(event):
        ret = jsoncreate.retriv_usrs(date)
        ret2 = []
        for f in ret:
            ret2.append(f['user'])
        dropmenu.config(values=ret2)
        if not ret:
            for x in range(11):
                usuario[x].config(text="")
                status_resposta[x].config(text="")
                resposta_obs[x].config(text="")
                resposta_feedback[x].config(text="")
                butao_pendencia[x].pack_forget()
        dropmenu.set('')

    def retriv_ans():
        jsoncreate.verif_adm(status_resposta, resposta_obs, resposta_feedback, dropmenu.get(), date, usuario,
                             butao_pendencia, questionario_id)

    root.geometry("950x550")
    # variaveis
    grid = bootstrap.Frame(root)
    grind_log = bootstrap.Frame(grid)
    grid_pendencia = bootstrap.Frame(grid)
    tab = []
    label = []
    resposta_obs = []
    usuario = []
    pergunta = []
    resposta_feedback = []
    status_resposta = []
    perg = controle.retrivequestions()
    butao_pendencia = []

    labeln = bootstrap.Label(grind_log)
    label2n = bootstrap.Label(grind_log)
    date = bootstrap.DateEntry(labeln, startdate=data.today(), dateformat="%Y-%m-%d")
    buscar = bootstrap.Button(label2n, text='Buscar', command=retriv_ans)
    volta = bootstrap.Button(label2n, text='Voltar', command=voltar)
    date.bind('<FocusIn>', retriv_users)
    date.pack(side='left')
    dropmenu = bootstrap.Combobox(labeln, width=40)
    dropmenu.pack()
    buscar.pack(side='left', padx=5)
    volta.pack()
    labeln.pack(side='top')
    label2n.pack(side='top')
    labename = Label(grind_log, text=username)
    labename.pack(side='bottom')
    questionario_id = bootstrap.Entry(grind_log)

    notebooks = bootstrap.Notebook(grind_log)
    notebooks.pack(pady=5)
    for i in range(11):
        tab.append(bootstrap.Frame(notebooks))
        tab[i].pack(pady=150, padx=150)
        label.append(bootstrap.Label(tab[i]))
        pergunta.append(bootstrap.Label(tab[i], text=f"{perg['obj'][i]['pergunta']}"))
        pergunta[i].pack(pady=0, side='top')
        usuario.append(bootstrap.Label(tab[i], text=""))
        usuario[i].pack(pady=5, side='top')
        status_resposta.append(bootstrap.Label(tab[i], text=''))
        status_resposta[i].pack(pady=5, side='top')
        resposta_obs.append(bootstrap.Label(tab[i], text=''))
        resposta_obs[i].pack(pady=5, side='top')
        resposta_feedback.append(bootstrap.Label(tab[i], text=''))
        resposta_feedback[i].pack(pady=5, side='top')
        label[i].pack(pady=40, padx=150, side='top')
        butao_pendencia.append(bootstrap.Button(tab[i], text=f'Gerar FeedBack', command=lambda: new_feed()))
        notebooks.add(tab[i], text=f"{i + 1}")

    button_list = bootstrap.Button(grind_log, text='Visualizar pendencias', command=list_pend)
    button_list.pack(side='bottom')

    grind_log.pack(side='left')
    grid_pendencia.pack(side='left')
    grid.pack()
