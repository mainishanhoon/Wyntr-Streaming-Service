import tkinter, pymysql, webbrowser, time

from tkinter import *

from tkinter import ttk, messagebox

from PIL import ImageTk

class Wynter :
	def __init__(self, root) :
		self.root = root
		self.root.title("Wyntr Streaming Service")
		self.root.iconbitmap("Images/Icon.ico")
		self.root.geometry("1536x801")
		self.root.state("zoomed")
		self.Login_Interface()


#*:..。o○☆○o。..:*゜*:..。o○☆○o。LOGIN ..:*゜*:..。o○☆○o。..:*゜*:..。o○☆○o。..:*

	def Login_Interface(self):
		self.bg = ImageTk.PhotoImage(file = "Images/LogIn.png")
		bg = Label(self.root, image = self.bg).place(x = 0, y = 0, height = 801,width = 1536)

		self.Logo = ImageTk.PhotoImage(file = "Images/Logo.jpg")
		Logo = Label(self.root, image = self.Logo).place(x = 210, y = 180, height = 435, width = 435)

		Login_Frame = Frame(self.root, bg = "#F3C892")
		Login_Frame.place(x = 648, y = 180, width = 680, height = 435)

		Title = Label(Login_Frame, text = "Sign In", font = ("FZShuTi", 50, "bold"), bg = "#F3C892", fg = "#021E2F").place(x = 50, y = 20)

		Username = Label(Login_Frame, text = "Username", font = ("Product Sans", 20, "bold"), bg = "#F3C892", fg = "#630000").place(x = 50, y = 130)
		self.txt_Username = Entry (Login_Frame, font = ("Product Sans", 15), bg = "#FFEFD5")
		self.txt_Username.place(x = 50, y = 170, height = 35, width = 350)

		Password = Label(Login_Frame, text = "Password", font = ("Product Sans", 20, "bold"), bg = "#F3C892", fg = "#630000").place(x = 50, y = 230)
		self.txt_Password = Entry (Login_Frame, font = ("Product Sans", 15, "bold"), bg = "#FFEFD5", show = "*")
		self.txt_Password.place(x = 50, y = 270, height = 35, width = 350)

		btn_register = Button(Login_Frame, text = "LOGIN",font = ("20th Century Font", 30), bd = 5, bg = "#F99A05", cursor = 'hand2', relief = RIDGE, command = self.Login)
		btn_register.place(x = 425, y = 345, height = 50, width = 150)

		Title = Label(Login_Frame, text = "Don't Have an Account ?", font = ("FZShuTi", 15, 'bold'), bg = "#F3C892", fg = "#021E2F").place(x = 50, y = 340)
		btn_login = Button(self.root, text = "SIGN UP", font = ("20th Century Font", 20), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Registration_Interface)
		btn_login.place(x = 770, y = 550, height = 40, width = 110)

		self.root.bind('<Return>',lambda event:self.Login())
	
	def Login(self):
		if self.txt_Username.get() == "" and self.txt_Password.get() == "" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ ᴀɴᴅ ᴘᴀꜱꜱᴡᴏʀᴅ", icon = "warning", parent = self.root)

		elif self.txt_Username.get() == "" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ", icon = "warning", parent = self.root)

		elif self.txt_Password.get() == "" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴘᴀꜱꜱᴡᴏʀᴅ", icon = "warning", parent = self.root)

		else:
			mycon = pymysql.connect(host="localhost",user="root",password="1234",database="Details")
			cursor = mycon.cursor()
			cursor.execute("SELECT * FROM Accounts WHERE Username = %s AND Password = %s", (self.txt_Username.get(), self.txt_Password.get()))
			row = cursor.fetchone()
			if self.txt_Username.get() == "mainishanhoon" and self.txt_Password.get() == "password" :
				self.Management_Interface()
			elif row == None :
				messagebox.showerror("Wyntr Streaming Service", "ɪɴᴠᴀʟɪᴅ ᴜꜱᴇʀɴᴀᴍᴇ / ᴘᴀꜱꜱᴡᴏʀᴅ", icon = "warning", parent = self.root)
				self.Login_Clear()
			else :
				messagebox.showinfo("Wyntr Streaming Service", "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ Wyntr Streaming Service", parent = self.root)
				self.Media_Interface()
			mycon.close()
			
	def Login_Clear(self) :
		self.txt_Username.delete("0",END)
		self.txt_Password.delete("0",END)

