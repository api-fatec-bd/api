from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
# tday, yday = aux_functions.etl_dates()
tday, yday = aux_functions.full_load_dates()
connPostgree = connections.postgreeConnection()


### USERS ETL
users_result = filters.usersFilter(tday, yday, connMongo)

for user in users_result:
    # print(user)
    if user["type"] == 'bot':
        codigo_perfil = 0
    elif user["type"] == 'user':
        codigo_perfil = 1
    else:
        codigo_perfil = 2

    connPostgree.execute("INSERT INTO dim_usuario (nome_usuario, username, codigo_perfil, descricao_perfil) VALUES('{0}','{1}','{2}','{3}');".format(user["name"],
                                                                                                                                            user["username"],
                                                                                                                                            codigo_perfil,
                                                                                                                                            user["type"]))

connMongo.close()
connPostgree.close()