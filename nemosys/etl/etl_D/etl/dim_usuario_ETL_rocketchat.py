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

result = filters.rocketUsersFilter(init_date, end_date, connMongo)

for doc in result:
    try:
        # print(user)
        if doc["type"] == 'bot':
            profile_code = 0
        elif doc["type"] == 'user':
            profile_code = 1
        else:
            profile_code = 2

        connPostgree.execute("INSERT INTO dim_usuario (nome_usuario, username, codigo_perfil, descricao_perfil) VALUES('{0}','{1}','{2}','{3}');".format(doc["name"],
                                                                                                                                                doc["username"],
                                                                                                                                                profile_code,
                                                                                                                                                doc["type"]))
    except Exception as e:
        print('Erro while inserting:', e)
        continue

connMongo.close()
connPostgree.close()