import unittest
import datetime
from helper import *

class testClassesObj(unittest.TestCase):
    def setUp(self):
        self.CO1 = classes(
            course_id = 1,
            class_no = 1,
            start_date  = datetime.date(year=2012, month=1,day=1),
            end_date  = datetime.date(year=2012, month=2,day=1),
            start_time  = datetime.time(hour=8,minute=0,second=0),
            end_time = datetime.time(hour=10,minute=0,second=0),
            class_size   = 40,
            trainer_name  = "Jane Doe",
            lesson = []
        )
    def tearDown(self):
        self.C01 = None

    def testViewJson(self):
        self.assertEqual(self.CO1.viewjson(), {
            'course_id': 1, 
            'class_no': 1, 
            'start_date': '2012-01-01', 
            'end_date': '2012-02-01', 
            'start_time': '08:00:00', 
            'end_time': '10:00:00', 
            'class_size': 40, 
            'trainer_name': 'Jane Doe',
            'lesson': []})

    def testJson(self):
        # print(self.CO1.json())
        self.assertEqual(self.CO1.json(),{
            'course_id': 1, 
            'class_no': 1, 
            'start_date': '2012-01-01', 
            'end_date': '2012-02-01', 
            'start_time': '08:00:00', 
            'end_time': '10:00:00', 
            'class_size': 40, 'trainer_name': 
            'Jane Doe'})


if __name__ == "__main__":
    unittest.main()
