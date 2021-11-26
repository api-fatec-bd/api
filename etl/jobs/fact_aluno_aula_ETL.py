import sys
from datetime import datetime

from pymongo.common import partition_node

sys.path.append("C:\\Users\\EBI\\Documents\\Daniel\\000_Personal\\api\\etl")
#sys.path.append("..")

from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
# init_date, end_date = aux_functions.etl_dates()
# init_date, end_date = aux_functions.full_load_dates()
connPostgree = connections.postgreeConnection()


#  userExitClassFilter ETL # 

result = filters.userExitClassFilter(connMongo)

if len(result) == 0:
    connMongo.close()
    connPostgree.close()
    print('nothing new')
    exit

for doc in result:
    mocked_missing = 1
    try:
        result_in_date = filters.userInClassFilter(doc["id_usuario"], doc["id_aula"], connMongo)

        in_date = result_in_date[0]["date"]

        partition_time = (datetime.strptime(doc["date"], "%Y-%m-%d %H:%M:%S") - datetime.strptime(in_date, "%Y-%m-%d %H:%M:%S")).total_seconds() / 3600.0
        connPostgree.execute('''INSERT INTO fact_aluno_aula (id_aluno, id_aula, tempo_participacao, reacao) VALUES('{0}','{1}','{2}','{3}');'''.format(doc["id_usuario"],
                                                                                                    doc["id_aula"],
                                                                                                    partition_time,
                                                                                                    mocked_missing))  
        aux_functions.genericETLFlag("Logs","Acesso_aula", doc["_id"], "1", connMongo)

    except Exception as e:
        print('Erro while inserting:', e)
        print('Erro type:', type(e))
        aux_functions.genericETLFlag("Logs","Acesso_aula", doc["_id"], "0", connMongo)
        continue


connMongo.close()
connPostgree.close()
