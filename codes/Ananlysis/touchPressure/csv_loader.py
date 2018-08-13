import pandas as pd
class CsvLoader():
    def __init__(self, input_csv_file_path):
        self.input_csv_file_path = input_csv_file_path

    def load(self):
        result = pd.read_csv(self.input_csv_file_path, delimiter=',')
        return result