#*:..。o○☆○o。..:*゜*:..。o○☆○o。REGISTRATION ..:*゜*:..。o○☆○o。..:*゜*:..。o○☆○o。..:*

	def Registration_Interface(self) :
		self.bg = ImageTk.PhotoImage(file = "Images/Registration.jpg")
		bg = Label(self.root, image = self.bg, bg = "#FAA460").place(x = 0, y = 0, height = 801,width = 1536)

		self.Logo = ImageTk.PhotoImage(file = "Images/Logo.jpg")
		Left = Label(self.root, image = self.Logo).place(x = 200, y = 180, height = 435, width = 435)

		Registration_Frame=Frame(self.root, bg = "#F3C892")
		Registration_Frame.place(x = 638, y = 180, width = 700, height = 435)

		title = Label(Registration_Frame, text = "Sign Up", font = ("FZShuTi", 50, "bold"), bg = "#F3C892", fg = "#021E2F").place(x = 50, y = 10)

		FirstName = Label(Registration_Frame, text = "First Name", font = ("Product Sans", 15, "bold"), bg = "#F3C892", fg = "#630000").place(x = 70, y = 120)
		self.txt_FirstName = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "#FFEFD5")
		self.txt_FirstName.place(x = 70, y = 150, width = 250)

		LastName = Label(Registration_Frame, text = "Last Name", font = ("Product Sans", 15, "bold"), bg = "#F3C892", fg = "#630000").place(x = 380, y = 120)
		self.txt_LastName = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "#FFEFD5")
		self.txt_LastName.place(x = 380, y = 150, width = 250)

		Username = Label(Registration_Frame, text = "Username", font = ("Product Sans", 15, "bold"), bg = "#F3C892", fg = "#630000").place(x = 70, y = 190)
		self.txt_Username = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "#FFEFD5")
		self.txt_Username.place(x = 70, y = 220, width = 250)

		Email = Label(Registration_Frame, text = "E-Mail", font = ("Product Sans", 15, "bold"), bg = "#F3C892", fg = "#630000").place(x = 380, y = 190)
		self.txt_Email = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "#FFEFD5")
		self.txt_Email.place(x = 380, y = 220, width = 250)

		Password = Label(Registration_Frame, text = "Password", font = ("Product Sans", 15, "bold"), bg = "#F3C892", fg = "#630000").place(x = 70, y = 270)
		self.txt_Password = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "#FFEFD5", show = "*")
		self.txt_Password.place(x = 70, y = 300, width = 250)

		ConfirmPassword = Label(Registration_Frame, text = "Confirm Password", font = ("Product Sans", 15, "bold"), bg = "#F3C892", fg = "#630000").place(x = 380, y = 270)
		self.txt_ConfirmPassword = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "#FFEFD5", show = "*")
		self.txt_ConfirmPassword.place(x = 380, y = 300, width = 250)

		btn_register = Button(Registration_Frame, text = "REGISTER",font = ("20th Century Font", 30), bd = 5, bg = "#F99A05", cursor = 'hand2', relief = RIDGE, command = self.Registration)
		btn_register.place(x = 410, y = 360, height = 50, width = 190)

		Title = Label(Registration_Frame, text = "Already Have An Account ?", font = ("FZShuTi", 15, 'bold'), bg = "#F3C892", fg = "#021E2F").place(x = 55, y = 350)
		btn_login = Button(self.root, text = "SIGN IN", font = ("20th Century Font", 20), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Login_Interface)
		btn_login.place(x = 775, y = 560, height = 40, width = 110)

		self.root.bind('<Return>',lambda event:self.Registration())

	def Registration(self) :
		if self.txt_FirstName.get() == "" or self.txt_Email.get() == "" or self.txt_FirstName.get() == "" or self.txt_Username.get() == "" or self.txt_Password.get() == "" or self.txt_ConfirmPassword.get() == "":
			messagebox.showerror("Wyntr Streaming Service", "ᴀʟʟ ꜰɪᴇʟᴅꜱ ᴀʀᴇ ʀᴇ🇶ᴜɪʀᴇᴅ", icon = "warning", parent = self.root)

		elif self.txt_Password.get() != self.txt_ConfirmPassword.get() :
			messagebox.showerror("Wyntr Streaming Service", "ᴄᴏɴꜰɪʀᴍ ᴘᴀꜱꜱᴡᴏʀᴅ ɪꜱ ᴅɪꜰꜰᴇʀᴇɴᴛ", icon = "warning",  parent = self.root)

		else :
			mycon = pymysql.connect(host="localhost",user="root",password="1234",database="Details")
			cursor = mycon.cursor()
			cursor.execute("SELECT * FROM Accounts WHERE Username = %s", self.txt_Username.get())
			Username = cursor.fetchone()
			cursor.execute("SELECT * FROM Accounts WHERE Email = %s", self.txt_Email.get())
			Email = cursor.fetchone()
			if Username != None :
				messagebox.showerror("Wyntr Streaming Service", "ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ ᴇxɪꜱᴛꜱ, ᴛʀʏ ᴏᴛʜᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ", icon = "warning", parent = self.root)
			elif Email != None :
				messagebox.showerror("Wyntr Streaming Service", "ᴇᴍᴀɪʟ ᴀʟʀᴇᴀᴅʏ ᴇxɪꜱᴛꜱ, ᴛʀʏ ᴏᴛʜᴇʀ ᴇᴍᴀɪʟ", icon = "warning", parent = self.root)
			else :
				cursor.execute("INSERT INTO Accounts (First_Name, Last_Name, Username, Email, Password) VALUES (%s,%s,%s,%s,%s)",
				                                 (self.txt_FirstName.get(),
				                                 self.txt_LastName.get(),
				                                 self.txt_Username.get(),
				                                 self.txt_Email.get(),
				                                 self.txt_Password.get()
				                                    ))
				messagebox.showinfo("Wyntr Streaming Service", "ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ ʙᴇᴇɴ ʀᴇɢɪꜱᴛᴇʀᴇᴅ")
				self.Media_Interface()         
			mycon.commit()
			mycon.close()	

	def Registration_Clear(self) :
		self.txt_FirstName.delete(0,END)
		self.txt_LastName.delete(0,END)
		self.txt_Username.delete(0,END)
		self.txt_Email.delete(0,END)
		self.txt_Password.delete(0,END)
		self.txt_ConfirmPassword.delete(0,END)

	def Management_Interface(self) :    
		Title_Frame = Frame(self.root, bd = 0, bg = "#FFE6BC")
		Title_Frame.place(x = 0, y= 0, width = 1535.5, height = 95)

		Title = Label(Title_Frame, text = "𝕎𝕪𝕟𝕥𝕣 𝕊𝕥𝕣𝕖𝕒𝕞𝕚𝕟𝕘 𝕊𝕖𝕣𝕧𝕚𝕔𝕖", bd = 8, relief = RIDGE, font = ("Product Sans", 50, "bold"), bg = "#ECB365", fg = "#630000")
		Title.place(x =0, y = 0, height = 90, width = 1535.5)

		Logo_Frame = Frame(self.root, bd = 0, bg = "#ffffff")
		Logo_Frame.place(x = 280, y = 10, width = 80, height = 70)
		self.Logo = ImageTk.PhotoImage(file = "Images/Logo.png")
		Logo = Label(Logo_Frame, image = self.Logo).place(x = 0, y = 0, height = 70, width = 80)

		self.Addbtn = PhotoImage(file = "Images/Sign_Out.png")
		btn = Button(Title_Frame, image = self.Addbtn, bd = 0, cursor = "hand2", relief = FLAT, command = self.SignOut)
		btn.place(x = 1484, y = 11, width = 40, height = 40)

		#Developers = Label(Title_Frame, text = "Developers : Nishan, Rishu, Yogesh",bd = 0, font = ("Bafora Demo", 20, 'bold'), bg = "#ECB365", fg = "#800000")
		#Developers.place(x =1178, y = 52, height = 30, width = 350)

