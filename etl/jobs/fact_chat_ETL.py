import sys
sys.path.append("..")

from connections import connections
from aux_functions import aux_functions

from datetime import datetime

import psycopg2


################################################################# INSERT FACT CHAT - DIM CHAT(NO BANCO ESTÁ ASSIM) #################################################################
def insertFactChat(id_chat, data_inicio, data_fim, quantidade_usuario, descricao, duracao):
    try:
        connection = connections.conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO dim_chat (id_chat, data_inicio, data_fim, quantidade_usuario, descricao, duracao) VALUES (%s,%s,%s,%s, %s, %s)"""
        values = (id_chat, data_inicio, data_fim, quantidade_usuario, descricao, duracao)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT FACT CHAT OK: ", values)
        return "Chat inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return error
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################


# CRIAR FILTRO PARA ALIMENTAR TABELA FACT_CHAT

"""""""""
Campos: ID_CHAT; DATA_INICIO; DATA_FIM; QUANTIDADE_USUARIO; DESCRICAO; DURACAO;
"""""""""

def filtroFactChat():
    collection_room = connections.mongoConnection()['rocketchat']['rocketchat_room'].find({"etl": {'$exists': False}})
    for room in collection_room:
        id_chat = room['_id']
        data_inicio = room['ts']
        data_fim = room['lm']
        quantidade_usuario = room['usersCount']
        descricao_chat = room['name']
        duracao_horas = (data_fim - data_inicio).total_seconds() / 60

        result = insertFactChat(id_chat, data_inicio, data_fim, quantidade_usuario, descricao_chat, duracao_horas)

        # INSERÇÃO DA FLAG 1 PARA DADO INSERIDO CORRETAMENTE E FALHA 0
        _id = room['_id']
        if result == "Chat inserido com sucesso!":
            aux_functions.atualizaFlag(_id, 'rocketchat', 'rocketchat_room', 1)
        elif "duplicate key value violates unique constraint" in str(result):
            aux_functions.atualizaFlag(_id, 'rocketchat', 'rocketchat_room', 1)
        else:
            aux_functions.atualizaFlag(_id, 'rocketchat', 'rocketchat_room', 0)
