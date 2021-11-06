
import sys
sys.path.append("..")

from connections import connections
from aux_functions import aux_functions

from datetime import datetime

import psycopg2

################################################################# INSERT DIM CURSO #################################################################
def insertDimCurso(id_curso, descricao, graduacao, duracao):
    try:
        connection = connections.conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO dim_curso (id_curso, descricao, graduacao, duracao) VALUES (%s,%s,%s,%s)"""
        values = (id_curso, descricao, graduacao, duracao)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT CURSO OK: ", values)
        return "Curso inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return error
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################

# CRIAR FILTRO PARA ALIMENTAR TABELA DIM_CURSO

"""""""""
Campos: ID_CURSO; DESCRICAO; GRADUACAO; DURACAO;
"""""""""

def filtroDimCurso():
    collection_curso = connections.mongoConnection()['Logs']['Curso'].find({"etl": {'$exists': False}})
    for curso in collection_curso:
        id_curso = curso['idcurso']
        descricao = curso['descricao']
        graduacao = curso['graduacao']
        duracao = curso['duracao']

        result = insertDimCurso(id_curso, descricao, graduacao, duracao)

        # INSERÇÃO DA FLAG 1 PARA DADO INSERIDO CORRETAMENTE E FALHA 0
        _id = curso['_id']
        if result == "Curso inserido com sucesso!":
            aux_functions.atualizaFlag(_id, 'Logs', 'Curso', 1)
        elif "duplicate key value violates unique constraint" in str(result):
            aux_functions.atualizaFlag(_id, 'Logs', 'Curso', 1)
        else:
            aux_functions.atualizaFlag(_id, 'Logs', 'Curso', 0)

filtroDimCurso()