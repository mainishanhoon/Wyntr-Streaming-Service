import os, pymysql
from customtkinter import END
from CTkMessagebox import CTkMessagebox
from dotenv import load_dotenv
from interfaces.user import User_Interface

load_dotenv()

def Login(app):
    if app.username.get() == '' and app.password.get() == '':
        CTkMessagebox(master=app.root, title='Wyntr Streaming Service', message='Enter Username & Password.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00',
                      text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif app.username.get() == '':
        CTkMessagebox(master=app.root, title='Wyntr Streaming Service', message='Enter Username.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='Icons/info.png',
                      option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                      button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00', text_color='#834333',
                      title_color='#954535', icon_size=(40, 40))

    elif app.password.get() == '':
        CTkMessagebox(master=app.root, title='Wyntr Streaming Service', message='Enter Password.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='Icons/info.png',
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
                       (app.username.get(), app.password.get()))

        row = cursor.fetchone()

        if app.username.get() == os.getenv('WYNTR_USERNAME') and app.password.get() == os.getenv('WYNTR_PASSWORD'):
            app.AdminUI()

        elif row is None:
            CTkMessagebox(master=app.root, title='Wyntr Streaming Service', message='Invalid Username/Password.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='Go Back', option_focus=1, justify='center',
                          fade_in_duration=1, button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
            app.username.delete('0', END)
            app.password.delete('0', END)

        else:
            CTkMessagebox(master=app.root, title='Wyntr Streaming Service',
                          message='Welcome to Wyntr Streaming Service.', font=('Stack Sans Text', 15, 'bold'),
                          wraplength=300, fg_color='#DAA06D', icon='Icons/check.png', option_1='OKAY',
                          option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                          button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00',
                          text_color='#834333', title_color='#954535', icon_size=(40, 40))
            User_Interface(app)

        MySQL_Connector.close()