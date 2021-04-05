from workCalendar import WorkCalendar
import unittest 
from datetime import datetime

class TestWorkCalendar(unittest.TestCase):
    def test_init_without_arguments(self):
        cc = WorkCalendar()
        current_year = datetime.now().year
        current_month = datetime.now().month
        self.assertEqual(cc.year, current_year)
        self.assertEqual(cc.month, current_month)
        
    def test_init_with_arguments(self):
        wc = WorkCalendar(year=2019, month=3)
        self.assertEqual(2019, wc.year )
        self.assertEqual(3, wc.month)


if __name__ == '__main__':
    unittest.main()