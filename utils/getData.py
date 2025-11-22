def Get_Data(self, event=None):
    selected = self.Media_Table.get_selected_row()
    print("Selected row:", selected)

    if selected is None or selected["row_index"] is None:
        return

    row_values = selected["values"]

    print("Selected row:", row_values)

    self.var_ID.set(row_values[0])
    self.var_Title.set(row_values[1])
    self.var_Genre.set(row_values[2])
    self.var_Type.set(row_values[3])
    self.var_IMDb.set(row_values[4])
    self.var_Certificate.set(row_values[5])
    self.var_Platform.set(row_values[6])
    self.var_Description.set(row_values[7])
    self.var_Link.set(row_values[8])