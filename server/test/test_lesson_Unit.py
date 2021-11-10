import unittest
from datetime import date, time
from helper import *

class testLessonObj(unittest.TestCase):
    def setUp(self):
        self.LM1 = lesson_materials(
            course_id = 1,
            class_no = 1 ,
            lesson_no = 1, 
            course_material_title = "Test Material 1", 
            link = "./somewhere"
        )

        self.CC1 = lesson(
            course_id = 1,
            class_no = 1,
            lesson_no = 1,
            lesson_name = "Test Lesson Name",
            lesson_description = "Test Description",
            lesson_materials = [self.LM1],
            quiz_assigned_id = 1
        )

    def tearDown(self):
        self.LM1 = None
        self.CC1 = None

    def testLessonJson(self):
        expected = {
            'course_id': 1, 
            'class_no': 1, 
            'lesson_no': 1, 
            'lesson_name': 'Test Lesson Name', 
            'lesson_description': 'Test Description', 
            'lesson_materials': [
                                    {'course_id': 1, 
                                    'class_no': 1, 
                                    'lesson_no': 1, 
                                    'course_material_title': 'Test Material 1', 
                                    'link': './somewhere'}
                                    ], 
            'quiz_assigned_id': 1}

        self.assertEqual(self.CC1.json(),expected)

    def testLesson_Material(self):
        expected = {
            'course_id': 1, 
            'class_no': 1, 
            'lesson_no': 1, 
            'course_material_title': 'Test Material 1', 
            'link': './somewhere'
        }

        self.assertEqual(self.LM1.json(),expected)


if __name__ == "__main__":
    unittest.main()
