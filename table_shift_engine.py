import csv
import pickle

class Table_Calc():
    def __init__(self, data=None):
        self.data = data

    def load_table(self, path):
        if path.find('.csv') != -1 or path.find('.txt') != -1 :
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                lines = [line.strip() for line in lines]
                self.data = [line.split(',') for line in lines]
        elif path.find('.pkl') != -1 or path.find('.pickle') != -1:
            with open(path, 'rb') as file:
                self.data = pickle.load(file)
        else:
            raise ValueError("Unsupported file format. Only CSV and Pickle files are supported.")

    def save_table(self, path):
        if path.find('.csv') != -1 or path.find('.txt') != -1:
            with open(path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.data)
        elif path.find('.pkl') != -1 or path.find('.pickle') != -1:
            with open(path, 'wb') as file:
                pickle.dump(self.data, file)
        else:
            raise ValueError("Unsupported file format. Only CSV and Pickle files are supported.")

    def print_table(self):
        if self.data is None:
            print("No data available.")
        else:
            for row in self.data:
                print(row)

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        try:
            if stop is None:
                data_slice = self.data[start]
            else:
                data_slice = self.data[start:stop]
            if copy_table:
                return Table_Calc(data_slice)
            else:
                return data_slice
        except IndexError:
            raise IndexError("Start or stop index is out of range.")
        except Exception as e:
            raise Exception(f"An error occurred in get_rows_by_number: {e}")

    def get_rows_by_index(self, *values, copy_table=False):
        try:
            data_slice = [row for row in self.data if row[0] in values]
            if copy_table:
                return Table_Calc(data_slice)
            else:
                return data_slice
        except Exception as e:
            raise Exception(f"An error occurred in get_rows_by_index: {e}")
    def get_column_types(self, by_number=True):
        try:
            column_len = len(self.data[0])
            type_dict = {}

            for col in range(column_len):
                if by_number:
                    type_dict[col] = set([type(row[col]) for row in self.data])
                else:
                    type_dict[str(col)] = set([type(row[col]) for row in self.data])
            return type_dict
        except IndexError:
            raise IndexError("Data rows have inconsistent lengths.")
        except Exception as e:
            raise Exception(f"An error occurred in get_column_types: {e}")

    def set_column_types(self, types_dict, by_number=True):
        try:
            column_len = len(self.data[0])

            for col in range(column_len):
                if by_number:
                    for row in range(len(self.data)):
                        self.data[row][col] = types_dict[col](self.data[row][col])
        except IndexError:
            raise IndexError("Data rows have inconsistent lengths.")
        except KeyError as ke:
            raise KeyError(f"Missing column in types_dict: {ke}")
        except Exception as e:
            raise Exception(f"An error occurred in set_column_types: {e}")

    def get_values(self, column=0):
        if self.data is None:
            print("No data available.")
        else:
            return [row[column] for row in self.data]

    def get_value(self, column=0):
        if self.data is None:
            print("No data available.")
        elif len(self.data) > 1:
            print("Table needs to be only one row in size.")
        else:
            return self.data[column]

    def set_values(self, values, column=0):
        if self.data is None:
            print("No data available.")
        else:
            for i in range(len(self.data)):
                self.data[i][column] = values[i]

    def set_value(self, value, column=0):
        if self.data is None:
            print("No data available.")
        elif len(self.data) > 1:
            print("Table needs to be only one row in size.")
        for i in range(len(self.data)):
            self.data[i][column] = value

table = Table_Calc()
