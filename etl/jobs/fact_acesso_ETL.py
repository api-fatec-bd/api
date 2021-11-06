
import sys
sys.path.append("..")

from connections import connections
from aux_functions import aux_functions

from datetime import datetime

import psycopg2


################################################################# INSERT FACT ACESSO #################################################################
def insertFactAcesso(id_usuario, data_login, data_logoff, origem):
    try:
        connection = connections.conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO fact_acesso (id_usuario, data_login, data_logoff, origem) VALUES (%s,%s,%s,%s)"""
        values = (id_usuario, data_login, data_logoff, origem)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT FACT ACESSO OK: ", values)
        return "Acesso inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return error
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


##########################################################################################################################################################


# CRIAR FILTRO PARA ALIMENTAR TABELA FACT_ACESSO

"""""""""
Campos: ID_USUARIO; ORIGEM; DATA_LOGIN; DATA_LOGOFF;
"""""""""

def dataHoraLogout(datetimeLogin, listLogoutUser):
    vetor = []
    for logoutUser in listLogoutUser:
        if logoutUser['DateTime'] > datetimeLogin:
            linha = logoutUser['DateTime']
            vetor.append(linha)
    if vetor != []:
        menorDatetimeLogout = min(vetor)
        return menorDatetimeLogout
    else:
        menorDatetimeLogout = 0
        return menorDatetimeLogout

def filtroFactAcesso():

    collection_login = connections.mongoConnection()['Logs']['Login']

    for loginLogout in collection_login.find({"etl": {'$exists': False}}):
        all_login_user = list(collection_login.find({'iduser': loginLogout['iduser'], 'funcao': 'Login'}))
        all_logout_user = list(collection_login.find({'iduser': loginLogout['iduser'], 'funcao': 'Logout'}))

        for login_user in all_login_user:
            data_login = login_user['DateTime']
            data_logoff = dataHoraLogout(data_login, all_logout_user)

        result = insertFactAcesso(loginLogout['iduser'], data_login, data_logoff, 'P')
        insertFactAcesso(loginLogout['iduser'], data_login, data_logoff, 'C')

        # INSERÇÃO DA FLAG 1 PARA DADO INSERIDO CORRETAMENTE E FALHA 0
        _id = loginLogout['_id']
        if result == "Acesso inserido com sucesso!":
            aux_functions.atualizaFlag(_id, 'Logs', 'Login', 1)
        elif "duplicate key value violates unique constraint" in str(result):
            aux_functions.atualizaFlag(_id, 'Logs', 'Login', 1)
        else:
            aux_functions.atualizaFlag(_id, 'Logs', 'Login', 0)
