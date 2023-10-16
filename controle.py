from connect import postgressbd
import models


def retrivequestions():
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.perguntas())
    verif = cursor.fetchall()
    ret = []
    if verif is None:
        con.commit()
        con.close()
        return {'bool': False, 'obj': 'erro ao recuperar mensagens'}

    for i in verif:
        ret.append({'id': i[0], 'pergunta': i[1], 'peso': i[2]})
    con.commit()
    con.close()
    return {'bool': True, 'obj': ret}


def exec_log(userid, senha):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.log(userid, senha))
    verif = cursor.fetchone()
    if verif is None:
        con.commit()
        con.close()
        return {'bool': False, 'obj': 'Usuario inexistente'}
    else:
        ret = {'id': verif[0], 'nome': verif[1]}
        con.commit()
        con.close()
        return {'bool': True, 'obj': ret}


def exec_nex_quest():
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.nex_quest())
    verif = cursor.fetchone()
    ret = verif[0]
    con.commit()
    con.close()
    return ret


def exec_nex_anser():
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.nex_anser())
    verif = cursor.fetchone()
    ret = verif[0]
    con.commit()
    con.close()
    return ret


def exec_nex_vinc():
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.nex_vinc())
    verif = cursor.fetchone()
    ret = verif[0]
    con.commit()
    con.close()
    return ret


def exec_verif_quest(usuario_id, data_questionario):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.verif_quest(usuario_id, data_questionario))
    verif = cursor.fetchone()
    con.commit()
    con.close()
    return {'bool': False, 'questionario': ''} if verif is None else {'bool': True, 'questionario': verif[0]}


def exec_verif_quest_pendencia(usuario_id):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.verif_quest_pendencia(usuario_id))
    verif = cursor.fetchall()
    row = []
    if len(verif) <= 0:
        row.append({'bool': False, 'questionario': ''})
        con.commit()
        con.close()
        return row
    for i in verif:
        row.append({'bool': True, 'questionario': i[0]})
    con.commit()
    con.close()
    return row


def exec_retrive_ansers(questionario_id):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.retrive_ansers(questionario_id))
    verif = cursor.fetchall()
    ret = []
    if not verif:
        con.commit()
        con.close()
        return {'bool': False, 'obj': ''}
    else:
        for i in verif:
            ret.append(
                {'id': i[0], 'questao': i[1], 'status_execucao': i[2], 'feedback': i[3], 'resposta_feedback': i[4]})
        con.commit()
        con.close()
        return {'bool': True, 'obj': ret}


def exec_insert_quest(usuario_id, data_questionario):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.insert_quest(usuario_id, data_questionario))
    con.commit()
    con.close()


def exec_insert_vinc(quest_id, resp_id):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.insert_vinc(quest_id, resp_id))
    con.commit()
    con.close()


def exec_insert_anser(questao_id, status_execucao, feedback, resposta_feedback):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.insert_anser(questao_id, status_execucao, feedback, resposta_feedback))
    con.commit()
    con.close()


def exec_update_anser(resposta_id, status_execucao, feedback, resposta_feedback):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.update_anser(resposta_id, status_execucao, feedback, resposta_feedback))
    con.commit()
    con.close()


def exec_update_date(questionario_id):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.update_date(questionario_id))
    con.commit()
    con.close()


def exec_select_pendencia(questionario_id):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.select_pendencia(questionario_id))
    verif = cursor.fetchall()
    ret = []
    if not verif:
        con.commit()
        con.close()
        return {'bool': False, 'obj': ''}
    else:
        for i in verif:
            ret.append({'datapendencia': i[5], 'pendencia': i[3], 'questao': i[4]})
    con.commit()
    con.close()
    return {'bool': True, 'obj': ret}

def exec_retrive_users(data_):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.retriv_users(data_))
    verif = cursor.fetchall()
    row = []
    if len(verif) <= 0:
        con.commit()
        con.close()
        return row
    for i in verif:
        row.append({'user': i[0], 'questionario': i[1]})
    con.commit()
    con.close()
    return row

def exec_insert_pend(fiscal, questionario, obs, questao_id, atraso, status, parecer, baixas, date):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.insert_pend(fiscal, questionario, obs, questao_id, atraso, status, parecer, baixas, date))
    con.commit()
    con.close()

def exec_select_pend_adm(username):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.select_pend_adm(username))
    verif = cursor.fetchall()
    row = []
    if len(verif) <= 0:
        con.commit()
        con.close()
        return row
    for i in verif:
        row.append({'id': i[0], 'fiscal': i[1], 'questionario': i[2], 'descricao': i[3], 'questao': i[4], 'data questionario': i[5], 'atraso': i[6], 'status': i[7], 'parecer': i[8], 'baixa pendencia': i[9]})
    con.commit()
    con.close()
    return row

def exec_update_pend(fiscal, questionario_id, questao_id, descricao, data_questionario, atraso, status, parecer, baixa, data_anterior, questao_anterior):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.update_pend(fiscal, questionario_id, questao_id, descricao, data_questionario, atraso, status, parecer, baixa, data_anterior, questao_anterior))
    con.commit()
    con.close()

def exec_excl_pend(fiscal, questionario_id, questao_id, data_questionario):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(
        models.delete_pend(fiscal, questionario_id, questao_id, data_questionario))
    con.commit()
    con.close()

def exec_create_task(usuario, loja, resumo, detalhes, numero, status, obs):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(
        models.create_task(usuario, loja, resumo, detalhes, numero, status, obs))
    con.commit()
    con.close()

def exec_retrive_task():
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(models.retrive_task())
    verif = cursor.fetchall()
    row = []
    if len(verif) <= 0:
        con.commit()
        con.close()
        return row
    for i in verif:
        row.append({'id': i[0], 'loja': i[1], 'usuario': i[2], 'resumo': i[3], 'detalhes': i[4], 'numero': i[5],
                    'status': i[6], 'obs': i[7], 'data_cad': i[8]})
    con.commit()
    con.close()
    return row

def exec_delete_task(id_task):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(
        models.delete_task(id_task))
    con.commit()
    con.close()

def exec_update_task(id_task, loja, resumo, detalhes, numero, status, obs):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(
        models.update_task(id_task, loja, resumo, detalhes, numero, status, obs))
    con.commit()
    con.close()

def update_weight(id_q,peso):
    con = postgressbd()
    cursor = con.cursor()
    cursor.execute(
        models.update_weight(id_q,peso))
    con.commit()
    con.close()