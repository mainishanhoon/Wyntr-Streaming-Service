def CenterWindow(self):
    from utils.center_window import Center_Window
    return Center_Window(self)

def login(self):
    from utils.login import Login
    return Login(self)

def register(self):
    from utils.registration import Registration
    return Registration(self)

def SignOut(self):
    from utils.signOut import Sign_Out
    return Sign_Out(self)

def AddData(self):
    from utils.addData import Add_Data
    return Add_Data(self)

def ShowData(self):
    from utils.showData import Show_Data
    return Show_Data(self)

def SearchData(self):
    from utils.searchData import Search_Data
    return Search_Data(self)

def DeleteData(self):
    from utils.deleteData import Delete_Data
    return Delete_Data(self)

def UpdateData(self):
    from utils.updateData import Update_Data
    return Update_Data(self)

def ClearData(self):
    from utils.clearData import Clear_Data
    return Clear_Data(self)

def GetData(self, event):
    from utils.getData import Get_Data
    return Get_Data(self, event)

def StreamNow(self):
    from utils.streamNow import Stream_Now
    return Stream_Now(self)