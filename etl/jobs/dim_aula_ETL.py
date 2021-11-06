
import sys
sys.path.append("..")

from connections import connections
from aux_functions import aux_functions

from datetime import datetime

import psycopg2

################################################################# INSERT DIM AULA #################################################################
def insertDimAula(id_aula, data_inicio, data_fim, id_disciplina, titulo, duracao, assunto):
    try:
        connection = connections.conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO dim_aula (id_aula, data_inicio, data_fim, id_disciplina, titulo, duracao, assunto) VALUES (%s,%s,%s,%s,%s, %s, %s)"""
        values = (id_aula, data_inicio, data_fim, id_disciplina, titulo, duracao, assunto)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT AULA OK: ", values)
        return "Aula inserida com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return error
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################

# CRIAR FILTRO PARA ALIMENTAR TABELA DIM_AULA

"""""""""
Campos: ID_AULA; DATA_INICIO; DATA_FIM; ID_DISCIPLINA; TITULO; ASSUNTO; DURACAO;
"""""""""

def filtroDimAula():
    collection_aula = connections.mongoConnection()['Logs']['Aula'].find({"etl": {'$exists': False}})
    for aula in collection_aula:
        id_aula = aula['idAula']
        data_inicio = datetime.strptime(aula['DateInicio'], '%Y-%m-%d %H:%M:%S')
        data_fim = datetime.strptime(aula['dateFim'], '%Y-%m-%d %H:%M:%S')
        id_disciplina = aula['idDisciplina']
        titulo = aula['Titulo']
        duracao = (data_fim - data_inicio).total_seconds() / 60
        duracao = round(duracao, 2)
        assunto = aula['Assunto']

        result = insertDimAula(id_aula, data_inicio, data_fim, id_disciplina, titulo, duracao, assunto)

        # INSERÇÃO DA FLAG 1 PARA DADO INSERIDO CORRETAMENTE E FALHA 0
        _id = aula['_id']
        if result == "Aula inserida com sucesso!":
            aux_functions.atualizaFlag(_id, 'Logs', 'Aula', 1)
        elif "duplicate key value violates unique constraint" in str(result):
            aux_functions.atualizaFlag(_id, 'Logs', 'Aula', 1)
        else:
            aux_functions.atualizaFlag(_id, 'Logs', 'Aula', 0)


filtroDimAula()