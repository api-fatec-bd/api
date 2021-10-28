import pyodbc
from pymongo import MongoClient
import datetime


mongo_conn = MongoClient(
    'mongodb://20.97.1.117:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')

# tbd
filter = {}

select_count = mongo_conn['rocketchat']['rocketchat_cron_history'].count_documents(filter=filter)

print(select_count)

current_year, current_month, current_day = datetime.datetime.today().year, datetime.datetime.today().month, \
                                           datetime.datetime.today().day

# your localhost server
sql_server = "EBI-DANIEL\SQLEXPRESS"

sql_conn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+sql_server+';'
                      'Database=nemo;'
                      'Trusted_Connection=yes;')

sql_conn.autocommit = True

cursor = sql_conn.cursor()
cursor.execute(
    'INSERT INTO sessoes_dia (syear, smonth, sday, sessions) values ({0},{1},{2},{3});'.format(current_year,
                                                                                               current_month,
                                                                                               current_day,
                                                                                               select_count))

print('gg wp')
