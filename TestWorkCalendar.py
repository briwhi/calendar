from workCalendar import WorkCalendar
import unittest 
from datetime import datetime

class TestWorkCalendar(unittest.TestCase):
    def test_init(self):
        wc = WorkCalendar(2019)
        self.assertEqual(2019, wc.year )
        cc = WorkCalendar()
        current_year = datetime.now().year
        self.assertEqual(cc.year, current_year)


if __name__ == '__main__':
    unittest.main()