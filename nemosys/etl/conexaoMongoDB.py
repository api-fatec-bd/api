from pymongo import MongoClient


#CONEXÃO COM SERVER MONGO
def connectionChatDB():
    chat_conn = MongoClient('mongodb://157.245.243.16:3002/')
    return chat_conn

def selectBanco():
    banco = connectionChatDB()['rocketchat']
    return banco


