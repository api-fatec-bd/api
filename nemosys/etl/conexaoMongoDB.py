from pymongo import MongoClient


#CONEXÃO COM SERVER MONGO


def connectionMongoDB():
    cliente = MongoClient('mongodb://34.135.95.193:27017/')
    return cliente

def selectBanco():
    banco = connectionMongoDB().rocketchat
    return banco



