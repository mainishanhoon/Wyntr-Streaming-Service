import os, pymysql
from customtkinter import END
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkLabel
from dotenv import load_dotenv

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

        query = f"SELECT * FROM Media WHERE {self.var_SearchBy.get()} LIKE %s"
        cursor.execute(query, ("%" + self.var_SearchBox.get() + "%",))

        data = cursor.fetchall()

        self.Media_Table.delete(*self.Media_Table.get_children())

        if len(data) != 0:
            self.Media_Table.delete(*self.Media_Table.get_children())
        for Data in data:
            self.Media_Table.insert('', END, values=Data)
        else:
            No_Data = CTkLabel(master=self.root, text='Oops! No Medias Were Found',
                               font=('Dela Gothic One', 45, 'bold'),
                               fg='#021E2F', bg='#FFEFD5')

        No_Data.place(x=622, y=189, height=597, width=890)

        No_Data.after(3000, No_Data.destroy)

        self.ClearData()

        MySQL_Connector.commit()

        MySQL_Connector.close()