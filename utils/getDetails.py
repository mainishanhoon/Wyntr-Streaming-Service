def GetDetails(app):
    Cursor_Row = app.Media_Table.focus()
    Contents = app.Media_Table.item(Cursor_Row)
    row = Contents['values']
    app.var_ID.set(row[0]),
    app.var_Title.set(row[1]),
    app.var_Genre.set(row[2]),
    app.var_Type.set(row[3]),
    app.var_IMDb.set(row[4]),
    app.var_Certificate.set(row[5]),
    app.var_Platform.set(row[6]),
    app.var_Description.set()
    app.var_Link.set(row[8])