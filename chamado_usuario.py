import ttkbootstrap as bootstrap

from ttkbootstrap.scrolled import ScrolledFrame

import controle

def chamado_init(root):

    def list_chamados():

        root.geometry("100x550")
        grid = bootstrap.Frame(root)
        grid.pack()
        label = bootstrap.Label(grid)
        label.pack(side='bottom', padx=30)
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

        bootstrap.Label(label2, text='Loja').grid(row=3, column=1, padx=10, pady=10),
        bootstrap.Label(label2, text='Usuario').grid(row=3, column=2, padx=10, pady=10),
        bootstrap.Label(label2, text='Resumo').grid(row=3, column=3, padx=10, pady=10),
        bootstrap.Label(label2, text='Detalhes').grid(row=3, column=4, padx=10, pady=10),
        bootstrap.Label(label2, text='Numero').grid(row=3, column=5, padx=10, pady=10),
        bootstrap.Label(label2, text='Status').grid(row=3, column=6, padx=10, pady=10),
        bootstrap.Label(label2, text='Obs').grid(row=3, column=7, padx=10, pady=10)

        ret = controle.exec_retrive_task()
        for i in range(len(ret)):
            loja.append(bootstrap.Entry(label2, width=5))
            loja[i].insert(0, ret[i]['loja'])
            loja[i].grid(row=4 + i, column=1, padx=10, pady=10)
            loja[i].config(state="readonly")
            usuario.append(bootstrap.Entry(label2))
            usuario[i].insert(0, ret[i]['usuario'])
            usuario[i].grid(row=4 + i, column=2, padx=10, pady=10)
            usuario[i].config(state="readonly")
            resumo.append(bootstrap.Entry(label2))
            resumo[i].insert(0, ret[i]['resumo'])
            resumo[i].grid(row=4 + i, column=3, padx=10, pady=10)
            resumo[i].config(state="readonly")
            detalhes.append(bootstrap.Entry(label2))
            detalhes[i].insert(0, ret[i]['detalhes'])
            detalhes[i].grid(row=4 + i, column=4, padx=10, pady=10)
            detalhes[i].config(state="readonly")
            numero.append(bootstrap.Entry(label2, width=10))
            numero[i].insert(0, ret[i]['numero'])
            numero[i].grid(row=4 + i, column=5, padx=10, pady=10)
            numero[i].config(state="readonly")
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
            obs[i].config(state="readonly")
    list_chamados()
