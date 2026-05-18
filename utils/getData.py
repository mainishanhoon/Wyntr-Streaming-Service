def Get_Data(self, data):
    row_idx = data.get("row")

    if row_idx == 0 or row_idx is None:
        return

    actual_record = self.full_data_records[row_idx - 1]

    self.var_ID.set(actual_record[0])
    self.var_Title.set(actual_record[1])
    self.var_Genre.set(actual_record[2])
    self.var_Type.set(actual_record[3])
    self.var_IMDb.set(actual_record[4])
    self.var_Certificate.set(actual_record[5])
    self.var_Platform.set(actual_record[6])
    self.txt_Description.delete("1.0", "end")
    self.txt_Description.insert("1.0", actual_record[7])
    self.var_Link.set(actual_record[8])

