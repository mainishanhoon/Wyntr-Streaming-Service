import os, pymysql
from CTkMessagebox import CTkMessagebox
from dotenv import load_dotenv
from utils import ClearData

load_dotenv()

def Search_Data(self):
    if self.var_SearchBy.get() == "Select Category":
        CTkMessagebox(
            master=self.root,
            title="Wyntr Streaming Service",
            message="On What Basis You Wanna Filter the List.",
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

    elif self.var_SearchBox.get() == "":
        CTkMessagebox(
            master=self.root,
            title="Wyntr Streaming Service",
            message="Search Box is Empty.",
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
        MySQL_Connector = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )

        cursor = MySQL_Connector.cursor()

        query = f"SELECT mediaId, title, genre, type, imdb, certificate, platform, description, link FROM media WHERE {self.var_SearchBy.get()} LIKE %s"

        cursor.execute(query, ("%" + self.var_SearchBox.get() + "%",))

        raw_data = cursor.fetchall()

        if raw_data:
            self.full_data_records = [list(row) for row in raw_data]

            ui_rows = [list(row)[:7] for row in raw_data]

            self.Media_Table.delete_rows(range(self.Media_Table.rows))

            self.Media_Table.add_row(self.header)

            column_widths = [50, 250, 50, 60, 50, 50, 60]

            for col, w in enumerate(column_widths):
                self.Media_Table.edit_column(col, width=w)

            for row_data in ui_rows:
                self.Media_Table.add_row(row_data)

        else:
            CTkMessagebox(
                master=self.root,
                title="Wyntr Streaming Service",
                message="Oops!! No Data Found.",
                font=("Google Sans Code Mono", 15),
                wraplength=450,
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

        ClearData(self)

        MySQL_Connector.close()