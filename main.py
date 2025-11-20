from customtkinter import StringVar
from customtkinter import CTk, set_appearance_mode
from utils.center_window import CenterWindow

class Wyntr:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x700')
        self.root.resizable(False, False)
        set_appearance_mode('light')

        self.root.iconbitmap('Images/Icon.ico')
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
        self.AdminUI()

    def LoginUI(self):
        from interfaces.login import Login_Interface
        Login_Interface(self)

    def login(self):
        from utils.login import Login
        Login(self)

    def RegistrationUI(self):
        from interfaces.registration import Registration_Interface
        Registration_Interface(self)

    def register(self):
        from utils.registration import Registration
        Registration(self)

    def AdminUI(self):
        from interfaces.admin import Admin_Interface
        Admin_Interface(self)

    def UserUI(self):
        from interfaces.user import User_Interface
        User_Interface(self)

    def SignOut(self):
        from utils.signOut import Sign_Out
        Sign_Out(self)

    def AddDetails(self):
        from utils.addData import Add_Details
        Add_Details(self)

    def ShowAllData(self):
        from utils.showData import Show_Data
        Show_Data(self)

    def SearchData(self):
        from utils.searchData import Search_Data
        Search_Data(self)

    def DeleteData(self):
        from utils.deleteData import Delete_Data
        Delete_Data(self)

    def UpdateData(self):
        from utils.updateData import Update_Data
        Update_Data(self)

    def ClearData(self):
        from utils.clearData import Clear_Data
        Clear_Data(self)

    def AddData(self):
        from utils.addData import Add_Data
        Add_Data(self)

if __name__ == "__main__":
    root = CTk()
    app = Wyntr(root)
    root.mainloop()
