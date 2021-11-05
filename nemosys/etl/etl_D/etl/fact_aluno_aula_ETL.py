import sys
from datetime import datetime

from pymongo.common import partition_node

sys.path.append("C:\\Users\\EBI\\Documents\\Daniel\\000_Personal\\api\\nemosys\\etl\\etl_D")

from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
# init_date, end_date = aux_functions.etl_dates()
init_date, end_date = aux_functions.full_load_dates()
connPostgree = connections.postgreeConnection()


########## userExitClassFilter ETL ##########

result = filters.userExitClassFilter(init_date, end_date, connMongo)
print(result)
for doc in result:
    mocked_missing = 1
    print(doc)
    try:
        result_in_date = filters.userInClassFilter(doc["id_usuario"], doc["id_aula"], connMongo)

        in_date = result_in_date[0]["date"]

        partition_time = (datetime.strptime(doc["date"], "%Y-%m-%d %H:%M:%S") - datetime.strptime(in_date, "%Y-%m-%d %H:%M:%S")).total_seconds() / 3600.0
        connPostgree.execute('''INSERT INTO fact_aluno_aula (id_aluno, id_aula, tempo_participacao, reacao) VALUES('{0}','{1}','{2}','{3}');'''.format(doc["id_usuario"],
                                                                                                    doc["id_aula"],
                                                                                                    partition_time,
                                                                                                    mocked_missing))  
        #TODO-fix fields
        # aux_functions.updateMongoFlag("Logs","Acesso_aula", doc["_id"], "assunto", connMongo)
  
    except Exception as e:
        print('Erro while inserting:', e)
        continue

connMongo.close()
connPostgree.close()
