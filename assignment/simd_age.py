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
            skip_lines(input_file, lines_to_skip_census)
            census_data_reader = csv.DictReader(input_file, delimiter=',', quotechar='"')
            for row in census_data_reader:
                pop = row["All people"]
                self.data_dict[row["Region"], row["Range"]] = pop
            return True
            
                
    def regions(self):
        """
        create an empty list, and append the key values unde region 
        """
        input_file = open(self.file_name, "r", newline='', encoding="iso-8859-1")
        skip_lines(input_file, lines_to_skip_census)
        census_data_reader = csv.DictReader(input_file, delimiter=',', quotechar='"')
        regions_list = []
        for row in census_data_reader:
            regions_list.append(row["Region"])
        regions_list_no_dupes = list(dict.fromkeys(regions_list))
        return regions_list_no_dupes
        
    
    def total_population(self, region, age_value):
        for region, age_value in self.data_dict:
            if region in self.data_dict.keys():
                if age_value in self.data_dict.keys():
                    return self.data_dict.values()
            
        

    
lines_to_skip_census = 4
census_data_file = "/Users/garybannon/Desktop/Intro to PP/assignment/DC1117SC.csv"
loaded_census_data = CensusData(census_data_file)
loaded_census_data.load()
#print(loaded_census_data.data_dict)
print(loaded_census_data.data_dict["Wishaw", "76"])
#loaded_census_data.total_population(region, age_value)
#print(loaded_census_data.data_dict)
#print(loaded_census_data.regions())




 

