from datetime import datetime, timedelta

from connections import connections

def etl_dates():
    t = datetime.today()
    y = t - timedelta(days=1)
    today = datetime.strptime(t.strftime('%Y-%m-%d'), '%Y-%m-%d')
    yesterday = datetime.strptime(y.strftime('%Y-%m-%d'), '%Y-%m-%d')
    return yesterday, today

def full_load_dates():
    t = datetime.today()
    od = t - timedelta(days=9999)
    fd = t + timedelta(days=10)
    future_date = datetime.strptime(fd.strftime('%Y-%m-%d'), '%Y-%m-%d')
    old_date = datetime.strptime(od.strftime('%Y-%m-%d'), '%Y-%m-%d')
    return old_date, future_date,

#TODO:implement function
def genericETLFlag(database, collection, docId, flagValue, mongoConnection):
    query = {"_id": docId}
    newvalues = { "$set": {"etl": flagValue} }
    mongoConnection[database][collection].update_one(query, newvalues)

    return


######### FLAG = PROCESSADO #########

# FUNÇÃO QUE RECEBERÁ A ID_OBJECT E DE QUAL COLLECTION ESSE ID PERTENCE, ONDE SERÁ ADICIONADA A FLAG DE PROCESSADO CASO O DADO SEJA INSERIDO NO BANCO DO DW CORRETAMENTE
def atualizaFlag(id_object, banco, collection, resultado):
    try:
        connections.mongoConnection()[banco][collection].update({'_id': id_object}, {'$set': {'etl': resultado}},upsert=False)
        print("A inserção do Flag no Object Id = %s na Collection = %s foi executada com sucesso!!", id_object,collection)
        return "Flag inserida com sucesso!!"
    except (Exception) as error:
        print("A inserção do Flag no Object Id = %s na Collection = %s falhou !! Erro: %s ", id_object,collection, error)
        return "Não foi possível inserir Flag"


