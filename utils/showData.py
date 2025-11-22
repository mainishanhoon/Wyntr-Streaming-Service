import os, pymysql
from dotenv import load_dotenv

load_dotenv()


def Show_Data(self):
    MySQL_Connector = pymysql.connect(host=os.getenv('DB_HOST'),
                                      user=os.getenv('DB_USER'),
                                      password=os.getenv('DB_PASSWORD'),
                                      database=os.getenv('DB_NAME'))

    command = MySQL_Connector.cursor()

    command.execute('SELECT mediaId, title, genre, type, imdb, certificate, platform FROM media')

    rows = command.fetchall()

    MySQL_Connector.close()

    return [self.header] + [list(row) for row in rows]
