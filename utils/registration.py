import os, pymysql
from customtkinter import END
from CTkMessagebox import CTkMessagebox
from dotenv import load_dotenv
from interfaces.user import User_Interface

load_dotenv()

def Registration(app):
    if app.firstname.get() == "" or app.lastname.get() == "" or app.username.get() == "" or app.password.get() == "":
        CTkMessagebox(master=app.root, title='Wyntr Streaming Service', message='Enter the Required Details.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00',
                      text_color='#834333', title_color='#954535', icon_size=(40, 40))

    else:
        MySQL_Connector = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        cursor = MySQL_Connector.cursor()

        cursor.execute("SELECT * FROM Accounts WHERE Username = %s", app.username.get())

        UserName = cursor.fetchone()

        if UserName is None:
            cursor.execute(
                "INSERT INTO Accounts (First_Name, Last_Name, Username, Email, Password) VALUES (%s,%s,%s,%s,%s)",
                (app.firstname.get(),
                 app.lastname.get(),
                 app.username.get(),
                 app.password.get()
                 ))
            CTkMessagebox(master=app.root, title='Wyntr Streaming Service', message='Enter the Required Details.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/info.png',
                          option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00',
                          text_color='#834333', title_color='#954535', icon_size=(40, 40))
            User_Interface(app)

        else:
            CTkMessagebox(master=app.root, title='Wyntr Streaming Service',
                          message='Username already Exists in the DataBase.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='Go Back', option_focus=1, justify='center',
                          fade_in_duration=1, button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
            app.username.delete(0, END)

        MySQL_Connector.commit()
        MySQL_Connector.close()