import sys
sys.path.append("..")

from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
# init_date, end_date = aux_functions.etl_dates()
init_date, end_date = aux_functions.full_load_dates()
connPostgree = connections.postgreeConnection()


########## content ETL ##########

result = filters.contentFilter(init_date, end_date, connMongo)

#subjects = filters.auxSubjectsFilter(init_date, end_date, connMongo)

for doc in result:
    try:
        # falta trocar id_conteudo, data_upload e id_aula
        connPostgree.execute("INSERT INTO fact_usuario_conteudo (id_usuario, data_upload, data_download, id_conteudo, id_disciplina, id_aula) VALUES('{0}','{1}','{2}','{3}','{4}','{5}');".format(doc["id_usuario"], doc["date"], doc["date"], 1, doc["id_disciplina"], 1))
    except Exception as e:
        print('Erro while inserting:', e)
        continue

connMongo.close()
connPostgree.close()