#*:..。o○☆○o。..:*゜*:..。o○☆○o。ALL VARIABLES ..:*゜*:..。o○☆○o。..:*゜*:..。o○☆○o。..:*

		self.ID_var = StringVar()
		self.Title_var = StringVar()
		self.Genre_var = StringVar()
		self.Type_var = StringVar()
		self.IMDb_var = StringVar()
		self.Certificate_var = StringVar()
		self.Streaming_Platform_var = StringVar()
		self.Description_var = StringVar()
		self.Link_var = StringVar()
		self.SearchBy_var = StringVar()
		self.SearchBox_var = StringVar()	

#════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆MANAGE FRAME⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════


		Manage_Frame = Frame(self.root, bd = 5, relief = GROOVE, bg = "#F3C892")
		Manage_Frame.place(x = 2, y= 93, width = 613, height = 700)

		Details_Title = Label(Manage_Frame, text = "Manage  Details", font = ("FZShuTi",40, "bold"), bg = "#F3C892", fg = "#630000")
		Details_Title.place(x = 45, y = 0, height = 55, width = 500)

		Label_ID = Label(Manage_Frame, text = "ID", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 70)
		txt_ID = Entry(Manage_Frame, textvariable = self.ID_var, font = ("Product Sans",15), justify = CENTER, bg = "#FFEFD5")
		txt_ID.place(x = 35, y = 105, width = 250)
		
		Label_Type = Label(Manage_Frame, text = "Type", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 315, y = 70)
		cmb_Type = ttk.Combobox(Manage_Frame, font = ("Product Sans",14), textvariable = self.Type_var, justify = CENTER, state = "readonly")
		cmb_Type['values'] = ("Movie", "Series", "Documentary", "Anime")
		cmb_Type.place(x = 315, y = 103, width = 250)
		self.Type_var.set("Select Type")

		Label_Title = Label(Manage_Frame, text = "Title", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 140)
		txt_Title = Entry(Manage_Frame, textvariable = self.Title_var, font = ("Product Sans",15), justify = CENTER, bg = "#FFEFD5")
		txt_Title.place(x = 35, y = 175, width = 530)

		Label_Genre = Label(Manage_Frame, text = "Genre", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 210)
		cmb_Genre = ttk.Combobox(Manage_Frame, textvariable = self.Genre_var, font = ("Product Sans",15), justify = CENTER, state = "readonly")
		cmb_Genre['values'] = ("Action", "Drama", "Thriller", "Horror", "Comedy", "Romance", "Science Fiction", "Fantasy", "Adventure", "Fiction")
		cmb_Genre.place(x = 35, y = 243, width = 250)
		self.Genre_var.set("Select Genre")

		Label_IMDb = Label(Manage_Frame, text = "IMDb", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 315, y = 210)
		txt_IMDb = Entry(Manage_Frame, textvariable = self.IMDb_var, font = ("Product Sans",15), justify = CENTER, bg = "#FFEFD5")
		txt_IMDb.place(x = 315, y = 245, width = 250)

		Label_Certificate = Label(Manage_Frame, text = "Certificate", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 280)
		cmb_Certificate = ttk.Combobox(Manage_Frame, textvariable = self.Certificate_var, font = ("Product Sans",14), justify = CENTER, state = "readonly")
		cmb_Certificate['values'] = ("U (Unrestricted)", "U/A (Parental Guidance)", "A (Adults)", "S (Special Class)")
		cmb_Certificate.place(x = 35, y = 313, width = 250)
		self.Certificate_var.set("Select Certificate")

		Label_Streaming_Platform = Label(Manage_Frame, text = "Streaming Platform", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 315, y = 280)
		cmb_Streaming_Platform = ttk.Combobox(Manage_Frame, textvariable = self.Streaming_Platform_var, font = ("Product Sans",14), justify = CENTER, state = "readonly")
		cmb_Streaming_Platform['values'] = ("Disney+", "ZEE 5", "VOOT", "Prime Video", "Netflix", "HBO Max", "Sony Liv", "Hulu", "Youtube", "Hotstar")
		cmb_Streaming_Platform.place(x = 315, y = 313, width = 250)
		self.Streaming_Platform_var.set("Select Streaming Platform")

		Label_Description = Label(Manage_Frame, text = "Description", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 350)
		self.txt_Description = Text(Manage_Frame, font = ("Cambria",11), bg = "#FFEFD5")
		self.txt_Description.place(x = 35, y = 382, width = 530, height = 185)

		Label_Link = Label(Manage_Frame, text = "Link", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 570)
		txt_Link = Entry(Manage_Frame, textvariable = self.Link_var, font = ("Product Sans",15), justify = CENTER, bg = "#FFEFD5")
		txt_Link.place(x = 35, y = 600, width = 530, height = 30)	

