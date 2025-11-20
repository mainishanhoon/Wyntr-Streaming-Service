import os, pymysql

def Show_Data(app):
    MySQL_Connector = pymysql.connect(host=os.getenv('DB_HOST'),
                                      user=os.getenv('DB_USER'),
                                      password=os.getenv('DB_PASSWORD'),
                                      database=os.getenv('DB_NAME'))

    cursor = MySQL_Connector.cursor()
    cursor.execute("SELECT ID, Title, Type, Genre, Certificate, IMDb, PlatForm FROM Media")

    rows = cursor.fetchall()

    MySQL_Connector.commit()
    MySQL_Connector.close()

    return rows