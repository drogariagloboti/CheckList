import ttkbootstrap as bootstrap
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification

import controle
import route_controler


def quest_edit(root, username):

    def voltar(grid):
        grid.destroy()
        route_controler.admin(root, username)

    toast = ToastNotification(
        title="Aviso",
        message="Peso Alterado",
        duration=3000,
        icon=''
    )

    def validar_numeros(char):
        return char.isdigit()

    validar_numeros_cmd = root.register(validar_numeros)

    def alterar(perg, peso, grid):
        for row in range(len(perg['obj'])):
            controle.update_weight(perg['obj'][row]['id'], peso[row].get())
        toast.message = 'Peso Alterado'
        toast.show_toast()
        grid.destroy()
        exc()

    def exc():

        root.geometry("650x550")
        perg = controle.retrivequestions()
        pergunta = []
        peso = []
        grid = bootstrap.Frame(root)
        grid.pack()
        label = bootstrap.Label(grid)
        label.pack(side='bottom', padx=30)
        butom_new = bootstrap.Button(label, text='Salvar Peso', command=lambda: alterar(perg, peso, grid))
        butom_new.grid(row=1, column=1, padx=40, pady=30, sticky='w')
        volta = bootstrap.Button(label, text='Voltar', command=lambda: voltar(grid))
        volta.grid(row=1, column=2, padx=40, pady=30, sticky='w')
        label2 = ScrolledFrame(grid, borderwidth=1, relief="solid", width=550, height=650, autohide=True)
        labelT = bootstrap.Label(label2, text='Questoes Peso')
        labelT.grid(row=0, column=1, padx=180, pady=10, sticky='e')
        label2.pack()
        for row in range(len(perg['obj'])):
            pergunta.append(bootstrap.Entry(label2, width=70))
            pergunta[row].insert(0, perg['obj'][row]['pergunta'])
            pergunta[row].config(state="readonly")
            pergunta[row].grid(row=3 + row, column=1, pady=10, padx=10)
            peso.append(bootstrap.Entry(label2, validate="key", validatecommand=(validar_numeros_cmd, '%S'), width=5))
            peso[row].insert(0, perg['obj'][row]['peso'])
            peso[row].grid(row=3 + row, column=2, pady=10, padx=10)

    exc()
