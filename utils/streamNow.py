import webbrowser
from CTkMessagebox import CTkMessagebox

def StreamNow(self):
    if self.var_ID.get() == '':
        CTkMessagebox(master=self.root, title='Wyntr Streaming Service',
                      message='Select Media that you want to Stream.',
                      font=('Stack Sans Text', 15, 'bold'), wraplength=300, fg_color='#DAA06D',
                      icon='assets/icons/info.png', option_1='OKAY', option_focus=1, justify='center',
                      fade_in_duration=1,
                      button_color='#954535', button_hover_color='#7B3F00', border_width=3,
                      border_color='#7B3F00', text_color='#834333', title_color='#954535', icon_size=(40, 40))
    else:
        webbrowser.open(str(self.var_Link.get()), new=2)