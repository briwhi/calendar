from workCalendar import WorkCalendar
import unittest 
from datetime import datetime



class TestWorkCalendar(unittest.TestCase):
    def test_init(self):
        cc = WorkCalendar()
        current_year = datetime.now().year
        current_month = datetime.now().month
        current_date = datetime.now()
        self.assertEqual(cc.year, current_year)
        self.assertEqual(cc.month, current_month)
        self.assertEqual(cc.start_date, current_date)
        
    def test_set_year(self):
        cc = WorkCalendar()
        cc.year = 2001
        self.assertEqual(cc.year, 2001)

    def test_set_month(self):
        cc = WorkCalendar()
        cc.month = 12
        self.assertEqual(cc.month, 12)

    

if __name__ == '__main__':
    unittest.main()