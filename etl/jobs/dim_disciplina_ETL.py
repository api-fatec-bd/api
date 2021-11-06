

import sys
sys.path.append("..")

from connections import connections
from aux_functions import aux_functions

from datetime import datetime

import psycopg2


################################################################# INSERT DIM DICIPLINA #################################################################
def insertDimDisciplina(id_disciplina, id_curso, descricao, id_turma):
    try:
        connection = connections.conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO dim_disciplina (id_disciplina, id_curso, descricao, id_turma) VALUES (%s,%s,%s,%s)"""
        values = (id_disciplina, id_curso, descricao, id_turma)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT DISCIPLINA OK: ", values)
        return "Disciplina inserida com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return error
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################

# CRIAR FILTRO PARA ALIMENTAR TABELA DIM_DISCIPLINA

"""""""""
Campos: ID_DISCIPLINA; ID_CURSO; ID_TURMA; DESCRICAO;
"""""""""

def filtroDimDisciplina():
    collection_disciplina = connections.mongoConnection()['Logs']['Disciplina'].find({"etl": {'$exists': False}})
    for disciplina in collection_disciplina:
        id_disciplina = disciplina['idDisciplina']
        id_curso = disciplina['idcurso']
        descricao = disciplina['descricao']
        id_turma = disciplina['idturma']

        result = insertDimDisciplina(id_disciplina, id_curso, descricao, id_turma)

        #duplicate key value violates unique constraint

        # INSERÇÃO DA FLAG 1 PARA DADO INSERIDO CORRETAMENTE E FALHA 0
        _id = disciplina['_id']
        if result == "Disciplina inserida com sucesso!":
            aux_functions.atualizaFlag(_id, 'Logs', 'Disciplina', 1)
        elif result in "duplicate key value violates unique constraint":
            aux_functions.atualizaFlag(_id, 'Logs', 'Disciplina', 1)
        else:
            aux_functions.atualizaFlag(_id, 'Logs', 'Disciplina', 0)


filtroDimDisciplina()