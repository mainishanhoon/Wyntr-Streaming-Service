import os, pymysql
from CTkMessagebox import CTkMessagebox
from utils import ShowAll, ClearData

def Delete_Data(self):
    if self.var_ID.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                      message='Select Media that You want to Delete.',
                      font=('Google Sans Code Mono', 15), wraplength=500, fg_color='#DAA06D',
                      icon='assets/icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#7B3F00', button_hover_color='#9E5D24', border_width=3,
                      border_color='#7B3F00', text_color='#7B3F00', title_color='#7B3F00', icon_size=(40, 40))
    else:
        MySQL_Connector = pymysql.connect(host=os.getenv('DB_HOST'),
                                          user=os.getenv('DB_USER'),
                                          password=os.getenv('DB_PASSWORD'),
                                          database=os.getenv('DB_NAME'))

        cursor = MySQL_Connector.cursor()

        cursor.execute('DELETE FROM Media WHERE mediaId = %s', self.var_ID.get())

        MySQL_Connector.commit()

        CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                      message='Selected Media has been Deleted.',
                      font=('Google Sans Code Mono', 15), wraplength=500, fg_color='#DAA06D',
                      icon='assets/icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#7B3F00', button_hover_color='#9E5D24', border_width=3,
                      border_color='#7B3F00', text_color='#7B3F00', title_color='#7B3F00', icon_size=(40, 40))

        ShowAll(self)

        ClearData(self)

        MySQL_Connector.close()