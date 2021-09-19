from pymongo import MongoClient


#CONEXÃO COM SERVER MONGO


def connectionMongoDB():
    cliente = MongoClient('mongodb://157.245.243.16:3002/')
    return cliente

def selectBanco():
    banco = connectionMongoDB()['rocketchat']
    return banco


