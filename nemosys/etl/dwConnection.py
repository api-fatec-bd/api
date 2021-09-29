import pyodbc

def connectionDW():
    dw_conn = pyodbc.connect('Driver={SQL Server};'
                             'Server=localhost;'
                             'Database=nemo;'
                             'UID=sa;'
                             'PWD=N3mosys@123;'
                             'Trusted_Connection=yes;')

    dw_conn.autocommit = True
    cursor = dw_conn.cursor()
    return cursor
