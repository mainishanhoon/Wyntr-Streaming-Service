def LoginUI(self):
    from interfaces.login import Login_Interface
    return Login_Interface(self)

def RegistrationUI(self):
    from interfaces.registration import Registration_Interface
    return Registration_Interface(self)

def AdminUI(self):
    from interfaces.admin import Admin_Interface
    return Admin_Interface(self)

def UserUI(self):
    from interfaces.user import User_Interface
    return User_Interface(self)