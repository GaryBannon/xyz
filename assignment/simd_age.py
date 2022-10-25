import os.path
import csv
lines_to_skip_census = 4

def skip_lines(file_connection, lines_to_skip):
    """
    skips a given amount of lines in a data file
    """
    for _ in range(lines_to_skip):
        file_connection.readline()
        continue


class CensusData:
    """
    a class to hold analysis functions 
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {} 
        
    def __repr__(self):
        return f"file_name: {self.file_name}\ndata_dict:{self.data_dict}"
    
    def load(self):
        """
        checks if file exists, and load the data from the file to the data_dict in the constructor
        """
        if os.path.isfile(self.file_name) is False:
            return False #returns false if file doesnt exist
        
        else:
            input_file = open(self.file_name, "r", newline='', encoding="iso-8859-1")
            skip_lines(input_file, lines_to_skip_census) #calls the skip lines function to ignore irrelevant rows in data 
            census_data_reader = csv.DictReader(input_file, delimiter=',', quotechar='"') 
            for row in census_data_reader:  
                pop = row["All people"]
                self.data_dict[row["Region"], row["Range"]] = pop #adds to dict as a key:value pair of [Region, Range]:Population
            input_file.close()
            return True
            
    def regions(self):
        """
        returns a list of the available regions in the data 
        """
        input_file = open(self.file_name, "r", newline='', encoding="iso-8859-1")
        skip_lines(input_file, lines_to_skip_census) #calls the skip lines function to ignore irrelevant rows in data
        census_data_reader = csv.DictReader(input_file, delimiter=',', quotechar='"')
        regions_list = [] 
        for row in census_data_reader: 
            regions_list.append(row["Region"]) #adds each rows region to the list, this will have duplicates
        regions_list_no_dupes = list(dict.fromkeys(regions_list)) #turns the list into a dict as this removes duplicates, then back into a list 
        input_file.close()
        for i in range(4):
            """
            removes the unnecessary info at the end of the list
            """
            del regions_list_no_dupes[-1] 
            i += 1
        return regions_list_no_dupes #returns list with no duplicate values or irrelevant lines
        
    def total_population(self, input_region, age_value):
        input_file = open(self.file_name, "r", newline='', encoding="iso-8859-1")
        skip_lines(input_file, lines_to_skip_census) #calls the skip lines function to ignore irrelevant rows in data
        census_data_reader = csv.DictReader(input_file, delimiter=',', quotechar='"')
        census_region_list = CensusData.regions(self) #calls regions function to make list available 
        population_list = [] 
        for row in census_data_reader: 
            if input_region not in census_region_list:
                return 0 #returns zero if region not in list
            if input_region != row["Region"]:
                continue #skips the row if the region of the row doesnt match input region
            elif row["Range"] == "All people":
                continue #skips the headings row
            elif row["Range"] == "Under 1":
                population_list.append(int(row["All people"]))
            elif row["Range"] == "85 to 89":
                row["Range"] = 89 
            elif row["Range"] == "90 to 94":
                row["Range"] = 94 
            elif row["Range"] == "95 and over":
                row["Range"] = 100 
            #the above lines convert the ranges to a value so the loop can read them 
            elif int(row["Range"]) == age_value:
                population_list.append(int(row["All people"]))
                break #stops the loop once input age is reached
            elif input_region == row["Region"]:
                population_list.append(int(row["All people"])) #appends integer value of population to the list 
        total_population = sum(population_list) 
        return total_population 


class SIMD_Data:
    """
    a class to hold analysis functions
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {} 
    
    def __repr__(self):
        return f"file_name: {self.file_name}\ndata_dict:{self.data_dict}"
    
    def load(self):
        """
        checks if file exists, and load the data from the file to the data_dict in the constructor
        """
        if os.path.isfile(self.file_name) is False:
            return False 
        
        else:
            input_file = open(self.file_name, "r", newline='', encoding="iso-8859-1") 
            SIMD_data_reader = csv.DictReader(input_file, delimiter=',', quotechar='"') 
             #creates empty list to store ranks in order to find an average 
            for row in SIMD_data_reader:
                """
                if the region has not been seen yet, add to the dictionary. if it has already appeared,
                append the rank value to the list in the dict value
                """
                if row["MMWname"] not in self.data_dict:
                    self.data_dict[row["MMWname"]] = [int(row["SIMD2020v2_Rank"])]
                
                elif row["MMWname"] in self.data_dict:
                    self.data_dict[row["MMWname"]].append(int(row["SIMD2020v2_Rank"])) #appends row to value list in data_dict
            
            for key in self.data_dict:
                """
                get value list from the key, find the average of the value list and replace the list with the average of the list
                """
                value = self.data_dict[key]
                average = sum(value)/len(value)
                self.data_dict[key] = average
            input_file.close()
            return True
    
    def regions(self):
        """
        returns a list of the available regions from the SIMD data by listing the keys from data_dict
        """
        SIMD_regions_list = list(self.data_dict.keys()) 
        return SIMD_regions_list
    
    def lowest_SIMD(self):
        """
        finds region with lowest average SIMD rank
        """
        lowest_region = min(self.data_dict, key=self.data_dict.get) #finds the lowest value in the values of the dict and returns the corresponding key
        return lowest_region


def main():
    census_data = CensusData("/Users/garybannon/Desktop/Intro to PP/assignment/DC1117SC.csv")
    if not census_data.load():
        return
    
    simd_data = SIMD_Data("/Users/garybannon/Desktop/Intro to PP/assignment/SIMD_2020v2csv.csv")
    if not simd_data.load():
        return
    
    print(simd_data.lowest_SIMD())
    print(simd_data.data_dict[simd_data.lowest_SIMD()])
    print(census_data.total_population("Wishaw", 6))
    print(simd_data.regions())
    pass

if __name__ == '__main__':
    main()
