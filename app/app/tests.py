"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc 

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """test adding numbers together"""
        res = calc.add(4, 5)
        self.assertEqual(res, 9)
