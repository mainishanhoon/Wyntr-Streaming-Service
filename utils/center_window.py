def Center_Window(self, width=1300, height=700):
    self.update_idletasks()
    screen_w = self.winfo_screenwidth()
    screen_h = self.winfo_screenheight()

    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)

    self.geometry(f'{width}x{height}+{x}+{y}')
