from psycopg2 import sql
import hashlib


def perguntas():
    return sql.SQL('select * from checklist_perguntas order by id')


def log(userid: int, senha: str):
    md5 = hashlib.md5(senha.encode()).hexdigest()
    return sql.SQL("select * from checklist_usuario where id = {userid} and senha = {md5}").format(
        userid=sql.Literal(userid), md5=sql.Literal(md5))


def nex_quest():
    return sql.SQL('select * from questionario_id_seq')


def nex_anser():
    return sql.SQL('select * from resposta_resposta_id_seq')


def nex_vinc():
    return sql.SQL('select * from vinculo_vinculo_id_seq')


def verif_quest(usuario_id, data_questionario):
    return sql.SQL(
        "select * from checklist_questionario where usuario_id = {usuario_id} and data_questionario = {data_questionario}").format(
        usuario_id=sql.Literal(usuario_id), data_questionario=sql.Literal(data_questionario))


def retrive_ansers(questionario_id):
    return sql.SQL(
        "select r.resposta_id,r.questao_id,r.status_execucao,r.feedback,r.resposta_feedback from checklist_vinculo v inner join checklist_resposta r on v.resposta_id = r.resposta_id where v.questionario_id = {questionario_id} order by r.questao_id").format(
        questionario_id=sql.Literal(questionario_id))


def insert_quest(usuario_id, data_questionario):
    return sql.SQL(
        "INSERT INTO public.checklist_questionario(usuario_id, data_questionario, ultima_alteracao) VALUES({usuario_id}, {data_questionario}, (SELECT CURRENT_DATE))").format(
        usuario_id=sql.Literal(usuario_id), data_questionario=sql.Literal(data_questionario))


def insert_vinc(quest_id, resp_id):
    return sql.SQL(
        "INSERT INTO public.checklist_vinculo (questionario_id, resposta_id) VALUES ( {quest_id}, {resp_id})").format(
        quest_id=sql.Literal(quest_id), resp_id=sql.Literal(resp_id))


def insert_anser(questao_id, status_execucao, feedback, resposta_feedback):
    return sql.SQL(
        "INSERT INTO public.checklist_resposta(questao_id, status_execucao, feedback, resposta_feedback) VALUES ({questao_id}, {status_execucao}, {feedback}, {resposta_feedback});").format(
        questao_id=sql.Literal(questao_id), status_execucao=sql.Literal(status_execucao),
        feedback=sql.Literal(feedback), resposta_feedback=sql.Literal(resposta_feedback))


def update_anser(resposta_id, status_execucao, feedback, resposta_feedback):
    return sql.SQL(
        "update checklist_resposta set status_execucao = {status_execucao}, feedback = {feedback} ,resposta_feedback = {resposta_feedback} where resposta_id = {resposta_id}").format(
        resposta_id=sql.Literal(resposta_id), status_execucao=sql.Literal(status_execucao),
        feedback=sql.Literal(feedback), resposta_feedback=sql.Literal(resposta_feedback))


def update_date(questionario_id):
    return sql.SQL(
        "update checklist_questionario set ultima_alteracao = (SELECT CURRENT_DATE) where id = {questionario_id}").format(
        questionario_id=sql.Literal(questionario_id))


def verif_quest_pendencia(usuario_id):
    return sql.SQL("select * from checklist_questionario where usuario_id = {usuario_id}").format(
        usuario_id=sql.Literal(usuario_id))


def select_pendencia(questionario_id: int):
    return sql.SQL(
        "select * from checklist_pendencia where questionario_id in ({questionario_id})").format(
        questionario_id=sql.Literal(questionario_id))


def retriv_users(date):
    return sql.SQL("select usuario_id, id from checklist_questionario where data_questionario = {date}").format(
        date=sql.Literal(date))


