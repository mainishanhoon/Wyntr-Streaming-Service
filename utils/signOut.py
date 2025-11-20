from CTkMessagebox import CTkMessagebox
from interfaces.login import Login_Interface

def Sign_Out(app):
    CTkMessagebox(master=app.root, title="Wyntr Streaming Service",
                  message="Thankyou for Using Wyntr Streaming Service!",
                  font=('Stack Sans Text', 15, 'bold'), wraplength=250, fg_color='#DAA06D', icon='Icons/check.png',
                  option_1='OKAY', option_focus=1, justify='center', fade_in_duration=1, button_color='#954535',
                  button_hover_color='#7B3F00', border_width=3, border_color='#7B3F00', text_color='#834333',
                  title_color='#954535', icon_size=(40, 40))

    Login_Interface(app.root)