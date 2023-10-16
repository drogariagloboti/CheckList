import tkinter

import ttkbootstrap as bootstrap
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification

from controle import exec_select_pend_adm, exec_update_pend, exec_excl_pend


def pd_view(username, root):
    toast = ToastNotification(
        title="Aviso",
        message="Pendencia Alterado",
        duration=3000,
        icon=''
    )

    pend = bootstrap.Toplevel(root)
    pend.title('Visualizar Pendencia')
    pend.size = [450, 950]
    #pend.iconbitmap('logo_globo.ico')
    ret = exec_select_pend_adm(username)
    main_label = bootstrap.Label(pend, text='Lista pendencia')
    main_label.pack(side='top')

    def handle_atualizar(indice, retu, questao, descr, date, atraso, status, parecer, baixa):
        exec_update_pend(username, retu[indice]['questionario'], questao[indice].get(), descr[indice].get(),
                         date[indice].entry.get(), atraso[indice].get(), status[indice].get(), parecer[indice].get(),
                         baixa[indice].get(), retu[indice]['data questionario'], retu[indice]['questao'])
        toast.show_toast()
        view()

    def handle_excluir(indice, retu, questao, date, labele):
        exec_excl_pend(username, retu[indice]['questionario'], questao[indice].get(), date[indice].entry.get())
        toast.message = 'Pendencia Deletada'
        toast.show_toast()
        labele[indice].destroy()

    def view():
        label = tkinter.Label(pend, width=950, height=450)
        sf = ScrolledFrame(label, autohide=True, height=450, width=950)
        labele = []
        date = []
        questao = []
        descr = []
        atraso = []
        status = []
        parecer = []
        baixa = []
        quet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        atualizar = []
        excluir = []

        for i in range(len(ret)):
            labele.append(bootstrap.Label(sf))
            date.append(
                bootstrap.DateEntry(labele[i], startdate=ret[i]['data questionario'], dateformat="%Y-%m-%d", width=10))
            date[i].pack(side='left')
            questao.append(bootstrap.Combobox(labele[i], width=5, values=quet))
            questao[i].current(ret[i]['questao'] - 1)
            questao[i].pack(side='left')
            descr.append(bootstrap.Entry(labele[i]))
            descr[i].delete(0, 'end')
            descr[i].insert(0, ret[i]['descricao'])
            descr[i].pack(side='left')
            atraso.append(bootstrap.Combobox(labele[i], width=5, values=['Sim', 'Não']))
            atraso[i].config(state="readonly")
            if ret[i]['atraso'] == 'Sim':
                atraso[i].current(0)
            else:
                atraso[i].current(1)
            atraso[i].pack(side='left')
            status.append(bootstrap.Combobox(labele[i], width=10, values=['No Prazo', 'Em atraso', 'Atraso/Apuração']))
            status[i].config(state="readonly")
            if ret[i]['status'] == 'No Prazo':
                status[i].current(0)
            elif ret[i]['status'] == 'Em atraso':
                status[i].current(1)
            else:
                status[i].current(2)
            status[i].pack(side='left')
            parecer.append(
                bootstrap.Combobox(labele[i], width=20,
                                   values=['Conf.c/Sucesso', 'Conf.c/Erros', 'Conf.c/Erros Ident.']))
            parecer[i].config(state="readonly")
            if ret[i]['parecer'] == 'Conf.c/Sucesso':
                parecer[i].current(0)
            elif ret[i]['parecer'] == 'Conf.c/Erros':
                parecer[i].current(1)
            else:
                parecer[i].current(2)
            parecer[i].pack(side='left')
            baixa.append(
                bootstrap.Combobox(labele[i], width=20, values=['Resolvido', 'Em Aberto', 'Falha Sistêmatica']))
            baixa[i].config(state="readonly")
            if ret[i]['baixa pendencia'] == 'Resolvido':
                baixa[i].current(0)
            elif ret[i]['baixa pendencia'] == 'Em Aberto':
                baixa[i].current(1)
            else:
                baixa[i].current(2)
            atualizar.append(
                bootstrap.Button(labele[i], width=10, text='Atualizar',
                                 command=lambda idx=i: handle_atualizar(i, ret, questao, descr, date, atraso, status,
                                                                        parecer, baixa)))
            excluir.append(
                bootstrap.Button(labele[i], width=10, text='Excluir',
                                 command=lambda idx=i: handle_excluir(idx, ret, questao, date, labele)))
            baixa[i].pack(side='left')
            atualizar[i].pack(side='left')
            excluir[i].pack(side='left')
            labele[i].pack(side='top')

        sf.pack()
        label.pack()

    view()
    pend.mainloop()
