import unittest
from helper import *

class testclassEnrollment_queue(unittest.TestCase):
    def testViewJson(self):
        CEQ1 = classEnrolmentQueue(staff_username = "jane", course_id = 1 , class_no = 1)
        self.assertEqual(CEQ1.json(), {'staff_username': 'jane', 'course_id': 1, 'class_no': 1})
    
if __name__ == "__main__":
    unittest.main()