#*:..。o○☆○o。..:*゜*:..。o○☆○o。BUTTON FRAME..:*゜*:..。o○☆○o。..:*゜*:..。o○☆○o。..:*

		Button_Frame = Frame(self.root, bd = 0, bg = "#F3C892")
		Button_Frame.place(x = 20, y= 725, width = 580, height = 60)

		Addbtn = Button(Button_Frame, text = "Add", width = 10, font = ("Gagalin", 20), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Add_Details)
		Addbtn.place(x = 0, y = 15, width = 100, height = 40)

		Addbtn = Button(Button_Frame, text = "Update", width = 10, font = ("Gagalin", 18), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Update_Data)
		Addbtn.place(x = 111, y = 15, width = 100, height = 40)
		
		Addbtn = Button(Button_Frame, text = "Delete", width = 10, font = ("Gagalin", 18), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Delete_Data)
		Addbtn.place(x = 222, y = 15, width = 100, height = 40)
		
		Addbtn = Button(Button_Frame, text = "Clear", width = 10, font = ("Gagalin", 18), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Clear)
		Addbtn.place(x = 333, y = 15, width = 100, height = 40)

		Addbtn = Button(Button_Frame, text = "Stream Now", width = 10, font = ("Gagalin", 16), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Stream_Now)
		Addbtn.place(x = 447, y = 15, width = 130, height = 40)

#════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆DETAILS FRAME⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════

		Details_Frame = Frame(self.root, bd = 5, relief = GROOVE, bg = "#F3C892")
		Details_Frame.place(x = 615, y= 93, width = 920, height = 700)

		Extract_Frame = Frame(self.root, bd = 0, bg = "#F3C892")
		Extract_Frame.place(x = 630, y= 100, width = 890, height = 60)

		Search_Title = Label(Extract_Frame, text = "Details", font = ("FZShuTi",50, "bold"), bg = "#F3C892", fg = "#630000")
		Search_Title.place(x = 0, y = 0, height = 55, width = 220)

		Label_SearchBy = Label(Extract_Frame, font = ("Product Sans",15, "bold"), bg = "#F3C892", fg = "#9B0000").place(x = 310, y = 110)
		SearchBy = ttk.Combobox(Extract_Frame, textvariable = self.SearchBy_var, font = ("Product Sans",14), justify = CENTER, state = 'readonly')
		SearchBy['values'] = ("Title", "Genre", "Type", "Certificate", "Streaming_Platform")
		SearchBy.place(x = 238, y = 15, width = 195, height = 35)
		self.SearchBy_var.set("Select Category")

		self.txt_SearchBox = Entry(Extract_Frame, width = 10, bg = "#FFEFD5", textvariable = self.SearchBox_var, font = ("Product Sans", 15), relief = GROOVE)
		self.txt_SearchBox.place(x = 455, y = 15, width = 160, height = 35)

		Addbtn = Button(Extract_Frame, text = "Search", width = 10, font = ("Gagalin", 18), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Search_Data)
		Addbtn.place(x = 640, y = 12, width = 100, height = 40)

		Addbtn = Button(Extract_Frame, text = "Show All", width = 10, font = ("Gagalin", 18), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.ShowAll_Data)
		Addbtn.place(x = 760, y = 12, width = 120, height = 40)

