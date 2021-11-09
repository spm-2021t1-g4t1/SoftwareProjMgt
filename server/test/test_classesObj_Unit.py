import unittest
from datetime import date, time
from helper import *

class testClassesObj(unittest.TestCase):
    def setUp(self):
        self.C1 = course(
            course_id = 1,
            course_name = "Test Course 1",
            description = "Test Description 1"
        )
        self.CO1 = classes(
            courses = self.C1,
            course_id = 1,
            class_no = 1,
            start_date  = date(year=2012, month=1,day=1),
            end_date  = date(year=2012, month=2,day=1),
            start_time  = time(hour=8,minute=0,second=0),
            end_time = time(hour=10,minute=0,second=0),
            class_size   = 40,
            trainer_name  = "Jane Doe",
            selfenrol_start = date(year=2011, month=9,day=1),
            selfenrol_end = date(year=2011, month=9,day=30),
            finalquiz_id = 1,
            lesson = []
        )

    def tearDown(self):
        self.C01 = None

    def testJson(self):
        # print(self.CO1.json())
        self.assertEqual(self.CO1.json(),{
            'course_id': 1, 
            'class_no': 1, 
            'start_date': '2012-01-01', 
            'end_date': '2012-02-01', 
            'start_time': '08:00:00', 
            'end_time': '10:00:00', 
            'class_size': 40, 
            'trainer_name': 'Jane Doe'})

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

    def testCourseJson(self):
        self.assertEqual(self.CO1.coursejson(), {
            'course_name': 'Test Course 1',
            'course_id': 1, 
            'class_no': 1, 
            'start_date': date(2012, 1, 1), 
            'end_date': date(2012, 2, 1), 
            'start_time': '08:00:00', 
            'end_time': '10:00:00', 
            'class_size': 40, 
            'trainer_name': 'Jane Doe',
            "selfenrol_start": date(2011, 9, 1),
            "selfenrol_end": date(2011, 9, 30)})

    def testGetSelfEnrolDates(self):
        self.assertEqual(self.CO1.getSelfEnrolDates(), {
            "start": '2011-09-01',
            "end": '2011-09-30'
        })
    
    def testGetFinalQuiz(self):
        self.assertEqual(self.CO1.getFinalQuiz(), 1)

    def testSetFinalQuiz(self):
        self.CO1.setFinalQuiz(2)
        self.assertEqual(self.CO1.getFinalQuiz(), 2)
    

if __name__ == "__main__":
    unittest.main()
