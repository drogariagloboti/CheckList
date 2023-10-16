import controle
from controle import exec_retrive_ansers


def mount(perg, dropmenu, entry, username, date, varcheck):
    next_r = controle.exec_nex_anser()
    controle.exec_insert_quest(username, date.entry.get())
    next_q = controle.exec_nex_quest()
    for i in range(11):
        controle.exec_insert_vinc(next_q, next_r + i + 1)
        controle.exec_insert_anser(perg['obj'][i]['id'], dropmenu[i].get(), entry[i].get(), varcheck[i].get())


def verif(dropmenu, entry, username, date, varcheck):
    ret = controle.exec_verif_quest(username, date.entry.get())
    if ret['bool']:
        obj = exec_retrive_ansers(ret['questionario'])
        x = 0
        for i in obj['obj']:
            if i['status_execucao'] == 'Executado c/Sucesso':
                dropmenu[x].current(0)
            elif i['status_execucao'] == 'Executado c/Pendência':
                dropmenu[x].current(1)
            elif i['status_execucao'] == 'Não Executado':
                dropmenu[x].current(2)
            if i['resposta_feedback'] == 'Sim':
                varcheck[x].current(0)
            elif i['resposta_feedback'] == 'Não':
                varcheck[x].current(1)
            entry[x].delete(0, 'end')
            entry[x].insert(0, i['feedback'])
            x = x + 1
        return True
    else:
        for i in range(11):
            dropmenu[i].set('')
            varcheck[i].current(1)
            entry[i].delete(0, 'end')
        return False

def verif_adm(status_resposta, resposta_obs, resposta_feedback, username, date, usuario, butao, questionario_id):
    ret = controle.exec_verif_quest(username, date.entry.get())
    if ret['bool']:
        questionario_id.delete(0, 'end')
        questionario_id.insert(0, ret['questionario'])
        obj = exec_retrive_ansers(ret['questionario'])
        x = 0
        for i in obj['obj']:
            usuario[x].config(text=f"Resposta do Usuario: {username}")
            status_resposta[x].config(text=f"Status Resposta: {i['status_execucao']}")
            resposta_obs[x].config(text=f"OBS: {i['feedback']}")
            resposta_feedback[x].config(text=f"FeedBack: {i['resposta_feedback']}")
            butao[x].pack(side='bottom')
            x = x + 1
    else:
        x = 0
        for i in range(11):
            usuario[x].config(text="")
            status_resposta[x].config(text="")
            resposta_obs[x].config(text="")
            resposta_feedback[x].config(text="")
            x = x + 1


def update_checklist(dropmenu, entry, username, date, varcheck):
    ret = controle.exec_verif_quest(username, date.entry.get())
    obj = exec_retrive_ansers(ret['questionario'])
    x = 0
    for i in obj['obj']:
        controle.exec_update_anser(i['id'], dropmenu[x].get(), entry[x].get(), varcheck[x].get())
        x = x + 1
    controle.exec_update_date(ret['questionario'])


def pendencia(username):
    ret = controle.exec_verif_quest_pendencia(username)
    if ret[0]['bool']:
        obj = []
        for i in ret:
            obj.append(controle.exec_select_pendencia(i['questionario']))
        return obj
    return None

def retriv_usrs(date):
    x = controle.exec_retrive_users(date.entry.get())
    return x
