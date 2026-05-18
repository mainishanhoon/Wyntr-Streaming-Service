from PIL import Image
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkImage, CTkFrame
from interfaces import RegistrationUI
from utils import login

def Login_Interface(self):
    CTkLabel(
        master=self.root,
        image=CTkImage(
            light_image=Image.open("assets/images/LogIn.png"), size=(1300, 700)
        ),
        text="",
    ).place(x=0, y=0)

    login_frame = CTkFrame(
        master=self.root, fg_color="#E5AA70", bg_color="#E5AA70", width=900, height=400
    )
    login_frame.place(x=(1300 - 900) / 2, y=(700 - 400) / 2)

    CTkLabel(
        master=login_frame,
        image=CTkImage(
            light_image=Image.open("assets/images/Logo.jpg"), size=(400, 400)
        ),
        text="",
    ).place(x=0, y=0)

    CTkLabel(
        master=login_frame,
        text="Sign In",
        text_color="#7B3F00",
        font=("Dela Gothic One", 50),
    ).place(x=450, y=25)

    CTkLabel(
        master=login_frame,
        text="Username",
        text_color="#7B3F00",
        font=("Poppins", 25, "bold"),
    ).place(x=450, y=130)
    self.username = CTkEntry(
        master=login_frame,
        placeholder_text="Enter Your Username...",
        placeholder_text_color="#B67E4A",
        border_width=2,
        fg_color="#F3C892",
        border_color="#7B3F00",
        font=("Poppins", 14, "bold"),
        corner_radius=10,
        width=300,
        height=30,
        text_color="#7B3F00",
    )
    self.username.place(x=450, y=165)

    CTkLabel(
        master=login_frame,
        text="Password",
        text_color="#7B3F00",
        font=("Poppins", 25, "bold"),
    ).place(x=450, y=210)
    self.password = CTkEntry(
        master=login_frame,
        placeholder_text="Enter Password...",
        placeholder_text_color="#B67E4A",
        border_width=2,
        fg_color="#F3C892",
        border_color="#7B3F00",
        font=("Poppins", 14, "bold"),
        show="*",
        corner_radius=10,
        width=300,
        height=30,
        text_color="#7B3F00",
    )
    self.password.place(x=450, y=245)

    CTkButton(
        master=login_frame,
        text="LOGIN",
        command=lambda: login(self),
        font=("Dela Gothic One", 15),
        fg_color="#7B3F00",
        hover_color="#9E5D24",
        text_color="#FFF3E3",
        cursor="hand2",
        hover=True,
        height=36,
        width=110,
    ).place(x=450, y=310)

    CTkLabel(
        master=login_frame,
        text="Don't Have an Account?",
        font=("Poppins", 15, "bold"),
        bg_color="#E5AA70",
        text_color="#7B3F00",
    ).place(x=660, y=285)

    CTkButton(
        master=login_frame,
        text="SIGN UP",
        command=lambda: RegistrationUI(self),
        font=("Dela Gothic One", 15),
        fg_color="#7B3F00",
        hover_color="#9E5D24",
        text_color="#FFF3E3",
        cursor="hand2",
        hover=True,
        height=36,
        width=120,
    ).place(x=695, y=310)

    self.root.bind("<Return>", lambda event: login(self))