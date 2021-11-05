from datetime import datetime, timedelta

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
def updateMongoFlag(database, collection, docId, flagField, mongoConnection):
    query = {"_id": docId}
    newvalues = { "$set": {flagField: "1" } }
    mongoConnection[database][collection].update_one(query, newvalues)

    return 