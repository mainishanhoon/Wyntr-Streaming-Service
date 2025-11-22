import os
from CTkMessagebox import CTkMessagebox
from dotenv import load_dotenv
from utils import ShowData, ClearData

load_dotenv()


def Add_Data(self):
    if self.var_ID.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the ID of Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_Type.get() == 'Select Type':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Type of Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_Title.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Title of Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_Genre.get() == 'Select Genre':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Genre of Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_IMDb.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the IMDb rating of Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_Certificate.get() == 'Select Certificate':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Certificate of Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_Platform.get() == 'Select Streaming Platform':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                      message='Enter the Streaming Platform of Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_Description.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Description of Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif self.var_Link.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter Link of the Media.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    else:
        MySQL_Connector = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        cursor = MySQL_Connector.cursor()

        cursor.execute('SELECT * FROM Media WHERE ID = %s', self.var_ID.get())

        Details = cursor.fetchone()

        if Details != None:
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Media with this ID already exists.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='assets/icons/alert.png', option_1='OKAY', option_focus=1, justify='center',
                          fade_in_duration=1, button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        else:
            cursor.execute('INSERT INTO Media VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                self.var_ID.get(),
                self.var_Title.get(),
                self.var_Genre.get(),
                self.var_Type.get(),
                self.var_IMDb.get(),
                self.var_Certificate.get(),
                self.var_Platform.get(),
                self.var_Description.get(),
                self.var_Link.get()
            ))

            MySQL_Connector.commit()

            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Your Media is now Streaming.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='assets/icons/info.png', option_1='OKAY', option_focus=1, justify='center',
                          fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

            ShowData(self)

            ClearData(self)

            MySQL_Connector.close()