import webbrowser
from CTkMessagebox import CTkMessagebox

def Stream_Now(self):
    if self.var_ID.get() == "":
        CTkMessagebox(
            master=self.root,
            title="Wyntr Streaming Service",
            message="Select Media that you want to Stream.",
            font=("Poppins", 14, 'bold'),
            wraplength=400,
            fg_color="#DAA06D",
            icon="assets/icons/info.png",
            option_1="OKAY",
            option_focus=1,
            justify="center",
            fade_in_duration=1,
            button_color="#7B3F00",
            button_hover_color="#9E5D24",
            border_width=3,
            border_color="#7B3F00",
            text_color="#7B3F00",
            title_color="#7B3F00",
            icon_size=(40, 40),
        )
    else:
        webbrowser.open(str(self.var_Link.get()), new=2)