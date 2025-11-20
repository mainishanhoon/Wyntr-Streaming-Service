from PIL import Image
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkImage, CTkFrame
from utils.registration import Registration

def Registration_Interface(app):
    CTkLabel(master=app.root, image=CTkImage(light_image=Image.open('Images/Registration.jpg'), size=(1300, 700)),
             text='').place(x=0, y=0)

    registration_frame = CTkFrame(master=app.root, fg_color='#E5AA70', bg_color='#E5AA70', width=900, height=400)
    registration_frame.place(x=(1300 - 900) / 2, y=(700 - 400) / 2)

    CTkLabel(master=registration_frame, image=CTkImage(light_image=Image.open('Images/Logo.jpg'), size=(400, 400)),
             text='').place(x=0, y=0)

    CTkLabel(master=registration_frame, text='Sign Up', text_color='#834333', font=('Dela Gothic One', 50)).place(
        x=450, y=15)
    CTkLabel(master=registration_frame, text='Username', text_color='#954535',
             font=('Stack Sans Text', 15, 'bold')).place(x=450, y=95)
    app.username = CTkEntry(master=registration_frame, placeholder_text='Enter Your Username...',
                             placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                             border_color='#834333', font=('Stack Sans Text', 15, 'bold'), corner_radius=10,
                             width=350,
                             height=30, text_color='#834333')
    app.username.place(x=450, y=120)

    CTkLabel(master=registration_frame, text='First Name', text_color='#954535',
             font=('Stack Sans Text', 15, 'bold')).place(x=450, y=150)
    app.firstname = CTkEntry(master=registration_frame, placeholder_text='Enter Your First Name...',
                              placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                              border_color='#834333', font=('Stack Sans Text', 15, 'bold'), corner_radius=10,
                              width=350,
                              height=30, text_color='#834333')
    app.firstname.place(x=450, y=175)

    CTkLabel(master=registration_frame, text='Last Name', text_color='#954535',
             font=('Stack Sans Text', 15, 'bold')).place(x=450, y=205)
    app.lastname = CTkEntry(master=registration_frame, placeholder_text='Enter Your Last Name...',
                             placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                             border_color='#834333', font=('Stack Sans Text', 15, 'bold'), corner_radius=10,
                             width=350,
                             height=30, text_color='#834333')
    app.lastname.place(x=450, y=230)

    CTkLabel(master=registration_frame, text='Password', text_color='#954535',
             font=('Stack Sans Text', 15, 'bold')).place(x=450, y=260)
    app.password = CTkEntry(master=registration_frame, placeholder_text='Enter Password...',
                             placeholder_text_color='#C19A6B', border_width=2, fg_color='#F3C892',
                             border_color='#834333', font=('Stack Sans Text', 15, 'bold'), show='*',
                             corner_radius=10,
                             width=350, height=30, text_color='#834333')
    app.password.place(x=450, y=285)

    CTkButton(master=registration_frame, text='REGISTER', command=app.register, font=('Dela Gothic One', 15),
              fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=36, width=135).place(
        x=450, y=325)

    CTkButton(master=registration_frame, text='BACK', command=app.LoginUI, font=('Dela Gothic One', 15),
              fg_color='#954535', hover_color='#7B3F00', cursor='hand2', hover=True, height=36, width=120).place(
        x=680, y=325)

    app.root.bind('<Return>', lambda event: Registration(app))