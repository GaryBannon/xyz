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
            input_file.close()
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
        input_file.close()
        return regions_list_no_dupes
        
    
    def total_population(self, input_region, age_value):
        if input_region not in region_list:
            return 0
        
        else:
            for self.data_dict[input_region] in range(0, age_value):
                pass
                
class SIMD_Data:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {}
    
    def __repr__(self):
        return f"file_name: {self.file_name}\ndata_dict:{self.data_dict}"
    
    def load(self):
        """
        a function to load the SIMD file data
        """
        if os.path.isfile(self.file_name) is False:
            """
            check if the file path exists and return false if not
            """
            return False
        
        else:
            input_file = open(self.file_name, "r", newline='', encoding="iso-8859-1") #create file connection
            SIMD_data_reader = csv.DictReader(input_file, delimiter=',', quotechar='"') #create dictreader 
            region_rank_list = []
            for row in SIMD_data_reader:
                if row["MMWname"] not in self.data_dict:
                    region_rank_list.clear()
                    self.data_dict[row["MMWname"]] = 0
                
                elif row["MMWname"] in self.data_dict:
                    region_rank_list.append(int(row["SIMD2020v2_Rank"]))
                    average = sum(region_rank_list)/len(region_rank_list)
                    self.data_dict[row["MMWname"]] = average
            input_file.close()
            return True
    
    def regions(self):
        """
        a function which returns a list of the available regions from the SIMD data
        """
        regions_list = list(self.data_dict.keys()) #creates a list of the keys in the data_dict
        return regions_list
    
    def lowest_SIMD(self):
        lowest_region = min(self.data_dict, key=self.data_dict.get) #finds the lowest value in the values of the dict and returns the corresponding key
        lowest_rank = self.data_dict[lowest_region] #takes lowest region from the previous line and uses it to find the corresponding value
        
        return lowest_region, lowest_rank
            

lines_to_skip_census = 4
census_data_file = "/Users/garybannon/Desktop/Intro to PP/assignment/DC1117SC.csv"
loaded_census_data = CensusData(census_data_file)
loaded_census_data.load()
#print(loaded_census_data.data_dict)
#print(loaded_census_data.data_dict["Wishaw", "76"])
#loaded_census_data.total_population(region, age_value)
#print(loaded_census_data.data_dict)
#region_list = loaded_census_data.regions()
#print(region_list)
#print(loaded_census_data.total_population("Wishaw", 67))

SIMD_data_file = "/Users/garybannon/Desktop/Intro to PP/assignment/SIMD_2020v2csv.csv"
loaded_SIMD = SIMD_Data(SIMD_data_file)
loaded_SIMD.load()
#print(loaded_SIMD.data_dict)
#print(loaded_SIMD.regions())
print(loaded_SIMD.lowest_SIMD())



 

