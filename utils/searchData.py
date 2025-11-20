import os, pymysql
from customtkinter import END
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkLabel
from utils.clearData import Clear


def Search_Data(app):
    if app.var_SearchBy.get() == "Select Category":
        CTkMessagebox(master=app.root, title='Wyntr Streaming Service',
                      message='On What Basis You Wanna Filter the List.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    elif app.var_SearchBox.get() == "":
        CTkMessagebox(master=app.root, title='Wyntr Streaming Service',
                      message='Search Box is Empty.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

    else:
        MySQL_Connector = pymysql.connect(host=os.getenv('DB_HOST'),
                                          user=os.getenv('DB_USER'),
                                          password=os.getenv('DB_PASSWORD'),
                                          database=os.getenv('DB_NAME'))
        cursor = MySQL_Connector.cursor()
        cursor.execute("SELECT * FROM Media WHERE " + str(app.var_SearchBy.get()) + "  LIKE '%" + str(
            app.var_SearchBox.get()) + "%' ")
        Details = cursor.fetchall()
        if len(Details) != 0:
            app.Media_Table.delete(*app.Media_Table.get_children())
        for Data in Details:
            app.Media_Table.insert("", END, values=Data)
        else:
            No_Data = CTkLabel(master=app.root, text="Oops! No Medias Were Found",
                               font=("Dela Gothic One", 45, 'bold'),
                               fg="#021E2F", bg='#FFEFD5')
        No_Data.place(x=622, y=189, height=597, width=890)
        No_Data.after(3000, No_Data.destroy)
        Clear()
        MySQL_Connector.commit()
        MySQL_Connector.close()