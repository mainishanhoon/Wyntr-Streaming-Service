def CenterWindow(app, width=1300, height=700):
    app.update_idletasks()
    screen_w = app.winfo_screenwidth()
    screen_h = app.winfo_screenheight()

    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)

    app.geometry(f"{width}x{height}+{x}+{y}")
