

import sys
sys.path.append("..")

from connections import connections
from aux_functions import aux_functions

from datetime import datetime

import psycopg2

################################################################# INSERT FACT USUARIO CHAT #################################################################

def insertFactUsuarioChat(id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg, tempo_participacao):
    try:
        connection = connections.conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO fact_usuario_chat (id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg, tempo_participacao) VALUES (%s,%s,%s,%s, %s, %s, %s, %s)"""
        values = (id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg,
                  tempo_participacao)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT FACT USUARIO CHAT OK: ", values)
        return "Usuario Chat inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return error
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
##########################################################################################################################################################


# CRIAR FILTRO PARA ALIMENTAR TABELA FACT_USUARIO_CHAT

"""""""""
Campos: ID_USUARIO_CHAT; ID_USUARIO; ID_CHAT; DATA_LOGIN; DATA_LOGOFF; TEMPO_PARTICIPACAO; DATA_ULTIMA_MSG; QUANTIDADE_MENSAGENS;
"""""""""

def filtroFactUsuarioChat():
    collection_usuarios = connections.mongoConnection()['Logs']['Usuario'].find()
    collection_message = connections.mongoConnection()['rocketchat']['rocketchat_message']
    id_usuario_chat = 0
    for usuario in collection_usuarios:

        mensagens_usuario = list(collection_message.find({'username': usuario['USERNAME'], "etl": {'$exists': False}}))
        #print("mensagens_usuario: ", mensagens_usuario)
        #PRIMEIRA MENSAGEM; ULTIMA MENSAGEM, TEMPO DURACAO; DA ROOM SELECIONADA NO USUÁRIO SELECIONADO
        salas = ["GENERAL", "SALA2", "SALA1"]

        for sala in salas:
            print("Sala: ", sala)
            vetor_mensagensPorSalaUsuario = []
            for mensagemUsuario in mensagens_usuario:
                print("SalamensagemUsuario: ", mensagemUsuario['rid'])


                if mensagemUsuario['rid'] == sala:
                    vetor_mensagensPorSalaUsuario.append(mensagemUsuario)
                else:
                    None

            if vetor_mensagensPorSalaUsuario != []:
                print("Teste vetor_mensagensPorSalaUsuario: ", vetor_mensagensPorSalaUsuario)
                id_usuario_chat = id_usuario_chat + 1
                data_login = datetime.strptime(vetor_mensagensPorSalaUsuario[0]['_updateAt'], '%d-%m-%Y %H:%M:%S')
                data_logoff = datetime.strptime(vetor_mensagensPorSalaUsuario[-1]['_updateAt'], '%d-%m-%Y %H:%M:%S')
                tempo_participacao = (data_logoff - data_login).total_seconds() / 60
                tempo_participacao = "{:.2f}".format(tempo_participacao)
                # QUANTIDADE DE MENSAGENS
                quantidade_mensagens = len(vetor_mensagensPorSalaUsuario)

                print("data_login: ", data_login)
                print("data_logoff: ", data_logoff)
                print("tempo_participacao: ", tempo_participacao)
                print("quantidade_mensagens: ", quantidade_mensagens)
                print("sala: ", vetor_mensagensPorSalaUsuario[0]['rid'])

                result = insertFactUsuarioChat(id_usuario_chat, usuario['IDUSUARIO'], vetor_mensagensPorSalaUsuario[0]['rid'],
                                      data_login, data_logoff, quantidade_mensagens, data_logoff, tempo_participacao)

                for mensagemPorSala in vetor_mensagensPorSalaUsuario:
                    # INSERÇÃO DA FLAG 1 PARA DADO INSERIDO CORRETAMENTE E FALHA 0
                    _id = mensagemPorSala['_id']
                    if result == "Usuario Chat inserido com sucesso!":
                        aux_functions.atualizaFlag(_id, 'rocketchat', 'rocketchat_message', 1)
                    elif "duplicate key value violates unique constraint" in str(result):
                        aux_functions.atualizaFlag(_id, 'rocketchat', 'rocketchat_message', 1)
                    else:
                        aux_functions.atualizaFlag(_id, 'rocketchat', 'rocketchat_message', 0)

filtroFactUsuarioChat()