import unittest
from  mainCode import *

from unittest.mock import Mock, MagicMock, patch

import pytest


# define the unit tests
class my_unit_tests(unittest.TestCase):

    # Tests if the days are printed quickly
    def test_days(self):
        self.assertEqual(calender_printer(31, 3), [" S", "M", "T", "W", "T", "F", "S"])

# ---------------------------------------------------------------------
# TESTING: get_days_in_month()
# ---------------------------------------------------------------------

    # Tests to see if users can pass in strings
    def tests_string_month(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = prompt_error_handling_month):
                get_days_in_month()

    # Tests to see if users can pass in floats
    def tests_float_month(self):
        with patch("builtins.input", return_value="29.2"):
            with pytest.raises(ValueError, match = prompt_error_handling_month):
                get_days_in_month()


    # Test to see if users can input values below 28
    def tests_min_month(self):
        with patch("builtins.input", return_value="27"):
            with pytest.raises(ValueError, match = prompt_error_handling_month):
                get_days_in_month()

    # Tests to see if users can input values above 31
    def tests_max_month(self):
        with patch("builtins.input", return_value="32"):
            with pytest.raises(ValueError, match = prompt_error_handling_month):
                get_days_in_month()
    
# ---------------------------------------------------------------------
# TESTING: get_days_in_week()
# ---------------------------------------------------------------------

    # Tests to see if users can pass in strings
    def tests_string_week(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = prompt_error_handling_week):
                get_days_in_week()

    # Tests to see if users can pass in floats
    def tests_float_week(self):
        with patch("builtins.input", return_value="6.5"):
            with pytest.raises(ValueError, match = prompt_error_handling_week):
                get_days_in_week()


    # Test to see if users can input values below 28
    def tests_min_week(self):
        with patch("builtins.input", return_value="0"):
            with pytest.raises(ValueError, match = prompt_error_handling_week):
                get_days_in_week()

    # Tests to see if users can input values above 31
    def tests_max_week(self):
        with patch("builtins.input", return_value="8"):
            with pytest.raises(ValueError, match = prompt_error_handling_week):
                get_days_in_week()



# make sure user cant input value greater than 7 for days

#i wanna add a try thingy so maybe a self.assert(equal) to an error message of "Insert a number no larger than (days)"

    # run the tests
if __name__ == "__main__":
    unittest.main()