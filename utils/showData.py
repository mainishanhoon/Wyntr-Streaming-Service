import os, pymysql
from dotenv import load_dotenv

load_dotenv()

def Show_Data(self):
    MySQL_Connector = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

    command = MySQL_Connector.cursor()
    command.execute(
        "SELECT mediaId, title, genre, type, imdb, certificate, platform, description, link FROM media"
    )
    rows = command.fetchall()
    MySQL_Connector.close()

    self.full_data_records = [list(row) for row in rows]

    header = ["ID", "Title", "Genre", "Type", "IMDb", "Certificate", "Platform"]

    ui_rows = [list(row)[:7] for row in rows]
    return [header] + ui_rows