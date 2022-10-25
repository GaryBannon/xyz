import unittest
import simd_age

class TestCensusData(unittest.TestCase):
    def test_regions(self):
        file = simd_age.CensusData("/Users/garybannon/Desktop/Intro to PP/assignment/DC1117SC.csv")
        length_of_list = len(file.regions())
        self.assertEqual(354, length_of_list)
    
    def test_total_population(self):
        file = simd_age.CensusData("/Users/garybannon/Desktop/Intro to PP/assignment/DC1117SC.csv")
        wishaw_under_6 = file.total_population("Wishaw", 6)
        self.assertEqual(1479, wishaw_under_6)
        
if __name__ == '__main__':
    unittest.main()
