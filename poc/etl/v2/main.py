from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
tday, yday = aux_functions.etl_dates()


### USERS ETL
users_result = filters.usersFilter(tday, yday, connMongo)

for user in users_result:
    print(user)

connPostgree = connections.postgreeConnection()

connPostgree.execute("INSERT INTO dim_usuario (nome_usuario, username, codigo_perfil, descricao_perfil) VALUES('ha', 'hebento', 1, '123');")