#════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆TABLE FRAME⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════
		
		Table_Frame = Frame(Details_Frame, bd = 0, bg = "#95D1CC" )
		Table_Frame.place(x = 0, y = 70, width = 910, height = 620)
		
		Style = ttk.Style(self.root)
		Style.theme_use("winnative")
		Style.configure(".", font=('Product Sans', 10), bg = "#FFDEAD")
		Style.configure("Media_Table.Heading", fg = "#630000", font = ('Product Sans', 20))
		scroll_y = Scrollbar(Table_Frame, orient = VERTICAL)
		self.Media_Table = ttk.Treeview(Table_Frame, columns = ("ID", "Title", "Genre", "Type", "IMDb", "Certificate", "Streaming_Platform"), yscrollcommand = scroll_y.set)
		scroll_y.pack(side = RIGHT, fill = Y)
		scroll_y.config(command = self.Media_Table.yview)
		self.Media_Table.heading("ID", text = "ID", anchor=tkinter.CENTER)
		self.Media_Table.heading("Title", text = "Title", anchor=tkinter.CENTER)
		self.Media_Table.heading("Genre", text = "Genre", anchor=tkinter.CENTER)
		self.Media_Table.heading("Type", text = "Type", anchor=tkinter.CENTER)
		self.Media_Table.heading("IMDb", text = "IMDb", anchor=tkinter.CENTER)
		self.Media_Table.heading("Certificate", text = "Certificate", anchor=tkinter.CENTER)
		self.Media_Table.heading("Streaming_Platform", text = "Streaming On", anchor=tkinter.CENTER)

		self.Media_Table['show'] = "headings"

		self.Media_Table.column("ID", width = 70, anchor=tkinter.CENTER)
		self.Media_Table.column("Title", width = 290, anchor=tkinter.CENTER)
		self.Media_Table.column("Genre", width = 110, anchor=tkinter.CENTER)
		self.Media_Table.column("Type", width = 100, anchor=tkinter.CENTER)
		self.Media_Table.column("IMDb", width = 60, anchor=tkinter.CENTER)
		self.Media_Table.column("Certificate", width = 160, anchor=tkinter.CENTER)
		self.Media_Table.column("Streaming_Platform", width = 100, anchor=tkinter.CENTER)
		self.Media_Table.pack(fill = BOTH, expand = 1)
		self.Media_Table.bind("<ButtonRelease-1>", self.Get_Details)
		self.root.bind('<Return>',lambda event:self.Search_Data())
		self.ShowAll_Data()

