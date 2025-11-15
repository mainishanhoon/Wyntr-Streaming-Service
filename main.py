import pymysql
from CTkMessagebox import CTkMessagebox
from customtkinter import CTk, CTkLabel, CTkImage, set_appearance_mode, CTkEntry, CTkButton, CTkFrame, END
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

class Wyntr:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700")
        self.root.resizable(False, False)
        set_appearance_mode("light")

        self.root.iconbitmap("Images/Icon.ico")
        self.root.title("Wyntr Streaming Service")

        self.center_window()
        self.Login_Interface()


    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width - 1300) / 2)
        y = int((screen_height - 700) / 2)

        self.root.geometry(f"{1300}x{700}+{x}+{y}")

    def Login_Interface(self):
        CTkLabel(master=self.root, image=CTkImage(light_image=Image.open("Images/LogIn.png"), size=(1300, 700)), text="").place(x=0,y=0)

        login_frame = CTkFrame(master=self.root, fg_color="#E5AA70", width=900, height=400)
        login_frame.place(x=(1300 - 900) / 2, y=(700 - 400) / 2)

        CTkLabel(master=login_frame, image=CTkImage(light_image=Image.open("Images/Logo.jpg"), size=(400, 400)), text="").place(x=0, y=0)

        CTkLabel(master=login_frame, text="Sign In", text_color="#834333", font=("Dela Gothic One", 50)).place(x=450, y=25)

        CTkLabel(master=login_frame, text="Username", text_color="#954535", font=("Product Sans", 25, "bold")).place(x=450, y=130)
        self.username=CTkEntry(master=login_frame, placeholder_text="Enter Your Username...", placeholder_text_color="#C19A6B", border_width=2, fg_color="#F3C892", border_color="#834333", font=("Product Sans", 15, "bold"), corner_radius=10, width=300, height=30, text_color="#834333")
        self.username.place(x=450, y=165)

        CTkLabel(master=login_frame, text="Password", text_color="#954535", font=("Product Sans", 25, "bold")).place(x=450, y=210)
        self.password=CTkEntry(master=login_frame, placeholder_text="Enter Password...", placeholder_text_color="#C19A6B", border_width=2, fg_color="#F3C892", border_color="#834333", font=("Product Sans", 15, "bold"), show="*", corner_radius=10, width=300, height=30, text_color="#834333")
        self.password.place(x=450, y=245)

        CTkButton(master=login_frame, text="LOGIN", command=self.Login, font=("Dela Gothic One", 15), fg_color="#954535", hover_color="#7B3F00", cursor='hand2', hover=True, height=36, width=110).place(x=450, y=310)

        CTkLabel(master=login_frame, text="Don't Have an Account?", font=("Product Sans", 15, "bold"), bg_color="#E5AA70", text_color="#834333").place(x=675, y=280)

        CTkButton(master=login_frame, text="SIGN UP", font=("Dela Gothic One", 15), fg_color="#954535", hover_color="#7B3F00", cursor='hand2', hover=True, height=36, width=120).place(x=695, y=310)

        self.root.bind('<Return>', self.Login)

    def Login(self, event=None):
        if self.username.get() == "" and self.password.get() == "":
            CTkMessagebox(master=self.root, title="Wyntr Streaming Service", message="Enter Username & Password.", font=("Product Sans", 15, "bold"), wraplength=300, fg_color="#DAA06D", icon="info", option_1="OKAY", option_focus=1, justify="center", fade_in_duration=2, button_color="#954535", button_hover_color="#7B3F00", border_width=3, border_color="#7B3F00", text_color="#834333", title_color="#954535", icon_size=(40,40))

        elif self.username.get() == "":
            CTkMessagebox(master=self.root, title="Wyntr Streaming Service", message="Enter Username.",
                          font=("Product Sans", 15, "bold"), wraplength=300, fg_color="#DAA06D", icon="info",
                          option_1="OKAY", option_focus=1, justify="center", fade_in_duration=2, button_color="#954535",
                          button_hover_color="#7B3F00", border_width=3, border_color="#7B3F00", text_color="#834333",
                          title_color="#954535", icon_size=(40, 40))

        elif self.password.get() == "":
            CTkMessagebox(master=self.root, title="Wyntr Streaming Service", message="Enter Password.",
                          font=("Product Sans", 15, "bold"), wraplength=300, fg_color="#DAA06D", icon="Icons/info.png",
                          option_1="OKAY", option_focus=1, justify="center", fade_in_duration=2, button_color="#954535",
                          button_hover_color="#7B3F00", border_width=3, border_color="#7B3F00", text_color="#834333",
                          title_color="#954535", icon_size=(40, 40))

        else:
            MySQL_Connector = pymysql.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            cursor = MySQL_Connector.cursor()

            cursor.execute("SELECT * FROM Accounts WHERE Username = %s AND Password = %s",
                           (self.username.get(), self.password.get()))

            row = cursor.fetchone()

            if self.username.get() == "a" and self.password.get() == "1":
                # self.Management_Interface()
                print("hfdhf")

            elif row is None:
                CTkMessagebox(master=self.root, title="Wyntr Streaming Service", message="Invalid Username/Password.", font=("Product Sans", 15, "bold"), wraplength=300, fg_color="#DAA06D", icon="Icons/alert.png", option_1="Sign Up", option_2="Go Back", option_focus=2, justify="center", fade_in_duration=2, button_color="#954535", button_hover_color="#7B3F00", border_width=3, border_color="#7B3F00", text_color="#834333", title_color="#954535", icon_size=(40, 40))
                self.Login_Clear()

            else:
                CTkMessagebox(master=self.root, title="Wyntr Streaming Service", message="Welcome to Wyntr Streaming Service.", font=("Product Sans", 15, "bold"), wraplength=300, fg_color="#DAA06D", icon="Icons/check.png", option_1="OKAY", option_focus=1, justify="center", fade_in_duration=2, button_color="#954535", button_hover_color="#7B3F00", border_width=3, border_color="#7B3F00", text_color="#834333", title_color="#954535", icon_size=(40, 40))
                # self.Media_Interface()

            MySQL_Connector.close()

    def Login_Clear(self):
        self.username.delete("0", END)
        self.password.delete("0", END)

root=CTk()
obj = Wyntr(root)
root.mainloop()
