import sys
sys.path.append("..")

from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
# init_date, end_date = aux_functions.etl_dates()
init_date, end_date = aux_functions.full_load_dates()
connPostgree = connections.postgreeConnection()


#  matriculation ETL # 

result = filters.matriculationFilter(init_date, end_date, connMongo)

for doc in result:
    mocked_data = '2002-02-02 00:00:00'
    mocked_missing = 1
    try:
        connPostgree.execute('''INSERT INTO fact_matricula (data_inicio, data_fim, id_aluno, id_turma, id_disciplina, id_certificado, numero_certificado, status_matricula, quantidade_matricula) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}');'''.format(mocked_data,
                                                                                                    mocked_data,
                                                                                                    doc["id_usuario"],
                                                                                                    doc["id_turma "],
                                                                                                    mocked_missing,
                                                                                                    mocked_missing,
                                                                                                    mocked_missing,
                                                                                                    mocked_missing,
                                                                                                    1))  
        aux_functions.genericETLFlag("Logs","Matricula", doc["_id"], "1", connMongo)

    except Exception as e:
        print('Erro while inserting:', e)
        aux_functions.genericETLFlag("Logs","Matricula", doc["_id"], "0", connMongo)

        continue

connMongo.close()
connPostgree.close()