#════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆FUNCTION⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════

	def Add_Details(self) :
		if self.ID_var.get() == "" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ ɪᴅ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)		
		elif self.Type_var.get() == "Select Type" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ ᴛʏᴘᴇ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)
		elif self.Title_var.get() == "" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ ᴛɪᴛʟᴇ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)
		elif self.Genre_var.get() == "Select Genre" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ ɢᴇɴʀᴇ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)
		elif self.IMDb_var.get() == "" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ ɪᴍᴅʙ ʀᴀɪᴛɪɴɢ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)
		elif self.Certificate_var.get() == "Select Certificate" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ ᴄᴇʀᴛɪꜰɪᴄᴀᴛᴇ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)
		elif self.Streaming_Platform_var.get() == "Select Streaming Platform" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ 🇸ᴛʀᴇᴀᴍɪɴɢ ᴘʟᴀᴛ🇫ᴏʀᴍ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)
		elif self.txt_Description.get('1.0' , END) == "" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ ᴅᴇ🇸ᴄʀɪᴘᴛɪᴏɴ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)
		elif self.Link_var.get() == "" :
			messagebox.showerror("Wyntr Streaming Service", "ᴇɴᴛᴇʀ ᴛʜᴇ ʟɪɴᴋ ᴏ🇫 ᴍᴇᴅɪᴀ", icon = "warning", parent = self.root)	
		else :	
			mycon = pymysql.connect(host = "localhost", user = "root", password = "1234", database = "details")
			cursor = mycon.cursor()	
			cursor.execute("SELECT * FROM Media WHERE ID = %s", self.ID_var.get())
			Details = cursor.fetchone()
			if Details != None :
				messagebox.showerror("Wyntr Streaming Service", "ᴍᴇᴅɪᴀ ᴡɪᴛʜ ᴛʜɪꜱ ɪᴅ ᴀʟʀᴇᴀᴅʏ ᴇxɪ🇸ᴛ", icon = "warning", parent = self.root)
			else :
				cursor.execute("INSERT INTO Media VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(
					self.ID_var.get(),
					self.Title_var.get(),
					self.Genre_var.get(),
					self.Type_var.get(),
					self.IMDb_var.get(),
					self.Certificate_var.get(),
					self.Streaming_Platform_var.get(),
					self.txt_Description.get('1.0', END),
					self.Link_var.get()
					))
				mycon.commit()
				messagebox.showinfo("Wyntr Streaming Service", "ʏᴏᴜʀ ᴍᴇᴅɪᴀ ɪ🇸 ɴᴏᴡ 🇸ᴛʀᴇᴀᴍɪɴɢ", parent = self.root)
				self.ShowAll_Data()
				self.Clear()
				mycon.close()
 
	def ShowAll_Data(self) :
		mycon = pymysql.connect(host = "localhost", user = "root", password = "1234", database = "details")
		cursor = mycon.cursor()
		cursor.execute("SELECT * FROM Media")
		rows = cursor.fetchall()
		if len(rows) != 0 :
			self.Media_Table.delete(*self.Media_Table.get_children())
			for row in rows :
				self.Media_Table.insert('', END, values = row)
			mycon.commit()
		mycon.close()

	def Clear(self) :
		self.ID_var.set(""),
		self.Title_var.set(""),
		self.Genre_var.set("Select Genre"),
		self.Type_var.set("Select Type"),
		self.IMDb_var.set(""),
		self.Certificate_var.set("Select Certificate"),
		self.Streaming_Platform_var.set("Select Streaming Platform"),
		self.txt_Description.delete("1.0", END),
		self.Link_var.set(""),
		self.SearchBy_var.set("Select Category"),
		self.txt_SearchBox.delete("0", END)

	def Get_Details(self, event) :
		Cursor_Row = self.Media_Table.focus()
		Contents = self.Media_Table.item(Cursor_Row)
		row = Contents['values']
		self.ID_var.set(row[0]),
		self.Title_var.set(row[1]),
		self.Genre_var.set(row[2]),
		self.Type_var.set(row[3]),
		self.IMDb_var.set(row[4]),
		self.Certificate_var.set(row[5]),
		self.Streaming_Platform_var.set(row[6]),
		self.txt_Description.delete("1.0", END)
		self.txt_Description.insert(END, row[7])
		self.Link_var.set(row[8])

	def Update_Data(self) :
		if self.ID_var.get() == "" :
		 	messagebox.showinfo("Wyntr Streaming Service", "ꜱᴇʟᴇᴄᴛ ᴍᴇᴅɪᴀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ᴜᴘᴅᴀᴛᴇ", icon = "warning", parent = self.root)
		else :		
			mycon = pymysql.connect(host = "localhost", user = "root", password = "1234", database = "details")
			cursor = mycon.cursor()
			cursor.execute("UPDATE Media SET Title = %s, Genre = %s, Type = %s, IMDb = %s, Certificate = %s, Streaming_Platform = %s, Description = %s, Link = %s WHERE ID = %s", (
				self.Title_var.get(),
				self.Genre_var.get(),
				self.Type_var.get(),
				self.IMDb_var.get(),
				self.Certificate_var.get(),
				self.Streaming_Platform_var.get(),
				self.txt_Description.get('1.0', END),
				self.Link_var.get(),
				self.ID_var.get()
				))
			mycon.commit()
			messagebox.showinfo("Wyntr Streaming Service", "ᴍᴇᴅɪᴀ ᴅᴇᴛᴀɪʟꜱ ʜᴀꜱ ʙᴇᴇɴ ᴜᴘᴅᴀᴛᴇᴅ", parent = self.root)
			self.ShowAll_Data()
			self.Clear()
			mycon.close()

	def Delete_Data(self) :
		if self.ID_var.get() == "" :
		 	messagebox.showinfo("Wyntr Streaming Service", "ꜱᴇʟᴇᴄᴛ ᴍᴇᴅɪᴀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ᴅᴇʟᴇᴛᴇ", icon = "warning", parent = self.root)
		else :
			mycon = pymysql.connect(host = "localhost", user = "root", password = "1234", database = "details")
			cursor = mycon.cursor()
			cursor.execute("DELETE FROM Media WHERE ID = %s", self.ID_var.get())
			mycon.commit()
			messagebox.showinfo("Wyntr Streaming Service", "ꜱᴇʟᴇᴄᴛᴇᴅ ᴍᴇᴅɪᴀ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ", parent = self.root)
			self.ShowAll_Data()
			self.Clear()
			mycon.close()
			
	def Stream_Now(self) :
		if self.ID_var.get() == "" :
		 	messagebox.showinfo("Wyntr Streaming Service", "ꜱᴇʟᴇᴄᴛ ᴍᴇᴅɪᴀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ꜱᴛʀᴇᴀᴍ", icon = "warning", parent = self.root)	
		else :
			webbrowser.open(str(self.Link_var.get()), new=2)

	def Search_Data(self) :
		if 	self.SearchBy_var.get() == "Select Category" :
			messagebox.showinfo("Wyntr Streaming Service", "ᴏɴ ᴡʜᴀᴛ ʙᴀꜱɪꜱ ʏᴏᴜ ᴡᴀɴɴᴀ ᴡᴀᴛᴄʜ", icon = "question", parent = self.root)
		elif 	self.txt_SearchBox.get() == "" :
			messagebox.showinfo("Wyntr Streaming Service", "ꜱᴇᴀʀᴄʜ ʙᴏx ɪꜱ ᴇᴍᴘᴛʏ", icon = "warning", parent = self.root)	
		elif 	self.SearchBy_var.get() == "Select Category" and self.txt_SearchBox.get() == "" :
			messagebox.showinfo("Wyntr Streaming Service", "ᴏɴ ᴡʜᴀᴛ ʙᴀꜱɪꜱ ʏᴏᴜ ᴡᴀɴɴᴀ ᴡᴀᴛᴄʜ", icon = "question", parent = self.root)
		else :
			mycon = pymysql.connect(host = "localhost", user = "root", password = "1234", database = "details")
			cursor = mycon.cursor()
			cursor.execute("SELECT * FROM Media WHERE " +str(self.SearchBy_var.get())+"  LIKE '%" +str(self.txt_SearchBox.get())+"%' ") 
			Details = cursor.fetchall()
			if len(Details) != 0 :
				self.Media_Table.delete(*self.Media_Table.get_children())
				for Data in Details :
					self.Media_Table.insert("", END, values = Data)
			else :
				No_Data = Label(self.root, text = "Oops! No Medias Were Found",font=("FZShuTi", 45, 'bold'), fg = "#021E2F", bg = '#FFEFD5')
				No_Data.place(x = 622, y = 189, height = 597, width = 890)
				No_Data.after(3000, No_Data.destroy)
				self.Clear()
			mycon.commit()
			mycon.close()

	def SignOut(self) :
		MessageBox = messagebox.askyesno("Wyntr Streaming Service", "Are You Sure You Wanna Sign Out ?")
		if MessageBox == True :
			self.Login_Interface()

	def Media_Interface(self) :   
		Title_Frame = Frame(self.root, bd = 0, bg = "#FFE6BC")
		Title_Frame.place(x = 0, y= 0, width = 1535.5, height = 95)

		Title = Label(Title_Frame, text = "Wyntr Streaming Service", bd = 8, relief = RIDGE, font = ("Product Sans", 50, "bold"), bg = "#ECB365", fg = "#630000")
		Title.place(x =0, y = 0, height = 90, width = 1535.5)

		Logo_Frame = Frame(self.root, bd = 0, bg = "#ffffff")
		Logo_Frame.place(x = 280, y = 10, width = 80, height = 70)
		self.Logo = ImageTk.PhotoImage(file = "Images/Logo.png")
		Logo = Label(Logo_Frame, image = self.Logo).place(x = 0, y = 0, height = 70, width = 80)

		self.Addbtn = PhotoImage(file = "Images/Sign_Out.png")
		btn = Button(Title_Frame, image = self.Addbtn, bd = 0, cursor = "hand2", relief = FLAT, command = self.SignOut)
		btn.place(x = 1484, y = 11, width = 40, height = 40)

		#Developers = Label(Title_Frame, text = "Developers : Nishan, Rishu, Yogesh",bd = 0, font = ("Bafora Demo", 20, 'bold'), bg = "#ECB365", fg = "#800000")
		#Developers.place(x =1178, y = 52, height = 30, width = 350)

