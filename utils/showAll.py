from utils import GetData
from utils.showData import Show_Data
from CTkTable import CTkTable

def Show_All(self):
    fresh_values = Show_Data(self)

    table_master = self.Media_Table.master

    self.Media_Table.destroy()

    self.Media_Table = CTkTable(
        master=table_master,
        column=7,
        values=fresh_values,
        header_color='#9E5D24',
        text_color='#4A2711',
        bg_color='#E5AA70',
        colors=['#C68B59', '#D9A06F'],
        font=('Stack Sans Text', 13),
        command=lambda data : GetData(self, data)
    )
    self.Media_Table.pack(fill='both', expand=False)

    column_widths = [50, 250, 50, 60, 50, 50, 60]

    for col, w in enumerate(column_widths):
        self.Media_Table.edit_column(col, width=w)