from customtkinter import StringVar
from customtkinter import CTk, set_appearance_mode
from interfaces import AdminUI
from utils import CenterWindow

class Wyntr:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x700')
        self.root.resizable(False, False)
        set_appearance_mode('light')

        self.root.iconbitmap('assets/images/Icon.ico')
        self.root.title('Wyntr Streaming Service')

        CenterWindow(self.root)

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

        AdminUI(self)

if __name__ == '__main__':
    app_root = CTk()
    app = Wyntr(app_root)
    app_root.mainloop()