#*:..。o○☆○o。..:*゜*:..。o○☆○o。ALL VARIABLES ..:*゜*:..。o○☆○o。..:*゜*:..。o○☆○o。..:*

		self.ID_var = StringVar()
		self.Title_var = StringVar()
		self.Genre_var = StringVar()
		self.Type_var = StringVar()
		self.IMDb_var = StringVar()
		self.Certificate_var = StringVar()
		self.Streaming_Platform_var = StringVar()
		self.Description_var = StringVar()
		self.Link_var = StringVar()
		self.SearchBy_var = StringVar()
		self.SearchBox_var = StringVar()	

#════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆MANAGE FRAME⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════


		Manage_Frame = Frame(self.root, bd = 5, relief = GROOVE, bg = "#F3C892")
		Manage_Frame.place(x = 2, y= 93, width = 613, height = 700)

		Details_Title = Label(Manage_Frame, text = "Media Details", font = ("FZShuTi",50, "bold"), bg = "#F3C892", fg = "#630000")
		Details_Title.place(x = 45, y = 0, height = 55, width = 500)

		Label_ID = Label(Manage_Frame, text = "ID", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 70)
		txt_ID = Entry(Manage_Frame, textvariable = self.ID_var, font = ("Product Sans",15), state = DISABLED, justify = CENTER, bg = "#FFEFD5")
		txt_ID.place(x = 35, y = 105, width = 250)
		
		Label_Type = Label(Manage_Frame, text = "Type", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 315, y = 70)
		txt_Type = Entry(Manage_Frame, textvariable = self.Type_var, font = ("Product Sans",15), state = DISABLED, justify = CENTER, bg = "#FFEFD5")
		txt_Type.place(x = 315, y = 105, width = 250)

		Label_Title = Label(Manage_Frame, text = "Title", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 140)
		txt_Title = Entry(Manage_Frame, textvariable = self.Title_var, font = ("Product Sans",15), state = DISABLED, justify = CENTER, bg = "#FFEFD5")
		txt_Title.place(x = 35, y = 175, width = 530)

		Label_Genre = Label(Manage_Frame, text = "Genre", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 210)
		txt_Genre = Entry(Manage_Frame, textvariable = self.Genre_var, font = ("Product Sans",15), state = DISABLED, justify = CENTER, bg = "#FFEFD5")
		txt_Genre.place(x = 35, y = 245, width = 250)

		Label_IMDb = Label(Manage_Frame, text = "IMDb", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 315, y = 210)
		txt_IMDb = Entry(Manage_Frame, textvariable = self.IMDb_var, font = ("Product Sans",15), state = DISABLED, justify = CENTER, bg = "#FFEFD5")
		txt_IMDb.place(x = 315, y = 245, width = 250)

		Label_Certificate = Label(Manage_Frame, text = "Cerificate", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 280)
		txt_Certificate = Entry(Manage_Frame, textvariable = self.Certificate_var, font = ("Product Sans",15), state = DISABLED, justify = CENTER, bg = "#FFEFD5")
		txt_Certificate.place(x = 35, y = 313, width = 250)

		Label_Streaming_Platform = Label(Manage_Frame, text = "Streaming Platform", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 315, y = 280)
		txt_Streaming_Platform = Entry(Manage_Frame, textvariable = self.Streaming_Platform_var, font = ("Product Sans",15), state = DISABLED, justify = CENTER, bg = "#FFEFD5")
		txt_Streaming_Platform.place(x = 315, y = 315, width = 250)

		Label_Description = Label(Manage_Frame, text = "Description", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 350)
		self.txt_Description = Text(Manage_Frame, font = ("Cambria",11), bg = "#FFEFD5")
		self.txt_Description.place(x = 35, y = 382, width = 530, height = 185)

		Label_Link = Label(Manage_Frame, text = "Link", font = ("Product Sans",17, "bold"), bg = "#F3C892", fg = "#800000").place(x = 35, y = 570)
		txt_Link = Entry(Manage_Frame, textvariable = self.Link_var, font = ("Product Sans",15), state = DISABLED, justify = CENTER, bg = "#FFEFD5")
		txt_Link.place(x = 35, y = 600, width = 530, height = 30)	

