import ttkbootstrap as bootstrap
from ttkbootstrap.toast import ToastNotification

import controle

def gen(username, questionario, date, root):

    def enviar_feedback():
        controle.exec_insert_pend(username, questionario.get(), resp_quest5.get(), dropmenu.get(), resp_quest1.get(), resp_quest2.get(), resp_quest3.get(), resp_quest4.get(), date.entry.get())
        toast.show_toast()
        pend.destroy()

    toast = ToastNotification(
        title="Aviso",
        message="Pendencia Submetido",
        duration=3000,
        icon=''
    )

    pend = bootstrap.Toplevel(root)
    pend.title('Visualizar Pendencia')
    pend.size = [450, 850]
    quet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    label_pend_titl = bootstrap.Label(pend, text='Enviar FeedBack')
    label_pend_titl.grid(row=0, column=0, columnspan=2, pady=20)

    label_q = bootstrap.Label(pend, text='Questão: ')
    label_q.grid(row=1, column=0, sticky='w')
    dropmenu = bootstrap.Combobox(pend, width=40, values=quet)
    dropmenu.config(state="readonly")
    dropmenu.grid(row=1, column=1, sticky='w')

    quest_1 = bootstrap.Label(pend, text='Preench. em Atraso? ')
    quest_1.grid(row=3, column=0, sticky='w')
    resp_quest1 = bootstrap.Combobox(pend, width=50, values=['Não', 'Sim'])
    resp_quest1.config(state="readonly")
    resp_quest1.grid(row=3, column=1, sticky='w')

    quest_2 = bootstrap.Label(pend, text='Status Entrega: ')
    quest_2.grid(row=4, column=0, sticky='w')
    resp_quest2 = bootstrap.Combobox(pend, width=50, values=['No Prazo', 'Em atraso', 'Atraso/Apuração'])
    resp_quest2.config(state="readonly")
    resp_quest2.grid(row=4, column=1, sticky='w')

    quest_3 = bootstrap.Label(pend, text='Parecer Geral: ')
    quest_3.grid(row=5, column=0, sticky='w')
    resp_quest3 = bootstrap.Combobox(pend, width=50, values=['Conf.c/Sucesso', 'Conf.c/Erros', 'Conf.c/Erros Ident.'])
    resp_quest3.config(state="readonly")
    resp_quest3.grid(row=5, column=1, sticky='w')

    quest_4 = bootstrap.Label(pend, text='Baixa das Pendências: ')
    quest_4.grid(row=6, column=0, sticky='w')
    resp_quest4 = bootstrap.Combobox(pend, width=50, values=['Resolvido', 'Em Aberto', 'Falha Sistêmatica'])
    resp_quest4.config(state="readonly")
    resp_quest4.grid(row=6, column=1, sticky='w')

    quest_5 = bootstrap.Label(pend, text='Retorno FeedBack:')
    quest_5.grid(row=7, column=0, sticky='w')
    resp_quest5 = bootstrap.Entry(pend, width=50)
    resp_quest5.grid(row=7, column=1, sticky='w')

    botao_enviar = bootstrap.Button(pend, text='Enviar FeedBack', command=enviar_feedback)
    botao_enviar.grid(row=8, column=0, columnspan=2, pady=10)

    pend.mainloop()
