import os, pymysql
from CTkMessagebox import CTkMessagebox
from utils import ShowData

def Delete_Data(self):
    if self.var_ID.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                      message='Select Media that You want to Delete.',
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

        cursor.execute('DELETE FROM Media WHERE ID = %s', self.var_ID.get())

        MySQL_Connector.commit()

        CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                      message='Selected Media has been Deleted.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        ShowData(self)

        MySQL_Connector.close()