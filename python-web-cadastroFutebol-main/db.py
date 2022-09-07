import pyodbc

server = 'serversqldevops.database.windows.net'
database = 'sqldb'
username = 'rm85846'
password = '121201'
driver = '{ODBC Driver 17 for SQL Server}'


def db_query(command):
    with pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(command)
            row = cursor.fetchall()
            return row


def db_insert(command):
    with pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(command)
            conn.commit()
