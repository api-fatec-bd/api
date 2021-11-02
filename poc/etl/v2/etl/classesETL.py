import sys
sys.path.append("..")

from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
# init_date, end_date = aux_functions.etl_dates()
init_date, end_date = aux_functions.full_load_dates()
connPostgree = connections.postgreeConnection()


########## classes ETL ##########

result = filters.classesFilter(init_date, end_date, connMongo)

for doc in result:
    try:
        connPostgree.execute("INSERT INTO dim_turma (id_turma, descricao, id_professor) VALUES('{0}','{1}','{2}');".format(doc["idturma"], doc["descricao"], doc["idprofessor"]))
    except Exception as e:
        print(e)
        continue
    
connMongo.close()
connPostgree.close()