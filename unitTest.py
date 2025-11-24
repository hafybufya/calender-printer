import unittest
from  mainCode import *

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if the days printed are correct
    def test_days(self):
        self.assertEqual(calender_printer(31, 3), [" S", "M", "T", "W", "T", "F", "S"])

        #user input only be between min_number_week_days and max_number_week_days


# make sure user cant input value greater than 7 for days

#i wanna add a try thingy so maybe a self.assert(equal) to an error message of "Insert a number no larger than (days)"

    # run the tests
if __name__ == "__main__":
    unittest.main()