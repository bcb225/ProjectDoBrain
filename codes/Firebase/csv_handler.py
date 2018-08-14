import csv

class CsvHandler:
    def __init__(self,filepath,header_list):
        self.csvFile = open(filepath, "wb")
        self.csvWriter = csv.writer(self.csvFile, delimiter = ',')
        self.header_list = header_list
        self.csvWriter.writerow(self.header_list)

        pass
    def dict_to_csv(self,dict_list):
        for dict_elm in dict_list:
            buffer = []
            for header in self.header_list:
                buffer.append(dict_elm[header])
            self.csvWriter.writerow(buffer)