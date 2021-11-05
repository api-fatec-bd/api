from pymongo import MongoClient
import psycopg2


def mongoConnection():
    mongo_conn = MongoClient('mongodb://157.245.243.16:3004/?retryWrites=false')
    return mongo_conn


def postgreeConnection():

    sql_conn = psycopg2.connect(host='157.245.243.16', database='PROJETO_API_NEMO',
    user='username', password='password')

    sql_conn.autocommit = True

    return sql_conn.cursor()


def conexaoBanco():
    conexao = psycopg2.connect(host='157.245.243.16',
                           port='5432',
                           database='PROJETO_API_NEMO',
                           user='username',
                           password='password')
    return conexao