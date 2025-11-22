import os, pymysql
from customtkinter import END
from CTkMessagebox import CTkMessagebox
from dotenv import load_dotenv
from interfaces import UserUI

load_dotenv()


def Login(self):
    if self.username.get() == '' and self.password.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter Username & Password.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00',
                      text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.username.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter Username.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/info.png',
                      option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                      button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00', text_color='#834333',
                      title_color='#954535', icon_size=(40, 40))

    elif self.password.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter Password.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/info.png',
                      option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                      button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00', text_color='#834333',
                      title_color='#954535', icon_size=(40, 40))

    else:
        MySQL_Connector = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        cursor = MySQL_Connector.cursor()

        cursor.execute('SELECT * FROM Accounts WHERE Username = %s AND Password = %s',
                       (self.username.get(), self.password.get()))

        row = cursor.fetchone()

        if self.username.get() == os.getenv('WYNTR_USERNAME') and self.password.get() == os.getenv('WYNTR_PASSWORD'):
            self.AdminUI()

        elif row is None:
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Invalid Username/Password.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='assets/icons/alert.png', option_1='Go Back', option_focus=1, justify='center',
                          fade_in_duration=1, button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
            self.username.delete('0', END)
            self.password.delete('0', END)

        else:
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Welcome to Wyntr Streaming Service.', font=('Stack Sans Text', 15, 'bold'),
                          wraplength=300, fg_color='#DAA06D', icon='assets/icons/check.png', option_1='OKAY',
                          option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                          button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00',
                          text_color='#834333', title_color='#954535', icon_size=(40, 40))
            UserUI(self)

        MySQL_Connector.close()