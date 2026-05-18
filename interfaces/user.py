from CTkTable import CTkTable
from PIL import Image
from customtkinter import (
    CTkFrame,
    CTkButton,
    CTkLabel,
    CTkComboBox,
    CTkImage,
    CTkEntry,
    CTkScrollableFrame,
    CTkTextbox,
)
from utils import SignOut, SearchData, ShowData, GetData, ShowAll, StreamNow


def User_Interface(self):
    user_frame = CTkFrame(
        master=self.root, fg_color="#F3C892", bg_color="#F3C892", width=1400, height=700
    )
    user_frame.place(x=0, y=0)

    title_frame = CTkFrame(
        master=user_frame,
        fg_color="#E5AA70",
        bg_color="#F3C892",
        width=1280,
        height=80,
        border_width=2,
        border_color="#7B3F00",
    )
    title_frame.place(x=10, y=10)

    CTkLabel(
        master=title_frame,
        image=CTkImage(light_image=Image.open("assets/images/Logo.png"), size=(70, 70)),
        text="",
    ).place(x=50, y=5)

    CTkLabel(
        master=title_frame,
        text="Wyntr Streaming Service",
        text_color="#7B3F00",
        font=("Dela Gothic One", 40, "bold"),
    ).place(x=350, y=5)

    CTkButton(
        master=title_frame,
        text="",
        image=CTkImage(
            light_image=Image.open("assets/images/Sign_Out.png"), size=(35, 35)
        ),
        command=lambda: SignOut(self),
        font=("Dela Gothic One", 15),
        fg_color="#E5AA70",
        hover_color="#7B3F00",
        cursor="hand2",
        hover=False,
        height=30,
        width=30,
    ).place(x=1180, y=20)

    details_frame = CTkFrame(
        master=user_frame,
        fg_color="#E5AA70",
        bg_color="#F3C892",
        width=370,
        height=590,
        border_width=2,
        border_color="#7B3F00",
    )
    details_frame.place(x=10, y=100)

    CTkLabel(
        master=details_frame,
        text="Details",
        text_color="#7B3F00",
        font=("Dela Gothic One", 30),
    ).place(x=110, y=2)

    CTkLabel(
        master=details_frame,
        text="ID",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=15, y=45)
    ID = CTkEntry(
        master=details_frame,
        placeholder_text="Enter ID...",
        textvariable=self.var_ID,
        placeholder_text_color="#C19A6B",
        border_width=2,
        fg_color="#F3C892",
        state="disabled",
        border_color="#7B3F00",
        font=("Stack Sans Text", 15),
        corner_radius=10,
        width=170,
        height=30,
        text_color="#7B3F00",
    )
    ID.place(x=10, y=70)

    CTkLabel(
        master=details_frame,
        text="Type",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=195, y=45)
    Type = CTkComboBox(
        master=details_frame,
        values=["Movie", "Series", "Documentary", "Anime"],
        state="disabled",
        height=30,
        width=170,
        variable=self.var_Type,
        text_color_disabled="#7B3F00",
        button_color="#9E5D24",
        fg_color="#F3C892",
        border_color="#7B3F00",
        border_width=2,
        button_hover_color="#7B3F00",
        dropdown_hover_color="#7B3F00",
        dropdown_fg_color="#9E5D24",
        dropdown_text_color="#FFF3E3",
        text_color="#7B3F00",
        font=("Stack Sans Text", 14),
        justify="center",
        dropdown_font=("Stack Sans Text", 14),
    )
    Type.place(x=190, y=70)
    self.var_Type.set("Select Type")

    CTkLabel(
        master=details_frame,
        text="Title",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=15, y=100)
    Title = CTkEntry(
        master=details_frame,
        placeholder_text="Enter Title...",
        textvariable=self.var_Title,
        placeholder_text_color="#C19A6B",
        border_width=2,
        fg_color="#F3C892",
        state="disabled",
        border_color="#7B3F00",
        font=("Stack Sans Text", 15),
        corner_radius=10,
        width=350,
        height=30,
        text_color="#7B3F00",
    )
    Title.place(x=10, y=125)

    CTkLabel(
        master=details_frame,
        text="Genre",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=15, y=155)
    Genre = CTkComboBox(
        master=details_frame,
        values=[
            "Action",
            "Drama",
            "Thriller",
            "Horror",
            "Comedy",
            "Romance",
            "Science Fiction",
            "Fantasy",
            "Adventure",
            "Fiction",
        ],
        state="disabled",
        height=30,
        width=170,
        variable=self.var_Genre,
        text_color_disabled="#7B3F00",
        button_color="#9E5D24",
        fg_color="#F3C892",
        border_color="#7B3F00",
        border_width=2,
        button_hover_color="#7B3F00",
        dropdown_hover_color="#7B3F00",
        dropdown_fg_color="#9E5D24",
        dropdown_text_color="#FFF3E3",
        text_color="#7B3F00",
        font=("Stack Sans Text", 14),
        justify="center",
        dropdown_font=("Stack Sans Text", 14),
    )
    Genre.place(x=10, y=180)
    self.var_Genre.set("Select Genre")

    CTkLabel(
        master=details_frame,
        text="IMDb",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=195, y=155)
    IMDb = CTkEntry(
        master=details_frame,
        placeholder_text="Enter IMDb...",
        textvariable=self.var_IMDb,
        placeholder_text_color="#A67B5B",
        border_width=2,
        fg_color="#F3C892",
        state="disabled",
        border_color="#7B3F00",
        font=("Stack Sans Text", 15),
        corner_radius=10,
        width=170,
        height=30,
        text_color="#7B3F00",
    )
    IMDb.place(x=190, y=180)

    CTkLabel(
        master=details_frame,
        text="Certificate",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=15, y=210)
    Certificate = CTkComboBox(
        master=details_frame,
        values=[
            "U (Unrestricted)",
            "U/A (Parental Guidance)",
            "A (Adults)",
            "S (Special Class)",
        ],
        state="disabled",
        height=30,
        width=170,
        variable=self.var_Certificate,
        text_color_disabled="#7B3F00",
        button_color="#9E5D24",
        fg_color="#F3C892",
        border_color="#7B3F00",
        border_width=2,
        button_hover_color="#7B3F00",
        dropdown_hover_color="#7B3F00",
        dropdown_fg_color="#9E5D24",
        dropdown_text_color="#FFF3E3",
        text_color="#7B3F00",
        font=("Stack Sans Text", 14),
        justify="center",
        dropdown_font=("Stack Sans Text", 14),
    )
    Certificate.place(x=10, y=235)
    self.var_Certificate.set("Select Certificate")

    CTkLabel(
        master=details_frame,
        text="Platform",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=195, y=210)
    Platform = CTkComboBox(
        master=details_frame,
        values=[
            "Disney+",
            "ZEE 5",
            "VOOT",
            "Prime Video",
            "Netflix",
            "HBO Max",
            "Sony Liv",
            "Hulu",
            "Youtube",
            "Hotstar",
        ],
        state="disabled",
        height=30,
        width=170,
        variable=self.var_Platform,
        text_color_disabled="#7B3F00",
        button_color="#9E5D24",
        fg_color="#F3C892",
        border_color="#7B3F00",
        border_width=2,
        button_hover_color="#7B3F00",
        dropdown_hover_color="#7B3F00",
        dropdown_fg_color="#9E5D24",
        dropdown_text_color="#FFF3E3",
        text_color="#7B3F00",
        font=("Stack Sans Text", 14),
        justify="center",
        dropdown_font=("Stack Sans Text", 14),
    )
    Platform.place(x=190, y=235)
    self.var_Platform.set("Select Platform")

    CTkLabel(
        master=details_frame,
        text="Description",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=15, y=265)
    self.txt_Description = CTkTextbox(
        master=details_frame,
        border_width=2,
        fg_color="#F3C892",
        border_color="#7B3F00",
        font=("Stack Sans Text", 12),
        scrollbar_button_color="#7B3F00",
        scrollbar_button_hover_color="#9E5D24",
        corner_radius=10,
        width=350,
        height=190,
        text_color="#7B3F00",
    )
    self.txt_Description.place(x=10, y=290)

    CTkLabel(
        master=details_frame,
        text="Link",
        text_color="#7B3F00",
        font=("Google Sans Code Mono", 14, "bold"),
    ).place(x=15, y=480)
    Link = CTkEntry(
        master=details_frame,
        placeholder_text="Enter Link...",
        textvariable=self.var_Link,
        placeholder_text_color="#C19A6B",
        border_width=2,
        fg_color="#F3C892",
        state="disabled",
        border_color="#7B3F00",
        font=("Stack Sans Text", 13),
        corner_radius=10,
        width=350,
        height=30,
        text_color="#7B3F00",
    )
    Link.place(x=10, y=505)

    CTkButton(
        master=details_frame,
        text="STREAM NOW",
        command=lambda: StreamNow(self),
        font=("Dela Gothic One", 12),
        fg_color="#7B3F00",
        hover_color="#9E5D24",
        text_color="#FFF3E3",
        cursor="hand2",
        hover=True,
        height=30,
        width=100,
    ).place(x=125, y=545)

    filter_frame = CTkFrame(
        master=user_frame,
        fg_color="#E5AA70",
        bg_color="#F3C892",
        width=900,
        height=50,
        border_width=2,
        border_color="#7B3F00",
    )
    filter_frame.place(x=390, y=100)

    CTkLabel(
        master=filter_frame,
        text="Filter",
        text_color="#7B3F00",
        font=("Dela Gothic One", 30),
    ).place(x=50, y=2)
    CTkComboBox(
        master=filter_frame,
        values=["Title", "Genre", "Type", "Certificate", "Platform"],
        state="readonly",
        height=30,
        width=200,
        variable=self.var_SearchBy,
        button_color="#9E5D24",
        fg_color="#F3C892",
        border_color="#7B3F00",
        border_width=2,
        button_hover_color="#7B3F00",
        dropdown_hover_color="#7B3F00",
        dropdown_fg_color="#9E5D24",
        dropdown_text_color="#FFF3E3",
        text_color="#7B3F00",
        font=("Stack Sans Text", 15),
        justify="center",
        dropdown_font=("Stack Sans Text", 14),
    ).place(x=260, y=10)

    self.var_SearchBy.set("Select Category")

    self.SearchBox = CTkEntry(
        master=filter_frame,
        textvariable=self.var_SearchBox,
        height=30,
        width=200,
        placeholder_text="Enter Value...",
        text_color="#7B3F00",
        placeholder_text_color="#C19A6B",
        border_width=2,
        fg_color="#F3C892",
        border_color="#7B3F00",
        font=("Stack Sans Text", 15),
    )
    self.SearchBox.place(x=470, y=10)
    self.SearchBox.bind("<Return>", lambda event: SearchData(self))

    CTkButton(
        master=filter_frame,
        text="SEARCH",
        command=lambda: SearchData(self),
        font=("Dela Gothic One", 12),
        fg_color="#7B3F00",
        hover_color="#9E5D24",
        text_color="#FFF3E3",
        cursor="hand2",
        hover=True,
        height=30,
        width=100,
    ).place(x=680, y=10)

    CTkButton(
        master=filter_frame,
        text="SHOW ALL",
        command=lambda: ShowAll(self),
        font=("Dela Gothic One", 12),
        fg_color="#7B3F00",
        hover_color="#9E5D24",
        text_color="#FFF3E3",
        cursor="hand2",
        hover=True,
        height=30,
        width=100,
    ).place(x=790, y=10)

    table_frame = CTkFrame(
        master=user_frame,
        fg_color="#E5AA70",
        bg_color="#F3C892",
        width=880,
        height=500,
        border_width=2,
        border_color="#7B3F00",
    )
    table_frame.place(x=390, y=160)

    scrollable_table_frame = CTkScrollableFrame(
        master=table_frame,
        fg_color="#E5AA70",
        scrollbar_button_color="#7B3F00",
        scrollbar_button_hover_color="#9E5D24",
        width=870,
        height=507,
    )
    scrollable_table_frame.pack(fill="both", expand=True, padx=2, pady=2)

    self.Media_Table = CTkTable(
        master=scrollable_table_frame,
        column=7,
        values=ShowData(self),
        header_color="#9E5D24",
        text_color="#4A2711",
        bg_color="#E5AA70",
        colors=["#C68B59", "#D9A06F"],
        font=("Stack Sans Text", 13),
        command=lambda data: GetData(self, data),
    )

    self.Media_Table.pack(fill="both", expand=False)

    column_widths = [50, 250, 50, 60, 50, 50, 60]

    for col, w in enumerate(column_widths):
        self.Media_Table.edit_column(col, width=w)