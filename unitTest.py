import unittest
from  calenderPrinter import calender_printer
import os

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if the days printed are correct
    def test_days(self):
        self.assertEqual(calender_printer(31, 3), ["S", "M" , "T", "W", "T", "F", "S"])

#make sure days in month only equal 28, 29, 30, 31

# make sure user cant input value greater than 7

    # run the tests
if __name__ == "__main__":
    unittest.main()