def insert_pend(fiscal: str, questionario: int, obs: str, questao_id: int, atraso: str, status: str, parecer: str,
                baixas: str, date: str):
    return sql.SQL(f"""
    INSERT INTO public.checklist_pendencia(
	fiscal, questionario_id, descricao, questao_id, data_questionario, atraso, status, parecer, baixas_pendencia)
	VALUES ('{fiscal}', {questionario}, '{obs}', {questao_id}, '{date}', '{atraso}', '{status}', '{parecer}', '{baixas}')
    """)


def select_pend_adm(username):
    return sql.SQL(f"select * from checklist_pendencia where fiscal = '{username}'")


def update_pend(fiscal, questionario_id, questao_id, descricao, data_questionario, atraso, status, parecer, baixa, data_anterior, questao_anterior):
    return sql.SQL("""UPDATE public.checklist_pendencia
	SET descricao={descricao}, questao_id={questao_id}, data_questionario={data_questionario}, atraso={atraso}, status={status}, parecer={parecer}, baixas_pendencia={baixa}
	WHERE questionario_id = {questionario_id} and fiscal = {fiscal} and questao_id = {questao_anterior} and data_questionario = {data_anterior} """).format(
        fiscal=sql.Literal(fiscal), questionario_id=sql.Literal(questionario_id), questao_id=sql.Literal(questao_id),
        descricao=sql.Literal(descricao), data_questionario=sql.Literal(data_questionario), atraso=sql.Literal(atraso),
        status=sql.Literal(status),
        parecer=sql.Literal(parecer), baixa=sql.Literal(baixa), data_anterior=sql.Literal(data_anterior), questao_anterior=sql.Literal(questao_anterior)
    )

def delete_pend(fiscal, questionario_id, questao_id, data_questionario):
    return sql.SQL("""DELETE FROM public.checklist_pendencia
	WHERE fiscal = {fiscal} and questionario_id = {questionario_id} and questao_id = {questao_id} and data_questionario = {data_questionario}""").format(
        fiscal=sql.Literal(fiscal), questionario_id=sql.Literal(questionario_id),
        questao_id=sql.Literal(questao_id), data_questionario=sql.Literal(data_questionario))

def create_task(usuario, loja, resumo, detalhes, numero, status, obs):
    return sql.SQL("""INSERT INTO public.checklist_chamados(
	 usuario, loja, resumo, detalhes, numero, status, obs, data_cad)
	VALUES ({usuario}, {loja}, {resumo}, {detalhes}, {numero}, {status}, {obs}, (SELECT CURRENT_DATE))""").format(
        usuario=sql.Literal(usuario), loja=sql.Literal(loja), resumo=sql.Literal(resumo),
        detalhes=sql.Literal(detalhes), numero=sql.Literal(numero), status=sql.Literal(status), obs=sql.Literal(obs)
    )

def retrive_task():
    return sql.SQL("""select id, loja, usuario, resumo, detalhes, numero, status, obs, data_cad from checklist_chamados;""")

def delete_task(id_task):
    return sql.SQL("""DELETE FROM public.checklist_chamados
	WHERE id = {id}""").format(id=sql.Literal(id_task))

def update_task(id_task, loja, resumo, detalhes, numero, status, obs):
    return sql.SQL("""UPDATE
    public.checklist_chamados
    SET 
    loja ={loja}, resumo ={resumo}, detalhes ={detalhes}, numero ={numero}, status ={status}, obs ={obs}
    WHERE
    id = {id};""").format(id=sql.Literal(id_task), loja=sql.Literal(loja),
                          resumo=sql.Literal(resumo), detalhes=sql.Literal(detalhes), numero=sql.Literal(numero),
                          status=sql.Literal(status), obs=sql.Literal(obs))

def update_weight(id_q, peso):
    return sql.SQL("""UPDATE public.checklist_perguntas
	SET peso={peso}
	WHERE id = {id}""").format(id=sql.Literal(id_q),peso=sql.Literal(peso))