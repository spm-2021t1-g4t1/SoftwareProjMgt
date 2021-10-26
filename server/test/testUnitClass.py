import unittest
from helper import *
import datetime


class testCaseClass(unittest.TestCase):
    import_data = {
        "course_id": 1,
        "class_no": 2,
        "start_date": "01/10/2021",
        "end_date": "31/10/2021",
        "start_time": datetime.time(hour=8, minute=0),
        "end_time": datetime.time(hour=10, minute=0),
        "class_size": 40,
        "trainer_name": 'Mr Chen',
    }
    
    

    def testClasses(self):
        classObj = classes(import_data)
        self.assertEqual(classObj,)
