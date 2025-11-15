from customtkinter import CTk, CTkLabel, CTkImage, set_appearance_mode, CTkEntry, CTkButton, CTkFrame
from PIL import Image

class Wyntr(CTk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.center_window()
        self.resizable(False, False)
        set_appearance_mode("light")
        self.login_interface()
        self.title("Wyntr Streaming Service")

    def center_window(self):
        scaling = self._get_window_scaling()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2 - self.width / 2) * scaling)
        y = int((screen_height / 2 - self.height / 2) * scaling)
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def login_interface(self):
        CTkLabel(master=self, image=CTkImage(light_image=Image.open("Images/LogIn.png"), size=(1300, 700)), text="").place(x=0,y=0)

        login_frame = CTkFrame(master=self, fg_color="#E5AA70", width=900, height=400)
        login_frame.place(x=(self.width - 900) // 2, y=(self.height - 400) // 2)

        CTkLabel(master=login_frame, image=CTkImage(light_image=Image.open("Images/Logo.jpg"), size=(400, 400)), text="").place(x=0, y=0)

        CTkLabel(master=login_frame, text="Sign In", text_color="#834333", font=("Dela Gothic One", 50)).place(x=450, y=25)

        CTkLabel(master=login_frame, text="Username", text_color="#954535", font=("Product Sans", 25, "bold")).place(x=450, y=130)
        CTkEntry(master=login_frame, placeholder_text="Enter Your Username...", placeholder_text_color="#C19A6B", border_width=2, fg_color="#F3C892", border_color="#834333", font=("Product Sans", 15, "bold"), corner_radius=10, width=300, height=30, text_color="#834333").place(x=450, y=165)

        CTkLabel(master=login_frame, text="Password", text_color="#954535", font=("Product Sans", 25, "bold")).place(x=450, y=210)
        CTkEntry(master=login_frame, placeholder_text="Enter Password...", placeholder_text_color="#C19A6B", border_width=2, fg_color="#F3C892", border_color="#834333", font=("Product Sans", 15, "bold"), show="*", corner_radius=10, width=300, height=30, text_color="#834333").place(x=450, y=245)

        CTkButton(master=login_frame, text="LOGIN", font=("Dela Gothic One", 15), fg_color="#954535", hover_color="#7B3F00", cursor='hand2', hover=True, height=36, width=110).place(x=450, y=310)

        CTkLabel(master=login_frame, text="Don't Have an Account?", font=("Product Sans", 15, "bold"), bg_color="#E5AA70", text_color="#834333").place(x=675, y=280)

        CTkButton(master=login_frame, text="SIGN UP", font=("Dela Gothic One", 15), fg_color="#954535", hover_color="#7B3F00", cursor='hand2', hover=True, height=36, width=120).place(x=695, y=310)


if __name__ == "__main__":
    app = Wyntr(1300, 700)
    app.mainloop()
