import sys
sys.path.append("..")

from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
# init_date, end_date = aux_functions.etl_dates()
init_date, end_date = aux_functions.full_load_dates()
connPostgree = connections.postgreeConnection()


#  USERS ETL # 

result = filters.logsUsersFilter(init_date, end_date, connMongo)

for doc in result:
    try:
        connPostgree.execute("INSERT INTO dim_usuario (id_usuario, nome_usuario, username, codigo_perfil, descricao_perfil) VALUES('{0}','{1}','{2}','{3}','{4}');".format(
                                                                                                                                                doc["IDUSUARIO"],
                                                                                                                                                doc["USERNAME"],
                                                                                                                                                doc["USERNAME"],
                                                                                                                                                doc["CODIGO_PERMISSAO"],
                                                                                                                                                doc["DESCRICAO_PERMISSAO"]))
        aux_functions.genericETLFlag("Logs","Usuario", doc["_id"], "1", connMongo)

    except Exception as e:
        print('Erro while inserting:', e)
        print('Erro type:', type(e))
        aux_functions.genericETLFlag("Logs","Usuario", doc["_id"], "0", connMongo)
        continue

connMongo.close()
connPostgree.close()
