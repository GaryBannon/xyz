import os.path

import csv

def skip_lines(file_connection, lines_to_skip):
    """
    a function to skip a given amount of lines in a data file
    """
    for _ in range(lines_to_skip):
        file_connection.readline()
        continue


class CensusData:
    """
    a class to load the census data file
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {}
        
    def __repr__(self):
        return f"file_name: {self.file_name}\ndata_dict:{self.data_dict}"
    
    def load(self):
        """
        check if file exists, return false if it doesnt, if it does funtion carries on
        """
        if os.path.isfile(self.file_name) is False:
            return False
        
        else:
            input_file = open(self.file_name, "r", newline='', encoding="iso-8859-1")
            skip_lines(input_file, lines_to_skip)
            census_data_reader = csv.DictReader(input_file, delimiter=',', quotechar='"')
            for row in census_data_reader:
                print(row)
                
    def regions(self):
        """
        create an empty list, and append the key values unde region 
        """
        regions = []
        for key in self.data_dict.keys():
            regions.append(key)
            return regions
    
    def total_population(self, region, age_value):
        
        if region not in self.data_dict.keys("Region"):
            return "0"
        
        elif age_value >= 85 and age_value <= 89:
            pass

    
lines_to_skip = 4
census_data_file = "/Users/garybannon/Desktop/Intro to PP/assignment/DC1117SC.csv"
loaded_census_data = CensusData(census_data_file)

print(loaded_census_data.load())




 