#*:..。o○☆○o。..:*゜*:..。o○☆○o。BUTTON FRAME..:*゜*:..。o○☆○o。..:*゜*:..。o○☆○o。..:*

		Button_Frame = Frame(self.root, bd = 0, bg = "#F3C892")
		Button_Frame.place(x = 20, y= 725, width = 580, height = 60)

		Addbtn = Button(Button_Frame, text = "Stream Now", width = 10, font = ("Gagalin", 16), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Stream_Now)
		Addbtn.place(x = 230, y = 10, width = 130, height = 40)

#════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆DETAILS FRAME⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════

		Details_Frame = Frame(self.root, bd = 5, relief = GROOVE, bg = "#F3C892")
		Details_Frame.place(x = 615, y= 93, width = 920, height = 700)

		Extract_Frame = Frame(self.root, bd = 0, bg = "#F3C892")
		Extract_Frame.place(x = 630, y= 100, width = 890, height = 60)

		Filter_Title = Label(Extract_Frame, text = "Filter", font = ("FZShuTi",50, "bold"), bg = "#F3C892", fg = "#630000")
		Filter_Title.place(x = 0, y = 0, height = 55, width = 220)

		Label_SearchBy = Label(Extract_Frame, font = ("Product Sans",15, "bold"), bg = "#F3C892", fg = "#9B0000").place(x = 310, y = 110)
		SearchBy = ttk.Combobox(Extract_Frame, textvariable = self.SearchBy_var, font = ("Product Sans",14), justify = CENTER, state = 'readonly')
		SearchBy['values'] = ("Title", "Genre", "Type", "Certificate", "Streaming_Platform")
		SearchBy.place(x = 238, y = 15, width = 195, height = 35)
		self.SearchBy_var.set("Select Category")

		self.txt_SearchBox = Entry(Extract_Frame, width = 10, bg = "#FFEFD5", textvariable = self.SearchBox_var, font = ("Product Sans", 15), relief = GROOVE)
		self.txt_SearchBox.place(x = 455, y = 15, width = 160, height = 35)

		Addbtn = Button(Extract_Frame, text = "Search", width = 10, font = ("Gagalin", 18), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Search_Data)
		Addbtn.place(x = 640, y = 12, width = 100, height = 40)

		Addbtn = Button(Extract_Frame, text = "Show All", width = 10, font = ("Gagalin", 18), bg = "#F99A05", bd = 5, relief = RIDGE, cursor = "hand2", command = self.ShowAll_Data)
		Addbtn.place(x = 760, y = 12, width = 120, height = 40)

#════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆TABLE FRAME⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════
		
		Table_Frame = Frame(Details_Frame, bd = 0, bg = "#95D1CC" )
		Table_Frame.place(x = 0, y = 70, width = 910, height = 620)
		
		Style = ttk.Style(self.root)
		Style.theme_use("winnative")
		Style.configure(".", font=('Product Sans', 10), bg = "#FFDEAD")
		Style.configure("Media_Table.Heading", fg = "#630000", font = ('Product Sans', 20))
		scroll_y = Scrollbar(Table_Frame, orient = VERTICAL)
		self.Media_Table = ttk.Treeview(Table_Frame, columns = ("ID", "Title", "Genre", "Type", "IMDb", "Certificate", "Streaming_Platform"), yscrollcommand = scroll_y.set)
		scroll_y.pack(side = RIGHT, fill = Y)
		scroll_y.config(command = self.Media_Table.yview)
		self.Media_Table.heading("ID", text = "ID", anchor=tkinter.CENTER)
		self.Media_Table.heading("Title", text = "Title", anchor=tkinter.CENTER)
		self.Media_Table.heading("Genre", text = "Genre", anchor=tkinter.CENTER)
		self.Media_Table.heading("Type", text = "Type", anchor=tkinter.CENTER)
		self.Media_Table.heading("IMDb", text = "IMDb", anchor=tkinter.CENTER)
		self.Media_Table.heading("Certificate", text = "Certificate", anchor=tkinter.CENTER)
		self.Media_Table.heading("Streaming_Platform", text = "Streaming On", anchor=tkinter.CENTER)

		self.Media_Table['show'] = "headings"

		self.Media_Table.column("ID", width = 70, anchor=tkinter.CENTER)
		self.Media_Table.column("Title", width = 290, anchor=tkinter.CENTER)
		self.Media_Table.column("Genre", width = 110, anchor=tkinter.CENTER)
		self.Media_Table.column("Type", width = 100, anchor=tkinter.CENTER)
		self.Media_Table.column("IMDb", width = 60, anchor=tkinter.CENTER)
		self.Media_Table.column("Certificate", width = 160, anchor=tkinter.CENTER)
		self.Media_Table.column("Streaming_Platform", width = 100, anchor=tkinter.CENTER)
		self.Media_Table.pack(fill = BOTH, expand = 1)
		self.Media_Table.bind("<ButtonRelease-1>", self.Get_Details)
		self.root.bind('<Return>',lambda event:self.Search_Data())
		self.ShowAll_Data()

#════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆FUNCTION⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════════ ⋆★⋆ ════
			
root = Tk()
obj = Wynter(root)
root.mainloop()
