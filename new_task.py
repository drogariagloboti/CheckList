import ttkbootstrap as bootstrap
import tkinter as tk

from ttkbootstrap.toast import ToastNotification

import controle

import task as tk_re


def new_task(root, username, grinder):
    toast = ToastNotification(
        title="Aviso",
        message="Chamado Cadastrado",
        duration=3000,
        icon=''
    )

    def enviar_task(*args):
        controle.exec_create_task(username, resp_loja.get(),
                                  resp_resumo.get(), resp_detalhe.get("1.0", tk.END),
                                  resp_numero.get(), resp_status.get(), resp_obs.get())
        toast.show_toast()
        grinder.destroy()
        tk_re.reup(root, username)
        task.destroy()

    def limitar_input(*args):
        value = entry.get()
        value = ''.join(filter(str.isdigit, value))  # Filtrar apenas os dígitos
        entry.set(value[:3])

    def validar_numeros(char):
        return char.isdigit()

    task = bootstrap.Toplevel(root)
    validar_numeros_cmd = task.register(validar_numeros)
    task.title('Novo Chamado')
    task.geometry("450x550")
    entry = tk.StringVar()
    entry.trace('w', limitar_input)

    label_cham_titl = bootstrap.Label(task, text='Enviar FeedBack')
    label_cham_titl.grid(row=0, column=0, columnspan=2, pady=20)
    label_loja = bootstrap.Label(task, text='Loja: ')
    label_loja.grid(row=1, column=0, sticky='w')
    resp_loja = bootstrap.Entry(task, width=50, validate="key", validatecommand=(validar_numeros_cmd, '%S'), textvariable=entry)
    resp_loja.grid(row=2, column=1, sticky='w')
    label_resumo = bootstrap.Label(task, text='Resumo: ')
    label_resumo.grid(row=3, column=0, sticky='w')
    resp_resumo = bootstrap.Entry(task, width=50)
    resp_resumo.grid(row=4, column=1, sticky='w')
    label_detalhe = bootstrap.Label(task, text='Detalhes: ')
    label_detalhe.grid(row=5, column=0, sticky='n')
    resp_detalhe = bootstrap.Text(task, height=5, width=30)
    resp_detalhe.grid(row=6, column=1, sticky='w')
    label_numero = bootstrap.Label(task, text='Numero: ')
    label_numero.grid(row=7, column=0, sticky='w')
    resp_numero = bootstrap.Entry(task, width=50, validate="key", validatecommand=(validar_numeros_cmd, '%S'))
    resp_numero.grid(row=8, column=1, sticky='w')
    label_status = bootstrap.Label(task, text='Status: ')
    label_status.grid(row=9, column=0, sticky='w')
    resp_status = bootstrap.Combobox(task, width=48, values=['Solicitação aberta', 'Aberto', 'Resolvido'])
    resp_status.config(state="readonly")
    resp_status.grid(row=10, column=1, sticky='w')
    label_obs = bootstrap.Label(task, text='Obs: ')
    label_obs.grid(row=11, column=0, sticky='w')
    resp_obs = bootstrap.Entry(task, width=50)
    resp_obs.grid(row=12, column=1, sticky='w')
    enviar = bootstrap.Button(task, width=30, command=enviar_task, text="Enviar")
    enviar.grid(row=13, column=1, sticky='s', pady=10)

    task.mainloop()