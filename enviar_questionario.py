from datetime import date as data
from tkinter import *
import ttkbootstrap as bootstrap
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.toast import ToastNotification
import controle
import jsoncreate
import route_controler


def init(root, username):
    root.geometry("950x650")
    colors = root.style.colors

    def voltar():
        grid.destroy()
        grid_pendencia.destroy()
        grind_log.destroy()
        route_controler.route(root, username)

    def update():
        jsoncreate.update_checklist(dropmenu, entry, username, date, varcheck)
        toast.show_toast()

    def update_verifi():
        questionario = jsoncreate.verif(dropmenu, entry, username, date, varcheck)
        if questionario:
            buton.config(command=update)
        else:
            buton.config(command=execut)

    def premountjson():
        jsoncreate.mount(perg, dropmenu, entry, username, date, varcheck)

    toast = ToastNotification(
        title="Aviso",
        message="CheckList Submetido",
        duration=3000,
        icon=''
    )

    def date_event(event):
        update_verifi()

    grid = bootstrap.Frame(root)
    grind_log = bootstrap.Frame(grid)
    grid_pendencia = bootstrap.Frame(grid)
    tab = []
    label = []
    tex2 = []
    text = []
    labeltxt = []
    dropdownvarcheck = ['Sim', 'Não']
    varcheck = []
    dropdown = ['Executado c/Sucesso', 'Executado c/Pendência', 'Não Executado']
    dropmenu = []
    entry = []
    perg = controle.retrivequestions()

    def execut():
        premountjson()
        toast.show_toast()
        update_verifi()

    notebooks = bootstrap.Notebook(grind_log)
    notebooks.pack(pady=5)
    for i in range(11):
        tab.append(bootstrap.Frame(notebooks))
        tab[i].pack(pady=150, padx=150)
        label.append(bootstrap.Label(tab[i]))
        text.append(bootstrap.Label(tab[i], text=f"{perg['obj'][i]['pergunta']}"))
        text[i].pack(pady=0, side='top')
        dropmenu.append(bootstrap.Combobox(tab[i], values=dropdown))
        dropmenu[i].config(state="readonly")
        dropmenu[i].pack(side='top')
        tex2.append(bootstrap.Label(tab[i], text=f"FeedBack Valido"))
        tex2[i].pack(pady=5, side='top')
        entry.append(bootstrap.Entry(tab[i], width=50))
        entry[i].pack(pady=20, side='top', ipadx=20, ipady=30)
        labeltxt.append(bootstrap.Label(tab[i], text='Resposta FeedBack'))
        labeltxt[i].pack(pady=5)
        varcheck.append(bootstrap.Combobox(tab[i], values=dropdownvarcheck))
        varcheck[i].config(state="readonly")
        varcheck[i].pack(side='top')
        varcheck[i].current(1)
        label[i].pack(pady=40, padx=150, side='top')
        notebooks.add(tab[i], text=f"{i + 1}")
    labeltime = Label(grind_log)
    date = bootstrap.DateEntry(labeltime, startdate=data.today(), dateformat="%Y-%m-%d")
    date.bind('<FocusIn>', date_event)
    date.pack()
    labeltime.pack()
    labelaux = bootstrap.Label(grind_log)
    labelaux.pack()
    buton = bootstrap.Button(labelaux, text='Enviar', command=execut)
    buton.pack(pady=10, padx=5, side='left')
    voltar = bootstrap.Button(labelaux, text='Voltar', command=voltar)
    voltar.pack(pady=10)
    labename = Label(grind_log, text=username)
    labename.pack(side='top')
    update_verifi()
    grind_log.pack(side='left', pady=10)

    data_table = jsoncreate.pendencia(username)
    row = []
    coldata = [
        {'text': 'data pendencia', "stretch": False, "width": 100},
        {'text': 'Pendência', "width": 180},
        {'text': 'questão', "width": 100}
    ]
    if data_table is not None:
        for i in data_table:
            if i['bool'] is True:
                for j in i['obj']:
                    row.append((j['datapendencia'], j['pendencia'], j['questao']))
        treeview = Tableview(master=grid_pendencia, rowdata=row, coldata=coldata, paginated=True, height=30,
                             searchable=False, bootstyle='primary', stripecolor=(colors.light, None), )
    else:
        treeview = Tableview(master=grid_pendencia, coldata=coldata, paginated=True, height=30,
                             searchable=False, bootstyle='primary', stripecolor=(colors.light, None), )
    treeview.pack(side='left')
    grid_pendencia.pack(side='left')
    grid.pack()