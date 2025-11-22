import os, pymysql
from CTkMessagebox import CTkMessagebox
from dotenv import load_dotenv
from utils import ClearData

load_dotenv()


def Search_Data(self):
    if self.var_SearchBy.get() == 'Select Category':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                      message='On What Basis You Wanna Filter the List.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_SearchBox.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                      message='Search Box is Empty.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    else:
        MySQL_Connector = pymysql.connect(host=os.getenv('DB_HOST'),
                                          user=os.getenv('DB_USER'),
                                          password=os.getenv('DB_PASSWORD'),
                                          database=os.getenv('DB_NAME'))

        cursor = MySQL_Connector.cursor()

        query = f"SELECT title, type, genre, certificate, imdb, platForm FROM media WHERE {self.var_SearchBy.get()} LIKE %s"

        cursor.execute(query, ("%" + self.var_SearchBox.get() + "%",))

        data = cursor.fetchall()

        data = [list(row) for row in data]

        if data:
            self.Media_Table.delete_rows(range(self.Media_Table.rows))
            self.Media_Table.add_row(self.header)

            for row_data in data:
                self.Media_Table.add_row(row_data)

        else:
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Oops!! No Data Found.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=350, fg_color='#DAA06D',
                          icon='assets/icons/info.png',
                          option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                          button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00', text_color='#834333',
                          title_color='#954535', icon_size=(40, 40))

        ClearData(self)

        MySQL_Connector.commit()

        MySQL_Connector.close()