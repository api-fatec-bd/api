from pymongo import MongoClient


#CONEXÃO COM SERVER MONGO


def connectionMongoDB():
    cliente = MongoClient('mongodb://20.97.1.117:27017/')
    return cliente

def selectBanco():
    banco = connectionMongoDB().rocketchat
    return banco



