from PIL import Image
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkImage, CTkFrame
from utils.login import Login

def Login_Interface(app):
    CTkLabel(master=app.root, image=CTkImage(light_image=Image.open('Images/LogIn.png'), size=(1300, 700)),
             text='').place(x=0, y=0)

    login_frame = CTkFrame(master=app.root, fg_color='#E5AA70', bg_color='#E5AA70', width=900, height=400)
    login_frame.place(x=(1300 - 900) / 2, y=(700 - 400) / 2)

    CTkLabel(master=login_frame, image=CTkImage(light_image=Image.open('Images/Logo.jpg'), size=(400, 400)),
             text='').place(x=0, y=0)

    CTkLabel(master=login_frame, text='Sign In', text_color='#834333', font=('Dela Gothic One', 50)).place(x=450,
                                                                                                           y=25)

    CTkLabel(master=login_frame, text='Username', text_color='#954535', font=('Stack Sans Text', 25, 'bold')).place(
        x=450, y=130)
    app.username = CTkEntry(master=login_frame, placeholder_text='Enter Your Username...',
                             placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                             border_color='#834333', font=('Stack Sans Text', 15, 'bold'), corner_radius=10,
                             width=300, height=30, text_color='#834333')
    app.username.place(x=450, y=165)

    CTkLabel(master=login_frame, text='Password', text_color='#954535', font=('Stack Sans Text', 25, 'bold')).place(
        x=450, y=210)
    app.password = CTkEntry(master=login_frame, placeholder_text='Enter Password...',
                             placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                             border_color='#834333', font=('Stack Sans Text', 15, 'bold'), show='*',
                             corner_radius=10, width=300, height=30, text_color='#834333')
    app.password.place(x=450, y=245)

    CTkButton(master=login_frame, text='LOGIN', command=app.login, font=('Dela Gothic One', 15),
              fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=36, width=110).place(
        x=450, y=310)

    CTkLabel(master=login_frame, text='Don\'t Have an Account?', font=('Stack Sans Text', 15, 'bold'),
             bg_color='#E5AA70', text_color='#834333').place(x=660, y=280)

    CTkButton(master=login_frame, text='SIGN UP', command=app.RegistrationUI, font=('Dela Gothic One', 15),
              fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=36, width=120).place(
        x=695, y=310)

    app.root.bind('<Return>', lambda event: Login(app))