#Shun Hui
#shunhui.lee.2019
import unittest
from helper import *

class testclassEnrollment_queue(unittest.TestCase):
    def setUp(self):
        self.S1 = staff(staff_username = 'coreyroberts', staff_name = 'Corey Roberts', role = 'Learner', department = 'Operation', current_designation = 'Engineer')
        self.C1 = course(
            course_id = 1,
            course_name = "Test Course 1",
            description = "Test Description 1"
        )
        self.CEQ1 = classEnrolmentQueue( staff = self.S1, course = self.C1, staff_username = "coreyroberts", course_id = 1 , class_no = 1)


    def testJson(self):
        self.assertEqual(self.CEQ1.json(), {'staff_username': 'coreyroberts', 'course_id': 1, 'class_no': 1})

    def testApprovJson(self):
        expected = {
            'course_id': 1, 
            'class_no': 1, 
            'course_name': 'Test Course 1', 
            'staff_name': 
            'Corey Roberts', 
            'staff_username': 'coreyroberts'
        }
        self.assertEqual(self.CEQ1.approvejson(),expected)

if __name__ == "__main__":
    unittest.main()
