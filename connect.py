import psycopg2
def postgressbd():
    conn = psycopg2.connect(
        host='10.10.0.52',
        database='aplicacoes_internas',
        user='master_app',
        password='M4st3#0238$')
    return conn
