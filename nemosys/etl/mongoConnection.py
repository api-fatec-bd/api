from pymongo import MongoClient


#CONEXÃO COM SERVER MONGO
def mongoConnection():
    chat_conn = MongoClient('mongodb://157.245.243.16:3004/?retryWrites=false')
    return chat_conn



