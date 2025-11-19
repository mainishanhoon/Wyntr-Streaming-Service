from tkinter import StringVar

import pymysql, webbrowser
from CTkMessagebox import CTkMessagebox
from CTkTable import CTkTable
from customtkinter import CTk, CTkLabel, CTkImage, set_appearance_mode, CTkEntry, CTkButton, CTkFrame, END, CTkComboBox
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()


class Wyntr:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x700')
        self.root.resizable(False, False)
        set_appearance_mode('light')

        self.root.iconbitmap('Images/Icon.ico')
        self.root.title('Wyntr Streaming Service')

        self.center_window()
        self.Management_Interface()

    def center_window(self):
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (1300 // 2)
        y = (screen_height // 2) - (700 // 2)

        self.root.geometry(f'{1300}x{700}+{x}+{y}')

    def Login_Interface(self):
        CTkLabel(master=self.root, image=CTkImage(light_image=Image.open('Images/LogIn.png'), size=(1300, 700)),
                 text='').place(x=0, y=0)

        login_frame = CTkFrame(master=self.root, fg_color='#E5AA70', bg_color='#E5AA70', width=900, height=400)
        login_frame.place(x=(1300 - 900) / 2, y=(700 - 400) / 2)

        CTkLabel(master=login_frame, image=CTkImage(light_image=Image.open('Images/Logo.jpg'), size=(400, 400)),
                 text='').place(x=0, y=0)

        CTkLabel(master=login_frame, text='Sign In', text_color='#834333', font=('Dela Gothic One', 50)).place(x=450,
                                                                                                               y=25)

        CTkLabel(master=login_frame, text='Username', text_color='#954535', font=('Stack Sans Text', 25, 'bold')).place(
            x=450, y=130)
        self.username = CTkEntry(master=login_frame, placeholder_text='Enter Your Username...',
                                 placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                                 border_color='#834333', font=('Stack Sans Text', 15, 'bold'), corner_radius=10,
                                 width=300, height=30, text_color='#834333')
        self.username.place(x=450, y=165)

        CTkLabel(master=login_frame, text='Password', text_color='#954535', font=('Stack Sans Text', 25, 'bold')).place(
            x=450, y=210)
        self.password = CTkEntry(master=login_frame, placeholder_text='Enter Password...',
                                 placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                                 border_color='#834333', font=('Stack Sans Text', 15, 'bold'), show='*',
                                 corner_radius=10, width=300, height=30, text_color='#834333')
        self.password.place(x=450, y=245)

        CTkButton(master=login_frame, text='LOGIN', command=self.Login, font=('Dela Gothic One', 15),
                  fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=36, width=110).place(
            x=450, y=310)

        CTkLabel(master=login_frame, text='Don\'t Have an Account?', font=('Stack Sans Text', 15, 'bold'),
                 bg_color='#E5AA70', text_color='#834333').place(x=675, y=280)

        CTkButton(master=login_frame, text='SIGN UP', command=self.Registration_Interface, font=('Dela Gothic One', 15),
                  fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=36, width=120).place(
            x=695, y=310)

        self.root.bind('<Return>', lambda event: self.Login())

    def Login(self):
        if self.username.get() == '' and self.password.get() == '':
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter Username & Password.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00',
                          text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.username.get() == '':
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter Username.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/info.png',
                          option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                          button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00', text_color='#834333',
                          title_color='#954535', icon_size=(40, 40))

        elif self.password.get() == '':
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter Password.',
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
                           (self.username.get(), self.password.get()))

            row = cursor.fetchone()

            if self.username.get() == os.getenv('USERNAME') and self.password.get() == os.getenv('PASSWORD'):
                self.Management_Interface()

            elif row is None:
                CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Invalid Username/Password.',
                              font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                              icon='Icons/alert.png', option_1='Go Back', option_focus=1, justify='center',
                              fade_in_duration=1, button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                              border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
                self.username.delete('0', END)
                self.password.delete('0', END)

            else:
                CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                              message='Welcome to Wyntr Streaming Service.', font=('Stack Sans Text', 15, 'bold'),
                              wraplength=300, fg_color='#DAA06D', icon='Icons/check.png', option_1='OKAY',
                              option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                              button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00',
                              text_color='#834333', title_color='#954535', icon_size=(40, 40))
                # self.Media_Interface()

            MySQL_Connector.close()

    def Registration_Interface(self):
        CTkLabel(master=self.root, image=CTkImage(light_image=Image.open('Images/Registration.jpg'), size=(1300, 700)),
                 text='').place(x=0, y=0)

        registration_frame = CTkFrame(master=self.root, fg_color='#E5AA70', bg_color='#E5AA70', width=900, height=400)
        registration_frame.place(x=(1300 - 900) / 2, y=(700 - 400) / 2)

        CTkLabel(master=registration_frame, image=CTkImage(light_image=Image.open('Images/Logo.jpg'), size=(400, 400)),
                 text='').place(x=0, y=0)

        CTkLabel(master=registration_frame, text='Sign Up', text_color='#834333', font=('Dela Gothic One', 50)).place(
            x=450, y=15)
        CTkLabel(master=registration_frame, text='Username', text_color='#954535',
                 font=('Stack Sans Text', 15, 'bold')).place(x=450, y=95)
        self.username = CTkEntry(master=registration_frame, placeholder_text='Enter Your Username...',
                                 placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                                 border_color='#834333', font=('Stack Sans Text', 15, 'bold'), corner_radius=10,
                                 width=350,
                                 height=30, text_color='#834333')
        self.username.place(x=450, y=120)

        CTkLabel(master=registration_frame, text='First Name', text_color='#954535',
                 font=('Stack Sans Text', 15, 'bold')).place(x=450, y=150)
        self.firstname = CTkEntry(master=registration_frame, placeholder_text='Enter Your First Name...',
                                  placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                                  border_color='#834333', font=('Stack Sans Text', 15, 'bold'), corner_radius=10,
                                  width=350,
                                  height=30, text_color='#834333')
        self.firstname.place(x=450, y=175)

        CTkLabel(master=registration_frame, text='Last Name', text_color='#954535',
                 font=('Stack Sans Text', 15, 'bold')).place(x=450, y=205)
        self.lastname = CTkEntry(master=registration_frame, placeholder_text='Enter Your Last Name...',
                                 placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                                 border_color='#834333', font=('Stack Sans Text', 15, 'bold'), corner_radius=10,
                                 width=350,
                                 height=30, text_color='#834333')
        self.lastname.place(x=450, y=230)

        CTkLabel(master=registration_frame, text='Password', text_color='#954535',
                 font=('Stack Sans Text', 15, 'bold')).place(x=450, y=260)
        self.password = CTkEntry(master=registration_frame, placeholder_text='Enter Password...',
                                 placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                                 border_color='#834333', font=('Stack Sans Text', 15, 'bold'), show='*',
                                 corner_radius=10,
                                 width=350, height=30, text_color='#834333')
        self.password.place(x=450, y=285)

        CTkButton(master=registration_frame, text='REGISTER', command=self.Registration, font=('Dela Gothic One', 15),
                  fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=36, width=135).place(
            x=450, y=325)

        CTkButton(master=registration_frame, text='BACK', command=self.Login_Interface, font=('Dela Gothic One', 15),
                  fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=36, width=120).place(
            x=680, y=325)

        self.root.bind('<Return>', lambda event: self.Registration())

    def Registration(self):
        if self.firstname.get() == "" or self.lastname.get() == "" or self.username.get() == "" or self.password.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Required Details.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/info.png',
                          option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
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

            cursor.execute("SELECT * FROM Accounts WHERE Username = %s", self.username.get())

            UserName = cursor.fetchone()

            if UserName is None:
                cursor.execute(
                    "INSERT INTO Accounts (First_Name, Last_Name, Username, Email, Password) VALUES (%s,%s,%s,%s,%s)",
                    (self.firstname.get(),
                     self.lastname.get(),
                     self.username.get(),
                     self.password.get()
                     ))
                CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Required Details.',
                              font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                              icon='Icons/info.png',
                              option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                              button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                              border_color='#7B3F00',
                              text_color='#834333', title_color='#954535', icon_size=(40, 40))
                # self.Media_Interface()

            else:
                CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                              message='Username already Exists in the DataBase.',
                              font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                              icon='Icons/alert.png', option_1='Go Back', option_focus=1, justify='center',
                              fade_in_duration=1, button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                              border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
                self.username.delete(0, END)

            MySQL_Connector.commit()
            MySQL_Connector.close()

    def Management_Interface(self):
        self.var_ID = StringVar()
        self.var_Title = StringVar()
        self.var_Genre = StringVar()
        self.var_Type = StringVar()
        self.var_IMDb = StringVar()
        self.var_Certificate = StringVar()
        self.var_Platform = StringVar()
        self.var_Description = StringVar()
        self.var_Link = StringVar()
        self.var_SearchBy = StringVar()
        self.var_SearchBox = StringVar()

        management_frame = CTkFrame(master=self.root, fg_color='#F3C892', bg_color='#F3C892', width=1300, height=700)
        management_frame.place(x=0, y=0)

        title_frame = CTkFrame(master=management_frame, fg_color='#E5AA70', bg_color='#F3C892', width=1280, height=80,
                               border_width=2, border_color='#834333')
        title_frame.place(x=10, y=10)

        CTkLabel(master=title_frame, image=CTkImage(light_image=Image.open('Images/Logo.png'), size=(70, 70)),
                 text='').place(x=50, y=5)

        CTkLabel(master=title_frame, text='Wyntr Streaming Service', text_color='#7B3F00',
                 font=('Dela Gothic One', 40, 'bold')).place(x=350, y=5)

        CTkButton(master=title_frame, text='',
                  image=CTkImage(light_image=Image.open('Images/Sign_Out.png'), size=(35, 35)), command=self.SignOut,
                  font=('Dela Gothic One', 15), fg_color='#E5AA70', hover_color='#7B3F00', cursor='hand2', hover=False,
                  height=30, width=30).place(x=1180, y=20)

        details_frame = CTkFrame(master=management_frame, fg_color='#E5AA70', bg_color='#F3C892', width=370, height=590,
                                 border_width=2, border_color='#834333')
        details_frame.place(x=10, y=100)

        CTkLabel(master=details_frame, text='Details', text_color='#954535', font=('Dela Gothic One', 30)).place(x=110, y=2)

        CTkLabel(master=details_frame, text='ID', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=15, y=45)
        ID = CTkEntry(master=details_frame, placeholder_text='Enter ID...', textvariable=self.var_ID,
                      placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                      border_color='#834333', font=('Stack Sans Text', 15, 'bold'),
                      corner_radius=10, width=170, height=30, text_color='#834333')
        ID.place(x=10, y=70)

        CTkLabel(master=details_frame, text='Type', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=195, y=45)
        Type = CTkEntry(master=details_frame, placeholder_text='Enter Type...', textvariable=self.var_Type,
                        placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                        border_color='#834333', font=('Stack Sans Text', 15, 'bold'),
                        corner_radius=10, width=170, height=30, text_color='#834333')
        Type.place(x=190, y=70)

        CTkLabel(master=details_frame, text='Title', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=15, y=100)
        Title = CTkEntry(master=details_frame, placeholder_text='Enter Title...', textvariable=self.var_Title,
                         placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                         border_color='#834333', font=('Stack Sans Text', 15, 'bold'),
                         corner_radius=10, width=350, height=30, text_color='#834333')
        Title.place(x=10, y=125)

        CTkLabel(master=details_frame, text='Genre', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=15, y=155)
        Genre = CTkEntry(master=details_frame, placeholder_text='Enter Genre...', textvariable=self.var_Genre,
                         placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                         border_color='#834333', font=('Stack Sans Text', 15, 'bold'),
                         corner_radius=10, width=170, height=30, text_color='#834333')
        Genre.place(x=10, y=180)

        CTkLabel(master=details_frame, text='IMDb', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=195, y=155)
        IMDb = CTkEntry(master=details_frame, placeholder_text='Enter IMDb...', textvariable=self.var_IMDb,
                         placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                         border_color='#834333', font=('Stack Sans Text', 15, 'bold'),
                         corner_radius=10, width=170, height=30, text_color='#834333')
        IMDb.place(x=190, y=180)

        CTkLabel(master=details_frame, text='Certificate', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=15, y=210)
        Certificate = CTkComboBox(master=details_frame, values=["U (Unrestricted)", "U/A (Parental Guidance)", "A (Adults)", "S (Special Class)"],
                    state='readonly', height=30, width=170, variable=self.var_Certificate, button_color="#207244",
                    fg_color='#F5DEB3', border_color='#834333', border_width=2, button_hover_color="#954535",
                    dropdown_hover_color="#954535", dropdown_fg_color="#207244", dropdown_text_color="#FFFFFF",
                    text_color="#954535", font=('Stack Sans Text', 14), justify='center',
                    dropdown_font=('Stack Sans Text', 14))
        Certificate.place(x=10, y=235)
        self.var_Certificate.set("Select Certificate")

        CTkLabel(master=details_frame, text='Platform', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=195, y=210)
        Platform = CTkComboBox(master=details_frame, values=["Disney+", "ZEE 5", "VOOT", "Prime Video", "Netflix", "HBO Max", "Sony Liv", "Hulu", "Youtube", "Hotstar"],
                    state='readonly', height=30, width=170, variable=self.var_Platform, button_color="#207244",
                    fg_color='#F5DEB3', border_color='#834333', border_width=2, button_hover_color="#954535",
                    dropdown_hover_color="#954535", dropdown_fg_color="#207244", dropdown_text_color="#FFFFFF",
                    text_color="#954535", font=('Stack Sans Text', 14), justify='center',
                    dropdown_font=('Stack Sans Text', 14))
        Platform.place(x=190, y=235)
        self.var_Platform.set("Select Platform")

        CTkLabel(master=details_frame, text='Description', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=15, y=265)
        Description = CTkEntry(master=details_frame, placeholder_text='Enter Description...', textvariable=self.var_Description,
                         placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                         border_color='#834333', font=('Stack Sans Text', 15, 'bold'),
                         corner_radius=10, width=350, height=30, text_color='#834333')
        Description.place(x=10, y=290)

        CTkLabel(master=details_frame, text='Link', text_color='#954535', font=('Stack Sans Text', 13, 'bold')).place(
            x=15, y=480)
        Link = CTkEntry(master=details_frame, placeholder_text='Enter Link...', textvariable=self.var_Link,
                         placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                         border_color='#834333', font=('Stack Sans Text', 15, 'bold'),
                         corner_radius=10, width=350, height=30, text_color='#834333')
        Link.place(x=10, y=505)

        CTkButton(master=details_frame, text='SEARCH', command=self.Search_Data, font=('Dela Gothic One', 12),
                  fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=30, width=100).place(
            x=10, y=550)

        CTkButton(master=details_frame, text='SHOW ALL', command=self.ShowAll_Data, font=('Dela Gothic One', 12),
                  fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=30, width=100).place(
            x=120, y=550)

        filter_frame = CTkFrame(master=management_frame, fg_color='#E5AA70', bg_color='#F3C892', width=900, height=50,
                                border_width=2, border_color='#834333')
        filter_frame.place(x=390, y=100)

        CTkLabel(master=filter_frame, text='Filter', text_color='#954535', font=('Dela Gothic One', 30)).place(x=50,
                                                                                                               y=2)
        CTkComboBox(master=filter_frame, values=["Title", "Genre", "Type", "Certificate", "Platform"],
                    state='readonly', height=30, width=200, variable=self.var_SearchBy, button_color="#207244",
                    fg_color='#F5DEB3', border_color='#834333', border_width=2, button_hover_color="#954535",
                    dropdown_hover_color="#954535", dropdown_fg_color="#207244", dropdown_text_color="#FFFFFF",
                    text_color="#954535", font=('Stack Sans Text', 15), justify='center',
                    dropdown_font=('Stack Sans Text', 14)).place(x=260, y=10)

        self.var_SearchBy.set("Select Category")

        CTkEntry(master=filter_frame, textvariable=self.var_SearchBox, height=30, width=200,
                 placeholder_text='Enter Value...',
                 placeholder_text_color='#C19A6B', border_width=2, fg_color='#F5DEB3', border_color='#834333',
                 font=('Stack Sans Text', 15)).place(x=470, y=10)

        CTkButton(master=filter_frame, text='SEARCH', command=self.Search_Data, font=('Dela Gothic One', 12),
                  fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=30, width=100).place(
            x=680, y=10)

        CTkButton(master=filter_frame, text='SHOW ALL', command=self.ShowAll_Data, font=('Dela Gothic One', 12),
                  fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=30, width=100).place(
            x=790, y=10)

        table_frame = CTkFrame(master=management_frame, fg_color='#E5AA70', bg_color='#F3C892', width=900, height=530,
                               border_width=2, border_color='#834333')
        table_frame.place(x=390, y=160)


    def SignOut(self):
        CTkMessagebox(master=self.root, title="Wyntr Streaming Service",
                      message="Thankyou for Using Wyntr Streaming Service!",
                      font=('Stack Sans Text', 15, 'bold'), wraplength=250, fg_color='#DAA06D', icon='Icons/check.png',
                      option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                      button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00', text_color='#834333',
                      title_color='#954535', icon_size=(40, 40))

        self.Login_Interface()

    def Add_Details(self):
        if self.var_ID.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the ID of Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_Type.get() == "Select Type":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Type of Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_Title.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Title of Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_Genre.get() == "Select Genre":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Genre of Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_IMDb.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the IMDb rating of Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_Certificate.get() == "Select Certificate":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Certificate of Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_Platform.get() == "Select Streaming Platform":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Enter the Streaming Platform of Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_Description.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter the Description of Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_Link.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service', message='Enter Link of the Media.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
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

            cursor.execute("SELECT * FROM Media WHERE ID = %s", self.var_ID.get())
            Details = cursor.fetchone()
            if Details != None:
                CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                              message='Media with this ID already exists.',
                              font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                              icon='Icons/alert.png', option_1='OKAY', option_focus=1, justify='center',
                              fade_in_duration=1, button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                              border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
            else:
                cursor.execute("INSERT INTO Media VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (
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
                              icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center',
                              fade_in_duration=1,
                              button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                              border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
                self.ShowAll_Data()

                self.Clear()
                MySQL_Connector.close()

    def Clear(self):
        self.var_ID.set(""),
        self.var_Title.set(""),
        self.var_Genre.set("Select Genre"),
        self.var_Type.set("Select Type"),
        self.var_IMDb.set(""),
        self.var_Certificate.set("Select Certificate"),
        self.var_Platform.set("Select Streaming Platform"),
        self.var_Description.set("Write Description"),
        self.var_Link.set(""),
        self.var_SearchBy.set("Select Category"),
        self.var_SearchBox.set("")

    def Get_Details(self, event):
        Cursor_Row = self.Media_Table.focus()
        Contents = self.Media_Table.item(Cursor_Row)
        row = Contents['values']
        self.var_ID.set(row[0]),
        self.var_Title.set(row[1]),
        self.var_Genre.set(row[2]),
        self.var_Type.set(row[3]),
        self.var_IMDb.set(row[4]),
        self.var_Certificate.set(row[5]),
        self.var_Platform.set(row[6]),
        self.var_Description.set()
        self.var_Link.set(row[8])

    def Update_Data(self):
        if self.var_ID.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Select Media that you want to Update.',
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
            cursor.execute(
                "UPDATE Media SET Title = %s, Genre = %s, Type = %s, IMDb = %s, Certificate = %s, Platform = %s, Description = %s, Link = %s WHERE ID = %s",
                (
                    self.var_Title.get(),
                    self.var_Genre.get(),
                    self.var_Type.get(),
                    self.var_IMDb.get(),
                    self.var_Certificate.get(),
                    self.var_Platform.get(),
                    self.var_Description.get(),
                    self.var_Link.get(),
                    self.var_ID.get()
                ))
            MySQL_Connector.commit()
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Media Details has been Updated.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
            self.ShowAll_Data()
            self.Clear()
            MySQL_Connector.close()

    def Delete_Data(self):
        if self.var_ID.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Select Media that You want to Delete.',
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
            cursor.execute("DELETE FROM Media WHERE ID = %s", self.var_ID.get())
            MySQL_Connector.commit()
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='Selected Media has been Deleted.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
            self.ShowAll_Data()
            self.Clear()
            MySQL_Connector.close()

    def ShowAll_Data(self):
        MySQL_Connector = pymysql.connect(host=os.getenv('DB_HOST'),
                                          user=os.getenv('DB_USER'),
                                          password=os.getenv('DB_PASSWORD'),
                                          database=os.getenv('DB_NAME'))
        cursor = MySQL_Connector.cursor()
        cursor.execute("SELECT ID, Title, Type, Genre, Certificate, IMDb, PlatForm FROM Media")
        rows = cursor.fetchall()
        MySQL_Connector.commit()
        MySQL_Connector.close()

        return rows

    def Stream_Now(self):
        if self.var_ID.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                              message='Select Media that you want to Stream.',
                              font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                              icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center',
                              fade_in_duration=1,
                              button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                              border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
        else:
            webbrowser.open(str(self.var_Link.get()), new=2)

    def Search_Data(self):
        if self.var_SearchBy.get() == "Select Category":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                          message='On What Basis You Wanna Filter the List.',
                          font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                          icon='Icons/info.png', option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1,
                          button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                          border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))

        elif self.var_SearchBox.get() == "":
            CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
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
            cursor.execute("SELECT * FROM Media WHERE " + str(self.var_SearchBy.get()) + "  LIKE '%" + str(
                self.var_SearchBox.get()) + "%' ")
            Details = cursor.fetchall()
            if len(Details) != 0:
                self.Media_Table.delete(*self.Media_Table.get_children())
            for Data in Details:
                self.Media_Table.insert("", END, values=Data)
            else:
                No_Data = CTkLabel(master=self.root, text="Oops! No Medias Were Found", font=("Dela Gothic One", 45, 'bold'),
                                fg="#021E2F", bg='#FFEFD5')
            No_Data.place(x=622, y=189, height=597, width=890)
            No_Data.after(3000, No_Data.destroy)
            self.Clear()
            MySQL_Connector.commit()
            MySQL_Connector.close()

root = CTk()
obj = Wyntr(root)
root.mainloop()
