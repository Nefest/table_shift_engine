import csv

class Table_Calc():
    def __init__(self, data=None):
        self.data = data

    def load_table(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        self.data = [line.split(',') for line in lines]

    def save_table(self, path):
        with open(path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    def print_table(self):
        for row in self.data:
            print(row)

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        if stop is None:
            data_slice = self.data[start]
        else:
            data_slice = self.data[start:stop]
        if copy_table:
            return Table_Calc(data_slice)
        else:
            return data_slice

    def get_rows_by_index(self, *values, copy_table=False):
        data_slice = [row for row in self.data if row[0] in values]
        if copy_table:
            return Table_Calc(data_slice)
        else:
            return data_slice

    def get_column_types(self, by_number=True):
        column_len = len(self.data[0])
        type_dict = {}

        for col in range(column_len):
            if by_number:
                type_dict[col] = set([type(row[col]) for row in self.data])
            else:
                type_dict[str(col)] = set([type(row[col]) for row in self.data])
        return type_dict

    def set_column_types(self, types_dict, by_number=True):
        column_len = len(self.data[0])

        for col in range(column_len):
            if by_number:
                if type([types_dict[col]]) == str:
                    self.data[col] = str(self.data[col])
                elif type([types_dict[col]]) == int:
                    self.data[col] = int(self.data[col])
                elif type([types_dict[col]]) == bool:
                    self.data[col] = bool(self.data[col])
                elif type([types_dict[col]]) == float:
                    self.data[col] = float(self.data[col])

    def get_values(self, column=0):
        return [row[column] for row in self.data]

    def get_value(self, column=0):
        return self.data[column]

    def set_values(self, values, column=0):
        for i in range(len(self.data)):
            self.data[i][column] = values[i]

    def set_value(self, value, column=0):
        for i in range(len(self.data)):
            self.data[i][column] = value

table = Table_Calc()
