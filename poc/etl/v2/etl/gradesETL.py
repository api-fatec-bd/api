import sys
sys.path.append("..")

from filters import filters
from connections import connections
from aux_functions import aux_functions


connMongo = connections.mongoConnection()
# init_date, end_date = aux_functions.etl_dates()
init_date, end_date = aux_functions.full_load_dates()
connPostgree = connections.postgreeConnection()


########## GRADES ETL ##########

result = filters.gradesFilter(init_date, end_date, connMongo)

for doc in result:
    try:
        connPostgree.execute('''INSERT INTO fact_nota (id_aluno, id_disciplina, nota, nota_avaliacao, percentual_nota, "data") VALUES('{0}','{1}','{2}','{3}','{4}','{5}');'''.format(
                                                                                                                                                doc["idaluno"],
                                                                                                                                                doc["iddisciplina"],
                                                                                                                                                doc["nota"],
                                                                                                                                                doc["notaAvaliacao"],
                                                                                                                                                (doc["nota"]/ doc["notaAvaliacao"]),
                                                                                                                                                doc["data"]))
    except Exception as e:
        print(e)
        continue

connMongo.close()
connPostgree.close()
