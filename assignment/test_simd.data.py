import unittest

from isort import file
import simd_age

class TestSIMD_Data(unittest.TestCase):
    def test_regions(self):
        file = simd_age.SIMD_Data("/Users/garybannon/Desktop/Intro to PP/assignment/SIMD_2020v2csv.csv")
        file.load()
        regions = len(file.regions())
        self.assertEqual(352, regions)
    
    def test_total_population(self):
        file = simd_age.SIMD_Data("/Users/garybannon/Desktop/Intro to PP/assignment/SIMD_2020v2csv.csv")
        file.load()
        lowest_rank = file.lowest_SIMD()
        self.assertEqual("Canal", lowest_rank)


if __name__ == '__main__':
    unittest.main()
